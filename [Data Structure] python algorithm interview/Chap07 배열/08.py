from typing import List, Set, Dict, Tuple
# 빗물 트래핑
input_value = [0,1,0,2,1,0,1,3,2,1,2,1]

# 01 투 포인터를 최대로 이동
def trap(height: List[int]) -> int:
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max),
                              max(height[right], right_max)
        
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
        
    return volume