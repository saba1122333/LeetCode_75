
from typing import Optional
import sys

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]


# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
#         if not root:
#             return []
#         queue = [root]
#         levels = []
#         while queue:
#             size = len(queue)
#             for i in range(size):
#                 rt = queue.pop(0)
#                 if rt.left:
#                     queue.append(rt.left)
#                 if rt.right:
#                     queue.append(rt.right)
#                 if i == size-1:
#                     levels.append(rt.val)
#         return levels


# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
# Example 1:

# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation:
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.

# class Solution:
#     def maxLevelSum(self, root: Optional[TreeNode]) -> int:
#         queue = [root]
#         maxSum, maxSumLevel, level = -sys.maxsize - 1, 0, 0
#         while queue:
#             level += 1
#             size, levelSum = len(queue), 0
#             for _ in range(size):
#                 rt = queue.pop(0)
#                 if rt.left:
#                     queue.append(rt.left)
#                 if rt.right:
#                     queue.append(rt.right)
#                 levelSum += rt.val

#             if levelSum > maxSum:
#                 maxSum = levelSum
#                 maxSumLevel = level

#         return maxSumLevel
