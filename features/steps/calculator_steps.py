import math
import re

from behave import given, when, then

from calc import Calculator

EXPRESSION_PATTERN = re.compile(r"^\s*(-?\d+(?:\.\d+)?)\s*([\+\-\*/])\s*(-?\d+(?:\.\d+)?)\s*$")


def parse_number(text):
    return float(text) if "." in text else int(text)


@given("내가 계산기를 켰을 때")
def step_given_start_calculator(context):
    context.calc = Calculator()
    context.result = None
    context.error = None


@when('나는 "{expression}" 를 계산한다')
def step_when_calculate(context, expression):
    match = EXPRESSION_PATTERN.match(expression)
    if not match:
        raise AssertionError(f"지원하지 않는 수식 형식: {expression}")

    a_text, operator, b_text = match.groups()
    a = parse_number(a_text)
    b = parse_number(b_text)

    try:
        context.result = context.calc.calculate(a, operator, b)
        context.error = None
    except Exception as exc:  # 계산 중 예외 저장
        context.result = None
        context.error = exc


@then('결과는 {expected} 이어야 한다')
def step_then_result(context, expected):
    assert context.error is None, f"예상치 못한 오류 발생: {context.error}"

    actual = context.result
    assert actual is not None, "결과가 설정되지 않았습니다."

    expected_value = parse_number(expected)

    if isinstance(actual, float) or isinstance(expected_value, float):
        assert math.isclose(actual, float(expected_value), rel_tol=1e-9, abs_tol=1e-9), (
            f"예상값 {expected_value} vs 실제값 {actual}"
        )
    else:
        assert actual == expected_value, f"예상값 {expected_value} vs 실제값 {actual}"


@then('오류 메시지는 "{message}" 이어야 한다')
def step_then_error_message(context, message):
    assert context.error is not None, "오류가 발생해야 하지만 결과가 존재합니다."
    assert str(context.error) == message, (
        f'예상 오류 메시지 "{message}" vs 실제 메시지 "{context.error}"'
    )
