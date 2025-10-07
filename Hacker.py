"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset

class Hacker:
    def __init__(self, name):
        self.name = name
        self.__trace_level = 0
        self.__inventory = [Asset("CryptoToken")]
        self.__rig = None



    def aquire(self):
        self.__rig = Rig()
        print (f"Rig successfully aquired: {self.__name}")


