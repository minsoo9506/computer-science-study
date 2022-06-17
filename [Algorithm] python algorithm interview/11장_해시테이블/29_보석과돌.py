# https://leetcode.com/problems/jewels-and-stones

from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = defaultdict(int)
        count = 0

        for s in stones:
            freqs[s] += 1

        for j in jewels:
            count += freqs[j]

        return count


# 그냥 collections.Counter 이용해도 될 것 같다
