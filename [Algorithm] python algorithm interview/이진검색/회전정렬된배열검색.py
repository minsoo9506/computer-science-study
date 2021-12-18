def solution(nums, target):
    if not nums:
        return -1
    
    pivot = nums.index(min(nums))

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_pivot = (mid + pivot) % len(nums) # 순환구조 -> 나눠서 나머지 이용!

        if nums[mid_pivot] < target:
            left = mid + 1
        elif nums[mid_pivot] > target:
            right = mid - 1
        else:
            return mid_pivot

    return -1