from typing import List


def search(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] == target:
            end = mid
        elif nums[mid] < target:
            start = mid
        else:
            end = mid
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end

    return -1


if __name__ == '__main__':
    numbers = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert search(numbers, target) == 4
