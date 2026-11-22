# Selenium Python POM Framework

UI test automation framework built with Selenium WebDriver, Python, and pytest using the Page Object Model pattern, with automated test execution via GitHub Actions.

## Project Structure

- `pages/login_page.py` - Page Object encapsulating login locators, explicit waits, and page actions
- `tests/test_login.py` - Login test cases covering valid login, locked-out user, and invalid credentials
- `conftest.py` - pytest browser fixture configuring headless Chrome setup and teardown
- `.github/workflows/selenium.yml` - CI workflow running the test suite on pushes and pull requests

## Running Tests Locally

```bash
pip install -r requirements.txt
pytest -v
```
