from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    def backtrack(nums, used, current, results):
        if len(nums) == len(current):
            results.append(current[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = 1
            current.append(nums[i])
            backtrack(nums, used, current, results)
            used[i] = 0
            current.pop()

    results = []
    used = [0] * len(nums)
    backtrack(nums, used, [], results)
    return results


if __name__ == '__main__':
    numbers = [1, 2, 3]
    assert sorted(permute(numbers)) == \
           sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
