# index in sequence
strTest = 'Hello world!'
print(strTest)
print(strTest[1:3])
print(strTest[:3])
print(strTest[1:])
print(strTest[1:6:2])  # step이 2만큼 띄어서

# List
listTest = [1, 2, 3, 4]
print(listTest[1])
print(listTest + listTest)  # list가 추가된다
print(listTest*3)  # 3번 반복된 list 생성

listTest = range(1, 20, 2)  # 1~19까지 step 2씩
print(listTest)
print(4 in listTest)

listTest = [1, 2, 3, 4]
listTest.append('hey')  # 'hey' 추가 (맨뒤에)
del listTest[0]
listTest.reverse()  # 순서를 반대로
print(listTest)
listTest.remove('hey')  # 'hey' 없애기
print(listTest)
listTest.sort()  # sort 역할
print(listTest)

# Tuple
# list랑 거의 비슷하다
# changing values에서만 다르다
# tuple은 value change를 허용하지 않는다
tplTest = (1, 2, 3)
print(tplTest)
print(tplTest[0])
print(tplTest*3)
# tplTest[0] = 100 불가능

# Dictionary
# not sequential
# key and value
dicTest = {1: 'one', 2: 'two', 3: 'three'}
print(dicTest[1])  # key 를 통해 value 소환!
dicTest[10] = 'ten'
dicTest[1] = 'hana'
print(dicTest)
print(dicTest.keys())
print(dicTest.values())
print(dicTest.items())
