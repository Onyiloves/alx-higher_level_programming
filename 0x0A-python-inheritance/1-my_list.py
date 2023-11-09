#!/usr/bin/python3
"""class mode"""


class MyList(list):
    """Mylist class that inherites from list"""
    def print_sorted(self):
        """function that prints the list, but sorted
            all the elements of the list is type int
        """
        arrange_list = sorted(self)
        print(arrange_list)
        del arrange_list
