# https://leetcode.com/problems/3sum/

nums = [-1, 0, 1, 2, -1, -4]

# 투 포인터

nums.sort()

result = []
for i in range(len(nums) - 2):
    left, right = i + 1, len(nums) - 1

    # 중복인 경우 skip
    if nums[i - 1] == nums[i]:
        continue

    while left < right:
        sum_val = nums[i] + nums[left] + nums[right]
        if sum_val < 0:
            left += 1
        elif sum_val > 0:
            right -= 1
        else:
            # 정답저장
            result.append([nums[i], nums[left], nums[right]])
            # left, right 동일한 값 skip
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            left += 1
            right -= 1

print(result)
