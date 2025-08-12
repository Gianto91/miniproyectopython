from behave import given, when, then
from selenium.webdriver.common.by import By
import allure
from utils import tomar_captura

def tomar_captura(driver, nombre="captura"):
    screenshot_path = f"screenshots/{nombre}.png"
    driver.save_screenshot(screenshot_path)
    allure.attach.file(screenshot_path, name=nombre, attachment_type=allure.attachment_type.PNG)


@given('que abro Google')
def step_abrir_google(context):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.get("https://www.google.com")
    tomar_captura(context.driver, "Google_home")

@when('busco "{texto}"')
def step_buscar_texto(context, texto):
    caja = context.driver.find_element(By.NAME, "q")
    caja.send_keys(texto)
    caja.submit()

@then('el título de la página contiene "{texto}"')
def step_verificar_titulo(context, texto):
    assert texto.lower() in context.driver.title.lower()
    context.driver.quit()
