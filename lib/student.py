#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
# this clears first two of pytest lib/testing/student_test.py
# Class "Student" in student.py is a subclass of "User". .                                                                                                                   [ 25%]
# Class "Student" in student.py initializes with first and last name. . 
        self.knowledge = []
# this clears number 3 of pytest lib/testing/student_test.py
# Class "Student" in student.py initializes with empty list attribute "knowledge". .
    
    def learn(self, knowldge_string):
        self.knowledge.append(knowldge_string)
# this clears number 4 of pytest lib/testing/student_test.py
# Class "Student" in student.py learns from a string and adds to self.knowledge.