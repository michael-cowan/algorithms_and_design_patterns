import matplotlib.pyplot as plt


def binary_search(val, data, ind=0, _stops=[]):
    """
    Conducts a binary search on a sorted data list
    and returns the index
    - returns -1 if val not in data
    """
    if data:
        i = len(data) // 2
        _stops.append(data[i])
        if val == data[i]:
            return ind + i, _stops
        elif val < data[i]:
            return binary_search(val, data[:i], ind, _stops)
        else:
            return binary_search(val, data[i:], ind + i, _stops)
    else:
        return -1, _stops


if __name__ == '__main__':
    data = range(100000)
    val = 44000
    index, stops = binary_search(val, data)

    x = range(len(stops))
    plt.plot(x, [val] * len(x), color='k')
    plt.plot(x, stops, 'o-')
    plt.show()
