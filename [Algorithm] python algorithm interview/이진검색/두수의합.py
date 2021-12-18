nums = [2,7,11,15]
target = 9

# 정렬된 배열에서 target을 만들 수 있는 두 숫자 index

# 투포인터
def solution1(nums, target):
    left, right = 0, len(nums) - 1
    while left != right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return left, right