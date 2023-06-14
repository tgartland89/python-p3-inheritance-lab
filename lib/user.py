#!/usr/bin/env python

# already clears first pytest
# Class "User" in user.py is a class. .  
class User:
    
# adding this clears the pytests for pytest lib/testing/user_test.py
# Class "User" in user.py initializes with first and last name. . 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name