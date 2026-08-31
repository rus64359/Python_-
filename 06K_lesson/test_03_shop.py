from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sauce_demo_store():
# Запускаем браузер Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)  # Увеличили таймаут для надёжности

    try:
# Шаг 1: Открываем сайт магазина
        print(" Открываю сайт магазина...")
        driver.get("https://www.saucedemo.com/")
        driver.save_screenshot("store_0.png")

# Шаг 2: Авторизуемся как standard_user
        print("🔹 Авторизуюсь как standard_user...")
        username_input = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()
        driver.save_screenshot("store_1.png")

# Ждем, пока загрузится страница с товарами
        print(" Жду загрузки страницы товаров...")
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))

# Шаг 3: Добавляем товары в корзину
        print(" Добавляю товары в корзину...")

# Sauce Labs Backpack
        backpack_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        backpack_button.click()
        print(" Sauce Labs Backpack добавлен")
# Ждем, пока кнопка сменится на "Remove"
        wait.until(EC.text_to_be_present_in_element((By.ID, "remove-sauce-labs-backpack"), "Remove"))

# Sauce Labs Bolt T-Shirt
        tshirt_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
        tshirt_button.click()
        print(" Sauce Labs Bolt T-Shirt добавлен")

# Sauce Labs Onesie
        onesie_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
        onesie_button.click()
        print(" Sauce Labs Onesie добавлен")

# Переход в корзину
        print(" Перехожу в корзину...")
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_container")))
        cart_button.click()

# Шаг 4: Оформляем покупку
        print(" Оформляю покупку...")
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

# Заполняем форму
        print(" Заполняю форму...")
        first_name = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        last_name = wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
        postal_code = wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))

        first_name.send_keys("Вячеслав")
        last_name.send_keys("Безгин")
        postal_code.send_keys("672000")

# Нажимаем Continue
        continue_button = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
        continue_button.click()

# Читаем итоговую сумму
        print(" Читаю итоговую сумму...")
        total_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary-total")))
        total_text = total_element.text
        print(f"Итоговая сумма на странице: {total_text}")

# Проверяем, что сумма равна 58.29
        print(" Проверяем сумму...")
        assert float(total_text.replace('$', '')) == 58.29, f"Ожидалась сумма 58.29, но получена {total_text}"

   
    finally:

     driver.quit()