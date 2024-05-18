import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1080,768")
    chrome_driver = webdriver.Chrome(options=options)
    request.cls.driver = chrome_driver
    yield chrome_driver
    chrome_driver.quit()
