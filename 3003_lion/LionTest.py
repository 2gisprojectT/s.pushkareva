__author__ = 'neliko'

from unittest import TestCase
from Lion import Lion
import unittest


class LionTest(TestCase):
    table = {
        ("fed", "tree"): ("hungry", "see"),
        ("hungry", "tree"): (None, "sleep")
    }

    def test_init(self):
        lion = Lion("fed", self.table)

        self.assertEqual("fed", lion.state, 'Init:State is not correct')
        self.assertEqual("", lion.action, 'Init:Action is not correct')
        self.assertEqual(self.table, lion.table, 'Init:Table is not correct')

    def test_isKnowTree(self):  # проверяем, знает ли лев входной объект
        lion = Lion("fed", self.table)
        self.assertTrue(lion.isKnowObject("tree"), 'Tree_isKnowObject:Return not true')  # Лев сыт
        lion.state = "hungry"
        self.assertTrue(lion.isKnowObject("tree"), 'Tree_isKnowObject:Return not true')  # Лев голоден

    def test_isKnowUnknown(self):
        lion = Lion("fed", self.table)
        self.assertFalse(lion.isKnowObject("frog"), 'Unknown_isKnowObject:Return not true')
        lion.state = "hungry"
        self.assertFalse(lion.isKnowObject("frog"), 'Unknown_isKnowObject:Return not true')

    def test_viewTree(self):  # тестирование реакции льва
        lion = Lion("fed", self.table)
        # Лев сыт
        lion.view("tree")
        self.assertEqual("hungry", lion.state, 'Tree_fed_view:State is not correct')
        self.assertEqual("see", lion.action, 'Tree_fed_view:Action is not correct')
        # Лев голоден
        lion.view("tree")
        self.assertEqual("hungry", lion.state, 'Tree_hungry_view:State is not correct')
        self.assertEqual("sleep", lion.action, 'Tree_hungry_view:Action is not correct')


if __name__ == '__main__':
    unittest.main()

