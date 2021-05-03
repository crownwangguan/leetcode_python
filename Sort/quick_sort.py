def quick_sort(num):
    less = []
    equal = []
    greater = []

    if len(num) > 1:
        pivot = num[0]
        for x in num:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return num


if __name__ == '__main__':
    numbers = [12, 4, 5, 6, 7, 3, 1, 15]
    assert quick_sort(numbers) == [1, 3, 4, 5, 6, 7, 12, 15]
