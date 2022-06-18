# https://leetcode.com/problems/longest-substring-without-repeating-characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = 0
        max_val = 0
        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_val = max(max_val, idx - start + 1)

            used[char] = idx

        return max_val
