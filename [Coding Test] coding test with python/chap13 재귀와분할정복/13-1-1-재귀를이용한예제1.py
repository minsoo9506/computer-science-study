# https://www.acmicpc.net/problem/10872

n = int(input())

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

print(factorial(n))