# https://leetcode.com/problems/daily-temperatures

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
output = [1, 1, 4, 2, 1, 1, 0, 0]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for idx, value in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < value:
                i = stack.pop()
                result[i] = idx - i
            stack.append(idx)
        return result
