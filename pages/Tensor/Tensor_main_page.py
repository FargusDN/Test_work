from selenium.webdriver.common.by import By
from pages.Base_page import BasePage
import allure


Power_in_people_selector = (By.XPATH, '//p[text() = "Сила в людях"]')
go_about = (By.XPATH, '''//a[@href="/about" and text()="Подробнее"]''')

class TensorMainPage(BasePage):

    @allure.step("Перейти на страницу 'О компании'")
    def go_about_page(self):
        self.clickable(go_about).click()

    @allure.step("Проверить видимость блока сила в людях")
    def Check_Blok_Power_in_people(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.find(Power_in_people_selector).is_displayed()


