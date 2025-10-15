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
        self.__name = name
        self.__trace_level = 0
        self.__inventory = [Asset("CryptoToken")]
        self.__rig = None

    def __str__(self):
        return (f"\nName: {self.__name}\n"
                f"Trace level: {self.__trace_level}\n"
                f"Inventory: {self.__inventory}\n"
                f"Rig: {self.__rig.name}\n")

    def __contains__(self, asset):
        return any(a.name == asset for a in self.__inventory)

    @property
    def name(self):
        return self.__name

    @property
    def rig(self):
        return self.__rig

    @property
    def trace_level(self):
        return self.__trace_level

    @property
    def inventory(self):
        return self.__inventory


    def scan_inventory(self, search, consume=True):
        for asset in self.__inventory:
            if asset.name == search:
                if consume:
                    self.__inventory.remove(asset)
                    return asset
                else:
                    return True
        return False

    def exposed(self):
        if self.__trace_level >= 5:
            return True
        return False

    def aquire(self):
        if self.__rig is not None:
            print("Rig already aquired")
            return

        token = self.scan_inventory("CryptoToken", True)

        if token is None:
            print("Cannot aquire rig, no CryptoToken found")
            return

        self.__rig = Rig(f"{self.__name}'s Rig")
        print(f"Rig successfully activated: {self.__name}\n")

    def upgrade_rig(self):
        if self.__rig is None:
            print("No Rig Available")
            return

        patch = self.scan_inventory("HardwarePatch", True)

        if not patch:
            print(f"Cannot upgrade rig. {self.__name} has no Hardware Patch in Inventory\n")
            return

        self.__rig.upgrade()
        print(f"Rig successfully upgraded to level {self.__rig.upgrade_level}: {self.name} \n")

    def launch_data_spike(self, target):
        if self.__rig is None:
            print(f"Cannot launch data spike. {self.__name} has no Rig available\n")
            return

        spike = self.__rig.scan_storage("DataSpike", True)

        if not spike:
            print(f"Cannot launch data spike. {self.__name} has no DataSpike available in Storage\n")
            return

        if self.exposed():
            print(f"Cannot launch data spike. {self.__name} is exposed\n")
            return

        target.rig.take_damage()
        self.__trace_level += 1
        print(f"Data Spike launched successfully by {self.__name} on {target.name}\n")

    def extract_assets(self, target):

        if self.__rig is None:
            print(f"Cannot extract assets. {self.__name} has no Rig available\n")
            return

        if not target.rig.broken:
            print(f"Cannot extract assets. {target.name} rig is not broken\n")
            return

        if self.exposed():
            print(f"Cannot extract assets. {self.__name} is exposed\n")
            return

        found_drive = self.scan_inventory("RemovableDrive", True)

        if not found_drive:
            found_drive = self.__rig.scan_storage("RemovableDrive", True)

        if not found_drive:
            print(f"Cannot extract asset. {self.__name} has no RemovableDrive available\n")
            return

        self.__inventory.extend(target.rig.release_unencrypted())
        self.__trace_level += 1
        print (f"Successfully extracted unencrypted assets from {target.name}'s Rig\n")

    def store_assets(self, quantity, asset_name):

        if self.__rig is None:
            print(f"Cannot store assets. {self.__name} has no Rig available\n")
            return

        if not self.__inventory:
            print("Cannot store assets. Inventory is empty\n")
            return

        if quantity <= 0:
            print("Quantity of assets to store must be positive\n")
            return

        can_store = [asset for asset in self.__inventory if asset.name == asset_name and not asset.encrypted]
        encrypted_same_type = [a for a in self.__inventory if a.name == asset_name and a.encrypted]

        if not can_store:
            if encrypted_same_type:
                print(f"Every {asset_name} is encrypted. Decrypt before trying to store\n")
            else:
                print(f"Cannot store assets. No {asset_name}s in inventory\n")
            return

        to_move = can_store[:quantity]
        moved = 0

        for asset in to_move:
            if not self.__rig.store_asset(asset):
                print(f"Cannot store any more assets. Storage capacity reached\n")
                return

            self.__inventory.remove(asset)
            moved += 1

        if moved < quantity and encrypted_same_type:
            print(f"Some {asset_name}(s) encrypted. Stored {moved} of {quantity} {asset_name}(s).\n")
        else:
            print(f"Successfully stored {moved} {asset_name}(s) in rig storage.\n")

    def retrieve_assets(self, quantity, asset_name):
        if self.__rig is None:
            print(f"Cannot retrieve assets. {self.__name} has no Rig available\n")
            return

        if quantity <= 0:
            print("Quantity of assets to retrieve must be positive\n")
            return

        storage = self.__rig.storage
        can_retrieve = [a for a in storage if a.name == asset_name and not a.encrypted]
        encrypted_same_type = [a for a in storage if a.name == asset_name and a.encrypted]

        if not can_retrieve:
            if encrypted_same_type:
                print(
                    f"Cannot retrieve assets. All {asset_name}(s) in storage are encrypted. Decrypt before retrieving\n")
            else:
                print(f"Cannot retrieve assets. No {asset_name}(s) in storage\n")
            return


        to_move = can_retrieve[:quantity]
        retrieved = []

        for _ in to_move:
            a = self.__rig.release_asset(asset_name)
            if a is None:
                break
            retrieved.append(a)

        if not retrieved:
            print(f"Cannot retrieve {asset_name}. Decrypt before retrieving\n")
            return

        self.__inventory.extend(retrieved)

        moved = len(retrieved)
        if moved < quantity:
            if encrypted_same_type:
                print(f"Some {asset_name}(s) are encrypted. Retrieved {moved} of {quantity} {asset_name}(s).\n")
            else:
                print(f"Retrieved only {moved} of {quantity} {asset_name}(s) (not enough in storage).\n")
        else:
            print(f"Successfully retrieved {moved} {asset_name}(s) from rig storage.\n")



    def encrypt_asset(self, asset_name, location):
        if self.exposed():
            print(f"Cannot perform encryption. {self.__name} is exposed\n")
            return

        found_chip = self.scan_inventory("SecurityChip", True)

        if not found_chip:
            found_chip = self.__rig.scan_storage("SecurityChip", True)
        if not found_chip:
            print(f"Cannot encrypt asset. {self.__name} has no Security Chip available\n")
            return

        if location == "Inventory":
            encryptable_assets = [item for item in self.__inventory if not item.encrypted and item.name == asset_name]
            if not encryptable_assets:
                print(f"Cannot encrypt asset. No encryptable {asset_name}(s) found in inventory\n")
                return

            for item in encryptable_assets:
                item.encrypted = True
                print(f"{item.name} in Inventory successfully encrypted")
                return

        if location == "Storage":
            encryptable_assets = [item for item in self.__rig.storage if not item.encrypted and item.name == asset_name]
            if not encryptable_assets:
                print(f"Cannot encrypt asset. No encryptable {asset_name}(s) found in storage\n")
                return

            for item in encryptable_assets:
                item.encrypted = True
                print(f"{item.name} in Storage successfully encrypted")
                return


    def decrypt_asset(self, asset_name, location):
        if self.exposed():
            print(f"Cannot perform decryption. {self.__name} is exposed\n")

        found_chip = self.scan_inventory("SecurityChip", True)
        if not found_chip:
            found_chip = self.__rig.scan_storage("SecurityChip", True)
        if not found_chip:
            print(f"Cannot encrypt asset. {self.__name} has no Security Chip available\n")
            return

        if location == "Inventory":
            decryptable_assets = [item for item in self.__inventory if item.encrypted and item.name == asset_name]
            if not decryptable_assets:
                print(f"Cannot decrypt asset. No decryptable {asset_name} found in storage\n")
                return
            for item in decryptable_assets:
                item.decrypted = True
                print(f"{item.name} in Inventory successfully decrypted")
                return

        if location == "Storage":
            decryptable_assets = [item for item in self.__rig.storage if item.encrypted and item.name == asset_name]
            if not decryptable_assets:
                print(f"Cannot decrypt asset. No decryptable {asset_name} found in storage\n")
                return

            for item in decryptable_assets:
                item.decrypted = True
                print(f"{item.name} in Inventory successfully decrypted")
                return


    def repair_rig(self):
        if self.__rig is None:
            print(f"Cannot repair rig. {self.__name} has no Rig available\n")
            return

        token = self.scan_inventory("CryptoToken", True)
        if not token:
            token = self.__rig.scan_storage("CryptoToken", True)
        if not token:
            print(f"Cannot repair rig. {self.__name} has no CryptoTokens available\n")
            return

        repair_success = self.__rig.repair()
        if not repair_success:
            print("Rig doesn't need repair\n")
            return

        print(f"Rig successfully repaired: {self.__rig.name}\n")


    def check_rig_condition(self):
        if self.__rig is None:
            print(f"Cannot check rig condition. {self.__name} has no Rig available\n")
            return

        print(self.__rig.condition())


    def lay_low(self):
        if self.__trace_level <= 0:
            print(f"No point in laying low. {self.__name} is untraceable")
            return

        self.__trace_level -= 1

        if self.__trace_level == 4:
            print(f"{self.__name} is no longer exposed. Current trace level: {self.__trace_level}\n")
            return

        print(f"{self.__name} is laying low, current trace level: {self.__trace_level}\n")
