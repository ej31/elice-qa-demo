# calc.py
def add(a: float, b: float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("0으로는 나눌 수 없습니다.")
    return a / b

if __name__ == "__main__":
    # 예시 실행
    print("2 + 3 =", add(2, 3))
