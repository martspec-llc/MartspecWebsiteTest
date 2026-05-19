from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_vitamin_page_opened(browser, wait, base_url):
    # Открываем страницу "Витамин"
    browser.get(f"{base_url}/vitamin")

    # Проверяем, что появился заголовок страницы
    heading = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h1[contains(normalize-space(), 'Витамин')]")
        )
    )

    # Проверяем навигационный путь
    breadcrumbs = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//nav[contains(@class, 'breadcrumbs')]")
        )
    )

    # Проверяем наличие кнопки перехода в App Store
    app_store_button = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "a.ms-btn-apple")
        )
    )

    # Финальные проверки
    assert heading.is_displayed() # проверить, что заголовок реально отображается на странице
    assert breadcrumbs.is_displayed() # проверить, что путь виден пользователю
    assert app_store_button.is_displayed() # проверить, что кнопка App Store видна пользователю