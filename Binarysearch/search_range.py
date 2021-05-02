from typing import List


def search_range(nums: List[int], target: int) -> List[int]:
    start = 0
    end = len(nums) - 1

    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid
        else:
            end = mid
    if nums[start] == target:
        leftBound = start
    elif nums[end] == target:
        leftBound = end
    else:
        return [-1, -1]

    start = leftBound
    end = len(nums) - 1

    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] <= target:
            start = mid
        else:
            end = mid
    if nums[end] == target:
        rightBound = end
    else:
        rightBound = start

    return [leftBound, rightBound]


if __name__ == '__main__':
    numbers = [5, 7, 7, 8, 8, 10]
    target = 8
    assert search_range(numbers, target) == [3, 4]
