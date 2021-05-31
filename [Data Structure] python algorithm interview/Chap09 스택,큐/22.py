# 일일 온도
T = [73, 74, 75, 71, 69, 72, 76, 73]

from typing import List

def dailyTemperature(T: List[int]) -> List[int]:
    answer = [0] * len(T)
    stack = [] 
    # stack에 index를 넣고 
    # 더 큰 값이 나왔을때 그 index와의 
    # 차이를 구해서 사용
    
    for i, current in enumerate(T):
        while stack and current > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer


print(dailyTemperature(T))