
from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3


# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         return max(self.maxDepth(root.left),self.maxDepth(root.left)) + 1


# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar

# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true


class Solution:
    def dfs(self, root: Optional[TreeNode], node_vals: Optional[list[int]]):
        if not root:
            return
        if not root.left and root.right:
            node_vals.append(root.val)
            return
        self.dfs(root.left, node_vals)
        self.dfs(root.right, node_vals)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        node_vals_1, node_vals_2 = [], []
        self.dfs(root1, node_vals_1)
        self.dfs(root2, node_vals_2)
        if len(node_vals_1) != len(node_vals_2):
            return False
        for node1, node2 in zip(node_vals_1, node_vals_2):
            if node1 != node2:
                return False
        return True
