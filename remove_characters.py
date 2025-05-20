def remove_characters(input_string, to_remove):
    """Removes characters from string"""
    to_remove_set = set(to_remove)
    
    result = []
    
    for char in input_string:
        if char not in to_remove_set:
            result.append(char)
    
    return ''.join(result)

new_string = remove_characters('abcd', 'c')
print(new_string)