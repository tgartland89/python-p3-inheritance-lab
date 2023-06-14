#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
# this is where first two pytest lib/testing/teacher_test.py are cleared 
# Class "Teacher" in teacher.py is a subclass of "User"
# Class "Teacher" in teacher.py initializes with first and last name

        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]
# adding this clears number 3  pytest lib/testing/teacher_test.py are cleared 
# Class "Teacher" in teacher.py has an attribute called "knowledge", a list with len > 0. .

    def teach(self):
        return self.knowledge[random.randint(0, len(self.knowledge) - 1)]
 # adding this clears number 4 pytest lib/testing/teacher_test.py are cleared 
#  Class "Teacher" in teacher.py teaches from list of knowledge. .