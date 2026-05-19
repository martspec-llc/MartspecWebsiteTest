from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def test_vitamin_header_dropdowns(browser, wait, base_url):
    print("\n=== ОТКРЫВАЕМ СТРАНИЦУ ВИТАМИН ===")
    # открываем страницу Витамин
    browser.get(base_url + "/vitamin")
    time.sleep(1)

    # ПРОВЕРКА МЕНЮ "О нас"
    print("\nПроверяем выпадающее меню 'О нас'")

    # ищем кнопку "О нас" по id
    about_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='navbarDropdownMain']")))

    # кликаем по кнопке "О нас"
    about_button.click()
    time.sleep(1)

    # ищем открывшийся выпадающий список "О нас"
    about_dropdown = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@aria-labelledby='navbarDropdownMain']")))

    # выводим текст списка в консоль
    print(about_dropdown.text)

    # проверяем пункты выпадающего списка
    assert "Наша история" in about_dropdown.text
    assert "Наша команда" in about_dropdown.text
    assert "Карьера" in about_dropdown.text

    print("Меню 'О нас' проверено")

    # ПРОВЕРКА МЕНЮ "Все устройства"
    print("\nПроверяем выпадающее меню 'Все устройства'")

    # ищем кнопку "Все устройства" по id
    devices_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='navbarDropdownPages']")))

    # кликаем по кнопке "Все устройства"
    devices_button.click()
    time.sleep(1)

    # ищем открывшийся выпадающий список "Все устройства"
    devices_dropdown = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@aria-labelledby='navbarDropdownPages']")))

    # выводим текст списка в консоль
    print(devices_dropdown.text)

    # проверяем пункты выпадающего списка
    assert "Вес" in devices_dropdown.text
    assert "Витамин" in devices_dropdown.text
    assert "Железо" in devices_dropdown.text
    assert "Кальций" in devices_dropdown.text
    assert "Магний" in devices_dropdown.text
    assert "Электролит" in devices_dropdown.text
    assert "Эмоция" in devices_dropdown.text

    print("Меню 'Все устройства' проверено")

    # ПРОВЕРКА МЕНЮ ЯЗЫКОВ
    print("\nПроверяем выпадающее меню языка")

    language_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='navbarDropdown']")))

    language_button.click()
    time.sleep(1)

    language_dropdown = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[@id='navbarDropdown']/following-sibling::ul")))

    print(language_dropdown.text)

    assert language_dropdown.is_displayed()
    assert len(language_dropdown.text) > 0

    print("Меню языка проверено")

    # ПРОВЕРКА КЛИКА ПО ЛОГОТИПУ
    print("\nПроверяем клик по логотипу")

    # ищем логотип сайта
    logo = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'ms-navbar-brand')]")))

    # кликаем по логотипу
    logo.click()
    time.sleep(1)

    # выводим текущий URL после клика
    print("Текущий URL после клика по логотипу:", browser.current_url)

    # проверяем, что после клика остались на сайте Martspec
    assert "martspec.com" in browser.current_url

    print("\n=== ТЕСТ ШАПКИ УСПЕШНО ЗАВЕРШЕН ===")
    time.sleep(1)

# Тест проверяет:
# 1. Открытие страницы /vitamin
# 2. Dropdown "О нас"
# 3. Dropdown "Все устройства"
# 4. Dropdown языка
# 5. Клик по логотипу
# 6. Переход на https://martspec.com/ru/