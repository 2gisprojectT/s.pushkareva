from unittest import TestCase
import unittest
from selenium import webdriver


class SeleniumWD(TestCase):
    # driver = webdriver.Remote(
    # command_executor = 'http://localhost:9515',
    # desired_capabilities={
    #        "browserName" : 'chrome'
    #    })

    def test_search(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)  # не всегда срабатывает при 0
        driver.get("http://www.google.com")
        self.assertTrue("Google" in driver.title, "Ожидаемое значение не найдено в заголовке")

        elem = driver.find_element_by_name("q")
        elem.send_keys("Cats")
        elem.submit()

        attr_val = elem.get_attribute('value')
        attr_id = elem.get_attribute('id')
        try:
            self.assertEqual("Cats", attr_val, "Невернное значение")
            self.assertEqual("lst-ib", attr_id, "Неверный id")
        finally:
            driver.close()

    def test_search2(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("http://www.google.com")

        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("vjkjrj")
        elem.submit()
        try:
            self.assertTrue("Возможно, вы имели в виду" in driver.page_source, "Не найдена ожидаемая строка")
            find_el = driver.find_elements_by_class_name('spell')
            self.assertEqual("молоко", find_el[1].text, 'Неверный возможный результат')
        finally:
            driver.close()


if __name__ == '__main__':
    unittest.main()