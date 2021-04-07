# 가장 긴 동일값의 경로
class Solution:
    def __init__(self):
        self.result = 0

    def diameterOfBinary(self, root):
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left+right)
            return max(left, right)

        dfs(root)
        return self.result