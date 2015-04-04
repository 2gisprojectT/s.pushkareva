__author__ = 'neliko'

from unittest import TestCase
from Lion import Lion
import unittest


class LionTest(TestCase):
    table = {
        ("hungry", "antelope"): ("fed", "eat"),
        ("hungry", "hunter"): (None, "run"),
        ("hungry", "tree"): (None, "sleep"),
        ("fed", "antelope"): ("hungry", "sleep"),
        ("fed", "hunter"): ("hungry", "run"),
        ("fed", "tree"): ("hungry", "see")
    }

    def test_init(self):
        lion = Lion("fed", self.table)

        self.assertEqual("fed", lion.state, 'Init:State is not correct')
        self.assertEqual("", lion.input_object, 'Init:Input object is not correct')
        self.assertEqual("", lion.action, 'Init:Action is not correct')
        self.assertEqual(self.table, lion.table, 'Init:Table is not correct')

    def test_findAntelope(self):  # тестирование поиска объекта в таблице
        lion = Lion("fed", self.table)
        self.assertTrue(lion.find_obj("antelope"), 'Antelope_find:Return not true')  # Лев сыт
        lion.state = "hungry"
        self.assertTrue(lion.find_obj("antelope"), 'Antelope_find:Return not true')  # Лев голоден

        self.assertEqual("antelope", lion.input_object, 'Antelope_find:Input object is not correct')

    def test_findHunter(self):
        lion = Lion("fed", self.table)
        self.assertTrue(lion.find_obj("hunter"), 'Hunter_find:Return not true')
        lion.state = "hungry"
        self.assertTrue(lion.find_obj("hunter"), 'Hunter_find:Return not true')

        self.assertEqual("hunter", lion.input_object, 'Hunter_find:Input object is not correct')

    def test_findTree(self):
        lion = Lion("fed", self.table)
        self.assertTrue(lion.find_obj("tree"), 'Tree_find:Return not true')
        lion.state = "hungry"
        self.assertTrue(lion.find_obj("tree"), 'Tree_find:Return not true')

        self.assertEqual("tree", lion.input_object, 'Tree_find:Input object is not correct')

    def test_findUnknown(self):
        lion = Lion("fed", self.table)
        self.assertFalse(lion.find_obj("frog"), 'Unknown_find:Return not true')
        lion.state = "hungry"
        self.assertFalse(lion.find_obj("frog"), 'Unknown_find:Return not true')

        self.assertEqual("", lion.input_object, 'Tree_find:Input object is not correct')

    def test_viewAntelope(self):  # тестирование реакции льва
        lion = Lion("fed", self.table)
        lion.find_obj("antelope")
        # Лев сыт
        lion.view()
        self.assertEqual("hungry", lion.state, 'Antelope_fed_view:State is not correct')
        self.assertEqual("sleep", lion.action, 'Antelope_fed_view:Action is not correct')
        # Лев голоден
        lion.view()
        self.assertEqual("fed", lion.state, 'Antelope_hungry_view:State is not correct')
        self.assertEqual("eat", lion.action, 'Antelope_hungry_view:Action is not correct')

    def test_viewHunter(self):
        lion = Lion("fed", self.table)
        lion.find_obj("hunter")

        lion.view()
        self.assertEqual("hungry", lion.state, 'Hunter_fed_view:State is not correct')
        self.assertEqual("run", lion.action, 'Hunter_fed_view:Action is not correct')

        lion.view()
        self.assertEqual("hungry", lion.state, 'Hunter_hungry_view:State is not correct')
        self.assertEqual("run", lion.action, 'Hunter_hungry_view:Action is not correct')

    def test_viewTree(self):
        lion = Lion("fed", self.table)
        lion.find_obj("tree")

        lion.view()
        self.assertEqual("hungry", lion.state, 'Tree_fed_view:State is not correct')
        self.assertEqual("see", lion.action, 'Tree_fed_view:Action is not correct')

        lion.view()
        self.assertEqual("hungry", lion.state, 'Tree_hungry_view:State is not correct')
        self.assertEqual("sleep", lion.action, 'Tree_hungry_view:Action is not correct')


if __name__ == '__main__':
    unittest.main()

