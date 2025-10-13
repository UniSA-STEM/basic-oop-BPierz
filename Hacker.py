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
                f"Rig: {self.__rig}\n")

    def __contains__(self, asset):
        return any(a.name == asset for a in self.__inventory)

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
        for asset in self.__inventory:
            if asset.name == search:
                return asset
        return None

    def consume_asset(self, search):

        asset = self.scan_inventory(search)
        if asset:
            self.__inventory.remove(asset)
            return asset
        return None


    def aquire(self):
        if self.__rig is not None:
            print("Rig already aquired")
            return

        token = self.consume_asset("CryptoToken")

        if token is None:
            print("Cannot aquire rig, no CryptoToken found")
            return

        self.__rig = Rig(f"{self.name}'s Rig")
        print(f"Rig successfully activated: {self.name}\n")



    def upgrade_rig(self):
        if self.__rig is None:
            print("No Rig Available")
            return

        patch = self.consume_asset("HardwarePatch")

        if not patch:
            print("Cannot upgrade rig. You have no Hardware Patch available\n")
            return
        self.__rig.upgrade()


    def launch_data_spike(self, target):
        if self.__rig is None:
            print("Cannot launch data spike. You have no Rig available\n")
            return

        spike = self.__rig.consume_asset("DataSpike")
        if spike is None:
            print("Cannot launch data spike. You have no DataSpike available\n")
            return

        target.rig.take_damage()

    def extract_assets(self, target):

        if self.__rig is None:
            print("Cannot extract assets. You have no Rig available\n")
            return

        if not target.rig.broken:
            print("Cannot extract assets. Target's rig is not broken\n")

        self.__inventory.extend(target.rig.release_asset())


    def store_assets(self, quantity, asset):

        if self.__rig is None:
            print("Cannot store assets. You have no Rig available\n")

        if self.__inventory == []:
            print("Cannot store assets. Inventory is empty\n")

        for i in range(quantity):
            asset_obj = self.consume_asset(asset)

            if asset_obj is None:
                print("Cannot store assets. No such asset in inventory\n")
                return

            self.__rig.store_asset(asset_obj)


    def retrieve_assets(self, quantity, asset):
        if self.__rig is None:
            print("Cannot retrieve assets. You have no Rig available\n")

        if self.__rig.storage == []:
            print("Cannot retrieve assets. Rig storage is empty\n")

        for i in range(quantity):
            self.__inventory.append(self.__rig.storage.release_asset(asset))


    def encrypt_asset(self, asset, location):

        combined_assets = [self.__rig.storage + self.__inventory]

        chip = Asset("SecurityChip")

        if chip not in combined_assets:
            print("Cannot perform encryption. No SecurityChips available \n")

        if location == "Inventory":
            for item in self.__inventory:
                if asset == item:
                    asset.encrypted = True

        if location == "Storage":
            for item in self.__rig.storage:
                if asset == item:
                    asset.encrypted = True

