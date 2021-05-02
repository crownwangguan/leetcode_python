from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    def backtrack(nums, used, current, results):
        if len(nums) == len(current):
            results.append(current[:])
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i-1] == nums[i] and not used[i-1]):
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
    numbers = [1, 1, 2]
    assert sorted(permute(numbers)) == \
           sorted([[1, 1, 2],
                   [1, 2, 1],
                   [2, 1, 1]])
