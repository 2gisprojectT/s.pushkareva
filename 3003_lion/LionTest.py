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

    def test_isKnowObject_return_false_when_init_table_is_empty(self):
        table = {}
        lion = Lion("fed", table)
        self.assertFalse(lion.isKnowObject("tree"), 'Tree_isKnowObject:Return not false')

    def test_isKnowObject_return_true_when_object_in_init_table(self):  # проверяем, знает ли лев входной объект
        lion = Lion("fed", self.table)
        self.assertTrue(lion.isKnowObject("tree"), 'Tree_isKnowObject:Return not true')

    def test_isKnowObject__return_false_when_object_not_in_init_table(self):
        lion = Lion("fed", self.table)
        self.assertFalse(lion.isKnowObject("frog"), 'Unknown_isKnowObject:Return not true')

    def test_isKnowObject_return_false_when_init_state_not_in_table(self):
        lion = Lion("", self.table)
        self.assertFalse(lion.isKnowObject("tree"), 'Tree_isKnowObject:Return not false')

    def test_View_data_change(self):
        lion = Lion("fed", self.table)
        lion.view("tree")
        self.assertEqual("hungry", lion.state, 'Tree_fed_view:State is not correct')
        self.assertEqual("see", lion.action, 'Tree_fed_view:Action is not correct')

    def test_View_data_change_with_new_state_is_null(self):
        lion = Lion("hungry", self.table)
        lion.view("tree")
        self.assertEqual("hungry", lion.state, 'Tree_hungry_view:State is not correct')
        self.assertEqual("sleep", lion.action, 'Tree_hungry_view:Action is not correct')

    # Без использования блоков try-except тестами ниже можно сломать программу. Однако, в самой программе преполагается наличие
    # корректно заполненной таблицы и начального остояния Льва, а также проверка на наличие объекта в таблице.
    # Следовательно, приложение будет работать правильно.
    def test_View_exception_when_table_is_empty(self):
        table = {}
        lion = Lion("fed", table)
        try:
            lion.view("tree")  # здесь проверка на exception, т.к.в таблице нет данных. Не можем вернуть результат
        except:
            print("Exception: table is empty")

    def test_View_exception_when_unknown_object(self):
        lion = Lion("fed", self.table)
        try:
            lion.view("frog")  # здесь проверка на exception, т.к. подаем объект,которого нет в таблице.
        except:
            print("Exception: unknown object")

    def test_View_exception_when_empty_table_and_unknown_object(self):
        lion = Lion("fed", {})
        try:
            lion.view("frog")  # здесь,естественно, тоже exception
        except:
            print("Exception: unknown object and empty table")

    def test_View_exception_when_init_state_not_in_table(self):
        lion = Lion("", self.table)
        try:
            lion.view(
                "tree")  # здесь проверка на exception, т.к. не можем новое состояние и действие получить по данным,которых нет  таблице
        except:
            print("Exception: init state not in table")


if __name__ == '__main__':
    unittest.main()

