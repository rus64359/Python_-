import pytest

from selenium import webdriver

from calculator_page import CalculatorPage



@pytest.fixture

def driver():

    driver = webdriver.Chrome()

    yield driver

    driver.quit()



def test_slow_calculator(driver):

    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    page = CalculatorPage(driver, timeout=60)



    driver.get(url)

    driver.maximize_window()



    # Устанавливаем задержку 45 секунд

    page.set_delay(45)



    # Выполняем 7 + 8 =

    page.click_button("7")

    page.click_button("+")

    page.click_button("8")

    page.click_button("=")



    # Получаем результат и проверяем

    result = page.get_result()

    assert result == "15", f"Ожидался результат 15, но получили '{result}'"