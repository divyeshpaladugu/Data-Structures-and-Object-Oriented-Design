def contains_permutation(input_string, pattern):
    """Determins if string input contains permutation(pattern)"""
    if len(input_string) < len(pattern):
        return False

    my_dict = {}
    new_dict = {}

    for char in pattern:
        my_dict[char] = my_dict.get(char, 0) + 1
    for char in input_string[:len(pattern)]:
        new_dict[char] = new_dict.get(char, 0) + 1

    if new_dict == my_dict:
        return True

    for i in range(len(pattern), len(input_string)):
        new_dict[input_string[i - len(pattern)]] -= 1
        if new_dict[input_string[i - len(pattern)]] == 0:
            del new_dict[input_string[i - len(pattern)]]
        new_dict[input_string[i]] = new_dict.get(input_string[i], 0) + 1

        if new_dict == my_dict:
            return True

    return False

result = contains_permutation('abcdef', 'cab')
print(result)