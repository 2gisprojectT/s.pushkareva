__author__ = 'neliko'
from base_component import BaseComponent


class ExpectedResult(BaseComponent):
    selectors = {
        'expected_text': 'spell'
    }

    @property
    def expected_text(self):
        self.element=self.driver.find_elements_by_class_name(self.selectors['expected_text'])
        expected_text=self.element[1].text
        return expected_text