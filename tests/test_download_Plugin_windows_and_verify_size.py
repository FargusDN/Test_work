import pytest
from pages.Saby.Saby_main_page import SabyMainPage
from pages.Saby.Saby_download_local_version_page import SabyDownloadPage
from loguru import logger
import allure

@allure.epic("Тестовое задание")
@allure.story('Тест: Проверка размера файла "Сбис Плагин" для windows версия = "Веб-установщик" на странице https://saby.ru/download?tab=plugin&innerTab=default')
@pytest.mark.flaky(reruns=2)
def test_download_Plagin_windows_verify_size(Chrome):
    logger.info(f"Начало теста: Проверка размера файла 'Сбис Плагин' для windows версия = 'Веб-установщик'")

    with allure.step("Инициализация страниц"):
        SMain = SabyMainPage(Chrome)  # https://sbis.ru/
        SDown = SabyDownloadPage(Chrome) # https://saby.ru/download?tab=plugin&innerTab=default
        logger.info("Страницы инициализированы")

    with allure.step("Открытие главной страницы"):
        SMain.open_page()
        logger.info("Главная страница открыта")

    with allure.step("Переход на страницу 'Скачать локальные версии'"):
        SMain.go_download_local_version()
        logger.info("Переход на страницу 'Скачать локальные версии выполнен")

    with allure.step("Открытие вкладки 'Saby Plagin'"):
        SDown.open_plugin_tab()
        logger.info("Открытие вкладки 'Saby Plagin' выполнена")

    with allure.step("Открытие вкладки 'Saby Plagin' версия для windows"):
        SDown.select_windows()
        logger.info("Открытие вкладки 'Saby Plagin' версия для windows выполнена")

    # Сбор текста для сравнения размеров файла пример "Скачать (Exe 10.43 МБ)"
    with allure.step("Сбор текста с кнопки скачать"):
        SDown.get_download_link_text()
        logger.info("Сбор текста выполнен")

    with allure.step("Нажатие на кнопку скачать Веб-установщик"):
        SDown.download_windows_plagin()
        logger.info("Нажатие на кнопку скачать Веб-установщик выполнен")

    with allure.step("Проверка размеров  скаченного Веб-установщика"):
        SDown.download_file()
        logger.info("Проверка размеров  скаченного Веб-установщика выполнена")

    logger.info(f"Завершение теста: Проверка размера файла 'Сбис Плагин' для windows версия = 'Веб-установщик'")
