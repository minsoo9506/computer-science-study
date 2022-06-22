# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# DFS
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def dfs(idx, letter):
            if len(letter) == len(digits):
                result.append(letter)
                return None
            else:
                for d in dic[digits[idx]]:
                    dfs(idx + 1, letter + d)

        dfs(0, "")

        return result
