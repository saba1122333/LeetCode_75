
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         shortest = min(len(word1),len(word2))
#         merged = [a+b for a,b in  zip(word1,word2)]
#         merged.append(word1[shortest:] or word2[shortest:])
#         return ''.join(merged)


# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"


# import math


# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         #  for GCD this should not matter as  a + b == b + a => (x*t + b*t) ==(b*t + x*t)
#         return str1[:math.gcd(len(str1),len(str2))] if str1 + str2 == str2 + str1 else ""


# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies,
#  denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if,
# after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.


# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.


# class Solution:
#     def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:

#         return  [ True if  i - max(candies)+extraCandies >=0 else False for i in candies]


# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
#  return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# class Solution:
#     def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

#         padded = [0] + flowerbed + [0]
#         for i in range(1,len(padded)-1):
#             if padded[i-1]==padded[i]==padded[i+1]==0:
#                 padded[i]=1
#                 n-=1
#         return n<=0


# sol = Solution()
# flowerbed = [1,0,0,0,1]
# n = 2
# print(sol.canPlaceFlowers(flowerbed,n))


# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         VOWELS = [ vowl.upper() for vowl in ['a', 'e', 'i', 'o','u']] + ['a', 'e', 'i', 'o','u']
#         i = 0
#         j = len(s)-1
#         vowels_reversed = list(s)

#         while i < j:

#             while i < j and vowels_reversed[i] not in VOWELS:
#                 i+=1
#             while i < j and vowels_reversed[j] not in VOWELS:
#                 j-=1
#             if i < j:
#                 vowels_reversed[i],vowels_reversed[j] =  vowels_reversed[j],vowels_reversed[i]
#                 i+=1
#                 j-=1

#         return  "".join(vowels_reversed)

# sol = Solution()
# s = "IceCreAm"
# res = "AceCreIm"
# print(sol.reverseVowels(s))


# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words. Do not include any extra spaces.


# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return " ".join(reversed(s.strip().split()))
# sol = Solution()
# s = "a good   example"
# print(sol.reverseWords(s))


# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         size = len(nums)
#         prefix_mul = [1] * size
#         suffix_mul = [1] * size

#         for i in range(1,size):
#             prefix_mul[i] = prefix_mul[i-1]*nums[i-1]
#         for i in range(size-2,-1,-1):
#             suffix_mul[i] = suffix_mul[i+1]*nums[i+1]

#         return [p*s for p,s in zip(prefix_mul,suffix_mul)]

# sol = Solution()
# nums = [1,2,3,4]
# print(sol.productExceptSelf(nums))


# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
#  Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.

# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

# class Solution:
#     def compress(self, chars: list[str]) -> int:

#         s = ""
#         i = 0
#         length = len(chars)
#         while i < length:
#             j = i + 1
#             group_size = 1
#             while j < length and chars[j] == chars[i]:
#                 j+=1
#                 group_size+=1
#             s+= chars[i] if group_size == 1 else chars[i]+ str(group_size)
#             i = j
#         chars[:] = [ch for ch in s]
#         print(chars)
#         return  len(chars)


# sol = Solution()
# chars =["a","a","b","b","c","c","c"]

# sol.compress(chars)

# class Solution:
#     def makeFancyString(self, s: str) -> str:
#         fancy = ""
#         i = 0
#         while i <len(s):
#             j = i + 1
#             while j < len(s) and s[i]==s[j]:
#                 j+=1
#             size = min(2,j-i)
#             fancy+=s[i] if size < 2 else s[i:i+size]
#             i=j
#         return fancy


# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
# If no such indices exists, return false.

# Example 3:
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


# class Solution:
#     def increasingTriplet(self, nums: list[int]) -> bool:
#         first = float("inf")
#         second = float("inf")
#         for num in nums:
#             if num <= first:
#                 first = num
#             elif num <= second:
#                 second = num
#             else:
#                 return True
#         return False
