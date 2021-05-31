# if
# python은 switch 문이 없다
weight = 70
if weight > 50:
    print('a')
elif weight > 60:
    print('b')
else:
    print('c')

# for
# loop statement
# continue, break
for i in range(10):
    print(i)

for i in range(10):
    if i == 5:
        continue  # continue 뒤를 실행 x 다시 for문
    else:
        print(i)

for i in range(10):
    print(i)
    if i == 4:
        break  # loop 중단
