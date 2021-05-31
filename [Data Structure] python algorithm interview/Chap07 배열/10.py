from typing import List
# 배열 파티션
nums = [1,4,3,2]

# 짝수합
def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    result = 0
    for i in range(0,len(nums),2):
        result += nums[i]

    return result

# 파이썬다운 방식
def arrayPairSum(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])