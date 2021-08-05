#### input ####
n, m = 3, 3
data = [[3,1,2],
        [4,1,4],
        [2,2,2]]
#### input ####

result = 0
for row in range(n):
    # 해당 row에서 가장 작은 값
    row_min = min(data[row])
    # 가장 작은 값들 중에서 가장 큰 값이 결과
    result = max(result, row_min)

print(result)