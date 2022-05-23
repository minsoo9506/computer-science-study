# https://leetcode.com/problems/longest-palindromic-substring/

x = input()

# 투포인터 활용
def longestPalindrome(s):
    def expand(left, right):
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1 : right - 1]
    
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''
    for i in range(0, len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len) # max에서 key를 이용할 수 있다
    return result

result = longestPalindrome(x)
print(result)