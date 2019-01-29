#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 - Assignment 1 Part 2"""


class Book(object):
    """ Object that creates book"""

    author = ""
    title = ""

    def __init__(self, athr, ttl):
        """Constructor for the Book() class.

        Args:
            athr (string): author of book
            ttl (string): title of book

        Attributes:
            athr (string): author of book
            ttl (string): title of book
        """
        self.theAuthor = athr
        self.theTitle = ttl

    def display(self):
        """Displays the author and title of a book

        Args:
            self (unknown): variables from constructor

        Returns:
            ""No return. Prints value

        Examples:

            >>> book1 = Book("John Steinbek", "Of Mice and Men")
            book1.display()
            Of Mice and Men written by author John Steinbek
        """
        print (self.theTitle + " written by author " + self.theAuthor)