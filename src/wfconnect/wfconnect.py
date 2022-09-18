#!/usr/bin/env python3

import base64
from logging import critical, debug, error, info, warning
import time

import requests

from .wfconnect_abc import WfConnectGeneratedAbc


class WfConnectException(Exception):
    def __init__(self, request_url, *args, **kwargs):
        self.request_url = request_url


class WfConnectError(WfConnectException):
    def __init__(self, request_url, id_, description):
        super().__init__(
            request_url, "WEBFLEET.connect error: %d %s" % (id_, description)
        )
        self.id = id_
        self.description = description


class WfConnect(WfConnectGeneratedAbc):
    def __init__(self, url):
        self._url = url

        # Creating a requests session allows us to make use of requests' automatic
        # connection pooling, which allows it to reuse an existing TLS connection
        self._requests_session = requests.Session()
        self._requests_session.params = {
            "lang": "en",  # or "de"
            "useISO8601": "true",
            "useUTF8": "true",  # false = ISO-8859-1
            "outputformat": "json",
        }

        # Set a User-Agent, so the backend thinks we are a real browser
        self._requests_session.headers = {"User-agent": "Mozilla/5.0"}

    def setAuthentication(self, account, username, password, apikey=None):
        self._requests_session.params["account"] = account
        self._requests_session.params["username"] = username
        self._requests_session.params["password"] = password

        if apikey is not None:
            self._requests_session.params["apikey"] = apikey
        else:
            self._requests_session.params.pop("apikey", None)

    def _request(self, action, **params):
        params["action"] = action

        request = self._requests_session.get(self._url, params=params)
        data1 = request.json()

        if "errorCode" in data1:
            err_code = data1["errorCode"]
            err_message = data1["errorMsg"]

            raise WfConnectError(request.url, err_code, err_message)
        elif data1 is None:
            raise WfConnectError(
                request.url, -1, "Got empty response from WEBFLEET.connect api"
            )

        return data1

    def sendAuxDeviceData(
        self,
        objectno=None,
        objectuid=None,
        data=None,
        deviceid=None,
        correlationid=None,
    ):  # the Correlation ID is used to identify the configured remote device via WF.connect
        assert not (
            objectno is None and objectuid is None
        ), "Either objectno or objectuid is required."
        assert deviceid is not None, "Device ID is missing"
        assert correlationid is not None, "Correlation ID is missing or not unique"
        assert 0 <= correlationid < 5, "Correlation ID must be in range 0..4"
        super().sendAuxDeviceData(
            objectno=objectno,
            objectuid=objectuid,
            data=base64.b64encode(data).decode("ascii"),
            deviceid=deviceid,
            correlationid=correlationid,
        )


class RetryingWfConnect(WfConnect):
    def __init__(self, url, retry=5):
        super().__init__(url)
        self.retries = retry

    def _request(self, action, **params):
        i = 0
        while True:
            try:
                try:
                    return super()._request(action, **params)
                except requests.exceptions.RequestException as ex:
                    raise WfConnectError(ex.request.url, -1, str(ex)) from None
            except WfConnectError as err:
                # Workaround the following errors:
                # -1: No WF.connect error code, used for other exceptions
                # 60: WebFleet general error
                # 8015: Username busy processing other request
                # 9199: An upstream system did not respond properly. At the moment we are unable to service this request.
                # 10000: resource currently busy, retry later
                if err.id in (-1, 60, 8015, 9199, 10000) and i <= self.retries:
                    wait_time = 10

                    if err.id == 10000:
                        wait_time = 30

                    description = err.description
                    if err.id == 8015:
                        description += (
                            ", consider setting 'WFc.sessionLocking.enabled' to 0"
                        )

                    warning(
                        "WEBFLEET.connect.%s failed with: %s. Retrying in %d seconds.",
                        action,
                        description,
                        wait_time,
                    )
                    time.sleep(wait_time)
                else:
                    error(
                        "WEBFLEET.connect call failed with error code %s (%s)",
                        err.id,
                        err.description,
                    )
                    error("Request was: %s", err.request_url)
                    raise
            i += 1
