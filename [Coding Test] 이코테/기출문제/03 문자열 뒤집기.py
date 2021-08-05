# 연속된 숫자 뒤집어서 모두 똑같은 숫자로 만들기
num = '0001100'

num_of_1 = 0
num_of_0 = 0

if num[0] == '1':
    num_of_1 += 1
else:
    num_of_0 += 1

for i in range(len(num)-1):
    if num[i] != num[i + 1]:
        if num[i + 1] == '0':
            num_of_0 += 1
        else:
            num_of_1 += 1

print(min(num_of_0, num_of_1))
