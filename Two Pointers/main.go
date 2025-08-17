package main

import (
	"math"
	"sort"
)

func moveZeroes(nums []int) {
	j := len(nums) - 1
	for i := len(nums) - 1; i >= 0; i-- {
		if nums[i] == 0 {
			swapWithOrder(i, j, &nums)
			j--
		}

	}
}
func swapWithOrder(i int, j int, nums *[]int) {
	for i < j {
		(*nums)[i], (*nums)[i+1] = (*nums)[i+1], (*nums)[i]
		i++
	}
}

func isSubsequence(s string, t string) bool {
	sI, tI, lenS, lenT := 0, 0, len(s), len(t)

	for sI < lenS && tI < lenT {
		if s[sI] == t[tI] {
			sI += 1
		}
		tI += 1
	}
	return sI == lenS

}

func maxOperations(nums []int, k int) int {

	sort.Ints(nums)
	count, i, j := 0, 0, len(nums)-1
	for i < j {
		if nums[i]+nums[j] > k {
			i += 1
		} else if nums[i]+nums[j] < k {
			j -= 1
		} else {
			i += 1
			j -= 1
			count += 1
		}
	}
	return count
}

func maxArea(height []int) int {
	i, j := 0, len(height)
	maxArea := float64(0)
	for i < j {
		l_pole, r_pole := height[i], height[j]
		area := math.Min(float64(l_pole), float64(r_pole)) * float64((j - i))
		maxArea = math.Max(area, maxArea)
		if l_pole <= r_pole {
			i += 1
		} else {
			j -= 1
		}

	}
	return int(maxArea)
}
