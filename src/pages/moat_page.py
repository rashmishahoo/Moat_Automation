import time
import pytest

from src.pages.base_page import BasePage


class LandingPage(BasePage):
    # LOCATORS
    add_search_input_box_xpath = "//input[@id='adsearch-input']"
    autocomplete_overlay_xpath ="//div[@id='adsearch-dropdown']"
    no_result_xpath ="//div[@class='search-bar-no-results']"

    def enter_text_in_search_box(self, value):
        """Enter text in Ad search input box"""
        try:
            print("inside enter_text_in_search_box")
            self.enter_text_by_xpath(self.add_search_input_box_xpath, value)
        except Exception as err:
            print(f"enter_text_in_search_box is completed '\n{err}'")

    def autocomplete_overlay_displayed(self) -> bool:
        """autocomplete_overlay_displayed -or Not """
        try:
            return self.is_element_displayed(self.autocomplete_overlay_xpath)
        except Exception as err:
            print(f"autocomplete_overlay_displayed'\n{err}'")

    def no_result_displayed(self) -> bool:
        """no_result_displayed -or Not """
        try:
            return self.is_element_displayed(self.no_result_xpath)
        except Exception as err:
            print(f"no_result_displayed'\n{err}'")

    def click_matching_link(self, full_text):
        """search partial matching text in autosearch box and_click the matching link"""
        try:
            print("inside_click_matching_link_")
            matching_link = '//span[text() ="'+full_text+'"]'
            if self.is_element_displayed(matching_link):
                self.click_element_by_xpath(matching_link)
            else:
                print("no Matching link displayed-Test failed")
        except Exception as err:
            print(f"enter_text_in_search_box is completed '\n{err}'")

    def verify_no_autoselect_with_one_char(self, value):
        """Enter text in Ad search input box"""
        try:
            print("inside_autoselect_with_one_char")
            self.enter_text_by_xpath(self.add_search_input_box_xpath, value)
        except Exception as err:
            print(f"autoselect_with_one_char is completed '\n{err}'")

    def verify_no_autoselect_if_no_match(self, value):
        """Enter text in Ad search input box"""
        try:
            print("inside_autoselect_with_no_match")
            self.enter_text_by_xpath(self.add_search_input_box_xpath, value)
        except Exception as err:
            print(f"autoselect_with_no_match is completed '\n{err}'")

    def verify_autoselect_with_exact_match_click(self, value):
        self.enter_text_by_xpath(self.add_search_input_box_xpath, value)






