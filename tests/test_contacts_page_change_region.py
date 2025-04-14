import pytest
import allure
from pages.Saby.Saby_main_page import SabyMainPage
from pages.Saby.Saby_contact_page import SabyContactPage
from pages.Base_page import BasePage
from loguru import logger

@allure.epic("Тестовое задание")
@allure.story('Тест: Смена регионов на странице https://saby.ru/contacts/')
@pytest.mark.parametrize(
    "initial_region_number, initial_region, initial_partner, target_region_number, target_region, target_partner, expected_url_part, expected_title_part",
    [
        # Формат: (начальный_регион, первый_партнёр, номер_региона, конечный_регион, партнёр_конечного_региона, часть_url, часть_title)
        (
                76,
                "Ярославская обл.",
                "Saby - Ярославль",
                41,
                "Камчатский край",
                "Saby - Камчатка",
                "kamchatskij-kraj",
                "Камчатский край"
        ),
        (
                76,
                "Ярославская обл.",
                "Saby - Ярославль",
                78,
                "г. Санкт-Петербург",
                "Saby - Санкт-Петербург",
                "78-sankt-peterburg",
                "г. Санкт-Петербург"
        )
    ],
    ids=["Переход из Ярославля в Камчатский край","Переход из Ярославля в Санкт-Петербург"]
)
@pytest.mark.flaky(reruns=2)  # К сожалению нехватает опыта чтоб полностью стабилизировать тесты
def test_region_change(
        Chrome,
        initial_region_number,
        initial_region,
        initial_partner,
        target_region_number,
        target_region,
        target_partner,
        expected_url_part,
        expected_title_part
):


    logger.info(f"Подготовка к тесту: смена региона с {initial_region} на {target_region}")

    with allure.step("Инициализация страниц"):
        SMain = SabyMainPage(Chrome)  # https://sbis.ru/
        SContact = SabyContactPage(Chrome)  # https://saby.ru/contacts/
        BP = BasePage(Chrome)
        logger.info("Страницы инициализированы")

    with allure.step("Открытие главной страницы"):
        SMain.open_page()
        logger.info("Главная страница открыта")

    with allure.step("Открытие попапа контакты на странице "):
        SMain.open_popup_contacts()
        logger.info("Popup контактов успешно открыт")

    with allure.step("Переход на страницу контактов"):
        SMain.go_contacts()
        logger.info("Переход на страницу контактов выполнен")

    # Иногда падает определяться регион Москва
    # Решение сначала переключаться на регион Ярославль и только потом проводить тест
    with allure.step("Открытие попапа выберете свой регион "):
        SContact.open_popup_region()
        logger.info("Открытие попапа выберете свой регион выполнен")

    with allure.step(f"Установка региона перед тестом  {initial_region} "):
        SContact.change_region(str(initial_region_number))  # Указываем номер региона для переключения на него
        logger.info("Переключение региона выполнен")



    logger.info(f"Начало теста: смена региона с {initial_region} на {target_region}")

    with allure.step("Определение региона"):
        SContact.get_current_region()  # Определяем регион.
        logger.info("Определение региона выполнено")

    with allure.step(f"Проверка региона {initial_region}"):
        SContact.check_current_region(initial_region)  # Указываем ожидаемый регион
        logger.info("Проверка региона выполнена")

    with allure.step(f"Проверка списка партнеров для региона {initial_region}"):
        SContact.is_partners_list_visible()
        logger.info("Проверка списка партнеров выполнена")

    with allure.step(f"Проверка первого партнера {initial_region}"):
        SContact.get_first_partner_text(initial_partner)  # Проверяем погрузился ли список партнёров и соответствие партнера
        logger.info("Проверка первого партнера выполнена")

    with allure.step("Открытие попапа выберете свой регион "):
        SContact.open_popup_region()
        logger.info("Открытие попапа выберете свой регион выполнен")

    with allure.step(f"Смена региона с {initial_region} на {target_region} "):
        SContact.change_region(str(target_region_number))  # Указываем номер региона для переключения на него
        logger.info(f"Смена региона с {initial_region} на {target_region} выполнена")

    with allure.step(f"Проверка списка партнеров для региона {target_region}"):
        SContact.is_partners_list_visible()
        logger.info(f"Проверка списка партнеров для региона {target_region} выполнена" )

    with allure.step(f"Проверка url региона {target_region}"):
        BP.check_url(expected_url_part)
        logger.info(f"Проверка url региона {target_region} выполнена")

    with allure.step(f"Проверка title региона {target_region}"):
        BP.check_title(expected_title_part)
        logger.info(f"Проверка title региона {target_region} выполнена")


    with allure.step(f"Проверка региона {target_region}"):
        SContact.check_current_region(target_region)  # Регион конечного перехода
        logger.info(f"Проверка региона {target_region} выполнена")

    with allure.step(f"Проверка списка партнеров для региона {target_region}"):
        SContact.is_partners_list_visible()
        logger.info(f"Проверка списка партнеров для региона {target_region} выполнена")

    with allure.step(f"Проверка первого партнера  {target_region}"):
        SContact.get_first_partner_text(target_partner)  # Партнер конечного перехода
        logger.info(f"Проверка первого партнера для {target_region} выполнена")

    logger.info(f"Завершение теста: смена региона с {initial_region} на {target_region}")
