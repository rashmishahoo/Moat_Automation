from src.pages.moat_page import *
from src.pages.search_result_page import *

def test_verify_share_ad_link_on_first_ad(driver):
    """
    Test scenario 4. Verify the “Share” ad feature (it appears on overlay when hovering over an ad).#
    run : pytest test_verify_share_ad.py --disable-pytest-warnings
    @author: @Rashmi Shahoo
    """
    obj = LandingPage(driver)
    obj_search = SearchResultPage(driver)

    # 1. open moat.com
    driver.get("http://www.moat.com")

    #2.Enter search text and go to search results page -any here-Saturn
    obj.enter_text_in_search_box('Saturn')

    #3. click on matching link to go to search results page
    obj.click_matching_link('Saturn')

    #4. hover over first ad
    obj_search.hover_over_first_ad()

    #5.verify share ad link is present on it
    assert obj_search.is_share_ad_link_present(),'share link not present-Failed'
    print('Share link present when user hover over an ad-Passed')

    print('Test4 verify share ad link is present on Passed-')
