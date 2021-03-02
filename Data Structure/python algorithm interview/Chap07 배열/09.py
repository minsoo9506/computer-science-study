from typing import List
# 세수의 합
nums = [-1, 0, 1, 2, -1, -4]

# 투 포인터로 합 계산
def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i in range(1, len(nums)-2):
        if nums[i] == nums[i-1]:
            continue

        left, right = 0, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1

    return result

result = threeSum(nums)
print(result)