nums = [1,3,-1,-3,5,3,6,7]
k = 3

from collections import deque

def solution(nums, k):
    window = deque()
    result = []
    current_max = -int(1e9)
    for idx, v in enumerate(nums):
        if idx < k - 1:
            continue
        
        if current_max == -int(1e9):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        result.append(current_max)

        if current_max == window.popleft():
            current_max = -int(1e9)
    
    return result