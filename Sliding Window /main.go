package main

// func findMaxAverage(nums []int, k int) float64 {
// 	slSum := 0.0
// 	for i := 0; i < k; i++ {
// 		slSum += float64(nums[i])
// 	}

// 	mxSum := slSum
// 	for i := 0; i < len(nums)-k; i++ {
// 		slSum = slSum + float64(nums[i+k]-nums[i])
// 		mxSum = math.Max(mxSum, slSum)
// 	}
// 	return mxSum / float64(k)
// }

//	func longestOnes(nums []int, k int) int {
//		i, flipped, mxSize := 0, 0, 0.
//		for j := range nums {
//			if nums[j] == 0 {
//				flipped++
//			}
//			for flipped > k {
//				if nums[i] == 0 {
//					flipped--
//				}
//				i++
//			}
//			mxSize = math.Max(mxSize, float64((j - i + 1)))
//		}
//		return int(mxSize)
//	}

// func longestSubarray(nums []int) int {
// 	i, mxSize, deleted := 0, 0., 0
// 	for j := range nums {
// 		if nums[j] == 0 {
// 			deleted--
// 		}
// 		for deleted > 1 {
// 			if nums[i] == 0 {
// 				deleted--
// 			}
// 			i++
// 		}
// 		mxSize = math.Max(mxSize, float64(j-i))

// 	}
// 	return int(mxSize)

// }
