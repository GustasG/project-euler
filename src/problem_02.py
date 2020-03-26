def fibonacci_sumator(max_limit: int) -> int:
    total = 0
    previous_number = 1
    current_number = 1

    while current_number < max_limit:
        if current_number % 2 == 0:
            total += current_number
            
        previous_number, current_number = current_number, current_number + previous_number

    return total

print(fibonacci_sumator(4000000))