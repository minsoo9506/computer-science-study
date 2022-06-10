# https://leetcode.com/problem/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {")": "(", "}": "{", "]": "["}
        for bracket in s:
            if bracket in ["(", "{", "["]:
                stack.append(bracket)
            elif not stack or table[bracket] != stack.pop():
                return False
        return len(stack) == 0
