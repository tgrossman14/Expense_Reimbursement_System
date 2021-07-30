# Configures cucumber environment. Modifies behave context.
# Referenced before any individual step definition

from selenium import webdriver
from testing.mercury.poms.login_page import MASHLoginPage
from testing.mercury.poms.employee_dash_page import EmployeeDashPage
from testing.mercury.poms.manager_dash_page import ManagerDashPage
from testing.mercury.poms.stats_page import StatsPage


# Runs before any features
def before_all(context):
    # Context gives access to metadata about features, scenarios, and steps
    # Treat metadata as read-only. Custom properties may be added.
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\Tal\6-7-2021-pyjwa\chromedriver")
    context.ml_page = MASHLoginPage(context.driver)
    context.ed_page = EmployeeDashPage(context.driver)


# Setup and teardown options:
def before_setup(context, step):
    pass


def before_scenario(context, scenario):
    # May want url for homepage here because there are two scenarios involving logging in
    pass


def before_feature(context, feature):
    pass


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    pass


def after_feature(context, feature):
    pass


def after_scenario(context,scenario):
    pass


def after_all(context):
    # Close browser after each test
    context.driver.quit()
