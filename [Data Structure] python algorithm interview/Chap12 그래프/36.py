# 조합의 합
candidates = [2,3,6,7]
target = 7

def combinationSum(candidates, target):
    result = []

    def dfs(csum, idx, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return
        
        # 자신부터 하위 원소까지 나열 by 재귀
        for i in range(idx, len(candidates)):
            dfs(csum - candidates[i], i, path+[candidates[i]])

    dfs(target, 0, [])
    return result

print(combinationSum(candidates, target))