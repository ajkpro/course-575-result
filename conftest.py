"""
Из комментов:
Вам понадобятся знания следующих модулей и вам их хватит:
https://stepik.org/lesson/237240/step/8?unit=209628
https://stepik.org/lesson/237240/step/6?unit=209628

Причем заготовку для conftest и самого test файлов можно взять из задачи:
https://stepik.org/lesson/237240/step/6?unit=209628 , только избавиться от if.

Взято из test_36_step08.py
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', \
                     action='store', \
                     default="chrome", \
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', \
                     action='store', \
                     default='en', \
                     help="Choose language: ru, en, ... (etc.)")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name") 
    user_language = request.config.getoption("language") 
    if (browser_name == "chrome"): 
        options = Options()
        options.add_experimental_option('prefs', \
                                        {'intl.accept_languages': user_language})
        print("\n\nStart chrome browser for test...") 
        print(dir(request))
        browser = webdriver.Chrome(options=options) 
    elif (browser_name == "firefox"): 
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language) 
        print("\n\nStart firefox browser for test...") 
        browser = webdriver.Firefox(firefox_profile=fp) 
    else:
        print("Browser <browser_name> still is not implemented") 
    yield browser
    print("\nQuit browser...") 
    browser.quit()
