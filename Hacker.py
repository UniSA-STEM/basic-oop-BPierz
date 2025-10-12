"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig


class Hacker:
    def __init__(self, name):
        self.name = name
        self.__trace_level = 0
        self.__inventory = [Asset("CryptoToken")]
        self.__rig = None
        self.__exposed = False if self.__trace_level < 5 else True

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Trace level: {self.__trace_level}\n"
                f"Inventory: {self.__inventory}\n"
                f"Rig: {self.__rig}\n\n")

    def __contains__(self, asset):
        for item in self.__inventory:
            if item == asset: return True
        return False

    @property
    def rig(self):
        return self.__rig

    @property
    def trace_level(self):
        return self.__trace_level

    @property
    def inventory(self):
        return self.__inventory

    @property
    def exposed(self):
        return self.__exposed




    def scan_inventory(self, search):
        asset_location = []


        for index in range(len(self.__inventory)):
            if self.__inventory[index] == search:
                asset_location.append(self.__inventory[index])

        asset_amount = len(asset_location)
        print(f" {self.name} has {asset_amount} {search}")


    def aquire(self):
        if self.__rig is not None:
            print("Rig already aquired")

        else:
            if "CryptoToken" in self.__inventory:
                self.__inventory.remove("CryptoToken")
                self.__rig = Rig(f"{self.name}'s Rig")
                print(f"Rig successfully activated: {self.name}\n")


    def upgrade_rig(self):
        if self.__rig is None:
            print("No Rig Available")
        else:
            if "HardwarePatch" not in self.__inventory:
                print("Cannot upgrade rig. You have no Hardware Patch available\n")

            else:
                self.__inventory.remove("HardwarePatch")
                self.__rig.upgrade()


    def launch_data_spike(self, target):
        if self.__rig is None:
            print("Cannot launch data spike. You have no Rig available\n")
        self.__rig.consume_asset("DataSpike")
        target.rig.take_damage()

    def extract_assets(self, target):

        if self.__rig is None:
            print("Cannot extract assets. You have no Rig available\n")

        if target.rig.broken:
            self.__inventory.extend(target.rig.release_unencrypted())
        else:
            print ("Cannot extract assets. Target's rig is not broken\n")

