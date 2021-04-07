# 이진 탐색 트리 합의 범위

# DFS 가지치기
def rangeSumBST(root: TreeNode, L: int, R: int) -> int:
    def dfs(node: TreeNode):
        if not node:
            return 0

        if node.val < L:
            return dfs(node.right)
        elif node.val > R:
            return dfs(node.left)
        else:
            return node.val + dfs(node.left) + dfs(node.right)

    return dfs(root)

# stack을 이용한 dfs
def rangeSumBST(root: TreeNode, L: int, R: int) -> int:
    stack, sum = [root], 0
    while stack:
        node = stack.pop()
        if node:
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
            if L <= node.val <= R:
                sum += node.val
    return sum