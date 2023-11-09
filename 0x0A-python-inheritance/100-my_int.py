#!/usr/bin/python3
"""class functions"""


class MyInt(int):
    '''Represents a rebellious integer object.
    MyInt has == and != operators inverted.
    '''
    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
