import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_all_food_additives_redirect(browser, wait):
    """Клик по каждой пищевой добавке и проверка перехода."""

    # 1. Открываем страницу витаминов
    browser.get("https://martspec.com/ru/vitamin")
    time.sleep(2)

    # 2. Находим и открываем категорию "Пищевые добавки"
    additives_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Пищевые добавки']]"))
    )
    ActionChains(browser).move_to_element(additives_button).perform()
    time.sleep(0.5)
    additives_button.click()
    print("✅ Категория 'Пищевые добавки' открыта")

    # 3. Ждём появления первой карточки (например, Aci)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(@class, 'card-vitamin')][contains(., 'Aci')]")
    ))
    time.sleep(0.5)

    # 4. Список всех пищевых добавок (символы)
    additives = [
        "Aci", "Awe", "Asg", "Chg", "Ccp", "Clp", "Cmb",
        "Crp", "Cur", "Frw", "Gkb", "Lmn", "Mca", "Tkt"
    ]

    # 5. Проходим по каждой добавке
    for additive in additives:
        # XPath ищет карточку, которая содержит текст символа добавки
        xpath = f"//div[contains(@class, 'card-vitamin')][contains(., '{additive}')]"

        # Ждём, когда карточка станет видимой
        card = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

        # Прокручиваем к карточке
        ActionChains(browser).move_to_element(card).perform()
        time.sleep(0.5)

        # Находим ссылку "Перейти"
        link = card.find_element(By.CSS_SELECTOR, ".text-link-arrow")
        href = link.get_attribute("href")

        # Проверяем, что ссылка не пустая
        assert href is not None and href != "", f"Ссылка для {additive} отсутствует"

        # Кликаем и проверяем, что произошёл переход (URL изменился)
        link.click()
        time.sleep(1.5)
        assert browser.current_url != "https://martspec.com/ru/vitamin", \
            f"Клик по {additive} не привёл к переходу"
        print(f"✅ Добавка {additive} перешла на {browser.current_url}")

        # Возвращаемся назад к списку
        browser.back()
        # Убеждаемся, что карточки снова видны (ждём появления Aci)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'card-vitamin')][contains(., 'Aci')]")
        ))
        time.sleep(0.5)

    print("🎉 Все пищевые добавки успешно проверены!")


"""
Тест для пищевых добавок (Aci, Awe, Asg, Chg, Ccp, Clp, Cmb, Crp, Cur, Frw, Gkb, Lmn, Mca, Tkt).

Особенности:
- Категория "Пищевые добавки" по умолчанию скрыта, её нужно открыть.
- Некоторые добавки ведут на страницы coming-soon, другие — на готовые страницы
  (коллаген, куркума, гинкго и т.д.).
- Проверяем только наличие ссылки и факт перехода (URL изменился),
  так как точные URL могут различаться.
- После каждого перехода возвращаемся назад командой browser.back().
"""