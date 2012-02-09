"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

class ExampleObjectTest(TestCase):

    def save(self):
        self.failUnlessEqual(1 + 1, 2)

    def remove(self):
        self.failUnlessEqual(1 + 1, 2)

    def getAllPics(self):
        self.failUnlessEqual(1 + 1, 2)

