from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")
    sleep(10)

    blue_button = driver.find_element(By.LINK_TEXT, "HTML Form")
    blue_button.click()
    sleep(5)
    assert (driver.current_url ==
            "https://httpbin.qa-territory.online/forms/post")
    sleep(5)
    driver.back()
    assert driver.current_url == "https://httpbin.qa-territory.online"
    sleep(10)

    driver.quit()
