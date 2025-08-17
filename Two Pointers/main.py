
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         last_non_zero = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[last_non_zero], nums[i] = nums[last_non_zero], nums[i]


# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true


# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:


# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

# Example 1:
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.



# class Solution:
#     def maxOperations(self, nums: list[int], k: int) -> int:
#         nums.sort()
#         c,i,j =0,0,len(nums)-1
#         while i < j:
#             if nums[i]+nums[j] < k:
#                 i+=1
#             elif nums[i]+nums[j]> k:
#                 j-=1
#             else:
#                 i+=1
#                 j-=1
#                 c+=1
#         return c

# class Solution:
#     def maxOperations(self, nums: list[int], k: int) -> int:
#         counter = collections.Counter(nums)
#         res = 0
#         for key in counter:
#             if counter[k - key]:
#                 res +=counter[k - key]
#         return res


# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         i, j = 0, len(height)-1
#         max_area = 0
#         while i < j:
#             l_pole, r_pole = height[i],height[j]
#             area = min(l_pole,r_pole) * (j-1)
#             max_area = max(max_area,area)
#             if l_pole <=r_pole:
#                 i+=1
#             else:
#                 j-=1
#         return max_area

