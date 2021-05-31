from typing import List, Set, Dict, Tuple
# 두 수의 합
nums = [2, 7, 11, 15]
target = 9

# 첫번째 수를 뺀 결과 조회
def twoSum(nums:List[int], target:int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num],i]
        nums_map[num] = i

result = twoSum(nums, target)
print(result)