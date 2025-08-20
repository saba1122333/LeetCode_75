package main

// // Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// var testTree = &TreeNode{
// 	Val: 1,
// 	Left: &TreeNode{
// 		Val: 2,
// 		Left: &TreeNode{
// 			Val: 4,
// 			Left: &TreeNode{
// 				Val: 8,
// 				Left: &TreeNode{
// 					Val: 16,
// 				},
// 				Right: &TreeNode{
// 					Val: 17,
// 				},
// 			},
// 			Right: &TreeNode{
// 				Val: 9,
// 				Left: &TreeNode{
// 					Val: 18,
// 				},
// 				Right: &TreeNode{
// 					Val: 19,
// 				},
// 			},
// 		},
// 		Right: &TreeNode{
// 			Val: 5,
// 			Left: &TreeNode{
// 				Val: 10,
// 				Left: &TreeNode{
// 					Val: 20,
// 				},
// 				Right: &TreeNode{
// 					Val: 21,
// 				},
// 			},
// 			Right: &TreeNode{
// 				Val: 11,
// 				Left: &TreeNode{
// 					Val: 22,
// 				},
// 				Right: &TreeNode{
// 					Val: 23,
// 				},
// 			},
// 		},
// 	},
// 	Right: &TreeNode{
// 		Val: 3,
// 		Left: &TreeNode{
// 			Val: 6,
// 			Left: &TreeNode{
// 				Val: 12,
// 				Left: &TreeNode{
// 					Val: 24,
// 				},
// 				Right: &TreeNode{
// 					Val: 25,
// 				},
// 			},
// 			Right: &TreeNode{
// 				Val: 13,
// 				Left: &TreeNode{
// 					Val: 26,
// 				},
// 				Right: &TreeNode{
// 					Val: 27,
// 				},
// 			},
// 		},
// 		Right: &TreeNode{
// 			Val: 7,
// 			Left: &TreeNode{
// 				Val: 14,
// 				Left: &TreeNode{
// 					Val: 28,
// 				},
// 				Right: &TreeNode{
// 					Val: 29,
// 				},
// 			},
// 			Right: &TreeNode{
// 				Val: 15,
// 				Left: &TreeNode{
// 					Val: 30,
// 				},
// 				Right: &TreeNode{
// 					Val: 31,
// 				},
// 			},
// 		},
// 	},
// }

// func rightSideView(root *TreeNode) []int {
// 	if root == nil {
// 		return []int{}
// 	}
// 	queue := []*TreeNode{root}
// 	levels := []int{}
// 	for len(queue) > 0 {
// 		size := len(queue)

// 		for i := 0; i < size; i++ {
// 			rt := queue[0]
// 			if rt.Left != nil {
// 				queue = append(queue, rt.Left)
// 			}
// 			if rt.Right != nil {
// 				queue = append(queue, rt.Right)
// 			}
// 			if i == size-1 {
// 				levels = append(levels, rt.Val)
// 			}
// 			queue = queue[1:]
// 		}
// 	}
// 	return levels
// }

// func maxLevelSum(root *TreeNode) int {
// 	queue := []*TreeNode{root}
// 	maxSum, maxSumLevel, level := -int(^uint(0)>>1)-1, 0, 0

// 	for len(queue) > 0 {
// 		level++
// 		size, levelSum := len(queue), 0

// 		for i := 0; i < size; i++ {
// 			rt := queue[0]
// 			queue = queue[1:]

// 			if rt.Left != nil {
// 				queue = append(queue, rt.Left)
// 			}
// 			if rt.Right != nil {
// 				queue = append(queue, rt.Right)
// 			}
// 			levelSum += rt.Val

// 		}
// 		if maxSum < levelSum {
// 			maxSum = levelSum
// 			maxSumLevel = level
// 		}

// 	}
// 	return maxSumLevel
// }
