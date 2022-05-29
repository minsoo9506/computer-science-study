# https://leetcode.com/problems/array-partition-i/

nums = [1, 4, 3, 2]


def solution(nums):
    sum = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            sum += nums[i]
    return sum


print(solution(nums))
