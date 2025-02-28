def coin_sum(coins: list[int], size: int, target: int) -> int:
    if target == 0:
        return 1

    if target < 0:
        return 0

    if size <= 0 and target >= 1:
        return 0

    return coin_sum(coins, size - 1, target) + coin_sum(coins, size, target - coins[size - 1])


def main() -> None:
    coins = [1, 2, 5, 10, 20, 50, 1 * 100, 2 * 100]
    value = 200

    print(coin_sum(coins, len(coins), value))


if __name__ == '__main__':
    main()
