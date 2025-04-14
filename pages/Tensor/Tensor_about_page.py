from selenium.webdriver.common.by import By
from pages.Base_page import BasePage
import allure


all_img_in_block_Working = (By.XPATH, '//img[contains(@class, "tensor_ru-About__block3-image") and @width="270" and @height="192"]')
block_working = (By.XPATH, '//h2[text() = "Работаем"]')
class TensorAboutPage(BasePage):


    @allure.step("Перейти на страницу 'О компании'")
    def Check_block_Working(self):
        self.find(block_working).is_displayed()

    @allure.step("Получить все изображения")
    def get_images(self):
        images = self.finds(all_img_in_block_Working)
        assert len(images) == 4, f"Ожидалось 4 изображения, найдено {len(images)} на странице https://tensor.ru/about"
        return images #Требовалось сравнить размеры по параметрам @width="270" and @height="192"

    @allure.step("Проверить размеры изображений")
    def check_images_size(self):

        images = self.get_images()

        first_size = {
            'width': images[0].get_attribute('width'),
            'height': images[0].get_attribute('height')
        }

        for i, img in enumerate(images[1:], start=4 ):
            current_size = {
                'width': img.get_attribute('width'),
                'height': img.get_attribute('height')
            }
            assert current_size == first_size, (
                f"Изображение {i}:\n"
                f"Фактические размеры: {current_size}\n"
            )


