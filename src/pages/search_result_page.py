import time
from src.pages.base_page import BasePage

class SearchResultPage(BasePage):
    # LOCATORS
    creative_count_label_xpath ="//div[@class='creative-count']"
    search_by_brand_xpath = "//div[@id='']"
    random_brand_link_xpath = "//div[contains(@class, 'dotcom-header')]//a[text()='Random Brand']"
    page_type_label_xpath = "//div[@class='header-info-container']//span[@class='page-type']"
    share_link_xpath ="//a[contains(text(),'Share')]"
    add_container_xpath ="//div[@class = 'er-creative-container']"

    def enter_text_in_search_by_brand_box(self, value):
        """Enter text_in_search_by_brand_box"""
        try:
            print("inside enter_text_in_search_by_brand_box")
            self.enter_text_by_xpath(self.search_by_brand_xpath, value)
        except Exception as err:
            print(f"enter_text_in_search_by_brand_box '\n{err}'")

    def get_creative_count(self):
        """Return creative count of brand """
        try:
            print("inside get_creative_count")
            time.sleep(2)
            creative_count = self.get_text_by_xpath(self.creative_count_label_xpath)
            creative_count = creative_count.split(" ")
            return int(creative_count[0])
        except Exception as err:
            print(f"enter_get_creative_count'\n{err}'")

    def click_random_brand_link(self):
        self.click_element_by_xpath(self.random_brand_link_xpath)

    def get_page_type_label(self):
        return self.get_text_by_xpath(self.page_type_label_xpath)

    def hover_over_first_ad(self):
        self.hover_over_element_by_xpath(self.add_container_xpath)

    def is_share_ad_link_present(self):
        time.sleep(1)
        return self.is_element_displayed(self.share_link_xpath)

