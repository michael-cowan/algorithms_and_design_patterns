def binary_search(val, data, ind=0, verbose=False):
    """
    Conducts a binary search on a sorted data list
    and returns the index
    - returns -1 if val not in data
    """
    if data:
        i = len(data) // 2
        if verbose:
            print(data[i])
        if val == data[i]:
            return ind + i
        elif val < data[i]:
            return binary_search(val, data[:i], ind, verbose)
        else:
            return binary_search(val, data[i:], ind + i, verbose)
    else:
        return -1


if __name__ == '__main__':
    data = range(100000)
    print(binary_search(44000, data, verbose=True))
