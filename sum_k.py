def sum_k(k):
    """Returns the sum of the first k positive integer"""
    if k < 0:
        raise(ValueError("K must be a postive integer"))
    
    return k/2 * (k+1)

assert sum_k(1) == 1
assert sum_k(2) == 3
assert sum_k(3) == 6
assert sum_k(4) == 10