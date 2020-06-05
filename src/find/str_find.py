def find_index(str, pattern):
    str_len = len(str)
    pattern_len = len(pattern)
    i = 0
    j = 0
    while i < str_len - 1 and j < pattern_len:
        s = str[i]
        p = pattern[j]
        if s == p:
            i = i + 1
            j = j + 1
        else:
            i = i - j + 1
            j = 0
    if j == pattern_len:
        return i - j
    else:
        return -1





if __name__ == '__main__':
    str = 'BBC ABCDAB ABCDABCDABDE'
    pattern = 'ABCDABD'
    print(find_index(str, pattern))
# 模式串匹配暴力匹配法
