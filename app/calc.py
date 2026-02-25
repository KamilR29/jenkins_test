def add(a: int, b: int) -> int:
    return a + b

def div(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero")
    return a / b