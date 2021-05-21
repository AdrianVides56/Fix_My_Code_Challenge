#!/usr/bin/python3
"""
User class
"""


class User():
    """ Defines a User """

    def __init__(self):
        """ Initial state of every User instance """
        self.__email = None

    @property
    def email(self):
        """ Gets a user's email """
        return self.__email

    @email.setter
    def email(self, value):
        """ Sets an user's email """
        if type(value) is not str:
            raise TypeError("email must be a string")
        else:
            self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
