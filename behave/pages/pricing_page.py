from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

RANGE_INPUT = (By.XPATH, "//input[@id='members']")
AUDIENCE_MEMBER_TEXT = (By.XPATH, "//div[@id='planselect']//span[1]")

class PricingPage(BasePage):
    def click_in_range(self, range_number):
        super().move_to_element(EC.visibility_of_element_located(RANGE_INPUT))
        super().select_range(EC.visibility_of_element_located(RANGE_INPUT), range_number)
    
    def get_member_audience_in_range_text(self):
        return super().find_element(EC.visibility_of_element_located(AUDIENCE_MEMBER_TEXT)).text
    
    def get_plan_price_text(self, plan):
        plan_price_locator = (By.XPATH, "//p[@data-price='"+plan+"']")
        return super().find_element(EC.visibility_of_element_located(plan_price_locator)).text