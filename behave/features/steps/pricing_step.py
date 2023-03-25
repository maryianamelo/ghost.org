from behave import step
from hamcrest import *

@step(u'I click in "{tab_name}" tab')
def step_impl(context, tab_name):
    context.main_page.click_in_single_tab(tab_name)

@step(u'I click "{range_number}" times in a range')
def step_impl(context, range_number):
    context.pricing_page.click_in_range(int(range_number))

@step(u'I verify that the audience number is defined as up to "{audience_member_number}" members')
def step_impl(context, audience_member_number):
    assert_that(context.pricing_page.get_member_audience_in_range_text(), is_(audience_member_number), "Audince member is not as expected")

@step(u'I verify that the plan prices is according to the ones below')
def step_impl(context):
    for row in context.table:
        assert_that(context.pricing_page.get_plan_price_text(row['plan']), is_(row['price']), "Price is not as expected")