package main

import (
	"math"
)

func largestAltitude(gain []int) int {
	altitudes := make([]int, len(gain)+1)
	mx_size := 0.
	for i := 1; i < len(altitudes); i++ {
		altitudes[i] = altitudes[i-1] + gain[i-1]
		mx_size = math.Max(mx_size, float64(altitudes[i]))
	}
	return int(mx_size)
}

func pivotIndex(nums []int) int {
	l := len(nums)
	lPreSum, rPreSum := make([]int, l), make([]int, l)
	for i := 1; i < l; i++ {
		lPreSum[i] = lPreSum[i-1] + nums[i-1]
	}
	for i := l - 2; i >= 0; i-- {
		rPreSum[i] = rPreSum[i+1] + nums[i+1]
	}

	for i := range lPreSum {
		if lPreSum[i] == rPreSum[i] {
			return i
		}
	}
	return 0

}

func main() {
	nums := []int{1, 7, 3, 6, 5, 6}
	pivotIndex(nums)
}
