# https://www.acmicpc.net/problem/15649
# N과 M (1)

n, m = map(int, input().split())
answer = []

def backTracking(depth):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n + 1):
        if i in answer:
            continue
        else:
            answer.append(i)
            backTracking(depth + 1)
            answer.pop()

backTracking(0)