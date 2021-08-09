arr = [1,1,2,2,2,2,3,4,5]
x = 2

from bisect import bisect_left, bisect_right

def count_by_range(arr, left_val, right_val):
    right_idx = bisect_right(arr, right_val)
    left_idx = bisect_left(arr, left_val)
    return right_idx - left_idx

count = count_by_range(arr, x, x)

print(count)