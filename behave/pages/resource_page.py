from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


INPUT_TEXT = (By.XPATH, "//input[@id='search-input']")
ARTICLE_TITLE = (By.CLASS_NAME, "gh-title")

class ResourcesPage(BasePage):
    def search_resource(self, text):
        super().type_in(EC.visibility_of_element_located(INPUT_TEXT), text)

    def click_in_result(self, result_number):
        result_selector = (By.CSS_SELECTOR, "li:nth-of-type("+result_number+")")
        super().move_to_element(EC.presence_of_element_located(result_selector))
        super().click(EC.visibility_of_element_located(result_selector))

    def get_page_title(self):
        super().move_to_element(EC.presence_of_element_located(ARTICLE_TITLE))
        super().wait(EC.visibility_of_element_located(ARTICLE_TITLE))
        title = super().find_element(EC.visibility_of_element_located(ARTICLE_TITLE)).text
        return super().remove_emoji(title)