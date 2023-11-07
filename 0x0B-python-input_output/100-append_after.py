#!/usr/bin/python3
"""
file: 100-append_after.py
functions:
-> append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """ add a new str to a file, after find containing search_str """
    with open(filename, "r+") as file:
        lines = file.readlines()
        new = []
        for line in range(len(lines)):
            new.append(lines[line])
            if search_string in lines[line]:
                new.append(new_string)

        file.seek(0)
        file.write("".join(new))
