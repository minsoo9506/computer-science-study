# https://www.acmicpc.net/problem/1931

n = int(input())
meet = []

for i in range(n):
    a, b = map(int, input().split())
    meet.append([a,b])

meet.sort(key=lambda x : (x[1], x[0]))

answer = 0
end_time = 0

for i in range(n):
    if end_time <= meet[i][0]:
        end_time = meet[i][1]
        answer += 1

print(answer)