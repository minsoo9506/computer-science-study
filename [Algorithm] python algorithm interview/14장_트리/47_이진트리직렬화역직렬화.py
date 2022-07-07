# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Codec:
    def serialize(self, root):
        q = collections.deque([root])
        # 트리를 배열로 나타낼 때는 index 1부터 시작
        result = ["#"]

        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)

                result.append(str(node.val))
            else:
                result.append("#")
        return result

    def deserialize(self, data):
        if data == ["#", "#"]:
            return None

        root = TreeNode(int(data[1]))
        q = collections.deque([root])
        index = 2

        while q:
            node = q.popleft()
            if data[index] is not "#":
                node.left = TreeNode(int(data[index]))
                q.append(node.left)
            index += 1

            if data[index] is not "#":
                node.right = TreeNode(int(data[index]))
                q.append(node.right)
            index += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
