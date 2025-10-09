"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset

class Rig:
    def __init__(self, name):
        self.name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = [Asset("DataSpike"), Asset("DataSpike")]
        self.__upgrade_level = 0
        self.__data_spikes = 2
        self.__removable_drive = 1

    def repair(self):
        if not self.__broken_state:
            print("No repair needed")
        else:
            self.__damage_counter = 0
            self.__broken_state = False

    def upgrade(self):
        self.__upgrade_level += 1

