from selenium.webdriver import ActionChains

from pages.Base_page import BasePage
from selenium.webdriver.common.by import By
import allure


openContactsPopupButton  = (By.XPATH, '//div[text()="Контакты"]')
Go_Contacts = (By.XPATH, '//a[@class="sbisru-link sbis_ru-link" and contains(@href, "/contacts")]')
Go_download_version = (By.XPATH, '//a[text()="Скачать локальные версии"]')
Go_Suby = "https://sbis.ru/"

class SabyMainPage(BasePage):
    def __init__(self, Chrome):
        super().__init__(Chrome)



    @allure.step("Открыть сайт Saby")
    def open_page(self):
        return self.get(Go_Suby)

    @allure.step("Открыть попапа контакты")
    def open_popup_contacts(self):
        popup = self.clickable(openContactsPopupButton)
        ActionChains(self.driver).move_to_element(popup).click().perform() #Использовал имитацию для повышения стабильности теста


    @allure.step("Открыть страницу загрузки")
    def go_download_local_version(self):
        self.find(Go_download_version).click()

    @allure.step("Открыть страницу контактов")
    def go_contacts(self):
        return self.find(Go_Contacts).click()














#
#
#
#
#
