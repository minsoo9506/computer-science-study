# https://leetcode.com/problems/product-of-array-except-self/

nums = [1, 2, 3, 4]


def solution(nums):
    result = []
    p = 1
    for num in nums:
        result.append(p)
        p *= num
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= p
        p *= nums[i]
    return result


print(solution(nums))
