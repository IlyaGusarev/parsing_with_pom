# pytest -s -v test_parsing.py

import pytest
import os
from pages.search_page import SearchPage
from pages.result_page import ResultPage
from conftest import OpenAndSafeXlsx


# В папке data лежат xlsx-файлы, в кажом файле список номеров, которые
# нужно проверить
files = list(os.walk('data'))[0][2]


@pytest.mark.parametrize('filename', files)
class TestGetInfo:
    def test_get_name(self, browser, search_link, filename):
        data = OpenAndSafeXlsx(filename)
        data.open_data()
        codes = data.codes
        for code in codes:
            search_page = SearchPage(browser, search_link)
            search_page.open()
            search_page.enter_request_number(code)
            result_page = ResultPage(browser, browser.current_url)
            name = result_page.get_name()
            data.append_name(name)
        data.save_result()
