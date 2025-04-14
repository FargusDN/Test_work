import pytest
import allure
from logs.logger import logger
from pages.Saby.Saby_main_page import SabyMainPage
from pages.Saby.Saby_contact_page import SabyContactPage
from pages.Base_page import BasePage
from pages.Tensor.Tensor_main_page import TensorMainPage
from pages.Tensor.Tensor_about_page import TensorAboutPage

@allure.epic("Тестовое задание")
@allure.story("Тест: роверка размеров изображения в блоке 'Работаем' на странице https://tensor.ru/about")
@pytest.mark.flaky(reruns=2)  # К сожалению нехватает опыта чтоб полностью стабилизировать тесты
def test_about_page_image_size(Chrome):

    logger.info("Начало теста: Проверка размеров изображения в блоке 'Работаем' на странице https://tensor.ru/about")

    with allure.step("Инициализация страниц"):
        SMain = SabyMainPage(Chrome)  # https://sbis.ru/
        SContact = SabyContactPage(Chrome)  # https://saby.ru/contacts/
        BP = BasePage(Chrome)
        TMain = TensorMainPage(Chrome)  # https://tensor.ru/
        TAbout = TensorAboutPage(Chrome)  # https://tensor.ru/about
        logger.info("Страницы инициализированы")

    with allure.step("Открытие главной страницы Saby"):
        SMain.open_page()
        logger.info("Открыта главная страница Saby")

    with allure.step("Открытие popup контактов"):
        SMain.open_popup_contacts()  # Иногда падает не успевает прогрузиться (Проблемное место)
        logger.info("Popup контактов успешно открыт")

    with allure.step("Переход на страницу контактов"):
        SMain.go_contacts()
        logger.info("Переход на страницу контактов выполнен")

    with allure.step("Переход на сайт Tensor"):
        SContact.go_tensor()
        logger.info("Переход на сайт Tensor выполнен")

    with allure.step("Переключение на новую вкладку"):
        BP.switch_window_two()
        logger.info("Переключение на новую вкладку выполнено")

    with allure.step("Проверка URL Tensor"):
        BP.check_url("https://tensor.ru")
        logger.info("URL Tensor корректный")

    with allure.step("Проверка блока 'Сила в людях'"):
        TMain.Check_Blok_Power_in_people()  # Иногда падает не успевает прогрузиться (Проблемное место)
        logger.info("Блок 'Сила в людях' проверен успешно")

    with allure.step("Переход на страницу 'О компании'"):
        TMain.go_about_page()
        logger.info("Переход на страницу 'О компании' выполнен")

    with allure.step("Переключение на новую вкладку"):
        BP.switch_window_two()
        logger.info("Переключение на новую вкладку выполнено")

    with allure.step("Проверка URL страницы 'О компании'"):
        BP.check_url("https://tensor.ru/about")
        logger.info("URL страницы 'О компании' корректный")

    with allure.step("Проверка блока 'Работаем'"):
        TAbout.Check_block_Working()
        logger.info("Блок 'Работаем' проверен успешно")

    with allure.step("Получение изображений"):
        TAbout.get_images()
        logger.info("Изображения успешно получены")

    with allure.step("Проверка размеров изображений"):
        TAbout.check_images_size()
        logger.info("Размеры изображений соответствуют требованиям")

    logger.info("Завершение теста: Проверка размеров изображения в блоке 'Работаем' на странице https://tensor.ru/about")
