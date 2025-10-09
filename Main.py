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

Thing = Asset("SecurityChip")
print(Thing)

Hacker1 = Hacker("Stevie McHacker")
print(Hacker1)

Hacker1.find_assets("CryptoToken")
Hacker1.aquire()
Hacker1.find_assets("CryptoToken")
