def sumation(k: int, n: int) -> int:
    p = (n - 1) // k
    return k * p * (p + 1) // 2


def multiples(number: int) -> int:
    return sumation(3, number) + sumation(5, number) - sumation(3 * 5, number)

print(f'Result: {multiples(1000)}')