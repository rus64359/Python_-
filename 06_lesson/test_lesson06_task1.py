from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_lo
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найдите и нажмите на кнопку "Start"
    start_buton = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button")))
    start_buton.click()

    # 3. Дождитесь появления текста "Hello World!"
    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!"))
    finish = driver.find_element(By.ID, "finish")

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("scrinhots/full_screen.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert finish.text == "Hello World!"
    driver.quit()
