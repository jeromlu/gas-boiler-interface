#
# Created on Sun Mar 07 2021
#
# Copyright (c) 2021 Your Company
# Name: Luka Jeromel
#
# ******************************Python imports***********************************
import pathlib
import datetime
from typing import Union

# ******************************Other third party imports************************
import viessmann_communicator

# ******************************My modules***************************************


class DataCollector(object):
    def __init__(self, fname: str) -> None:
        self.__boiler_communication = viessmann_communicator.ViessmanCommunicator()
        self.__fname = None

    def start_data_acquisition(self):
        print(self.__boiler_communication.get_outside_temp())

    def write_to_file(self):
        with self.__fname.open(mode="w") as fhandle:
            fhandle.write("new data")

    def get_boiler(self):
        return self.__boiler_communication
