class Page():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self._search_bar = None
        self._expected_result = None

    @property
    def search_bar(self):
        from search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_name(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def page_source(self):
        return self.driver.page_source

    @property
    def expected_result(self):
        from expected_result import ExpectedResult
        if self._expected_result is None:
            self._expected_result = ExpectedResult(self.driver,
                                               self.driver.find_elements_by_class_name(ExpectedResult.selectors['expected_text']))
        return self._expected_result

    def open(self, url):
        self.driver.get(url)

    @property
    def title(self):
        return self.driver.title




