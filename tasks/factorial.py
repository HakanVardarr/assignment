def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n cannot be negative")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
