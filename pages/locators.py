from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class SearchPageLocators:
    INPUT_FORM = (By.CSS_SELECTOR, 'input.form-control')
    FIND_BUTTON = (By.CSS_SELECTOR, '#find-btn')


class ResultPageLocators:
    RESULT_FORM = (By.CSS_SELECTOR, 'tbody td:nth-child(5)')
