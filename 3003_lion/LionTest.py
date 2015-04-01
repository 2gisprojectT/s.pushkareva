__author__ = 'neliko'

from unittest import TestCase
from Lion import Lion
import unittest


class LionTest(TestCase):

    def test_init(self):
        obj=Lion()
        self.assertEqual("",obj.state, 'State is not correct')
        self.assertEqual("",obj.obj,'Input object is not correct')
        self.assertEqual("",obj.action, 'Action is not correct')

    def test_run(self):
        lion=Lion()
        lion.start("hungry")
        self.assertEqual("hungry",lion.state,'State have wrong value')
        self.assertEqual("",lion.action,'Action is not correct')
        self.assertEqual("",lion.obj,'Input object is not correct')

    def test_findAntilope(self):
         lion=Lion()
         lion.start("fed")
         self.assertEqual(True,lion.find_obj("antilope"),'Antilope_find:Return not true')
         lion.start("hungry")
         self.assertEqual(True,lion.find_obj("antilope"),'Antilope_find:Return not true')

         lion.find_obj("antilope")
         self.assertEqual("antilope",lion.obj,'Antilope_find:Input object is not correct')


    def test_findHunter(self):
         lion=Lion()
         lion.start("fed")
         self.assertEqual(True,lion.find_obj("hunter"),'Hunter_find:Return not true')
         lion.start("hungry")
         self.assertEqual(True,lion.find_obj("hunter"),'Hunter_find:Return not true')

         lion.find_obj("hunter")
         self.assertEqual("hunter",lion.obj,'Hunter_find:Input object is not correct')

    def test_findTree(self):
         lion=Lion()
         lion.start("fed")
         self.assertEqual(True,lion.find_obj("tree"),'Tree_find:Return not true')
         lion.start("hungry")
         self.assertEqual(True,lion.find_obj("tree"),'Tree_find:Return not true')

         lion.find_obj("tree")
         self.assertEqual("tree",lion.obj,'Tree_find:Input object is not correct')

    def test_findUnknown(self):
         lion=Lion()
         lion.start("fed")
         self.assertEqual(False,lion.find_obj("frog"),'Unknown_find:Return not true')
         lion.start("hungry")
         self.assertEqual(False,lion.find_obj("frog"),'Tree_find:Return not true')

         lion.find_obj("frog")
         self.assertEqual("",lion.obj,'Unknown_find:Input object is not correct')

    def test_newDataAntilopeFed(self):
        lion=Lion()
        lion.start("fed")
        lion.find_obj("antilope")
        lion.newData()

        self.assertEqual("hungry",lion.state,'Antilope_fed:State is not correct')
        self.assertEqual("sleep",lion.action,'Antilope_fed:Action is not correct')

    def test_newDataAntilopeHungry(self):
        lion=Lion()
        lion.start("hungry")
        lion.find_obj("antilope")
        lion.newData()

        self.assertEqual("fed",lion.state,'Antilope_hungry:State is not correct')
        self.assertEqual("eat",lion.action,'Antilope_hungry:Action is not correct')

    def test_newDataHunterFed(self):
        lion=Lion()
        lion.start("fed")
        lion.find_obj("hunter")
        lion.newData()

        self.assertEqual("hungry",lion.state,'Hunter_fed:State is not correct')
        self.assertEqual("run",lion.action,'Hunter_fed:Action is not correct')

    def test_newDataHunterHungry(self):
        lion=Lion()
        lion.start("hungry")
        lion.find_obj("hunter")
        lion.newData()

        self.assertEqual("hungry",lion.state,'Hunter_hungry:State is not correct')
        self.assertEqual("run",lion.action,'Hunter_hungry:Action is not correct')

    def test_newDataTreeFed(self):
        lion=Lion()
        lion.start("fed")
        lion.find_obj("tree")
        lion.newData()

        self.assertEqual("hungry",lion.state,'Tree_fed:State is not correct')
        self.assertEqual("see",lion.action,'Tree_fed:Action is not correct')

    def test_viewTreeHungry(self):
        lion=Lion()
        lion.start("hungry")
        lion.find_obj("tree")
        lion.newData()

        self.assertEqual("hungry",lion.state,'Tree_fed:State is not correct')
        self.assertEqual("sleep",lion.action,'Tree_fed:Action is not correct')




if __name__ == '__main__':
    unittest.main()

