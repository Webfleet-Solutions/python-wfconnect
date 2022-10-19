#!/usr/bin/env python3

import html.parser
import os.path
import sys
from textwrap import dedent, indent
import xml.etree.ElementTree as ET

import requests

# method names which never get a Extern appended
UNCHANGED_NAMES = [
    "geocodeLocation",
    "listQueues",
    "showDriverAssignmentReport",
    "showLogbookReport",
    "showObjectAccelerationEvents",
    "showObjectSpeedingEvents",
    "showOrderMessageReport",
    "showPersonReport",
    "showQueueExtern",
    "showSessions",
    "showStoplistReport",
    "showTrailerReport",
    "getCrashLog",
]

# names from WDSL to real names as in documentation/csv interface
MAPPED_NAMES = {
    "showObjectGroupObjectReport": "showObjectGroupObjects",
    "showObjectGroupReport": "showObjectGroups",
    "showStandStillReport": "showStandStills",
    "showTripReport": "showTrips",
    "showVehicleReport": "showVehicleReportExtern",
    "popQueueMessagesExtern": "popQueueMessages",
    "deleteQueueExtern": "deleteQueue",
    "createQueueExtern": "createQueue",
}


def main():
    output_file_header = (
        dedent(
            """\
        #!/usr/bin/env python3
        # -*- coding: utf-8 -*-

        \"""
        An abstract WEBFLEET.connect API class.

        IMPORTANT: This file is generated automatically using the %s script.
                   Do NOT modify it manually or your changes will be overwritten!
        \"""

        from abc import ABCMeta, abstractmethod


        class WfConnectGeneratedAbc(metaclass=ABCMeta):
            @abstractmethod
            def _request(self, method, **kwargs):
                pass
    """
        )
        % (os.path.basename(__file__))
    )

    # create methods in WFconnect class for all WFconnect methods
    filename = os.path.join(os.path.dirname(__file__), "wfconnect_abc.py")
    with open(filename + ".new", "w") as fp:
        fp.write(output_file_header)
        for method in get_method_names_from_wsdl():
            fp.write(
                indent(
                    dedent(
                        """
                def {method}(self, **kwargs):
                    return self._request("{method}", **kwargs)
            """
                    ).format(method=method),
                    "    ",
                )
            )
    os.replace(filename + ".new", filename)


def get_method_names_from_wsdl():
    """
    Load method names from soap/wsdl api server.

    As the SOAP and CSV use different names for some methods some name mangling is needed.
    """

    # get base document
    soap = requests.get("https://soap.webfleet.com").text

    # the next step collects all links in the main file
    wsdl_links = []

    class MyHTMLParser(html.parser.HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == "a":
                for name, value in attrs:
                    if name == "href":
                        https_value = value.replace("http://","https://")
                        wsdl_links.append(https_value)

    MyHTMLParser().feed(soap)

    # process all links and filter the messages aka methods out
    for link in wsdl_links:
        wsdl = requests.get(link).text
        root = ET.fromstring(wsdl)
        messages = root.findall(
            "./wsdl:portType/wsdl:operation",
            namespaces=dict(wsdl="http://schemas.xmlsoap.org/wsdl/"),
        )
        for message in messages:
            yield mangle_method_name(message.attrib["name"])


def mangle_method_name(name):
    # check if the name should be as it is
    for s in UNCHANGED_NAMES:
        if name.startswith(s):
            return name

    # check if we have a special mapping defined
    try:
        return MAPPED_NAMES[name]
    except KeyError:
        pass

    # mangle some other names
    if not name.endswith("Extern"):
        extern = False  # true is an Extern needs to be added

        # these need in most cases the Extern
        for s in [
            "Queue",
            "Report",
            "Order",
            "TextMessage",
            "Address",
            "RouteSimple",
            "Event",
            "Driver",
        ]:
            if name.find(s) >= 0:
                extern = True
                break

        if extern:
            # but there are some exception which should be not "Extern"ed
            for s in [
                "DriverGroup",
                "Events",
                "AccountOrder",
                "Vehicle",
                "Aux",
                "ArchivedReport",
                "ReportList",
                "ObjectGroup",
                "Vehicle",
                "attachDriverToGroup",
                "createReport",
                "detachDriverFromGroup",
                "sendReportViaMail",
                "geocodeAddress",
                "showOrderWaypoints",
            ]:
                if name.find(s) >= 0:
                    extern = False
                    break

        # now as we know if it should get added the Extern do it
        if extern:
            name += "Extern"

    return name


if __name__ == "__main__":
    sys.exit(main())
