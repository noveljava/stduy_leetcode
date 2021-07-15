# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from helper import make_tree_from_list, TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self._longest: int = 0

        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self._longest = max(self._longest, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self._longest


root = make_tree_from_list([3, None, 1, 2])
print(Solution().diameterOfBinaryTree(root))
