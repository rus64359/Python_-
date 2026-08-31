from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_slow_calculator():
# Запускаем драйвер Chrome и задаём таймаут (50 секунд — с запасом, учитывая задержку на странице)
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)

    try:
# Шаг 1: Открываем страницу
       print(" Открываю страницу калькулятора...")
       driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
       driver.maximize_window()

# Шаг 2: Вводим значение 45 в поле delay
       print(" Устанавливаю задержку 45 секунд...")
       delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
       delay_input.clear()
       # Если в поле уже есть текст
       delay_input.send_keys("45")

# Шаг 3: Нажимаем кнопки 7 + 8 =
       print(" Выполняю вычисление: 7 + 8...")
# Кнопка 7
       button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
       button_7.click()
# Кнопка +
       button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
       button_plus.click()
# Кнопка 8
       button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
       button_8.click()
# Кнопка =
       button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
       button_equals.click()

# Шаг 4: Проверяем результат через 45 секунд
       print(" Ожидаю результат 15 через 45 секунд...")
# Используем WebDriverWait с ожиданием, что текст в элементе с классом screen станет равен "15"
       result_element = wait.until(
          EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
       )
# Получаем фактический текст результата для проверки
       actual_result = driver.find_element(By.CLASS_NAME, "screen").text

# Проверяем с помощью assert
       assert actual_result == "15", f"Ожидался результат 15, но получили '{actual_result}'"
       print(" Результат 15 отобразился корректно!")

    except Exception as e:
# Если тест упал, делаем скриншот для отладки
       print(f" Тест не прошёл: {e}")
       driver.save_screenshot("calc_error.png")

    driver.quit()