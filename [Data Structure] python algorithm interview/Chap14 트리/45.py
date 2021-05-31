# 이진트리반전
import collections

# 재귀
def invertTree1(self, root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = \
            self.invertTree1(root.right), self.invertTree1(root.left)
        return root
    return None

# BFS
def invertTree2(root: TreeNode) -> TreeNode:
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()

        if node:
            node.left, node.right = node.right, node.left
        
            queue.append(node.left)
            queue.append(node.right)
    
    return root

# DFS
def invertTree3(root: TreeNode) -> TreeNode:
    stack = collections.deque([root])

    while stack:
        node = stack.pop()

        if node:
            node.left, node.right = node.right, node.left
        
            stack.append(node.left)
            stack.append(node.right)
    
    return root