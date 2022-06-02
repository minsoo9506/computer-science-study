# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

nums = [7, 1, 5, 3, 6, 4]


def solution(nums):
    min_val = int(1e9)
    profit = 0
    for num in nums:
        min_val = min(min_val, num)
        profit = max(profit, num - min_val)
    return profit


print(solution(nums))
