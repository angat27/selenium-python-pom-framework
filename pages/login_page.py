from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.CSS_SELECTOR, '[data-test="username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-test="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')
    ERROR_BANNER = (By.CSS_SELECTOR, '[data-test="error"]')

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self) -> None:
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))

    def login(self, username: str, password: str) -> None:
        username_el = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        username_el.clear()
        username_el.send_keys(username)

        password_el = self.driver.find_element(*self.PASSWORD_INPUT)
        password_el.clear()
        password_el.send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_text(self) -> str:
        error_el = self.wait.until(EC.visibility_of_element_located(self.ERROR_BANNER))
        return error_el.text
