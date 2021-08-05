# 이진탐색 구현
data = [1,2,3,4,5,6,7,8,9]
x = 3

data.sort()

def binary_search(data, x, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if data[mid] == x:
        return True
    elif data[mid] > x:
        return binary_search(data, x, start, mid - 1)
    else:
        return binary_search(data, x, mid + 1, end)

if binary_search(data, x, 0, len(data)-1):
    print('Yes')
else:
    print('No')