#Scenarios 2. Verify the creatives count on the search results page is correct
# for these 3 search iterms: Saturn, Saturday’s Market, and Krux.
#Verify below counts
#1)Saturn has creative count as 205
#2) Saturday’s Market  has creative count as 8
#3) Krux has creative count as 51

from src.pages.moat_page import *
from src.pages.search_result_page import *
from selenium import webdriver

@pytest.mark.parametrize("brand_name, creative_count", [("Saturn", 205),("Saturday's Market", 8), ("Krux", 51)])
def test_verify_creative_count(driver, brand_name, creative_count):
    """
    Test scenario 2: Verify the creatives count on the search results page is correct###
    # for these 3 search iterms: Saturn, Saturday’s Market, and Krux.
    #Verify below counts
    #1)Saturn has creative count as 205
    #2) Saturday’s Market  has creative count as 8
    #3) Krux has creative count as 51
    @author: @Rashmi Shahoo
    """

    #create objects for page classes
    obj = LandingPage(driver)
    obj_search = SearchResultPage(driver)

    #launch url and go to search result page by entering text in search box
    driver.get("http://www.moat.com")
    obj.enter_text_in_search_box(brand_name)
    obj.click_matching_link(brand_name)

    #verify creative count on the Page equal to expected value of the brand as given in test
    assert obj_search.get_creative_count() == creative_count





