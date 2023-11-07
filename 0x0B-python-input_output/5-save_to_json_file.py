#!/usr/bin/python3
'''
file: 7-save_to_json_file.py
functions:
-> save_to_json_file
'''
import json


def save_to_json_file(my_obj, filename):
    """ using a JSON reps,Write a function of an Object to a text file """

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
