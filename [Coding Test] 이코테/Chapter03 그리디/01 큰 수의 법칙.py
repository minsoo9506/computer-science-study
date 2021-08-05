#### input ####
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
#### input ####

# 가장 큰 수와 두번째 큰 수만 사용하면 된다
data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수 (first) 가 더해지는 횟수 계산
count = (m // (k+1)) * k + m % (k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)

# 이렇게 해도 되지만 시간초과
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1