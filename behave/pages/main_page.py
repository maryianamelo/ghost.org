from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def click_in_tab_grid(self, tab_grid_name):
        tab_selector = (By.XPATH, "//button//span[contains(text(),'" + tab_grid_name + "')]")
        super().click(EC.visibility_of_element_located(tab_selector))
    
    def click_in_item(self, tab_name, item_name):
        item_selector = (By.XPATH, "//a[@href='/" + tab_name.lower() + "/']//div//div//p[text()='" + item_name + " ']")
        super().wait(EC.visibility_of_element_located(item_selector))
        super().click(EC.visibility_of_element_located(item_selector))

    def click_in_single_tab(self, tab_name):
        tab_selector = (By.XPATH, "//nav//a[text()='" + tab_name + "']")
        super().click(EC.visibility_of_element_located(tab_selector))






