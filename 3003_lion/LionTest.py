__author__ = 'neliko'

from unittest import TestCase
from Lion import Lion
import unittest


class LionTest(TestCase):

    def test_init(self):
        lion=Lion("fed")
        self.assertEqual("fed",lion.state, 'State is not correct')
        self.assertEqual("",lion.input_object,'Input object is not correct')
        self.assertEqual("",lion.action, 'Action is not correct')



    def test_get_state(self):
        lion=Lion("fed")
        lion.find_obj("antilope")
        self.assertEqual("hungry",lion.get_state(),'Get_state:State have wrong value')
        lion.state="hungry"
        self.assertEqual("fed",lion.get_state(),'Get_state:State have wrong value')

    def test_get_action(self):
        lion=Lion("fed")
        lion.find_obj("antilope")
        self.assertEqual("sleep",lion.get_action(),'Get_action:Action have wrong value')
        lion.state="hungry"
        self.assertEqual("eat",lion.get_action(),'Get_action:Action have wrong value')

    def test_findAntilope(self):
         lion=Lion("fed")
         self.assertEqual(True,lion.find_obj("antilope"),'Antilope_find:Return not true')
         lion=Lion("hungry")
         self.assertEqual(True,lion.find_obj("antilope"),'Antilope_find:Return not true')

         lion.find_obj("antilope")
         self.assertEqual("antilope",lion.input_object,'Antilope_find:Input object is not correct')

    def test_findHunter(self):
         lion=Lion("fed")
         self.assertEqual(True,lion.find_obj("hunter"),'Hunter_find:Return not true')
         lion=Lion("hungry")
         self.assertEqual(True,lion.find_obj("hunter"),'Hunter_find:Return not true')

         lion.find_obj("hunter")
         self.assertEqual("hunter",lion.input_object,'Hunter_find:Input object is not correct')

    def test_findTree(self):
         lion=Lion("fed")
         self.assertEqual(True,lion.find_obj("tree"),'Tree_find:Return not true')
         lion=Lion("hungry")
         self.assertEqual(True,lion.find_obj("tree"),'Tree_find:Return not true')

         lion.find_obj("tree")
         self.assertEqual("tree",lion.input_object,'Tree_find:Input object is not correct')

    def test_findUnknown(self):
         lion=Lion("fed")
         self.assertEqual(False,lion.find_obj("frog"),'Unknown_find:Return not true')
         lion=Lion("hungry")
         self.assertEqual(False,lion.find_obj("frog"),'Tree_find:Return not true')

         lion.find_obj("frog")
         self.assertEqual("",lion.input_object,'Unknown_find:Input object is not correct')

    def test_newDataAntilopeFed(self):
        lion=Lion("fed")
        lion.find_obj("antilope")
        lion.newData()

        self.assertEqual("hungry",lion.state,'Antilope_fed:State is not correct')
        self.assertEqual("sleep",lion.action,'Antilope_fed:Action is not correct')

    def test_newDataAntilopeHungry(self):
        lion=Lion("hungry")
        lion.find_obj("antilope")
        lion.newData()

        self.assertEqual("fed",lion.state,'Antilope_hungry:State is not correct')
        self.assertEqual("eat",lion.action,'Antilope_hungry:Action is not correct')

    def test_newDataHunterFed(self):
        lion=Lion("fed")
        lion.find_obj("hunter")
        lion.newData()

        self.assertEqual("hungry",lion.state,'Hunter_fed:State is not correct')
        self.assertEqual("run",lion.action,'Hunter_fed:Action is not correct')

    def test_newDataHunterHungry(self):
        lion=Lion("hungry")
        lion.find_obj("hunter")
        lion.newData()

        self.assertEqual("hungry",lion.state,'Hunter_hungry:State is not correct')
        self.assertEqual("run",lion.action,'Hunter_hungry:Action is not correct')

    def test_newDataTreeFed(self):
        lion=Lion("fed")
        lion.find_obj("tree")
        lion.newData()

        self.assertEqual("hungry",lion.state,'Tree_fed:State is not correct')
        self.assertEqual("see",lion.action,'Tree_fed:Action is not correct')

    def test_viewTreeHungry(self):
        lion=Lion("hungry")
        lion.find_obj("tree")
        lion.newData()

        self.assertEqual("hungry",lion.state,'Tree_fed:State is not correct')
        self.assertEqual("sleep",lion.action,'Tree_fed:Action is not correct')




if __name__ == '__main__':
    unittest.main()

