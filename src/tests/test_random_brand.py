from src.pages.moat_page import *
from src.pages.search_result_page import *

def test_verify_random_brand_search_result_page(driver, iteratrion_count=10):
    """
    Test scenario 3. Verify the “Random Brand” link on the search results page is random.###
    run : pytest test_random_brand.py --disable-pytest-warnings
    @author: @Rashmi Shahoo
    """

    obj = LandingPage(driver)
    obj_search = SearchResultPage(driver)

    #1. open moat.com
    driver.get("http://www.moat.com")

    #2. enter text in serch box - any here-Saturn
    obj.enter_text_in_search_box('Saturn')

    #3. click on matching link to go to search results page
    obj.click_matching_link('Saturn')

    #4. store Brand Name on left hand top of page in temporary variable
    previous_brand_name = obj_search.get_page_type_label()

    #5. Click on Random Brand name link multiple time (=10) compare the brand name with Previous one displayed
    # -Should not be Same as previous one -Random Name
    for x in range(0, iteratrion_count):
        obj_search.click_random_brand_link()
        current_brand_name = obj_search.get_page_type_label()

        assert current_brand_name != previous_brand_name
        previous_brand_name = current_brand_name
