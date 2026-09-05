# Установить Python (MacOS)

brew install python  
python3 --version  
pip3 --version  
python3 -m venv .venv  
source .venv/bin/activate  
pip install selenium pytest webdriver-manager  
pip freeze > requirements.txt  

# MartspecWebsiteTest
- При именовании методов в патерне POM использовать говорящие названия, 
которые имитируют поведение пользователя.
- Необходимо стремиться к тому, чтобы стиль написания методов классов,
были идентичные, чтобы любой из пользователей мог понять их суть.
- Метод (дествие), должен начинаться с глагола.

Предлагаю использовать следующие названия для методов:

- click_ - (click_button) Для нажатия на кнопку, иконку, ссылку.
- select_ - (select_element) Для  выбора элемента из выпадающего списка.
- hover_ - (hover_dropdown) Для наведения указателя мыши.
- check_/uncheck_ - (check_radio_button) Для отметки или снятия отметки радио кнопки, чекбокса.
- go_to_ - (go_to_page) Для перехода на страницу.