#### input ####
n = 25
k = 5
#### input ####

count = 0

while True:
    # k로 나눠서 떨어지는 수가 될 때까지 1씩 빼기 
    # (한번에 진행)
    exact_num = (n // k) * k
    count += (n - exact_num)
    n = exact_num
    # n이 K보다 작을 때 반복문 break
    if n < k:
        break
    # k로 나누기
    count += 1
    n //= k

# n < k의 경우, 남은 수만큼 1씩 빼기
count += (n-1)

print(count)

# 아래처럼 할 수도 있지만 느리다
# count = 0
# while n != 1:   
#     if n % k == 0:
#         n //= k
#         count += 1
#     else:
#         n -= 1
#         count += 1