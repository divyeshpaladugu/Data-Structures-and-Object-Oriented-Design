def find_factors(L):
    d_return = dict()

    for item in L:
        d_return[item] = []
        for item2 in L:
            if item % item2 == 0:
                d_return[item].append(item2)

    return d_return

if __name__ == '__main__':
    print(find_factors([6, 7, 18, 1, 3]))