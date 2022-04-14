# https://www.acmicpc.net/problem/11729

n = int(input())

def hanoi(num, start, to, end):
    if num == 1:
        print(start, end)
    else:
        hanoi(num - 1, start, end, to)
        print(start, end)
        hanoi(num - 1, to, start, end)

hanoi(n, 1, 2, 3)