from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException
from cleantext import clean

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def open_url(self, url):
        self.driver.get(url)

    def wait(self, condition, seconds=15):
        return WebDriverWait(driver=self.driver, timeout=seconds).until(condition)
    
    def find_element(self, condition, seconds=15):
        return self.wait(condition, seconds)

    def click(self, condition):
        try:
            self.find_element(condition).click()
        except:
            button = self.find_element(condition)
            self.driver.execute_script("arguments[0].click();", button)

    def type_in(self, condition, text):
        self.find_element(condition).send_keys(text)

    def move_to_element(self, condition):
        element = self.find_element(condition)
        try:
            self.action.move_to_element(element).perform()
        except StaleElementReferenceException:
            pass   

    def wait_text_to_be_displayed(self, condition, text, timeout=15):
        element = self.find_element(condition)
        time = 0
        while element.text != text or time < timeout:
            element = self.find_element(condition)
            time = time + 1

    def get_alert_text(self):
        alert_obj = self.driver.switch_to.alert
        return alert_obj.text

    def get_all_opened_tabs_title(self):
        tab_titles = []
        browser_tabs = self.driver.window_handles
        for tab in browser_tabs:
            self.driver.switch_to.window(tab)
            tab_titles.append(self.driver.title)
        return tab_titles

    def switch_to_window(self, condition):
        return self.driver.switch_to.window(condition)

    def open_element_on_new_tab(self, condition):
        element = self.find_element(condition)
        ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_element_text(self, condition):
        element = self.find_element(condition)
        return element.text

    def select_drop_down_option(self, condition, book_rows):
        select = Select(self.find_element(condition))
        book_rows = str(book_rows) + ' rows'
        select.select_by_visible_text(book_rows)

    def accept_alert(self):
        alert_obj = self.driver.switch_to.alert
        return alert_obj.accept()
    
    def remove_emoji(self, text):
        return clean(text, no_emoji=True)
    
    def select_range(self, condition, range):
        element = self.find_element(condition)
        i=0
        while i < range:
            element.send_keys(Keys.RIGHT)
            i = i + 1
