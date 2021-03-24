# 순열
nums = list(input())
#nums = [1,2,3]

def permute(nums):
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements.copy())

        for e in elements:
            next_elements = elements.copy()
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results

import itertools

def permute2(nums):
    return list(itertools.permutations(nums))

print(permute2(nums))