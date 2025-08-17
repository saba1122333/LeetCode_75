# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
# Example 1:

# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.


# class Solution:
#     def largestAltitude(self, gain: list[int]) -> int:
#         altitudes = (len(gain)+1) * [0]
#         mx_alt = 0
#         for i in range(1,len(altitudes)):
#             altitudes[i] = altitudes[i-1] + altitudes[i-1]
#             mx_alt = max(mx_alt,altitudes[i])
#         return mx_alt


# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

# Example 1:

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        l = len(nums)
        l_pre_sum = r_pre_sum = l * [0]
        for i in range(1, l):
            l_pre_sum[i] = l_pre_sum[i-1] + nums[i-1]
        for i in reversed(range(l-2)):
            r_pre_sum[i] = r_pre_sum[i+1] + nums[i+1]

        for i in range(l):
            if l_pre_sum[i] == r_pre_sum[i]:
                return i
        return -1
