#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 - Assignment 1 Part 2"""


class Book(object):
    """ Object that creates book"""

    author = ""
    title = ""

    def __init__(self, author, title):
        """Constructor for the Book() class.

        Args:
            author (string): author of book
            title (string): title of book

        Attributes:
            author (string): author of book
            title (string): title of book
        """
        self.author = author
        self.title = title

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
        print (self.title + " written by author " + self.author)