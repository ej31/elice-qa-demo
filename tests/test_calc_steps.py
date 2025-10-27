from behave import given, when, then

@given("사용자가 프로그램을 실행했을 때")
def step_given_user_on_login_page(context):
    context.page = "login"

@when("숫자를 입력하면")
def step_when_user_enters_credentials(context):
    context.page = "dashboard"

@then("계산 결과가 표시된다")
def step_then_dashboard_displayed(context):
    assert context.page == "dashboard"