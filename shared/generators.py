from typing import Any, Generator, Iterable

from shared.primes import is_prime


def even(iterable: Iterable[int]) -> Generator[int, Any, None]:
    for value in iterable:
        if value % 2 == 0:
            yield value


def odd(iterable: Iterable[int]) -> Generator[int, Any, None]:
    for value in iterable:
        if value % 2 != 0:
            yield value


def fibonacci(limit: int) -> Generator[int, Any, None]:
    prev, curr = 1, 1

    while curr < limit:
        yield curr
        prev, curr = curr, curr + prev


def prime_generator(limit: int) -> Generator[int, Any, None]:
    for i in range(2, limit):
        if is_prime(i):
            yield i


def number_digits(number: int) -> Generator[int, Any, None]:
    number = abs(number)

    while number > 0:
        yield number % 10
        number //= 10


def factorization(number: int) -> Generator[int, Any, None]:
    for d in range(2, int(number**0.5) + 1):
        while number % d == 0:
            number //= d
            yield d

    if number > 1:
        yield number
