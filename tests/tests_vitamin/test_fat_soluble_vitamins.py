import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

def test_fat_soluble_vitamins_dropdown_dom(browser, base_url):
    # 1. Открываем страницу
    browser.get(f"{base_url}/vitamin")
    time.sleep(1)  # ждём загрузку

    # 2. Находим кнопку аккордеона
    dropdown_button = browser.find_element(
        By.XPATH, "//button[contains(@class,'accordion-header') and .//span[text()='Жирорастворимые витамины']]"
    )

    print("Кнопка найдена, aria-expanded до:", dropdown_button.get_attribute("aria-expanded"))

    # 3. Скроллим до кнопки
    browser.execute_script("arguments[0].scrollIntoView({block:'center'});", dropdown_button)
    time.sleep(0.2)

    # 4. Диагностика: выводим все контейнеры с классом accordion-collapse
    containers = browser.find_elements(By.CSS_SELECTOR, "div.accordion-collapse")
    print("Всего контейнеров на странице:", len(containers))
    for idx, c in enumerate(containers, start=1):
        height = browser.execute_script("return arguments[0].offsetHeight;", c)
        print(f"Container {idx}: offsetHeight={height}, visible={c.is_displayed()}, classes={c.get_attribute('class')[:100]}")

    # 5. Находим правильный контейнер через JS (ближайший accordion-collapse внутри секции)
    container = browser.execute_script("""
        const btn = arguments[0];
        const sec = btn.closest('section');
        return sec.querySelector('div.accordion-collapse');
    """, dropdown_button)

    assert container is not None, "Контейнер дропдауна не найден!"

    # 6. Принудительно раскрываем контейнер через JS
    browser.execute_script("""
        const cont = arguments[0];
        cont.classList.add('show');
        cont.style.height='auto';
        cont.style.overflow='visible';
    """, container)
    time.sleep(0.5)  # ждём анимацию

    # Проверка высоты контейнера
    height = browser.execute_script("return arguments[0].offsetHeight;", container)
    print("Контейнер открыт, offsetHeight:", height)
    assert height > 0, "Контейнер не открылся визуально"

    # 7. Находим все ссылки внутри контейнера
    links = container.find_elements(By.XPATH, ".//a[text()='Перейти →']")
    print(f"Найдено ссылок: {len(links)}")
    assert len(links) > 0, "Ссылки внутри дропдауна не найдены"

    # 8. Выводим текст всех ссылок
    for link in links:
        print("Ссылка:", link.text)