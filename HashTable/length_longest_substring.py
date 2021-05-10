def length_longest_substring(s: str) -> int:
    if not s:
        return 0
    if len(s) == 1:
        return 1
    char_dict = {s[0]: 0}
    lf, rt = 0, 0
    longest_substring = 0
    while rt + 1 < len(s):
        rt += 1
        if s[rt] not in char_dict:
            char_dict[s[rt]] = rt
        else:
            if lf <= char_dict[s[rt]]:
                lf = char_dict[s[rt]] + 1
                char_dict[s[rt]] = rt
            else:
                char_dict[s[rt]] = rt
        if rt - lf + 1 > longest_substring:
            longest_substring = rt - lf + 1
    return longest_substring


if __name__ == '__main__':
    s = "abba"
    assert length_longest_substring(s) == 3
