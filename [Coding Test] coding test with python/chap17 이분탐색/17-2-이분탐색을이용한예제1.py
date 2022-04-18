# https://www.acmicpc.net/problem/1920
# 수 찾기

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

def binary_search(target):
    start, end = 0, n - 1
    mid = (start + end) // 2
    while start <= end:
        if a[mid] == target:
            return mid
        elif a[mid] > target:
            start = mid + 1
        else:
            end = mid - 1

result = 0
for i in b:
    tof = binary_search(0, len(a) - 1, i)
    if tof:
        result += 1

print(result)