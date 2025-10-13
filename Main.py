"""
File: main.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Hacker import Hacker

Hacker1 = Hacker("Stevie McHacker")
Hacker2 = Hacker("Mike Wazowski")

Hacker1.aquire()
Hacker2.aquire()
print(Hacker1.rig)
print(Hacker2.rig)


Hacker1.launch_data_spike(Hacker2)
Hacker1.launch_data_spike(Hacker2)

print(Hacker2.rig)
Hacker1.extract_assets(Hacker2)
print(Hacker2.rig)
print(Hacker1)

Hacker1.encrypt_asset("DataSpike", "Inventory")
Hacker1.upgrade_rig()

print(Hacker1)
Hacker1.rig.generate_asset()
Hacker1.rig.generate_asset()
Hacker1.rig.generate_asset()
Hacker1.rig.generate_asset()
print(Hacker1)