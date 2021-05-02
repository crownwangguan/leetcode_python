from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    def backtrack(first=0, curr=[]):
        if len(curr) == k:
            output.append(curr[:])
            return
        for i in range(first, n):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

    output = []
    n = len(nums)
    for k in range(n + 1):
        backtrack()
    return output


if __name__ == '__main__':
    numbers = [1, 2, 3]
    assert sorted(subsets(numbers)) == \
           sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
