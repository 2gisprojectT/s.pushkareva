from unittest import TestCase
import unittest
from selenium import webdriver
from page import Page


class SeleniumWD(TestCase):
    def setUp(self):
        # driver = webdriver.Remote(
        # command_executor = 'http://localhost:9515',
        # desired_capabilities={
        # "browserName" : 'chrome'
        # })
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.page.open("http://www.google.com")

    def tearDown(self):
        self.driver.close()


    def test_search(self):
        self.assertTrue("Google" in self.page.title, "Ожидаемое значение не найдено в заголовке")
        self.page.search_bar.search("Cats")
        self.assertEqual("Cats", self.page.search_bar.value, "Невернное значение")
        self.assertEqual("lst-ib", self.page.search_bar.id, "Неверный id")

    def test_search2(self):
        self.page.search_bar.search("vjkjrj")
        print(self.page.expected_result.expected_text)
        self.assertTrue("Возможно, вы имели в виду" in self.page.page_source, "Не найдена ожидаемая строка")
        self.assertEqual("молоко", self.page.expected_result.expected_text, 'Неверный возможный результат')


if __name__ == '__main__':
    unittest.main()