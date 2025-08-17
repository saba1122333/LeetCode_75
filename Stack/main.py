# You are given a string s, which contains stars *.
# In one operation, you can:

# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Note:

# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.

# Example 1:

# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".

# class Solution:
#     def removeStars(self, s: str) -> str:
#         stack = []
#         for i in s:
#             if i != "*":
#                 stack.append(i)
#             else:
#                 if stack:
#                     stack.pop()
#         return "".join(stack)


# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
# The test cases are generated so that the length of the output will never exceed 105.


# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []

#         for ch in s:
#             if ch != ']':
#                 stack.append(ch)
#             else:
#                 wrd = ""
#                 k = ""
#                 while stack and stack[-1] != '[':
#                     wrd += stack.pop()
#                 stack.pop()
#                 while stack and stack[-1].isdigit():
#                     k += stack.pop()
#                 wrd = int(k[::-1]) * wrd[::-1]
#                 stack = stack + list(wrd)
#         return "".join(stack)


# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

from re import I


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for astr in asteroids:
            if astr > 0:
                stack.append(astr)
            else:
                is_destr = False
                while stack and stack[-1] > 0:
                    if stack[-1] < abs(astr):
                        stack.pop()
                    else:
                        if stack[-1] == abs(astr):
                            stack.pop()
                        is_destr = True
                        break

                if not is_destr:
                    stack.append(astr)
        return stack
sol = Solution()
asteroids = [5,10,-5]
asteroids = [8,-8]
asteroids = [10,2,-5]
print(sol.asteroidCollision(asteroids))