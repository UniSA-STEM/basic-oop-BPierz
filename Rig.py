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
        self.__storage_capacity = 5

    def __repr__(self):
        return self.name

    def __str__(self):
        return (f"---{self.name}---\n"
                f"Rig Damage: {round(self.__damage_counter,2)}\n"
                f"Rig Broken: {self.__broken_state}\n"
                f"Rig Storage: {self.__storage}\n"
                f"Rig Level: {self.__upgrade_level}\n")

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

    def release_unencrypted(self):
        if not self.__broken_state:
            return None

        unencrypted_assets = [asset for asset in self.__storage if not asset.encrypted]
        self.__storage = [asset for asset in self.__storage if asset.encrypted]

        return unencrypted_assets

    def release_asset(self, asset_name):

        unencrypted_assets = [asset for asset in self.__storage if not asset.encrypted]

        if not unencrypted_assets:
            return None

        for item in unencrypted_assets:
            if item.name == asset_name:
                self.__storage.remove(item)
                return item
        return None

    def store_asset(self, asset):
        if len(self.__storage) >= self.__storage_capacity:
            return False
        self.__storage.append(asset)
        return True

    def scan_storage(self, search, consume=True):
        for asset in self.__storage:
            if asset.name == search:
                if consume:
                    self.__storage.remove(asset)
                    return asset
                else:
                    return True
        return False

    def repair(self):
        if self.__damage_counter == 0:
            return False

        self.__damage_counter = 0
        self.__broken_state = False
        return True

    def upgrade(self):
        self.__upgrade_level += 1
        self.__break_threshold += 1
        self.__attack_damage += 1
        self.__storage_capacity += 2

    def take_damage(self):
        effective_damage = 1 - (0.2 * self.__upgrade_level)

        self.__damage_counter += effective_damage

        if self.__damage_counter >= self.__break_threshold:
            self.__broken_state = True

    def generate_asset(self):
        asset_names = ["CryptoToken", "DataSpike", "SecurityChip", "HardwarePatch", "RemovableDrive"]
        random_type = random.choice(asset_names)
        generated_asset = Asset(random_type)

        if len(self.__storage) >= self.__storage_capacity:
            print("Cannot generate asset. Storage capacity reached.")
            return None

        self.__storage.append(generated_asset)
        return print(f"{self.name}: Generated: {generated_asset}")


    def condition(self):

        damage_proportion = self.__damage_counter / self.__break_threshold

        if self.__broken_state:
            condition = "Broken"
            return (f"Rig is {condition} (Level: {self.__upgrade_level})")

        if 0 <= damage_proportion <= 0.25:
            condition = "Pristine"
            return (f"Rig is {condition} (Level: {self.__upgrade_level})")

        if 0.25 <= damage_proportion <= 0.5:
            condition = "Fine"
            return (f"Rig is {condition} (Level: {self.__upgrade_level})")

        if 0.5 <= damage_proportion <= 0.75:
            condition = "Failing"
            return (f"Rig is {condition} (Level: {self.__upgrade_level})")
