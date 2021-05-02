from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    cols = len(matrix[0])
    left, right = 0, len(matrix) * cols - 1
    while left + 1 < right:
        mid = (left + right) // 2
        value = matrix[int(mid / cols)][mid % cols]
        if value == target:
            return True
        elif value > target:
            right = mid
        else:
            left = mid
    x, y = int(left / cols), left % cols
    if matrix[x][y] == target:
        return True

    x, y = int(right / cols), right % cols
    if matrix[x][y] == target:
        return True

    return False


if __name__ == '__main__':
    numbers = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 5
    assert search_matrix(numbers, target)
