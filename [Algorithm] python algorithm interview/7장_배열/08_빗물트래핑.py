# https://leetcode.com/problems/trapping-rain-water/

x = [0,1,0,2,1,0,1,3,2,1,2,1]

# 투포인터 이용
def solution1(x):
    if len(x) == 0:
        return 0
    
    volume = 0
    left, right = 0, len(x) - 1
    left_max, right_max = x[left], x[right]
    
    while left <= right:
        left_max, right_max = max(left_max, x[left]), max(right_max, x[right])
        # 더 높은 쪽으로 포인터 이동
        if left_max <= right_max:
            volume += left_max - x[left]
            left += 1
        else:
            volume += right_max - x[right]
            right -= 1
    return volume

# stack 이용
def solution2(x):
    stack = []
    volume = 0
    for i in range(len(x)):
        # 직전보다 높이가 커지는 경우
        while stack and x[i] > x[stack[-1]]:
            top = stack.pop()
            if len(stack) == 0:
                break
            # 이전과의 차이만큼 물 높이 처리
            dis = i - stack[-1] - 1
            waters = min(x[i], x[stack[-1]]) - x[top]
            volume += dis * waters
        stack.append(i)
    return volume