#!/usr/bin/python3
'''
file: 11-student.py
Classes:
-> Student
'''


class Student:
    """ Student class using Public instance attributes """

    def __init__(self, first_name, last_name, age):
        ''' Constructor method '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ functn that returns directory description with filter """

        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            result = {}
            for j in attrs:
                if j in self.__dict__:
                    result[j] = self.__dict__[j]
            return result
        return self.__dict__
