class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("0으로 나눌 수 없음")
        return a / b

    def calculate(self, a, operator, b):
        operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
        }
        if operator not in operations:
            raise ValueError(f"지원하지 않는 연산자: {operator}")
        return operations[operator](a, b)
