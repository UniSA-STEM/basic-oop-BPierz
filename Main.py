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

print(Hacker1)
print(Hacker2)

Hacker1.launch_data_spike(Hacker2)
Hacker1.launch_data_spike(Hacker2)

print(Hacker1)
print(Hacker2)

Hacker1.extract_assets(Hacker2)

print(Hacker1)
print(Hacker2)