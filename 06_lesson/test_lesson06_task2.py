from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

    # Первый пользователь
    driver.add_cookie({
        "name": "SESSION",
        "value": "ZGM2NTRjZmMtMDY0MC00MThlLTg2NzItYWVhZmI2OWM4ZTA1",
        "domain": "gitflic.ru"
    })

    # Обновляем страницу, чтобы куки применилась
    driver.refresh()
    # Сохранение URL  первого пользователя.
    url_user_1 = driver.current_url
    # Очистка куки.
    driver.delete_all_cookies()
    driver.get(driver.current_url)
    # Второй  пользователь.
    driver.add_cookie({
            "name": "SESSION",
            "value": "NmM3MWVhODAtMDQ3NS00YzgyLWExZWYtMWZiYzM0Nzk3ODM5",
            "domain": "gitflic.ru"
        })
    # Обновляем страницу.
    driver.refresh()
    driver.get(driver.current_url)
    # Сохранение URL второго пользователя.
    url_user_2 = driver.current_url
    # Проверка отличия URL
    assert url_user_1 != url_user_2
    driver.quit()
