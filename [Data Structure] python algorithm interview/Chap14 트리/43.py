# 이진 트리의 직경
class Solution:
    def __init__(self):
        self.longest = 0

    def diameterOfBinary(self, root):
        def dfs(node):
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left+right+2)
            
            return max(left, right) + 1

        dfs(root)
        return self.longest