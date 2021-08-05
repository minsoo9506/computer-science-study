n = 5
max_data = 3
data = [1,3,2,3,2]

# 무게가 다른 공을 고르는 경우의 수

# count에 각 무게의 공이 몇개 있는지 담겨있다
count = [0] * (max_data + 1)
for x in data:
    count[x] += 1

print(count)

result = 0
for x in range(1, max_data + 1):
    n -= count[x]
    result += n * count[x]

print(result)
