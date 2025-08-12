from behave import given, when, then
from selenium.webdriver.common.by import By
from helpers import get_browser, attach_screenshot
import time

@given('abro el navegador en la página de login')
def step_open_login(context):
    context.driver = get_browser()
    context.driver.get("https://the-internet.herokuapp.com/login")

@when('ingreso usuario "{username}" y contraseña "{password}"')
def step_login(context, username, password):
    context.driver.find_element(By.ID, "username").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

@then('debería ver el mensaje "{mensaje}"')
def step_validate_message(context, mensaje):
    time.sleep(1)
    body_text = context.driver.find_element(By.ID, "flash").text
    attach_screenshot(context.driver)
    context.driver.quit()
    assert mensaje in body_text
