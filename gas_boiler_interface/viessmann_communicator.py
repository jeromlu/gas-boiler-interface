#
# Created on Sun Mar 07 2021
#
# Copyright (c) 2021 Your Company
# Name: Luka Jeromel
#
# ******************************Python imports***********************************
# ******************************PyQt5 imports*************************************
# ******************************Other third party imports************************
from PyViCare.PyViCareGazBoiler import GazBoiler


# ******************************My modules***************************************


class ViessmanCommunicator(object):
    def __init__(self, username: str, password: str) -> None:
        self.__gas_boiler = GazBoiler(username, password, "token.save")

    def get_outside_temp(self):
        return self.__gas_boiler.getOutsideTemperature()

    def get_room_temperature(self):
        return self.__gas_boiler.getRoomTemperature()


# t = GazBoiler("luka.jeromel1@gmail.com", "7Z3NPPi$y9JcqV64", "token.save")
# print(t.getDomesticHotWaterConfiguredTemperature())
# print(t.getDomesticHotWaterStorageTemperature())
# print(t.getOutsideTemperature())
# print(t.getRoomTemperature())
# print(t.getSupplyTemperature())
# print(t.getOutsideTemperature())
# print(t.getHeatingCurveShift())
# print(t.getHeatingCurveSlope())
# print(t.getBoilerTemperature())
# print(t.getActiveProgram())
# print(t.getPrograms())

# print(t.getCurrentDesiredTemperature())
# print(t.getMonthSinceLastService())
# print(t.getLastServiceDate())

# print(t.getDesiredTemperatureForProgram("comfort"))
# print(t.getActiveMode())

# print(t.getDesiredTemperatureForProgram("comfort"))
# print(t.setProgramTemperature("comfort", 21))
# print(t.activateProgram("comfort"))
# print(t.setDomesticHotWaterTemperature(59))
# print(t.activateProgram("comfort"))
# print(t.deactivateComfort())
