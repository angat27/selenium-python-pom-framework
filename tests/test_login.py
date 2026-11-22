from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url


def test_locked_out_user_error(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    assert "Sorry, this user has been locked out." in login_page.get_error_text()


def test_invalid_credentials_error(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("invalid_user", "wrong_password")
    assert "Username and password do not match" in login_page.get_error_text()
