# Definition for a binary tree node.
from helper import TreeNode, make_tree_from_list


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.max_depth = 0

        def tracking(node: TreeNode, depth: int):
            if root.val is not None:
                self.max_depth = max(self.max_depth, depth)
                if node.left is not None:
                    tracking(node.left, depth+1)

                if node.right is not None:
                    tracking(node.right, depth+1)

        tracking(root, 0)
        return self.max_depth


root = make_tree_from_list([3, 9, 20, None, None, 15, 7])
print(Solution().maxDepth(root))
