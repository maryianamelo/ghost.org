from pages.main_page import MainPage
from pages.resource_page import ResourcesPage
from pages.pricing_page import PricingPage

def open_application(context):
    context.resources_page = ResourcesPage(context.driver)
    context.main_page = MainPage(context.driver)
    context.pricing_page = PricingPage(context.driver)
    context.main_page.open_url(context.base_url_mainpage)
