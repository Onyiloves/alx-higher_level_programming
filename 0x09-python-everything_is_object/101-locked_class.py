#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    only allow to creating new instance attributes called first_name
    otherwise,prevents the user from creating new instance attributes
    """

    __slots__ = ["first_name"]
