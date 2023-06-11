import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def browser():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920x1080")
    options.add_argument('--headless=new')
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def search_link():
    return 'https://www.reestr-zalogov.ru/search/index'
