from typing import List


def subsets2(nums: List[int]) -> List[List[int]]:
    def backtrack(first=0, curr=[]):
        if len(curr) == k and curr not in output:
            output.append(curr[:])
            return
        for i in range(first, n):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

    output = []
    n = len(nums)
    nums.sort()
    for k in range(n + 1):
        backtrack()
    return output


if __name__ == '__main__':
    numbers = [4, 4, 4, 1, 4]
    assert sorted(subsets2(numbers)) == \
           sorted([[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]])
