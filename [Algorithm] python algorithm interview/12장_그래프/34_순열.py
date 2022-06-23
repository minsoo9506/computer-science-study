# https://leetcode.com/problems/permutations/


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_values = []

        def dfs(values):
            if len(values) == 0:
                result.append(prev_values[:])

            for value in values:
                next_values = values[:]
                next_values.remove(value)

                prev_values.append(value)
                dfs(next_values)
                prev_values.pop()

        dfs(nums)
        return result
