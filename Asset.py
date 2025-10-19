"""
File: Asset.py
Description: This module stores the Asset Class. Instances of this class are used as "currency" for actions performed by the Rig and Hacker classes. Instances of Asset are stored in Hacker.inventory and Rig.storage.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Misconduct Policy.
"""


# Creating class Asset
class Asset:
    """ Represents a digital asset used by hackers and rigs.
    Assets are: CryptoTokens, DataSpikes, SecurityChips, HardwarePatches and RemovableDrives.
    Assets have a name, description and encryption status which determines whether an asset can be moved. """

    # Class variables constant across all instances.

    ASSET_NAMES = ["CryptoToken", "DataSpike", "SecurityChip", "HardwarePatch",
                   "RemovableDrive"]  # Acceptable Asset object names stored here.
    DESCRIPTIONS = {
        "CryptoToken": "Used to acquire and repair rigs",
        "DataSpike": "Used in battles",
        "SecurityChip": "Used to encrypt or decrypt assets",
        "HardwarePatch": "Used to upgrade rigs",
        "RemovableDrive": "Found in rigs and used for extraction",
    }  # A dictionary of descriptions tied to Asset object names.

    def __init__(self, asset_name):
        """ Initialise a new Asset.
        Args:
            asset_name (str): The name of the asset.
                                Must be a valid name. """
        # Raises error if invalid asset_name is passed in.
        if asset_name not in Asset.ASSET_NAMES:
            raise ValueError(f"Invalid asset name: {asset_name}")

        # Assign name if name passes test above
        self.__name = asset_name

        # Assign description based on name and from class variable.
        self.__description = self.DESCRIPTIONS[asset_name]

        # Default asset state is unencrypted.
        self.__encrypted = False

    # Read only properties for reading private attributes
    @property
    def encrypted(self):
        """Returns True if the asset is encrypted, False otherwise."""
        return self.__encrypted

    @property
    def name(self):
        """Returns the name of the asset."""
        return self.__name

    # Write property for setting encryption status.
    @encrypted.setter
    def encrypted(self, value):
        """Sets the encrypted attribute."""
        self.__encrypted = value

    def __str__(self):
        """Returns a string representation of the asset."""
        if self.__encrypted:
            return f"{self.__name}: {self.__description} [Encrypted]"
        else:
            return f"{self.__name}: {self.__description}"

    def __eq__(self, other):
        """ Compare two assets or an asset and a string for equality."""
        if isinstance(other, Asset):
            return self.__name == other.__name
        elif isinstance(other, str):
            return self.__name == other
        return False

    def __repr__(self):
        """Returns a developer friendly representation of the asset."""
        if self.__encrypted:
            return f"{self.__name} [E]"
        else:
            return f"{self.__name}"
