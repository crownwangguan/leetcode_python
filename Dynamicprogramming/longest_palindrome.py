def longest_palindrome(s: str) -> str:
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    ans = ''

    for i in range(n):
        dp[i][i] = True
        ans = s[i]

    max_len = 1

    for start in range(n - 1, -1, -1):
        for end in range(start + 1, n):
            if s[start] == s[end]:
                if end - start == 1 or dp[start + 1][end - 1]:
                    dp[start][end] = True
                    if max_len < end - start + 1:
                        max_len = end - start + 1
                        ans = s[start: end + 1]
    return ans


if __name__ == '__main__':
    assert "aba" == longest_palindrome("babad")
