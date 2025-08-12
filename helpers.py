from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
import allure

def get_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless=new")  # Modo headless
    chrome_options.add_argument("--no-sandbox")  # Recomendado en entornos CI/CD
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.maximize_window()
    return driver

def attach_screenshot(driver, name="screenshot"):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )
