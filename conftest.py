from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser language (for ex: ru, en, es etc.")

@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    if user_language:
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be specified")
    yield browser
    browser.quit()

