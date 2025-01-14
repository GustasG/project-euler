import math

from shared.numeric import is_pandigital


def last_digits(number: int, n: int) -> int:
    return number % 10**n


def first_digits(number: int, n: int) -> int:
    num_log = math.log(number, 10)
    return number // 10**(int(num_log) - n + 1)


def main() -> None:
    k = 3
    fn1, fn2 = 1, 1

    while True:
        fn = fn1 + fn2

        if is_pandigital(last_digits(fn, 9)) and is_pandigital(first_digits(fn, 9)):
            print(k)
            break

        fn1, fn2 = fn2, fn
        k += 1


if __name__ == "__main__":
    main()
