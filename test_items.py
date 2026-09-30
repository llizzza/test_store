import time
from selenium.webdriver.by import By

def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Требуемая по условию задания пауза для визуальной проверки языка (например, --language=fr)
    time.sleep(30)
    
    # Проверяем наличие кнопки добавления в корзину с использованием уникального селектора
    add_to_basket_buttons = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    assert len(add_to_basket_buttons) > 0, "Кнопка добавления в корзину отсутствует на странице!"
