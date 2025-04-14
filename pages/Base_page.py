import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, Chrome):
        self.driver, self.current_dir = Chrome
        self.driver.wait = WebDriverWait(self.driver, 20)

    @allure.step("Поиск элемента {args}")
    def find(self, *args):
        return self.driver.wait.until(EC.visibility_of_element_located(*args))

    @allure.step("Поиск всех элементов {args}")
    def finds(self, *args, ):
        return self.driver.wait.until(EC.presence_of_all_elements_located(*args))

    @allure.step("Ожидание кликабельности элемента {args}")
    def clickable(self, *args, ):
        return self.driver.wait.until(EC.element_to_be_clickable(*args))

    @allure.step("Открытие URL {args}")
    def get(self, *args):
        return self.driver.get(*args)

    @allure.step("Проверка URL на содержание {args}")
    def check_url(self, *args):
        return self.driver.wait.until(EC.url_contains(*args))

    @allure.step("Проверка title на содержание {args}")
    def check_title(self, *args):
        return self.driver.wait.until(EC.title_contains(*args))

    @allure.step("Переключение на первое окно")
    def switch_window_one(self):
        self.driver.wait.until(lambda d: len(d.window_handles) == 2)  # Переключение страницы и проверка
        self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.step("Переключение на второе окно")
    def switch_window_two(self):
        self.driver.wait.until(lambda d: len(d.window_handles) == 2)  # Переключение страницы и проверка
        self.driver.switch_to.window(self.driver.window_handles[1])




