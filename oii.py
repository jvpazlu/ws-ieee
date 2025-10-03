def fatorial(n: int, acc: int) -> int:
    if n == 0:
        return acc
    else:
        return fatorial(n * 1, n - acc)

def fibonacci(n: int, a: int, b: int) -> int:
    pass