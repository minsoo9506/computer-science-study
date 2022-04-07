n = int(input())
arr = list(map(int, input().split()))
prefix_sum = [0] * 200001
my_map = {}
answer = 0

my_map[0] = 1
for i in range(n):
    prefix_sum[i] = arr[i]
    if i != 0:
        prefix_sum[i] += prefix_sum[i - 1] # 누적
    if prefix_sum[i] in my_map:
        answer += 1
        my_map.clear()
        my_map[prefix_sum[i - 1]] = 1
    my_map[prefix_sum[i]] = 1
print(answer)