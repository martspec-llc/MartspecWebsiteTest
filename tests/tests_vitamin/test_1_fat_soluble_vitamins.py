import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_all_fat_soluble_vitamins_redirect(browser, wait):
    """Клик по каждому жирорастворимому витамину и проверка перехода."""

    # 1. Открываем страницу витаминов
    browser.get("https://martspec.com/ru/vitamin")
    time.sleep(2)  # пауза, чтобы мы успели увидеть загрузку

    # 2. Список всех жирорастворимых витаминов
    vitamins = ["A", "D", "E", "K"]

    # 3. Цикл по каждому витамину
    for vitamin in vitamins:
        # 3.1 Ищем карточку витамина по его букве (A, D, E, K)
        card = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//div[contains(@class, 'card-vitamin')][.//p[text()='{vitamin}']]"))
        )

        # 3.2 Прокручиваем страницу так, чтобы карточка стала видимой
        ActionChains(browser).move_to_element(card).perform()
        time.sleep(0.5)  # небольшая пауза для визуального эффекта

        # 3.3 Находим ссылку "Перейти" внутри карточки
        link = card.find_element(By.CSS_SELECTOR, ".text-link-arrow")

        # 3.4 Проверяем, что ссылка ведёт на правильный URL (например, .../vitamin_a)
        href = link.get_attribute("href")
        assert f"vitamin_{vitamin.lower()}" in href, f"Неверная ссылка для {vitamin}"

        # 3.5 Кликаем по ссылке - переходим на страницу конкретного витамина
        link.click()
        time.sleep(1.5)  # ждём загрузки страницы витамина

        # 3.6 Убеждаемся, что мы действительно там
        assert f"vitamin_{vitamin.lower()}" in browser.current_url, f"Ошибка перехода для {vitamin}"
        print(f"✅ Витамин {vitamin} перешёл на {browser.current_url}")

        # 3.7 Возвращаемся назад, к списку витаминов
        browser.back()
        time.sleep(1)  # даём странице "успокоиться"

        # 3.8 Ждём, пока карточки снова появятся (подтверждение возврата)
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card-vitamin')]")))

    # 4. Если дошли сюда - все витамины успешно проверены
    print("🎉 Все жирорастворимые витамины протестированы!")



"""
Этот тест проверяет ссылки всех жирорастворимых витаминов (A, D, E, K).

Что делает:
- Открывает главную страницу витаминов.
- Для каждого витамина:
  - Находит его карточку.
  - Кликает по ссылке "Перейти".
  - Проверяет, что открылась правильная страница (URL содержит vitamin_a, vitamin_d и т.д.).
  - Возвращается назад (browser.back()).
- Всё происходит в одном окне браузера, очень быстро благодаря кэшированию.

Почему browser.back() работает быстро:
- Страница витаминов уже загружена и лежит в кэше браузера.
- Selenium не перезапрашивает все ресурсы (CSS, картинки) заново.
- Нет задержек, связанных с человеческим фактором.
"""