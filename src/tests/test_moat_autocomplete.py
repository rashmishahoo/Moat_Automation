#Test 1. Verify the search bar autocomplete drop down text.
#following test functions verify the search bar autocomplete drop down text.
#run : pytest -m test_moat_autocomplete.py --disable-pytest-warnings
# comment: here i have written positive and negative test cases for Autosearch

from src.pages.moat_page import *
from selenium import webdriver

def test_verify_no_result_displayed_if_no_match(driver):
    """
    Test scenario to verify "No Result" text displayed if no match found for text in search bar###
    @author: @Rashmi Shahoo
    """
    #create object for LandingPage
    obj = LandingPage(driver)

    #launch url
    driver.get("http://www.moat.com")

    #enter invalid text in search box and assert if No result - displayed
    obj.enter_text_in_search_box("!!!+")
    assert obj.no_result_displayed()
    print("No result_displayed if search characters are not valid-eg !!+-Autoserch negative test-Passed")

def test_verify_autocomplete_overlay_displayed_with_min_char(driver):
    """
    Test scenario to verify autocomplete overlay is displayed when user provides minimum of 2 matching  characters in search bar###
    @author: @Rashmi Shahoo
    """
    obj = LandingPage(driver)
    # enter with 2 characters text in search box and assert autocomplete overlay- displayed
    obj.enter_text_in_search_box("sa")
    assert obj.autocomplete_overlay_displayed()
    print("No overlay diaplyed if serch characters is equal to 2-Autosearch Negative testPassed")

def test_verify_search_bar_autocomplete_with_partial_click(driver):
    """
    Test scenario to verify search autocomplete overlay displays correct link option when partial matching characters
    is provided in search bar.Cliking on link takes to correct page with title'Saturn Creatives | Moat'
    'Satur'  || Saturn Creatives | Moat

    @author: @Rashmi Shahoo
    """
    obj = LandingPage(driver)
    #Enter partial text
    obj.enter_text_in_search_box("satur")
    assert obj.autocomplete_overlay_displayed()

    #Enter partial text 'Satur' to find and click the matching link 'Saturn'
    obj.click_matching_link("Saturn")

    expected_title = 'Saturn Creatives | Moat'
    # Getting current URL source code
    get_title = driver.title

    # Printing the title of this URL
    print(get_title)

    #check if matches expected if yes Passed else Failed
    if get_title == expected_title:
        print('clicking on link with partial search landed correctly-Passed')
    else:
        print('clicking on link with partial search -Failed')
