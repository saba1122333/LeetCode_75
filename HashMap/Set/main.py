

# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].

# class Solution:
#     def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
#         return [[list(set(nums1)-set(nums2))],list(set(nums2)-set(nums1))]


# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

# import collections


# class Solution:
#     def uniqueOccurrences(self, arr: list[int]) -> bool:
#         counter = collections.Counter(arr)
#         occurrences = sorted(counter.values())
#         for i in range(1,len(occurrences)):
#             if occurrences[i] == occurrences[i-1]:
#                 return False
#         return True


# IS NOT IMPLEMENTED YET


# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

# Example 1:

# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"


# from collections import Counter

# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         if set(word1) != set(word2):
#             return False
#         return sorted(Counter(word1).values()) == sorted(Counter(word2).values())


# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).


# Example 1:

# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]


# class Solution:
#     def equalPairs(self, grid: list[list[int]]) -> int:
#         dict = {}
#         ans = 0
#         for row in grid:
#             key = hash(tuple(row))
#             if key in dict:
#                 dict[key] += 1
#             else:
#                 dict[key] = 1

#         for col in zip(*grid):
#             key = hash(tuple(col))
#             if key in dict:
#                 ans += dict[key]
#         return ans

