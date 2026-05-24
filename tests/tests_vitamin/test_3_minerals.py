import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_all_minerals_redirect(browser, wait):
    """Клик по каждому минералу и проверка перехода."""

    # 1. Открываем страницу витаминов
    browser.get("https://martspec.com/ru/vitamin")
    time.sleep(2)

    # 2. Находим и открываем категорию "Минералы"
    minerals_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Минералы']]"))
    )
    ActionChains(browser).move_to_element(minerals_button).perform()
    time.sleep(0.5)
    minerals_button.click()
    print("✅ Категория 'Минералы' открыта")

    # 3. Ждём появления первой карточки минерала (например, Ca)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(@class, 'card-vitamin')][contains(., 'Ca')]")
    ))
    time.sleep(0.5)

    # 4. Список минералов (символ -> ожидаемая часть URL)
    #    Для K (калий) сделаем отдельный XPath, чтобы не перепутать с витамином K
    minerals = [
        ("Ca", "calcium"),
        ("Cl", "chloride"),
        ("Cr", "chrome"),
        ("Cu", "copper"),
        ("I", "iodine"),
        ("Fe", "iron"),
        ("Mg", "magnesium"),
        ("Mn", "manganese"),
        ("Mo", "molybdenum"),
        ("P", "phosphorus"),
        ("K", "potassium"),  # калий, не путать с витамином K
        ("Se", "selenium"),
        ("Na", "sodium"),
        ("Zn", "zinc")
    ]

    # 5. Проходим по каждому минералу
    for symbol, url_part in minerals:
        # 5.1 Составляем XPath для поиска карточки
        if symbol == "K":
            # Для калия добавим проверку подзаголовка, чтобы не взять витамин K
            xpath = "//div[contains(@class, 'card-vitamin')][.//p[text()='K'] and .//p[contains(@class, 'subtitle') and contains(text(), 'калий')]]"
        else:
            xpath = f"//div[contains(@class, 'card-vitamin')][contains(., '{symbol}')]"

        # Ждём, когда карточка станет видимой
        card = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

        # Прокручиваем к карточке
        ActionChains(browser).move_to_element(card).perform()
        time.sleep(0.5)

        # Находим ссылку "Перейти"
        link = card.find_element(By.CSS_SELECTOR, ".text-link-arrow")
        href = link.get_attribute("href")

        # Проверяем, что ссылка ведёт на правильный URL
        assert f"/ru/vitamin/{url_part}" in href or f"vitamin_{url_part}" in href, \
            f"Неверная ссылка для {symbol}: {href}"

        # Кликаем и проверяем переход
        link.click()
        time.sleep(1.5)
        assert url_part in browser.current_url, f"Ошибка перехода для {symbol}"
        print(f"✅ Минерал {symbol} перешёл на {browser.current_url}")

        # Возвращаемся назад к списку
        browser.back()
        # Убеждаемся, что карточки минералов снова видны
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'card-vitamin')][contains(., 'Ca')]")
        ))
        time.sleep(0.5)

    print("🎉 Все минералы успешно проверены!")


"""
Тест для минералов (Ca, Cl, Cr, Cu, I, Fe, Mg, Mn, Mo, P, K, Se, Na, Zn).

Особенности:
- Категория "Минералы" по умолчанию скрыта, её нужно открыть.
- Минерал K (калий) — особый случай: на странице есть и витамин K (жирорастворимый),
  поэтому для калия используем дополнительную проверку подзаголовка, чтобы не перепутать.
- Для остальных минералов достаточно проверки по символу.
- После каждого перехода возвращаемся назад командой browser.back().
"""