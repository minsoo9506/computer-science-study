# 이진 탐색 트리를 더 큰 수 합계 트리로

class Solution:
    val = 0

    def bstToGst(self, node: TreeNode):
        if node:
            self.bstToGst(node.right)
            self.val += node.val
            node.val = self.val
            self.bstToGst(node.left)