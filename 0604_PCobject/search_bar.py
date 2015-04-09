__author__ = 'neliko'
from base_component import BaseComponent


class SearchBar(BaseComponent):
    selectors = {
        'self': 'q',
        'submit': 'btnK',
        'input': 'q',
    }

    def search(self, query):
        self.driver.find_element_by_name(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_name(self.selectors['submit']).submit()

    @property
    def value(self):
        return self.element.get_attribute('value')
    @property
    def id(self):
        return  self.element.get_attribute('id')