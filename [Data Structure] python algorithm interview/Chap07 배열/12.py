import sys
from typing import List
# 주식을 사고팔기 가장 좋은 시점
nums = [7,1,5,3,6,4]

def maxProfit(nums: List[int]) -> int:
    profit = 0
    min_value = sys.maxsize

    for num in nums:
        min_value = min(min_value, num)
        profit = max(profit, num - min_value)

    return profit