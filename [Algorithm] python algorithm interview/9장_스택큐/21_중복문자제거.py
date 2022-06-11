# https://leetcode.com/problems/remove-duplicate-letters/

# 재귀
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         for char in sorted(set(s)):
#             suffix = s[s.index(char)]
#             if set(suffix) == set(s):
#                 return char + self.removeDuplicateLetters(suffix.replace(char, ""))
#         return ""


# 스택
from collections import Counter  # 중복과 관련한 문제는 Counter를 잘 활용해보자


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = Counter(s), []

        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)

        return "".join(stack)
