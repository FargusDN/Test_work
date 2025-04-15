import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture()
def Chrome():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = os.path.join(current_dir, 'downloads') #указываем папку для скачивания файла
    options = Options()
    options.add_argument("--headless=new")
    options.add_experimental_option("prefs", {
    "download.default_directory": current_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    })
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options
                              )

    yield driver, current_dir

    driver.quit()



