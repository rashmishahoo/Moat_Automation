import time

import pytest
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    # PRIVATE FUNCTIONS (TO BE USED WITHIN BASE PAGE ONLY)
    def __click_element(self, locator):
        """ Args: Locator should be like ('By.ID, 'someid') or (By.XPATH, 'xpath') etc."""
        try:
            button = self.wait.until(EC.presence_of_element_located(locator))
            button.click()
        except (WebDriverException, TimeoutException) as err:
            print(str(err))

    def __enter_text(self, locator, text):
        """enters the text provided to text field lacoated.
        Locator should be like ('By.ID, 'someid') or (By.XPATH, 'xpath') etc."""
        try:
            input_field = self.wait.until(EC.presence_of_element_located(locator))
            input_field.clear()
            input_field.send_keys(text)
        except (WebDriverException, TimeoutException) as err:
            print(str(err))

    def __get_text(self, locator) -> str:
        """returns the text of the element by provided locator.
         Locator should be like ('By.ID, 'someid') or (By.XPATH, 'xpath') etc. """
        try:
            return self.wait.until(EC.presence_of_element_located(locator)).text.strip()
        except (WebDriverException, TimeoutException) as err:
            print(str(err))

    def __get_attribute_by_locator(self, locator, attribute):
        """returns the attribute value of the element by provided locator and attribute.
         Locator should be like ('By.ID, 'someid') or (By.XPATH, 'xpath') etc. """
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.get_attribute(attribute)
        except (WebDriverException, TimeoutException) as err:
            print(str(err))

    # CLICK_ELEMENT_BY
    def click_element_by_xpath(self, xpath):
        self.__click_element((By.XPATH, xpath))

    def click_element_by_id(self, id):
        self.__click_element((By.ID, id))

    def click_element_by_css_selector(self, css_selector):
        self.__click_element((By.CSS_SELECTOR, css_selector))

    def click_element_by_tag_name(self, tag_name):
        self.__click_element((By.TAG_NAME, tag_name))

    # ENTER_TEXT_BY
    def enter_text_by_xpath(self, xpath, text):
        self.__enter_text((By.XPATH, xpath), text)

    def enter_text_by_id(self, id, text):
        self.__enter_text((By.ID, id), text)

    def enter_text_by_css_selector(self, css_selector, text):
        self.__enter_text((By.CSS_SELECTOR, text), text)

    # GET_TEXT_BY
    def get_text_by_xpath(self, xpath):
        return self.__get_text((By.XPATH, xpath))

    def get_text_by_id(self, id):
        return self.__get_text((By.ID, id))

    def get_text_by_css_selector(self, css_selector):
        return self.__get_text((By.CSS_SELECTOR, css_selector))

    def is_element_displayed(self, xpath) -> bool:
        try:
            webwait = WebDriverWait(self.driver, 5)
            element = webwait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return element.is_displayed()
        except (WebDriverException, TimeoutException) as err:
            return False

    def get_attribute_by_xpath(self, xpath, attribute):
        return self.__get_attribute_by_locator((By.XPATH, xpath), attribute)

    def hover_over_element_by_xpath(self, xpath):
        """ Performs mouse over action on element. """
        try:
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            ActionChains(self.driver).move_to_element(element).perform()
        except (WebDriverException, TimeoutException) as err:
            print(str(err))