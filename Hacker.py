"""
File: Hacker.py
Description: Defines the Hacker class. Hacker objects perform actions using Rig and Asset objects.
             Hackers own a single Rig object and interact with it. Hackers launch attacks on other Hacker objects.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig


class Hacker:
    """ Represents a hacker who manages assets and a rig, performs attacks
        and accumulates a trace level when performing risky actions."""

    def __init__(self, name):
        """ Creates a new Hacker object with a trace level, an inventory with a CryptoToken Asset
            and a rig with no Rig object yet.
            Args:
                name (str): The name of the Hacker.
                """
        self.__name = name
        self.__trace_level = 0
        self.__inventory = [Asset("CryptoToken")]
        self.__rig = None

    def __str__(self):
        """ Returns a string representation of the Hacker object."""
        # Guard against if rig is still not acquired.
        rig_name = self.__rig.name if self.__rig else "None"

        return (f"\nName: {self.__name}\n"
                f"Trace level: {self.__trace_level}\n"
                f"Inventory: {self.__inventory}\n"
                f"Rig: {rig_name}\n")

    def __contains__(self, asset):
        """ Return True if an asset with this name exists in the inventory."""
        return any(a.name == asset for a in self.__inventory)

    @property
    def name(self):
        """ Returns the name of the Hacker."""
        return self.__name

    @property
    def rig(self):
        """ Returns the Rig object."""
        return self.__rig

    @property
    def trace_level(self):
        """ Returns the trace level of the Hacker."""
        return self.__trace_level

    @property
    def inventory(self):
        """ Returns the inventory of the Hacker."""
        return self.__inventory


    def scan_inventory(self, search, consume=True):
        """ Search inventory for Asset name and remove if consume = True
            Args:
                search (str): The search string to search for.
                consume (bool): If True, consume the search string."""
        # Scan for and return first asset in inventory with name = search.
        for asset in self.__inventory:
            if asset.name == search:
                if consume:
                    self.__inventory.remove(asset)
                    return asset

                return True
        # Return None if in consume mode, else False.
        return None if consume else False

    def exposed(self):
        """ Returns True if the hacker is exposed."""
        if self.__trace_level >= 5:
            return True
        return False

    def aquire(self):
        """ Acquires a personal Rig object for the Hacker by consuming a CryptoToken
             from Inventory and stores under rig attribute."""
        # Handle precondition if Hacker has no Rig.
        if self.__rig is not None:
            print("Rig already aquired")
            return
        # Call method to scan for and consume asset as cost of action.
        token = self.scan_inventory("CryptoToken", True)

        # Handle case if asset not available.
        if token is None:
            print("Cannot aquire rig, no CryptoToken found")
            return
        # Create Rig object and pass in a name based on Hacker's name as a parameter.
        self.__rig = Rig(f"{self.__name}'s Rig")
        # Confirm Rig acquisition.
        print(f"Rig successfully activated: {self.__name}\n")

    def upgrade_rig(self):
        """ Upgrades the Hacker's Rig if present and consumes a HardwarePatch from Inventory."""
        # Handle precondition if no Rig available.
        if self.__rig is None:
            print("No Rig Available")
            return
        # Consume asset object as cost of action using scan_inventory method.
        patch = self.scan_inventory("HardwarePatch", True)

        # Handle case if no asset available.
        if not patch:
            print(f"Cannot upgrade rig. {self.__name} has no Hardware Patch in Inventory\n")
            return

        # Handle case if maximum upgrade level reached, rig method returns None.
        if self.__rig.upgrade() is None:
            print(f"Cannot upgrade rig {self.__name}. Maximum upgrade level reached.\n")
            return

        # Confirm success
        print(f"Rig successfully upgraded to level {self.__rig.upgrade_level}: {self.name} \n")

    def launch_data_spike(self, target):
        """ Launch an attack on a target Hacker. Consume a DataSpike from Storage and increase trace level.
            Args:
                target (Hacker): The targeted Hacker."""
        # Handle precondition if Hacker has no Rig.
        if self.__rig is None:
            print(f"Cannot launch data spike. {self.__name} has no Rig available\n")
            return
        # Consume asset object from storage calling rig method as cost of action.
        spike = self.__rig.scan_storage("DataSpike", True)

        # Handle case if no cost of action object available.
        if not spike:
            print(f"Cannot launch data spike. {self.__name} has no DataSpike available in Storage\n")
            return

        # Block action if Hacker is exposed.
        if self.exposed():
            print(f"Cannot launch data spike. {self.__name} is exposed\n")
            return

        # Call take_damage on target rig as a result of launching data spike action.
        # Increase trace level as action consequence.
        target.rig.take_damage()
        self.__trace_level += 1

        # Confirm successful attack.
        print(f"Data Spike launched successfully by {self.__name} on {target.name}\n")

    def extract_assets(self, target):
        """ Extract all unencrypted assets from a Hacker whose Rig is broken.
            Consumes a RemovableDrive.
            Args:
                target (Hacker): The targeted Hacker."""
        
        # Handle precondition if Hacker doesn't have rig. 
        if self.__rig is None:
            print(f"Cannot extract assets. {self.__name} has no Rig available\n")
            return
        
        # Handle case if rig is broken. Cannot perform action
        if not target.rig.broken:
            print(f"Cannot extract assets. {target.name} rig is not broken\n")
            return
        
        # Handle case if Hacker exposed, cannot perform action. 
        if self.exposed():
            print(f"Cannot extract assets. {self.__name} is exposed\n")
            return
        
        # Consume asset cost of action from inventory. 
        found_drive = self.scan_inventory("RemovableDrive", True)
        # If not found in Inventory, search in Rig Storage as action allows for consump
        if not found_drive:
            found_drive = self.__rig.scan_storage("RemovableDrive", True)

        if not found_drive:
            print(f"Cannot extract asset. {self.__name} has no RemovableDrive available\n")
            return

        # Get all unencrypted assets form target's broken rig by calling method.
        released_assets = target.rig.release_unencrypted()
        # If there are none, output information to screen.
        if not released_assets:
            print(f"There are no assets available for extraction from: {target.rig.name}.\n")
            return
        # Add extracted assets to inventory.
        self.__inventory.extend(released_assets)
        self.__trace_level += 1
        print (f"Successfully extracted unencrypted assets from {target.name}'s Rig\n")

    def store_assets(self, quantity, asset_name):
        """ From inventory, stores a number of chosen Asset types in Hacker's Rig's storage.
         Args:
             quantity (int): The number of chosen assets.
             asset_name (str): The name of the chosen asset."""
        # Handle precondition if Hacker has no Rig.
        if self.__rig is None:
            print(f"Cannot store assets. {self.__name} has no Rig available\n")
            return

        # Handle precondition of empty inventory, no assets to store at all.
        if not self.__inventory:
            print("Cannot store assets. Inventory is empty\n")
            return

        # Handle error if quantity of assets to move is negative or zero.
        if quantity <= 0:
            print("Quantity of assets to store must be positive\n")
            return

        # Create a list of storable asset positions, assets pass condition of asset.name == asset_name parameter and are not encrypted.
        can_store_idx = [i for i, a in enumerate(self.__inventory) if a.name == asset_name and not a.encrypted]
        # Boolean flag to see if there are any assets of the same type but encrypted in inventory.
        has_encrypted_same_type = any(a.name == asset_name and a.encrypted for a in self.__inventory)

        # Handle case if all assets of asset.name == asset_name are unavailable for storing
        # or no such assets in inventory.
        if not can_store_idx:
            if has_encrypted_same_type:
                print(f"Every {asset_name} is encrypted. Decrypt before trying to store\n")
            else:
                print(f"Cannot store assets. No {asset_name}s in inventory\n")
            return

        # From the assets available for storing, make a selection based on passed in quantity parameter.
        to_move_idx = can_store_idx[:quantity]
        moved = 0

        # Append each asset to inventory using store_asset rig method.
        # Handle case if cannot append to storage because storage capacity has been reached.
        for idx in reversed(to_move_idx):
            asset = self.__inventory[idx]
            if not self.__rig.store_asset(asset):
                print(f"Cannot store any more assets. Storage capacity reached\n")
                break
            # Remove asset from inventory and count number moved.
            self.__inventory.pop(idx)
            moved += 1

        # Report if fewer assets than asked of the method were moved.
        # Otherwise confirm success.
        if moved == 0:
            print("Cannot store any more assets. Storage capacity reached\n")
        elif moved < quantity:
            if has_encrypted_same_type:
                print(f"Some {asset_name}(s) encrypted. Stored {moved} of {quantity} {asset_name}(s).\n")
            else:
                print(f"Stored only {moved} of {quantity} {asset_name}(s) (capacity or availability).\n")
        else:
            print(f"Successfully stored {moved} {asset_name}(s) in rig storage.\n")

    def retrieve_assets(self, quantity, asset_name):
        """ From Hacker's Rig's storage, retrieves a number of chosen Asset types and stores in Inventory.
         Args:
             quantity (int): The number of chosen assets.
             asset_name (str): The name of the chosen asset."""
        # Handle precondition if Hacker has no Rig.
        if self.__rig is None:
            print(f"Cannot retrieve assets. {self.__name} has no Rig available\n")
            return
        
        # Handle error if quantity less than or equal to zero.
        if quantity <= 0:
            print("Quantity of assets to retrieve must be positive\n")
            return
        
        # Create a list of retrievable assets from storage, assets pass condition of 
        # asset.name == asset_name parameter and are not encrypted.
        storage = self.__rig.storage
        can_retrieve = [a for a in storage if a.name == asset_name and not a.encrypted]
        # Create a list of same type but encrypted assets for comparison and edge cases.
        encrypted_same_type = [a for a in storage if a.name == asset_name and a.encrypted]

        # Handle case if all assets of asset.name == asset_name are unavailable for retrieval
        # or no such assets in inventory.
        if not can_retrieve:
            if encrypted_same_type:
                print(
                    f"Cannot retrieve assets. All {asset_name}(s) in storage are encrypted. Decrypt before retrieving\n")
            else:
                print(f"Cannot retrieve assets. No {asset_name}(s) in storage\n")
            return

        # From the assets available for retrieval, make a selection based on passed in quantity parameter.
        to_move = can_retrieve[:quantity]
        retrieved = []
        
        # Call release asset method from rig for every element in to_move and collect in retrieved.
        for _ in to_move:
            a = self.__rig.release_asset(asset_name)
            if a is None:
                break
            retrieved.append(a)
        # If retrieved not populated, no assets available for retrieval from storage. 
        if not retrieved:
            print(f"Cannot retrieve {asset_name}. Decrypt before retrieving\n")
            return
        # Populate inventory with retrieved assets. 
        self.__inventory.extend(retrieved)

        # Handle cases where the number of moved assets is lower than requested. 
        moved = len(retrieved)
        if moved < quantity:
            if encrypted_same_type:
                print(f"Some {asset_name}(s) are encrypted. Retrieved {moved} of {quantity} {asset_name}(s).\n")
            else:
                print(f"Retrieved only {moved} of {quantity} {asset_name}(s) (not enough in storage).\n")
        # Confirm action success. 
        else:
            print(f"Successfully retrieved {moved} {asset_name}(s) from rig storage.\n")



    def encrypt_asset(self, asset_name, location):
        """ From Hacker's Rig's storage or Inventory, encrypts a single Asset.
            Consumes one SecurityChip.
            Args:
                asset_name (str): The name of the chosen asset.
                location (str): The location in which the asset is to be found (Storage or Inventory)."""
        # Block action if Hacker exposed.
        if self.exposed():
            print(f"Cannot perform encryption. {self.__name} is exposed\n")
            return
        # Block action if wrong method input.
        if location not in ["Storage", "Inventory"]:
            print(f"Location of asset {location} is invalid. Choose 'Storage' or 'Inventory'\n")
            return
        # Look for and consume cost of action asset.
        found_chip = self.scan_inventory("SecurityChip", True)

        # Handle case if asset not available.
        if not found_chip:
            found_chip = self.__rig.scan_storage("SecurityChip", True)
        if not found_chip:
            print(f"Cannot encrypt asset. {self.__name} has no Security Chip available\n")
            return

        # Search for available to encrypt assets in Inventory. If none available, print message.
        if location == "Inventory":
            encryptable_assets = [item for item in self.__inventory if not item.encrypted and item.name == asset_name]
            if not encryptable_assets:
                print(f"Cannot encrypt asset. No encryptable {asset_name}(s) found in inventory\n")
                return

            # Encrypt the first encryptable asset found in inventory.
            for item in encryptable_assets:
                item.encrypted = True
                print(f"{item.name} in Inventory successfully encrypted")
                return
        # Search for available to encrypt assets in Storage. If none available, print message.
        if location == "Storage":
            encryptable_assets = [item for item in self.__rig.storage if not item.encrypted and item.name == asset_name]
            if not encryptable_assets:
                print(f"Cannot encrypt asset. No encryptable {asset_name}(s) found in storage\n")
                return

            # Encrypt first available asset found in Storage.
            for item in encryptable_assets:
                item.encrypted = True
                print(f"{item.name} in Storage successfully encrypted")
                return


    def decrypt_asset(self, asset_name, location):
        """ From Hacker's Rig's storage or Inventory, decrypts a single Asset.
            Consumes one SecurityChip.
            Args:
                asset_name (str): The name of the chosen asset.
                location (str): The location in which the asset is to be found (Storage or Inventory)."""
        # Handle case if Hacker exposed.
        if self.exposed():
            print(f"Cannot perform decryption. {self.__name} is exposed\n")
            return

        # Block action if wrong method input.
        if location not in ["Storage", "Inventory"]:
            print(f"Location of asset {location} is invalid. Choose 'Storage' or 'Inventory'\n")
            return

        # Look for cost of action asset SecurityChip in Inventory and Storage.
        found_chip = self.scan_inventory("SecurityChip", True)

        # Handle case if cost of action asset not found in either location.
        if not found_chip:
            found_chip = self.__rig.scan_storage("SecurityChip", True)
        if not found_chip:
            print(f"Cannot encrypt asset. {self.__name} has no Security Chip available\n")
            return

        # Search for available to decrypt assets in Inventory. If none available, print message.
        if location == "Inventory":
            decryptable_assets = [item for item in self.__inventory if item.encrypted and item.name == asset_name]
            if not decryptable_assets:
                print(f"Cannot decrypt asset. No decryptable {asset_name} found in storage\n")
                return
            # Decrypt first available asset in Inventory.
            for item in decryptable_assets:
                item.decrypted = True
                print(f"{item.name} in Inventory successfully decrypted")
                return

        # Search for available to decrypt assets in Inventory. If none available, print message.
        if location == "Storage":
            decryptable_assets = [item for item in self.__rig.storage if item.encrypted and item.name == asset_name]
            if not decryptable_assets:
                print(f"Cannot decrypt asset. No decryptable {asset_name} found in storage\n")
                return
            # Decrypt first available asset in Inventory.
            for item in decryptable_assets:
                item.decrypted = True
                print(f"{item.name} in Inventory successfully decrypted")
                return


    def repair_rig(self):
        """If damaged, repair the Hacker's Rig by consuming a CryptoToken from Inventory or Storage (Inventory first)."""
        # Handle case if Hacker has no rig.
        if self.__rig is None:
            print(f"Cannot repair rig. {self.__name} has no Rig available\n")
            return
        # Search for cost of action token in both Inventory and Storage and consume if found.
        token = self.scan_inventory("CryptoToken", True)

        # If not found in either, report error.
        if not token:
            token = self.__rig.scan_storage("CryptoToken", True)
        if not token:
            print(f"Cannot repair rig. {self.__name} has no CryptoTokens available\n")
            return

        # Call rig.repair() method to repair own rig.
        repair_success = self.__rig.repair()
        # If method returns False, the rig does not need repair. Print message.
        if not repair_success:
            print("Rig doesn't need repair\n")
            return
        # After all checks, report action success.
        print(f"Rig successfully repaired: {self.__rig.name}\n")


    def check_rig_condition(self):
        """ Return the current, readable condition of the Hacker's Rig, if present."""

        # Handle case if no rig is available.
        if self.__rig is None:
            print(f"Cannot check rig condition. {self.__name} has no Rig available\n")
            return
        # Print the call of  rig.condition() method to display rig condition output.
        print(self.__rig.condition())


    def lay_low(self, time):
        """ Reduce trace level by one and report exposure status changes
            Args:
                time (int): The number of days that the Hacker is laying low.
                            Expose level goes down by 1 each day. """

        # Report if action is redundant as trace level is not above 0.
        if self.__trace_level <= 0:
            print(f"No point in laying low. {self.__name} is untraceable")
            return
        # Check if time parameter passed in is whole number representing number of days.
        if not isinstance(time, int):
            print(f"Time must be a whole number. How many days do you want {self.__name} to be laying low?")
            return
        # Handle case if time parameter is less than 0.
        if time <= 0:
            print(f"Time must be greater than 0.")
            return

        # Lower attribute trace level for every day that Hacker is laying low.
        for i in range(time):
            self.__trace_level -= 1

            # Terminate if Hacker is no longer exposed.
            if self.__trace_level == 4:
                print(f"{self.__name} is no longer exposed. Current trace level: {self.__trace_level}\n")
                return

            # Report successful lowering of trace level.
            print(f"{self.__name} is laying low, current trace level: {self.__trace_level}\n")
