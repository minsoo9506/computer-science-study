# https://leetcode.com/problems/combination-sum


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, idx, lst):
            if csum == target:
                result.append(lst)
                return
            if csum > target:
                return

            # combination이라서 for문에 아래처럼 idx부터 시작해야한다
            for i in range(idx, len(candidates)):
                dfs(csum + candidates[i], i, lst + [candidates[i]])

        dfs(0, 0, [])

        return result
