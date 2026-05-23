from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_appstore_redirect(browser, wait):
    """Проверка ссылки App Store со страницы Vitamin."""
    # Открываем страницу Vitamin
    browser.get("https://martspec.com/ru/vitamin")
    # Сохраняем текущую вкладку браузера
    # Это нужно для последующего переключения на новую вкладку
    original_window = browser.current_window_handle

    # Находим кнопку App Store и ждем,
    # пока элемент станет доступен для клика
    appstore_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="ms-btn-apple"]')))

    # Получаем ссылку из атрибута href
    href = appstore_button.get_attribute("href")

    # Получаем target ссылки
    # target="_blank" означает открытие в новой вкладке
    target = appstore_button.get_attribute("target")

    # Проверяем что href существует и не пустой
    # Защита от битой или пустой ссылки
    assert href is not None

    # Проверяем что ссылка ведет на App Store
    assert "apps.apple.com" in href

    # Проверяем что ссылка содержит ID нужного приложения
    # Это защита от перехода на другое приложение
    assert "1519596234" in href

    # Проверяем что ссылка должна открываться в новой вкладке
    assert target == "_blank"

    # Кликаем по кнопке App Store
    appstore_button.click()

    # Ждем открытия второй вкладки
    # До клика была 1 вкладка, после должно стать 2
    wait.until(EC.number_of_windows_to_be(2))

    # Переключаемся на новую вкладку
    for window in browser.window_handles:
        if window != original_window:
            browser.switch_to.window(window)
            break

    # Получаем URL открывшейся страницы
    current_url = browser.current_url

    # Проверяем что действительно открылась страница App Store
    assert "apps.apple.com" in current_url

    # Проверяем что открылась страница нужного приложения
    assert "1519596234" in current_url


# Что проверяет тест:
# assert href is not None	- ссылка не пустая
# assert "apps.apple.com" in href	- ссылка ведет на App Store
# assert "1519596234" in href	- открывается нужное приложение
# assert target == "_blank"	- ссылка должна открываться в новой вкладке
# EC.number_of_windows_to_be(2)	- новая вкладка реально открылась
# assert "apps.apple.com" in current_url	- произошел переход на App Store
# assert "1519596234" in current_url	- после перехода открылась нужная страница приложения

