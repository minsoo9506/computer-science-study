n = 5
data = [2,3,1,2,2]

result = 0
count = 0

# 오름차순 정렬
data.sort()

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)