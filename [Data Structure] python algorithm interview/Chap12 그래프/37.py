# 부분 집합
nums = [1,2,3]

def subsets(nums):
    result = []

    def dfs(idx, path):
        result.append(path)

        for i in range(idx, len(nums)):
            dfs(i+1, path+[nums[i]])

    dfs(0, [])
    return result