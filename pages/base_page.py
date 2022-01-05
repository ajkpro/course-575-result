#
from selenium.common.exceptions import NoSuchElementException

class BasePage():

        def __init__(self, browser, url, timeout=10):
            self.browser = browser
            self.url = url
            # команда для неявного ожидания со значением по умолчанию 10
            self.browser.implicitly_wait(timeout)

        def open(self):
            self.browser.get(self.url)

        # Чтобы перехватывать исключение, нужна конструкция try/except: 
        def is_element_present(self, how, what):
            try:
                self.browser.find_element(how, what)
            except (NoSuchElementException):
                return False
            return True
