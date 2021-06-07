from sys import platform

import pytest
from selenium import webdriver

HOST = "http://www.moat.com"

@pytest.fixture(scope="module", params=['Chrome'], autouse=True)
def driver(request):
    print("********************************************SETUP********************************************")
    print("I'm the fixture - setUp")
    # Create folder to save today's screenshots
    # utils.create_screenshot_folder(time.strftime("%Y_%m_%d"))
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()

    driver.get(HOST)
    driver.execute_script("document.body.style.zoom='100%'")
    yield driver
    print("********************************************TEARDOWN********************************************")
    print("I'm the fixture - tearDown")
    driver.quit()
    print("Testsuit Execution is completed!")
