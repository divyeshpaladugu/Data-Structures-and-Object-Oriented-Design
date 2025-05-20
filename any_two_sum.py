def any_two_sum(numbers, total):
    """Determins if any two numbers in set equal total"""
    numbers_set = set()

    for num in numbers:
        other = total - num
        if other in numbers_set:
            return True

        numbers_set.add(num)

    return False

result = any_two_sum([1, 3, 4, 5], 7)
print(result)