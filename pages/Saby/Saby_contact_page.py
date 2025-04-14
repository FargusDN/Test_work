from selenium.webdriver.common.by import By
import allure
from pages.Base_page import BasePage
from selenium.webdriver import ActionChains




Go_tensor = (By.XPATH, '//a[@href="https://tensor.ru/"]')
Region_selector = (By.XPATH, '''//span[@class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]''')
partners_list = (By.XPATH, '''//div[@class = "sbisru-Contacts-List__col ws-flex-shrink-1 ws-flex-grow-1"]''')
first_partner = (By.XPATH, '''//div[@title="{}"]''')
Change_region_selector = (By.XPATH, '''//span[@class='controls-DecoratorHighlight' and contains(text(), '{}')] ''')

class SabyContactPage(BasePage):
    def __init__(self, Chrome):
        super().__init__(Chrome)

    @allure.step("Кликнуть на ссылку Tensor")
    def go_tensor(self):
        return self.find(Go_tensor).click()


    @allure.step("Открыть popup для выбора региона")
    def open_popup_region(self):
        self.find(Region_selector).click()
    @allure.step("Получить текущий регион")
    def get_current_region(self):
        return self.clickable(Region_selector).text

    @allure.step("Проверить текущий регион")
    def check_current_region(self, target_region):
        Region = self.get_current_region()
        assert Region == target_region, f"Ожидаемый регион {target_region} не совпадает с фактическим {Region}"




    @allure.step("Сменить регион на '{nomer_region}'")
    def change_region(self, nomer_region): #Старался писать динамические функции чтобы было удобнее масштабировать
        locator  = (
            Change_region_selector[0],
            Change_region_selector[1].format(nomer_region)
        )
        Name_change_region = self.find(locator)
        ActionChains(self.driver).move_to_element(Name_change_region).click().perform() #Использовал имитацию для повышения стабильности теста


    @allure.step("Проверить видимость списка партнеров")
    def is_partners_list_visible(self):
        return self.find(partners_list).is_displayed()

    @allure.step("Проверка названия первого партнера")
    def get_first_partner_text(self, name_first_partner):
        locator = (
            first_partner[0],
            first_partner[1].format(name_first_partner)
        )
        name_partner = self.find(locator).text
        assert name_partner == name_first_partner, f"Указанный первый {name_first_partner} не совпадает с найденным {name_partner}"

