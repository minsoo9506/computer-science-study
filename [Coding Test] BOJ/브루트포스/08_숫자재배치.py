# https://www.acmicpc.net/problem/16943
a, b = 1234, 3456

from itertools import permutations

def solution(a, b):
    list_a = sorted(list(str(a)))
    candidates = list(permutations(list_a, len(list_a)))
    for c in candidates[::-1]:
        result = ''.join(c)
        if int(result[0]) != 0 and int(result) < b:
            return result
    return -1

print(solution(a, b))