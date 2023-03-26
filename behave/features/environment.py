import os

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from utils.util import *


def before_all(context):
    context.base_url_mainpage = context.config.userdata['BASE_URL']

def before_scenario(context, feature):
    chrome_options = Options()
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    context.driver.maximize_window()
    open_application(context)    

def after_scenario(context, scenario):
    context.driver.quit()

