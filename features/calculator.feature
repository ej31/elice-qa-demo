Feature: 사칙연산 계산기
  사용자는 계산기를 이용하여 덧셈, 뺄셈, 곱셈, 나눗셈을 수행할 수 있다.

  Background:
    Given 내가 계산기를 켰을 때

  Scenario Outline: 두 숫자의 수식을 계산한다
    When 나는 "<expression>" 를 계산한다
    Then 결과는 <result> 이어야 한다

    Examples:
      | 설명      | expression | result |
      | 덧셈      | 2 + 3      | 5      |
      | 뺄셈      | 10 - 4     | 6      |
      | 곱셈      | 3 * 5      | 15     |
      | 나눗셈    | 8 / 2      | 4      |
      | 소수 덧셈 | 2.5 + 1.5  | 4      |
      | 음수 곱셈 | -2 * 3     | -6     |

  Scenario: 0으로 나누면 오류가 발생한다
    When 나는 "5 / 0" 를 계산한다
    Then 오류 메시지는 "0으로 나눌 수 없음" 이어야 한다
