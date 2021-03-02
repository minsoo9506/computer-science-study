x = [1, 2, 3]
y = [100, x, 120]  # list 안에 list가 들어간다(nested)
print(y)

# 이렇게 하면 x를 수정하면 y도 수정된다
# x has two reference from y
# 그냥 int, float은 reference를 사용하지 않지만
# list, tuple 등 과 같은 object들은 사용
x[1] = 171
print(y)

# == vs is
# == 는 값을 비교 is는 저장된 id, 위치
print(x[1] == y[1][1])  # True
print(x[1] is y[1][1])  # True
z = [1, 2, 3]
print(x is z)  # False
print(x == z)  # True
