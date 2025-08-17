
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
#  Any answer with a calculation error less than 10-5 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# class Solution:
#     def findMaxAverage(self, nums: list[int], k: int) -> float:
#         sl_sum = sum(nums[0: 0 + k])
#         mx_sum = sl_sum
#         for i in range(len(nums)-k):
#             sl_sum = sl_sum + nums[i+k]-nums[i]
#             mx_sum = max(sl_sum, mx_sum)
#         return mx_sum / k


# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:
#         vowels_hash = dict.fromkeys(['a', 'e', 'i', 'o', 'u'], 0)
#         sl_sum, mx_sum = 0, 0
#         for i in range(k):
#             if s[i] in vowels_hash:
#                 sl_sum += 1
#         mx_sum = sl_sum

#         for i in range(len(s)-k):
#             if s[i+k] in vowels_hash:
#                 sl_sum += 1
#             if s[i] in vowels_hash:

#                 sl_sum = max(sl_sum-1, 0)
#             mx_sum = max(sl_sum, mx_sum)
#         return mx_sum


# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


# class Solution:
#     def longestOnes(self, nums: list[int], k: int) -> int:
#         i = 0
#         mx_size = 0
#         flipped = 0
#         for j,_ in enumerate(nums):
#             if nums[j] == 0:
#                 flipped += 1
#             while flipped > k :
#                 if nums[i] == 0:
#                     flipped-=1
#                 i+=1
#             mx_size = max(mx_size,j-i+1)
#         return mx_size

# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

# class Solution:
#     def longestSubarray(self, nums: list[int]) -> int:
#         i, mx_size, deleted = 0, 0, 0
#         for j, _ in enumerate(nums):
#             if nums[j] == 0:
#                 deleted += 1
#             while deleted > 1:
#                 if nums[i] == 0:
#                     deleted -= 1
#                 i += 1
#             mx_size = max(mx_size,j-i)
#         return mx_size
