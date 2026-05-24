import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_all_water_soluble_vitamins_redirect(browser, wait):
    """Клик по каждому водорастворимому витамину и проверка перехода."""

    # 1. Открываем страницу витаминов
    browser.get("https://martspec.com/ru/vitamin")
    time.sleep(2)

    # 2. Находим кнопку "Водорастворимые витамины" и открываем категорию
    water_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Водорастворимые витамины']]"))
    )
    ActionChains(browser).move_to_element(water_button).perform()
    time.sleep(0.5)
    water_button.click()
    print("✅ Категория 'Водорастворимые витамины' открыта")

    # 3. Ждём появления хотя бы одной карточки витамина (например, B1)
    #    Используем contains(., 'B1') — поиск по любому тексту внутри карточки
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(@class, 'card-vitamin')][contains(., 'B1')]")
    ))
    time.sleep(0.5)  # дополнительная пауза для полной отрисовки

    # 4. Список всех водорастворимых витаминов
    vitamins = ["B1", "B2", "B3", "B5", "B6", "B7", "B9", "B12", "C"]

    # 5. Проходим по каждому витамину
    for vitamin in vitamins:
        # 5.1 Составляем XPath для поиска карточки
        if vitamin == "C":
            # Витамин C: ищем точное совпадение текста 'C' в заголовке
            xpath = f"//div[contains(@class, 'card-vitamin')][.//p[text()='{vitamin}']]"
        else:
            # B1...B12: ищем частичное совпадение (из-за вложенного span)
            xpath = f"//div[contains(@class, 'card-vitamin')][contains(., '{vitamin}')]"

        # Ждём, когда карточка станет видимой (не просто присутствует, а видима)
        card = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

        # Прокручиваем к карточке
        ActionChains(browser).move_to_element(card).perform()
        time.sleep(0.5)

        # Находим ссылку "Перейти"
        link = card.find_element(By.CSS_SELECTOR, ".text-link-arrow")
        href = link.get_attribute("href")

        # Ожидаемый URL: vitamin_b1, vitamin_b2, ..., vitamin_c
        expected_url_part = f"vitamin_{vitamin.lower()}"
        assert expected_url_part in href, f"Неверная ссылка для {vitamin}: {href}"

        # Кликаем и проверяем переход
        link.click()
        time.sleep(1.5)  # ждём загрузки страницы витамина
        assert expected_url_part in browser.current_url, f"Ошибка перехода для {vitamin}"
        print(f"✅ Витамин {vitamin} перешёл на {browser.current_url}")

        # Возвращаемся назад к списку витаминов
        browser.back()
        # Убеждаемся, что карточки снова видны (для следующей итерации)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'card-vitamin')][contains(., 'B1')]")
        ))
        time.sleep(0.5)

    print("🎉 Все водорастворимые витамины успешно проверены!")



"""
Тест для водорастворимых витаминов (B1, B2, B3, B5, B6, B7, B9, B12, C).

Особенности:
- Перед проверкой кликов необходимо открыть категорию "Водорастворимые витамины",
  так как по умолчанию она скрыта.
- Поиск карточек: для B1...B12 используется contains(., 'B1'), потому что в HTML
  номер витамина обёрнут в <span class="title-subscript">.
- Для витамина C — точное совпадение 'C'.
- После каждого перехода выполняется browser.back() для возврата к списку.
"""