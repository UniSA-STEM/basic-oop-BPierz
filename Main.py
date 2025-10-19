"""
File: main.py
Description: This module runs the Hacker simulation based on the modules in this repository.
             This is where the code is tested.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
from Rig import Rig
from Asset import Asset

# Create two Hacker objects with names as parameters.
Hacker1 = Hacker("Stevie McHacker")
Hacker2 = Hacker("Mike Wazowski")

# Test __str__ method and constructors by printing both Hacker objects.
print(Hacker1)
print(Hacker2)

# Test Hacker.acquire() method by calling on Hacker objects.
Hacker1.aquire()
Hacker2.aquire()

# Test __str___ method and constructor for rig objects.
print(Hacker1.rig)
print(Hacker2.rig)

# Test multiple rig and asset object functionalities by launching Hacker attacks with
# Hacker.launch_data_spike() method.
Hacker1.launch_data_spike(Hacker2)
Hacker1.launch_data_spike(Hacker2)

# Test the state of the second Hacker's rig post attacks.
print(Hacker2.rig)

# Test broken state of Hacker 2's rig and extraction method by extracting assets from Rig.
# Display Rigs and Hackers to confirm.
Hacker1.extract_assets(Hacker2)
print(Hacker2.rig)
print(Hacker1)
print(Hacker1.rig)

# Add a HardwarePatch to test retrieval and rig upgrading.
Hacker1.rig.store_asset(Asset("HardwarePatch"))
print(Hacker1.rig)

# Test Hacker retrieval of asset and upgrading rig.
Hacker1.retrieve_assets(1, "HardwarePatch")
print(Hacker1)
Hacker1.upgrade_rig()
print(Hacker1.rig)

# Test storing and retrieving.
# Add 2 CryptoTokens from storage into Inventory, then store them back.

Hacker1.rig.store_asset(Asset("CryptoToken"))
Hacker1.rig.store_asset(Asset("CryptoToken"))

Hacker1.retrieve_assets(2, "CryptoToken")
print(Hacker1)

# Store 2 DataSpikes into storage.
Hacker1.store_assets(2, "CryptoToken")
print(Hacker1.rig)

# Test encryption.
# Add 2 DataSpikes to Inventory.
Hacker1.rig.store_asset(Asset("DataSpike"))
Hacker1.rig.store_asset(Asset("DataSpike"))
Hacker1.retrieve_assets(2, "DataSpike")
print(Hacker1)

# Encrypt a single DataSpike in Inventory.
Hacker1.inventory.append(Asset("SecurityChip"))
Hacker1.encrypt_asset("DataSpike", "Inventory")
print(Hacker1)

# Store 2 DataSpikes, one is encrypted.
Hacker1.store_assets(2, "DataSpike")
print(Hacker1)
print(Hacker1.rig)

# Test Rig Condition method.
Hacker1.check_rig_condition()
Hacker2.check_rig_condition()

# Add a CryptoToken and test repair.
Hacker2.rig.store_asset(Asset("CryptoToken"))
Hacker2.repair_rig()
Hacker2.check_rig_condition()
print(Hacker2.rig)

# Increase trace level and test exposure and laying low.
Hacker1._Hacker__trace_level = 5

Hacker1.lay_low(2)
print(Hacker1.trace_level)
Hacker1.lay_low(3)
print(Hacker1.trace_level)

# Simulate final battle between Hackers.
# Add DataSpikes for testing.
Hacker2.rig.store_asset(Asset("DataSpike"))
Hacker2.rig.store_asset(Asset("DataSpike"))

# Launch data spikes.
Hacker2.launch_data_spike(Hacker1)
Hacker2.launch_data_spike(Hacker1)
print(Hacker1.rig)

# Extract from broken rig.
Hacker2.rig.store_asset(Asset("RemovableDrive"))
Hacker2.extract_assets(Hacker1)
print(Hacker1.rig)
print(Hacker2)

