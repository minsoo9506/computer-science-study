arr = [-15, -6, 1, 3, 7]

def find(arr, left_idx, right_idx):
    if left_idx > right_idx:
        return None
    mid_idx = (left_idx + right_idx) // 2
    mid_val = arr[mid_idx]
    if mid_idx == mid_val:
        return mid_idx
    elif mid_idx > mid_val:
        find(arr, mid_idx + 1, right_idx)
    else:
        find(arr, left_idx, mid_idx -1)
    return None

print(find(arr, 0, len(arr) - 1))