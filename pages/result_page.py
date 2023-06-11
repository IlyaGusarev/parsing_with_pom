from .locators import ResultPageLocators
from .base_page import BasePage


class ResultPage(BasePage):
    def get_name(self):
        result = self.wait_element(
            *ResultPageLocators.RESULT_FORM)
        if result:
            return result.text
