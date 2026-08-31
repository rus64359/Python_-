from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_form_validation():
# Определяем браузер 
    if os.name == 'nt':
        driver = webdriver.Edge()

# Максимизируем окно и ждём полной загрузки формы
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

# Шаг 1: Открыть страницу
    print("Открываю страницу в", driver.capabilities['Edge'], "...")
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Убеждаемся, что форма загрузилась (ждём появления поля first-name)
    wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

# Шаг 2: Заполняем форму
    print(" Заполняю форму...")

    # First name
    first_name = driver.find_element(By.NAME, "first-name")
    first_name.clear()
    first_name.send_keys("Иван")

    # Last name
    last_name = driver.find_element(By.NAME, "last-name")
    last_name.clear()
    last_name.send_keys("Петров")

    # Address
    address = driver.find_element(By.NAME, "address")
    address.clear()
    address.send_keys("Ленина, 55-3")

    # Email
    email = driver.find_element(By.NAME, "e-mail")
    email.clear()
    email.send_keys("test@skypro.com")

    # Phone number
    phone = driver.find_element(By.NAME, "phone")
    phone.clear()
    phone.send_keys("+7985899998787")

# Zip code (оставляем пустым)
    zip_code = driver.find_element(By.NAME, "zip-code")
    zip_code.clear()

   # City
    city = driver.find_element(By.NAME, "city")
    city.clear()
    city.send_keys("Москва")

    # Country
    country = driver.find_element(By.NAME, "country")
    country.clear()
    country.send_keys("Россия")

    # Job position
    job_position = driver.find_element(By.NAME, "job-position")
    job_position.clear()
    job_position.send_keys("QA")

    # Company
    company = driver.find_element(By.NAME, "company")
    company.clear()
    company.send_keys("SkyPro")

 # Шаг 3: Нажимаем Submit
    submit_button = driver.find_element(By.NAME, "submit")
    submit_button.click()

    # Шаг 4: Проверки
    # Проверяем, что поле Zip code подсвечено красным
    zip_code_error = driver.find_element(By.CSS_SELECTOR, ".error")
    assert zip_code_error.is_displayed(), "Поле Zip code не подсвечено красным"

  # Проверяем, что остальные поля подсвечены зелёным
  # Сначала проверяем, что не все поля зелёные (на всякий случай)
    all_green = all(
        driver.find_element(By.CSS_SELECTOR, f".field:not(.error)")
        .get_attribute("class")
        .split()
        .count("green") == 8
    )
    assert all_green, "Не все поля, кроме Zip code, подсвечены зелёным"

    print(" Все проверки пройдены!")

    driver.quit()