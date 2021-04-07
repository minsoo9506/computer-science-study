# 두 이진 트리 병합
def mergeTree(t1: TreeNode, t2: TreeNode):
    if t1 and t2:
        node = TreeNode(t1.val+t2.val)
        node.left = mergeTree(t1.left, t2.left)
        node.right = mergeTree(t1.right, t2.right)
        return node
    else:
        return t1 or t2