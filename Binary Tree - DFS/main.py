
from locale import currency
import re
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


# class Solution:
#     def dfs(self, root: Optional[TreeNode], node_vals: Optional[list[int]]):
#         if not root:
#             return
#         if not root.left and root.right:
#             node_vals.append(root.val)
#             return
#         self.dfs(root.left, node_vals)
#         self.dfs(root.right, node_vals)

#     def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#         node_vals_1, node_vals_2 = [], []
#         self.dfs(root1, node_vals_1)
#         self.dfs(root2, node_vals_2)
#         if len(node_vals_1) != len(node_vals_2):
#             return False
#         for node1, node2 in zip(node_vals_1, node_vals_2):
#             if node1 != node2:
#                 return False
#         return True


# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.


# Example 1:

# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

# class Solution:
    # def maxDfs(self, root: Optional[TreeNode], max_val: int) -> int:
    #     if not root:
    #         return 0
    #     if root.val >= max_val:
    #         return self.maxDfs(root.left, root.val) + self.maxDfs(root.right, root.val) + 1
    #     else:
    #         return self.maxDfs(root.left, root.val) + self.maxDfs(root.right, root.val)
    # using stored argumetns
    # def maxDfs(self, root: Optional[TreeNode], max_val: int, nodes: list[int]) -> None:
    #     if not root:
    #         return
    #     if root.val >= max_val:
    #         max_val = root.val
    #         nodes[0] += 1
    #     self.maxDfs(root.left, max_val, nodes)
    #     self.maxDfs(root.right, max_val, nodes)

    # def goodNodes(self, root: TreeNode) -> int:
    #     nodes = [0]
    #     self.maxDfs(root, root.val, nodes)
    #     return nodes[0]


# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Example 1
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.


# class Solution:
#     def dfs(self, root: Optional[TreeNode], curSum: int, targetSum: int, prefix: dict) -> int:
#         if not root:
#             return 0
#         curSum += root.val
#         count = prefix.get(curSum-targetSum, 0)
#         prefix[curSum] = prefix.get(curSum,0) + 1
#         count += self.dfs(root.left, curSum, targetSum, prefix)
#         count += self.dfs(root.right, curSum, targetSum, prefix)
#         prefix[curSum] =  prefix.get(curSum,0) - 1
#         return count

#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         prefix = {0: 1}
#         return self.dfs(root, 0, targetSum, prefix)


# You are given the root of a binary tree.
# A ZigZag path for a binary tree is defined as follow:
# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
# Return the longest ZigZag path contained in that tree.


# Example 1:


# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).


# class Solution:
#     def maxZigZag(self, root: Optional[TreeNode], maxZig: list[int], direction: int):
#         if not root:
#             return 0
#         zigLeft = self.maxZigZag(root.left, maxZig, "left") + 1
#         zigRight = self.maxZigZag(root.right, maxZig, "right") + 1
#         if direction == "right":
#             if maxZig[0] < zigLeft:
#                 maxZig[0] = zigLeft
#             return zigLeft
#         if direction == "left":
#             if maxZig[0] < zigRight:
#                 maxZig[0] = zigRight
#             return zigRight
#         return 1

#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         maxZig = [0]
#         self.maxZigZag(root.left, maxZig, "left")
#         self.maxZigZag(root.right, maxZig, "right")
#         return maxZig


# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q
# as descendants (where we allow a node to be a descendant of itself).”


# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        lTree = self.lowestCommonAncestor(root.left, p, q)
        rTree = self.lowestCommonAncestor(root.right, p, q)

        if lTree and rTree:
            return root

        elif lTree:
            return lTree

        elif rTree:
            return rTree
        else:
            return None
