from behave import step
from hamcrest import *

@step('I click in "{tab_grid_name}" tab grid')
def step_impl(context, tab_grid_name):
    context.main_page.click_in_tab_grid(tab_grid_name)
    context.tab_grid_name = tab_grid_name

@step('I click on "{item_name}" page')
def step_impl(context, item_name):
    context.main_page.click_in_item(context.tab_grid_name,  item_name)

@step(u'I search for "{search_text}"')
def step_impl(context, search_text):
    context.resources_page.search_resource(search_text)

@step(u'I click in the "{result_number}" th result')
def step_impl(context, result_number):
    context.resources_page.click_in_result(result_number)
    context.result_number = result_number

@step(u'I verify that the article title is correct')
def step_impl(context):
    if (context.result_number == "10"):
        expected_title = "Why there's nothing artificial about AI's future"
        assert_that(context.resources_page.get_page_title(), is_(expected_title.lower()), "Title is not being displayed correctly")
    