# https://www.acmicpc.net/problem/9328

# 키를 얻으면 잃지 않는다, 키 1개로 해당하는 대문자는 다 열수 있다
# 열쇠없는 문: 이후에 열쇠를 얻을 수 있음 -> 보관용 큐 26개 이용 (알파벳 수)

from collections import deque
moves = [(0,1),(0,-1),(-1,0),(1,0)]
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # input 밖에서 왔다갔다 가능하므로 이를 구현
    a = ['*.' + input() + '.*' for _ in range(n)]
    n += 4
    m += 4
    a = ['*' * m, '*' + '.' * (m - 2) + '*'] + a + ['*' + '.' * (m - 2) + '*', '*' * m]
    key = set(input())
    
    ans = 0
    check = [[False] * m for _ in range(n)]
    q = deque()
    door = [deque() for _ in range(26)]
    q.append((1,1))
    check[1][1] = True

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + moves[k], c + moves[k]
            if check[nr][nc]:
                continue
            w = a[nr][nc]
            if w == '*':
                continue
            check[nr][nc] = True
            if w == '.':
                q.append((nr, nc))
            elif w == '$':
                q.append((nr, nc))
                ans += 1
            elif 'A' <= w <= 'Z':
                if w.lower() in key:
                    q.append((nr, nc))
                else:
                    door[ord(w) - ord('A')].append((nr, nc))
            elif 'a' <= w <= 'z':
                q.append((nr, nc))
                if not w in key:
                    key.add(w)
                    q.extend(door[ord(w) - ord('a')])
print(ans)