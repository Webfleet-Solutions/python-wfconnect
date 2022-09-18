#!/usr/bin/env python3

"""
An abstract WEBFLEET.connect API class.

IMPORTANT: This file is generated automatically using the generate_wfconnect_abc.py script.
           Do NOT modify it manually or your changes will be overwritten!
"""

from abc import ABCMeta, abstractmethod


class WfConnectGeneratedAbc(metaclass=ABCMeta):
    @abstractmethod
    def _request(self, method, **kwargs):
        pass

    def attachAddressToGroupExtern(self, **kwargs):
        return self._request("attachAddressToGroupExtern", **kwargs)

    def insertAddressGroupExtern(self, **kwargs):
        return self._request("insertAddressGroupExtern", **kwargs)

    def insertAddressExtern(self, **kwargs):
        return self._request("insertAddressExtern", **kwargs)

    def updateAddressExtern(self, **kwargs):
        return self._request("updateAddressExtern", **kwargs)

    def detachAddressFromGroupExtern(self, **kwargs):
        return self._request("detachAddressFromGroupExtern", **kwargs)

    def showAddressGroupReportExtern(self, **kwargs):
        return self._request("showAddressGroupReportExtern", **kwargs)

    def deleteAddressExtern(self, **kwargs):
        return self._request("deleteAddressExtern", **kwargs)

    def geocodeAddress(self, **kwargs):
        return self._request("geocodeAddress", **kwargs)

    def showAddressReportExtern(self, **kwargs):
        return self._request("showAddressReportExtern", **kwargs)

    def deleteAddressGroupExtern(self, **kwargs):
        return self._request("deleteAddressGroupExtern", **kwargs)

    def calcRouteSimpleExtern(self, **kwargs):
        return self._request("calcRouteSimpleExtern", **kwargs)

    def showAddressGroupAddressReportExtern(self, **kwargs):
        return self._request("showAddressGroupAddressReportExtern", **kwargs)

    def geocodeLocation(self, **kwargs):
        return self._request("geocodeLocation", **kwargs)

    def insertAreaSchedule(self, **kwargs):
        return self._request("insertAreaSchedule", **kwargs)

    def updateArea(self, **kwargs):
        return self._request("updateArea", **kwargs)

    def getAreaPoints(self, **kwargs):
        return self._request("getAreaPoints", **kwargs)

    def getAreaSchedules(self, **kwargs):
        return self._request("getAreaSchedules", **kwargs)

    def deleteAreaAssignment(self, **kwargs):
        return self._request("deleteAreaAssignment", **kwargs)

    def getAreaAssignments(self, **kwargs):
        return self._request("getAreaAssignments", **kwargs)

    def insertAreaAssignment(self, **kwargs):
        return self._request("insertAreaAssignment", **kwargs)

    def getAreas(self, **kwargs):
        return self._request("getAreas", **kwargs)

    def deleteAreaSchedule(self, **kwargs):
        return self._request("deleteAreaSchedule", **kwargs)

    def insertArea(self, **kwargs):
        return self._request("insertArea", **kwargs)

    def deleteArea(self, **kwargs):
        return self._request("deleteArea", **kwargs)

    def removeRemoteAuxDeviceConfig(self, **kwargs):
        return self._request("removeRemoteAuxDeviceConfig", **kwargs)

    def getLocalAuxDeviceConfig(self, **kwargs):
        return self._request("getLocalAuxDeviceConfig", **kwargs)

    def clearAuxDeviceDataQueue(self, **kwargs):
        return self._request("clearAuxDeviceDataQueue", **kwargs)

    def resetAuxDeviceData(self, **kwargs):
        return self._request("resetAuxDeviceData", **kwargs)

    def configureRemoteAuxDevice(self, **kwargs):
        return self._request("configureRemoteAuxDevice", **kwargs)

    def getRemoteAuxDeviceConfig(self, **kwargs):
        return self._request("getRemoteAuxDeviceConfig", **kwargs)

    def sendAuxDeviceData(self, **kwargs):
        return self._request("sendAuxDeviceData", **kwargs)

    def configureLocalAuxDevice(self, **kwargs):
        return self._request("configureLocalAuxDevice", **kwargs)

    def updateAccountOrderState(self, **kwargs):
        return self._request("updateAccountOrderState", **kwargs)

    def showAccountOrderAutomations(self, **kwargs):
        return self._request("showAccountOrderAutomations", **kwargs)

    def setVehicleConfig(self, **kwargs):
        return self._request("setVehicleConfig", **kwargs)

    def getVehicleConfig(self, **kwargs):
        return self._request("getVehicleConfig", **kwargs)

    def setAccountStatusMessages(self, **kwargs):
        return self._request("setAccountStatusMessages", **kwargs)

    def createSession(self, **kwargs):
        return self._request("createSession", **kwargs)

    def showSessions(self, **kwargs):
        return self._request("showSessions", **kwargs)

    def getStatusMessages(self, **kwargs):
        return self._request("getStatusMessages", **kwargs)

    def updateAccountOrderAutomation(self, **kwargs):
        return self._request("updateAccountOrderAutomation", **kwargs)

    def terminateSession(self, **kwargs):
        return self._request("terminateSession", **kwargs)

    def showSettings(self, **kwargs):
        return self._request("showSettings", **kwargs)

    def getAccountStatusMessages(self, **kwargs):
        return self._request("getAccountStatusMessages", **kwargs)

    def showAccountOrderStates(self, **kwargs):
        return self._request("showAccountOrderStates", **kwargs)

    def setStatusMessages(self, **kwargs):
        return self._request("setStatusMessages", **kwargs)

    def attachDriverToVehicle(self, **kwargs):
        return self._request("attachDriverToVehicle", **kwargs)

    def deleteDriverExtern(self, **kwargs):
        return self._request("deleteDriverExtern", **kwargs)

    def detachDriverFromGroup(self, **kwargs):
        return self._request("detachDriverFromGroup", **kwargs)

    def showDriverGroupDrivers(self, **kwargs):
        return self._request("showDriverGroupDrivers", **kwargs)

    def updateDriverExtern(self, **kwargs):
        return self._request("updateDriverExtern", **kwargs)

    def detachDriverFromVehicle(self, **kwargs):
        return self._request("detachDriverFromVehicle", **kwargs)

    def attachDriverToGroup(self, **kwargs):
        return self._request("attachDriverToGroup", **kwargs)

    def insertDriverGroup(self, **kwargs):
        return self._request("insertDriverGroup", **kwargs)

    def showDriverGroups(self, **kwargs):
        return self._request("showDriverGroups", **kwargs)

    def deleteDriverGroup(self, **kwargs):
        return self._request("deleteDriverGroup", **kwargs)

    def insertDriverExtern(self, **kwargs):
        return self._request("insertDriverExtern", **kwargs)

    def updateDriverGroup(self, **kwargs):
        return self._request("updateDriverGroup", **kwargs)

    def insertEventForwardConfigExtern(self, **kwargs):
        return self._request("insertEventForwardConfigExtern", **kwargs)

    def getEventForwardConfigsExtern(self, **kwargs):
        return self._request("getEventForwardConfigsExtern", **kwargs)

    def showEventReportExtern(self, **kwargs):
        return self._request("showEventReportExtern", **kwargs)

    def deleteEventForwardConfigExtern(self, **kwargs):
        return self._request("deleteEventForwardConfigExtern", **kwargs)

    def resolveEventExtern(self, **kwargs):
        return self._request("resolveEventExtern", **kwargs)

    def getEventForwardConfigRecipientsExtern(self, **kwargs):
        return self._request("getEventForwardConfigRecipientsExtern", **kwargs)

    def acknowledgeEventExtern(self, **kwargs):
        return self._request("acknowledgeEventExtern", **kwargs)

    def updateEventForwardConfigExtern(self, **kwargs):
        return self._request("updateEventForwardConfigExtern", **kwargs)

    def createQueue(self, **kwargs):
        return self._request("createQueue", **kwargs)

    def resetBinaryMessages(self, **kwargs):
        return self._request("resetBinaryMessages", **kwargs)

    def showMessages(self, **kwargs):
        return self._request("showMessages", **kwargs)

    def clearBinaryMessages(self, **kwargs):
        return self._request("clearBinaryMessages", **kwargs)

    def deleteQueue(self, **kwargs):
        return self._request("deleteQueue", **kwargs)

    def sendBinaryMessage(self, **kwargs):
        return self._request("sendBinaryMessage", **kwargs)

    def clearTextMessagesExtern(self, **kwargs):
        return self._request("clearTextMessagesExtern", **kwargs)

    def listQueuesExtern(self, **kwargs):
        return self._request("listQueuesExtern", **kwargs)

    def sendTextMessageExtern(self, **kwargs):
        return self._request("sendTextMessageExtern", **kwargs)

    def popQueueMessages(self, **kwargs):
        return self._request("popQueueMessages", **kwargs)

    def ackQueueMessagesExtern(self, **kwargs):
        return self._request("ackQueueMessagesExtern", **kwargs)

    def showQueueExtern(self, **kwargs):
        return self._request("showQueueExtern", **kwargs)

    def detachObjectFromGroup(self, **kwargs):
        return self._request("detachObjectFromGroup", **kwargs)

    def showWakeupTimers(self, **kwargs):
        return self._request("showWakeupTimers", **kwargs)

    def showObjectGroups(self, **kwargs):
        return self._request("showObjectGroups", **kwargs)

    def showObjectGroupObjects(self, **kwargs):
        return self._request("showObjectGroupObjects", **kwargs)

    def showDriverReportExtern(self, **kwargs):
        return self._request("showDriverReportExtern", **kwargs)

    def switchOutput(self, **kwargs):
        return self._request("switchOutput", **kwargs)

    def showObjectReportExtern(self, **kwargs):
        return self._request("showObjectReportExtern", **kwargs)

    def showNearestVehicles(self, **kwargs):
        return self._request("showNearestVehicles", **kwargs)

    def updateObjectGroup(self, **kwargs):
        return self._request("updateObjectGroup", **kwargs)

    def attachObjectToGroup(self, **kwargs):
        return self._request("attachObjectToGroup", **kwargs)

    def showVehicleReportExtern(self, **kwargs):
        return self._request("showVehicleReportExtern", **kwargs)

    def updateWakeupTimers(self, **kwargs):
        return self._request("updateWakeupTimers", **kwargs)

    def deleteObjectGroup(self, **kwargs):
        return self._request("deleteObjectGroup", **kwargs)

    def showContracts(self, **kwargs):
        return self._request("showContracts", **kwargs)

    def getObjectFeatures(self, **kwargs):
        return self._request("getObjectFeatures", **kwargs)

    def updateContractInfo(self, **kwargs):
        return self._request("updateContractInfo", **kwargs)

    def updateVehicle(self, **kwargs):
        return self._request("updateVehicle", **kwargs)

    def insertObjectGroup(self, **kwargs):
        return self._request("insertObjectGroup", **kwargs)

    def updateDestinationOrderExtern(self, **kwargs):
        return self._request("updateDestinationOrderExtern", **kwargs)

    def cancelOrderExtern(self, **kwargs):
        return self._request("cancelOrderExtern", **kwargs)

    def updateOrderExtern(self, **kwargs):
        return self._request("updateOrderExtern", **kwargs)

    def sendOrderExtern(self, **kwargs):
        return self._request("sendOrderExtern", **kwargs)

    def insertDestinationOrderExtern(self, **kwargs):
        return self._request("insertDestinationOrderExtern", **kwargs)

    def assignOrderExtern(self, **kwargs):
        return self._request("assignOrderExtern", **kwargs)

    def clearOrdersExtern(self, **kwargs):
        return self._request("clearOrdersExtern", **kwargs)

    def showOrderReportExtern(self, **kwargs):
        return self._request("showOrderReportExtern", **kwargs)

    def showOrderWaypoints(self, **kwargs):
        return self._request("showOrderWaypoints", **kwargs)

    def sendDestinationOrderExtern(self, **kwargs):
        return self._request("sendDestinationOrderExtern", **kwargs)

    def reassignOrderExtern(self, **kwargs):
        return self._request("reassignOrderExtern", **kwargs)

    def deleteOrderExtern(self, **kwargs):
        return self._request("deleteOrderExtern", **kwargs)

    def showOrderMessageReport(self, **kwargs):
        return self._request("showOrderMessageReport", **kwargs)

    def setExternalObjectData(self, **kwargs):
        return self._request("setExternalObjectData", **kwargs)

    def insertExternalEventExtern(self, **kwargs):
        return self._request("insertExternalEventExtern", **kwargs)

    def getArchivedReportList(self, **kwargs):
        return self._request("getArchivedReportList", **kwargs)

    def getReportList(self, **kwargs):
        return self._request("getReportList", **kwargs)

    def createReport(self, **kwargs):
        return self._request("createReport", **kwargs)

    def deleteArchivedReport(self, **kwargs):
        return self._request("deleteArchivedReport", **kwargs)

    def sendReportViaMail(self, **kwargs):
        return self._request("sendReportViaMail", **kwargs)

    def getArchivedReport(self, **kwargs):
        return self._request("getArchivedReport", **kwargs)

    def showWorkingTimes(self, **kwargs):
        return self._request("showWorkingTimes", **kwargs)

    def updateLogbookMode(self, **kwargs):
        return self._request("updateLogbookMode", **kwargs)

    def showIOReportExtern(self, **kwargs):
        return self._request("showIOReportExtern", **kwargs)

    def showStandStills(self, **kwargs):
        return self._request("showStandStills", **kwargs)

    def updateWorkState(self, **kwargs):
        return self._request("updateWorkState", **kwargs)

    def getDriverKPIsExtern(self, **kwargs):
        return self._request("getDriverKPIsExtern", **kwargs)

    def getKPIs(self, **kwargs):
        return self._request("getKPIs", **kwargs)

    def showIdleExceptions(self, **kwargs):
        return self._request("showIdleExceptions", **kwargs)

    def showObjectSpeedingEvents(self, **kwargs):
        return self._request("showObjectSpeedingEvents", **kwargs)

    def getCrashLog(self, **kwargs):
        return self._request("getCrashLog", **kwargs)

    def showLogbookReport(self, **kwargs):
        return self._request("showLogbookReport", **kwargs)

    def showAccelerationEvents(self, **kwargs):
        return self._request("showAccelerationEvents", **kwargs)

    def showOptiDriveIndicator(self, **kwargs):
        return self._request("showOptiDriveIndicator", **kwargs)

    def showLogbook(self, **kwargs):
        return self._request("showLogbook", **kwargs)

    def getObjectKPIs(self, **kwargs):
        return self._request("getObjectKPIs", **kwargs)

    def showLogbookHistory(self, **kwargs):
        return self._request("showLogbookHistory", **kwargs)

    def showSpeedingEvents(self, **kwargs):
        return self._request("showSpeedingEvents", **kwargs)

    def showObjectAccelerationEvents(self, **kwargs):
        return self._request("showObjectAccelerationEvents", **kwargs)

    def showTracks(self, **kwargs):
        return self._request("showTracks", **kwargs)

    def getRemainingDrivingTimesEU(self, **kwargs):
        return self._request("getRemainingDrivingTimesEU", **kwargs)

    def showTripSummaryReportExtern(self, **kwargs):
        return self._request("showTripSummaryReportExtern", **kwargs)

    def updateLogbook(self, **kwargs):
        return self._request("updateLogbook", **kwargs)

    def showTrips(self, **kwargs):
        return self._request("showTrips", **kwargs)

    def insertUser(self, **kwargs):
        return self._request("insertUser", **kwargs)

    def removeUserRight(self, **kwargs):
        return self._request("removeUserRight", **kwargs)

    def showUsers(self, **kwargs):
        return self._request("showUsers", **kwargs)

    def resetUserRights(self, **kwargs):
        return self._request("resetUserRights", **kwargs)

    def getUserRights(self, **kwargs):
        return self._request("getUserRights", **kwargs)

    def updateUser(self, **kwargs):
        return self._request("updateUser", **kwargs)

    def deleteUser(self, **kwargs):
        return self._request("deleteUser", **kwargs)

    def changePassword(self, **kwargs):
        return self._request("changePassword", **kwargs)

    def setUserRight(self, **kwargs):
        return self._request("setUserRight", **kwargs)

    def deleteMaintenanceSchedule(self, **kwargs):
        return self._request("deleteMaintenanceSchedule", **kwargs)

    def updateMaintenanceSchedule(self, **kwargs):
        return self._request("updateMaintenanceSchedule", **kwargs)

    def showMaintenanceTasks(self, **kwargs):
        return self._request("showMaintenanceTasks", **kwargs)

    def showMaintenanceSchedules(self, **kwargs):
        return self._request("showMaintenanceSchedules", **kwargs)

    def insertMaintenanceSchedule(self, **kwargs):
        return self._request("insertMaintenanceSchedule", **kwargs)

    def resolveMaintenanceTask(self, **kwargs):
        return self._request("resolveMaintenanceTask", **kwargs)
