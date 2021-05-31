# 조합
import itertools

def combine(n, k):
    return list(itertools.combinations(range(1, n+1), k))