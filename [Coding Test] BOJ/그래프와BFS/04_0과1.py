# https://www.acmicpc.net/problem/8111
# 잘 모르겠음...

# a를 b로 나누면 나머지는 0 ~ b-1 이다 : 이를 이용

# next_val: 1부터 시작해서 하나씩 now * 10 + (1 or 0) 해서 숫자가 커지고
# 이를 n을 나눠서 나머지를 계산

# now라는 수를 n으로 나누어서 나머지가 0이 아니면
# next_val을 하는데
# now와 나머지가 같은 임의의 수는 next_val의 나머지도 같기에 할 필요 x

from collections import deque

t = int(input())
data = [0] * t
for i in range(t):
    n = int(input())
    
    via = [-1] * n  # 어디에서 만들어졌는지
    how = [-1] * n  # 방법 0, 1
    dist = [-1] * n # 나올 수 있는 나머지 갯수
    
    q = deque()
    q.append(1 % n)
    dist[1 % n] = 0
    how[1 % n] = 1

    while q:
        now = q.popleft()
        for i in [0, 1]:
            next_val = (now * 10 + i) % n
            if dist[next_val] == -1:
                dist[next_val] = dist[now] + 1
                via[next_val] = now
                how[next_val] = i
                q.append(next_val)
    if dist[0] == -1: # 나머지=0 인 경우가 없음
        print('brak')
    else:
        ans = ''
        i = 0
        while i != -1:
            ans += str(how[i])
            i = via[i]
        print(ans[::-1])