from typing import List


def insert_position(nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1

    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid
        else:
            end = mid
    if nums[start] >= target:
        return start
    elif nums[end] >= target:
        return end
    else:
        return len(nums)


if __name__ == '__main__':
    numbers = [1, 3, 5, 6]
    target = 2
    assert insert_position(numbers, target) == 1
