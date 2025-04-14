from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.Base_page import BasePage
import os
import time
import allure
from selenium.webdriver.support import expected_conditions as EC
plagin_tab = (By.XPATH, '//div[text()="Saby Plugin"]')
windows = (By.XPATH, '//span[text()="Windows"]')
download_link = (By.XPATH, '//a[@href="https://update.saby.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')

class SabyDownloadPage(BasePage):
    def __init__(self, Chrome):
        super().__init__(Chrome)


    @allure.step("Открыть вкладку плагина")
    def open_plugin_tab(self):
        self.find(plagin_tab).click()

    @allure.step("Выбрать Windows")
    def select_windows(self):
        self.find(windows).click()

    @allure.step("Получить информацию о ссылке для скачивания")
    def get_download_link_text(self):
        return self.find(download_link).text

    @allure.step("Скачать файл")
    def download_windows_plagin(self):
        name_file = self.find(download_link)
        ActionChains(self.driver).move_to_element(name_file).click().perform()


    @allure.step("Проверка размера файла")
    def download_file(self):
        Size_file = self.get_download_link_text()
        downloaded_file = os.path.join(self.current_dir, "sbisplugin-setup-web.exe")  # Проверка размера файла
        # пыталься избежать sleep сделал костыль если скорость загрузки низкая не успевает загрузиться
        timeout = 25
        end_time = time.time() + timeout
        while time.time() < end_time:
            if os.path.exists(downloaded_file):
                return True
            continue

        assert os.path.exists(downloaded_file) == True, f"файл sbisplugin-setup-web.exe не загрузился за {timeout} сек"

        file_size_mb = round(os.path.getsize(downloaded_file) / (1024 * 1024), 2)
        SizefileMB = Size_file.split()[2]
        SizefileMB = float(SizefileMB)
        assert SizefileMB == file_size_mb, f"Размер на сайте указан {SizefileMB} но файл {file_size_mb} страница https://saby.ru/download?tab=plugin&innerTab=default"

    #
