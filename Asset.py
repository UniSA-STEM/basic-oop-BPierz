"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Asset:
    def __init__(self, type):

        self.__name = type if type in ["CryptoToken", "DataSpike", "SecurityChip", "HardwarePatch", "RemovableDrive"] else "Unknown"

        if type == "CryptoToken":
            self.__description = "Used in battles."
        elif type == "DataSpike":
            self.__description = "Found in rigs and used for extrac�on. "
        elif type == "SecurityChip":
            self.__description = "Used to encrypt or decrypt assets. "
        elif type == "HardwarePatch":
            self.__description = "Used to upgrade rigs."
        else:
            self.__description = "Unknown."

        self.__encrypted = False

    @property
    def encrypted(self):
        return self.__encrypted

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @encrypted.setter
    def encrypted(self, value):
        self.__encrypted = value

    def __str__(self):
        if self.__encrypted:
            return f"{self.__name}: {self.__description} [encrypted]"
        else:
            return f"{self.__name}: {self.__description}"

    def __eq__(self, other):
        if isinstance(other, Asset):
            if self.__name == other.__name:
                return True

    def __repr__(self):
        return self.__name

