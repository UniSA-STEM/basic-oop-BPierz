"""
File: Rig.py
Description: This module stores the Rig class which represents a computer object.
             Each instance of Hacker can aquire 1 instance of the Rig class and call its methods to perform actions.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Imported Asset class to create Asset objects inside rig
from Asset import Asset
# Imported random for generating random Asset objects in self.generate_asset() method
import random


class Rig:
    """Represents a computer which generates and stores instances of Asset, used by Hacker objects to perform actions and takes attacks from other Hacker objects."""


    def __init__(self, rig_name):
        """ Initialise a new Rig object with default storage, damage level and upgrade level.
                Args:
                    rig_name (str): The name of the rig.
        """
        # Private attributes for encapsulation, not accessible from outside.
        self.__name = rig_name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = [Asset("DataSpike"), Asset("DataSpike"), Asset("RemovableDrive")]
        self.__upgrade_level = 0
        self.__attack_damage = 1
        self.__break_threshold = 2
        self.__storage_capacity = 5


    def __repr__(self):
        """ Return a representation of Rig object for readability"""
        return self.__name

    def __str__(self):
        """Return a formatted string displaying the rig's statys and contents"""
        return (f"---{self.__name}---\n"
                f"Rig Damage: {round(self.__damage_counter,2)}\n"
                f"Rig Broken: {self.__broken_state}\n"
                f"Rig Storage: {self.__storage}\n"
                f"Rig Level: {self.__upgrade_level}\n")

    # Properties, read only accessors
    @property
    def name(self):
        """ Return the name of the Rig object."""
        return self.__name

    @property
    def damage_count(self):
        """ Return the current damage counter."""
        return self.__damage_counter

    @property
    def broken(self):
        """ Return the current broken state."""
        return self.__broken_state

    @property
    def storage(self):
        """ Return the current storage with asset objects represented."""
        return tuple(self.__storage)

    @property
    def upgrade_level(self):
        """ Return the current upgrade level."""
        return self.__upgrade_level

    def release_unencrypted(self):
        """ Release all unencrypted assets when the rig is broken."""
        # Precondition: rig must be broken, if not, return None.
        if not self.__broken_state:
            return None

        # Split assets into unencrypted to release and encrypted to keep in storage.
        unencrypted_assets = [asset for asset in self.__storage if not asset.encrypted]
        self.__storage = [asset for asset in self.__storage if asset.encrypted]

        if not unencrypted_assets:
            return None

        # Return only unencrypted, rest stay in storage.
        return unencrypted_assets

    def release_asset(self, asset_name):
        """ Release a single, unencrypted asset from the rig by name
            Args:
                asset_name (str): The name of the asset.
                """
        for i, item in enumerate(self.__storage):
            if not item.encrypted and item.name == asset_name:
                return self.__storage.pop(i)
        return None

    def store_asset(self, asset):
        """Add an asset to Rig storage if capacity allows.
            Args:
                asset (Asset): The asset to add.
                """

        if len(self.__storage) >= self.__storage_capacity:
            return False
        self.__storage.append(asset)
        return True

    def scan_storage(self, search, consume=True):
        """ Search for an asset in storage and optionally remove it.
            Args:
                search (str): The asset name to search for.
                consume (bool): If true, consume the asset.
                """
        # Precondition: search must be a valid asset type name
        for asset in self.__storage:
            if asset.name == search:
                if consume:
                    self.__storage.remove(asset)
                    return asset
                return True
        # Return None if consuming mode, False if not
        return None if consume else False

    def repair(self):
        """ Repair the rig and reset broken state."""
        if self.__damage_counter == 0:
            return False

        self.__damage_counter = 0
        self.__broken_state = False
        return True

    def upgrade(self):
        """ Upgrade the rig by one upgrade level. Increase durability, attack damage and storage capacity."""
        # Arbitrary limit of 5 upgrades to prevent runaway stats
        if self.__upgrade_level >= 5:
            return None
        # Set attributes higher as upgrade level increases
        self.__upgrade_level += 1
        self.__break_threshold += 1
        self.__attack_damage += 1
        self.__storage_capacity += 2
        return True

    def take_damage(self):
        """Increase damage counter reduced by upgrade level and set to broken if threshold reached."""
        # Each upgrade level reduces effective damage taken by 20%
        effective_damage = 1 - (0.2 * self.__upgrade_level)

        self.__damage_counter += effective_damage

        # Rig becomes broken once damage meets or exceeds break threshold
        if self.__damage_counter >= self.__break_threshold:
            self.__broken_state = True

    def generate_asset(self, time):
        """ Generate a random asset per time(day) and store in rig storage.
            Args:
                time (int): The number of days that the Rig generates assets in.
                            The rig generates 1 per day.
                            Therefore time == number of assets to generate."""

        # Handle case if time is not passed in as an integer. I.e. number of days.
        if not isinstance(time, int):
            print(f"Time must be a whole number of days.")
            return None
        # Handle case if time is less than 0.
        if time <= 0:
            print (f" Time must be greater than 0 days.")
            return None

        # Make a reference list of names that can be passed in to create assets.
        asset_names = ["CryptoToken", "DataSpike", "SecurityChip", "HardwarePatch", "RemovableDrive"]

        # For every day passed in as time, create one asset.
        for i in range(time):

            # Generate a new asset and attempt to store it.
            random_type = random.choice(asset_names)
            generated_asset = Asset(random_type)
            stored_asset = self.store_asset(generated_asset)

            # Handle case if storage is full, terminate asset generation.
            if not stored_asset:
                print(f"{self.__name}: Cannot generate assets. Storage capacity reached.")
                return None

            # Notification for asset generation.
            print(f"{self.__name}: Generated: {generated_asset}")


    def condition(self):
        """Return a descriptive string indicating the rig’s current condition."""

        # Damage proportion is relative to break threshold (increases with level)
        # and determines condition category.
        damage_proportion = self.__damage_counter / self.__break_threshold

        if self.__broken_state:
            condition = "Broken"
            return (f"{self.__name} is {condition} (Level: {self.__upgrade_level})")

        if 0 <= damage_proportion <= 0.25:
            condition = "Pristine"
            return (f"{self.__name} is {condition} (Level: {self.__upgrade_level})")

        if 0.25 <= damage_proportion <= 0.5:
            condition = "Fine"
            return (f"{self.__name} is {condition} (Level: {self.__upgrade_level})")

        if 0.5 <= damage_proportion <= 0.75:
            condition = "Failing"
            return (f"{self.__name} is {condition} (Level: {self.__upgrade_level})")
