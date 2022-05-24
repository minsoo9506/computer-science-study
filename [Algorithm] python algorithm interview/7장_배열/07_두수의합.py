# https://leetcode.com/problems/two-sum/

nums = [2, 7, 11, 15]
target = 9


def solution(nums, target):
    nums_map = {} # dict를 이용하면 뒤에서 조회할 때 O(1)이 가능
    for i, n in enumerate(nums):
        nums_map[n] = i
        
    for i, n in enumerate(nums):
        if target - n in nums:
            return nums_map[n], nums_map[target - n]
        
print(solution(nums, target))