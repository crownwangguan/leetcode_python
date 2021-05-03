def merge_sort(num):
    if len(num) > 1:
        mid = len(num) // 2
        left = num[:mid]
        right = num[mid:]
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                num[k] = left[i]
                i += 1
            else:
                num[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            num[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            num[k] = right[j]
            j += 1
            k += 1
    return num


if __name__ == '__main__':
    numbers = [12, 4, 5, 6, 7, 3, 1, 15]
    assert merge_sort(numbers) == [1, 3, 4, 5, 6, 7, 12, 15]
