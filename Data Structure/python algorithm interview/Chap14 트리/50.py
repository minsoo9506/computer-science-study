# 정렬된 배열의 이진 탐색 트리 변환
from typing import List

nums = [-10, -3, 0, 5, 9]

def sortedArr(nums: List) -> TreeNode:
    if not nums:
        return None

    mid = len(nums) // 2 # 내림 나눗셈
     
    node = TreeNode(nums[mid])
    node.left = sortedArr(nums[:mid])
    node.right = sortedArr(nums[mid+1:])

    return node