"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
import random

class Rig:



    def __init__(self, name):
        self.name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = [Asset("DataSpike"), Asset("DataSpike"), Asset("RemovableDrive")]
        self.__upgrade_level = 0
        self.__attack_damage = 1
        self.__break_threshold = 2

    def __repr__(self):
        return self.name

    def __str__(self):
        return (f"---{self.name}---\n"
                f"Rig Damage: {self.__damage_counter}\n"
                f"Rig Broken: {self.__broken_state}\n"
                f"Rig Storage: {self.__storage}\n"
                f"Rig Level: {self.__upgrade_level}\n\n")

    @property
    def damage_count(self):
        return self.__damage_counter

    @property
    def broken(self):
        return self.__broken_state

    @property
    def storage(self):
        return self.__storage

    @property
    def upgrade_level(self):
        return self.__upgrade_level



    def release_asset(self, asset = None):

        if self.__storage == []:
            return None

        unencrypted_assets =  [asset for asset in self.__storage if not asset.encrypted]

        if asset == None:
            for asset in unencrypted_assets:
                self.__storage.remove(asset)
            return unencrypted_assets

        if asset not in unencrypted_assets:
            return None

        released_asset = asset
        self.__storage.remove(asset)
        return released_asset


    def store_asset(self, asset):
        self.__storage.append(asset)

    def scan_storage(self, search):
        for asset in self.__storage:
            if asset.name == search:
                return asset
        return None

    def consume_asset(self, search):
        if self.__storage == []:
            return None

        asset = self.scan_storage(search)
        if asset:
            self.__storage.remove(asset)
            return asset
        return None


    def repair(self):
        if not self.__broken_state:
            print("No repair needed")

        self.__damage_counter = 0
        self.__broken_state = False

    def upgrade(self):
        self.__upgrade_level += 1
        self.__break_threshold += 1
        self.__attack_damage += 1

    def take_damage(self):
        self.__damage_counter += 1
        if self.__damage_counter >= self.__break_threshold:
            self.__broken_state = True

    def generate_asset(self):
        asset_list = ["CryptoToken", "DataSpike", "SecurityChip", "HardwarePatch", "RemovableDrive"]
        random_type = random.choice(asset_list)
        generated_asset = Asset(random_type)
        self.__storage.append(generated_asset)
        return

    def condition(self):
        if self.__broken_state:
            return f"Rig is Broken"





