import allure

def tomar_captura(driver, nombre="captura"):
    screenshot_path = f"screenshots/{nombre}.png"
    driver.save_screenshot(screenshot_path)
    allure.attach.file(screenshot_path, name=nombre, attachment_type=allure.attachment_type.PNG)
