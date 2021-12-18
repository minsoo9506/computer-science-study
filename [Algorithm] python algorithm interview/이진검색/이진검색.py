# 정렬된 nums에서 이진검색으로 target의 index를 찾기
nums = [-1,0,3,5,9,12]
target = 9

def binary_search(start, end):
    if start > end:
        return
    mid = (start + end) // 2 # overflow 발생하면 : left + (right - left) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binary_search(start, mid - 1) # return 넣는 것 까먹지 말자
    else:
        return binary_search(mid + 1, end)

print(binary_search(0, len(nums) - 1))


#### bisect 이용 ####
import bisect

def solution():
    idx = bisect.bisect_left(nums, target)
    if idx < len(nums) and nums[idx] == target:
        return idx
    else:
        return -1