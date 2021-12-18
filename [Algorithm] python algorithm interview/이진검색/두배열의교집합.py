num1 = [1,2,2,1]
num2 = [2,2]

# num1_set = set(num1)
# num2_set = set(num2)
# result = num1_set.intersection(num2_set)
# print(result)

# 이진검색으로 찾기
import bisect

result = set()
num1.sort()

for n1 in num1:
    n2_idx = bisect.bisect_left(num2, n1)
    if n1 == num2[n2_idx]:
        result.add(n1)
print(result)