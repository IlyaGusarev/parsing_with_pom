from .base_page import BasePage
from .locators import SearchPageLocators


class SearchPage(BasePage):
    def enter_request_number(self, number):
        search_form = self.wait_element(
            *SearchPageLocators.INPUT_FORM)

        search_form.send_keys(number)

        search_button = self.browser.find_element(
            *SearchPageLocators.FIND_BUTTON)

        search_button.click()
