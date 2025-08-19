package main

// * Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// func maxDepth(root *TreeNode) int {
// 	if root == nil {
// 		return 0
// 	}
// 	leftDepth := maxDepth(root.Left)
// 	rightDepth := maxDepth(root.Right)
// 	if leftDepth > rightDepth {
// 		return leftDepth + 1
// 	} else {
// 		return rightDepth + 1
// 	}

// }

// func dfs(root *TreeNode, nodeVals *[]int) {
// 	if root == nil {
// 		return
// 	}
// 	if root.Left == nil && root.Right == nil {
// 		*nodeVals = append(*nodeVals, root.Val)
// 		return
// 	}
// 	dfs(root.Left, nodeVals)
// 	dfs(root.Right, nodeVals)
// }

// func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
// 	nodeVals1, nodeVals2 := []int{}, []int{}
// 	dfs(root1, &nodeVals1)
// 	dfs(root2, &nodeVals2)

// 	if len(nodeVals1) != len(nodeVals2) {
// 		return false
// 	}
// 	for i, _ := range nodeVals1 {
// 		if nodeVals1[i] != nodeVals2[i] {
// 			return false
// 		}
// 	}
// 	return true
// }

// func maxDfs(root *TreeNode, maxVal int) int {
// 	if root == nil {
// 		return 0
// 	}
// 	if root.Val >= maxVal {
// 		return maxDfs(root.Left, root.Val) + maxDfs(root.Right, root.Val) + 1
// 	}
// 	return maxDfs(root.Left, maxVal) + maxDfs(root.Right, maxVal)

// }
// maxDfs using pointers
// func maxDfs(root *TreeNode, maxVal int, nodes *int) {
// 	if root == nil {
// 		return
// 	}
// 	if root.Val >= maxVal {
// 		*nodes++
// 		maxVal = root.Val
// 	}
// 	maxDfs(root.Left, maxVal, nodes)
// 	maxDfs(root.Right, maxVal, nodes)

// }

// func goodNodes(root *TreeNode) int {
// 	nodes := 0
// 	rootVal := root.Val
// 	maxDfs(root, rootVal, &nodes)
// 	return nodes
// }

// func targetPathCount(root *TreeNode, targetSum int, count *int) {
// 	if root == nil {
// 		return
// 	}
// 	targetSum -= root.Val
// 	if targetSum == 0 {
// 		*count++
// 	}
// 	targetPathCount(root.Left, targetSum, count)
// 	targetPathCount(root.Right, targetSum, count)
// }

//	func pathSum(root *TreeNode, targetSum int) int {
//		stack := []*TreeNode{root}
//		count := 0
//		for len(stack) > 0 {
//			rt := stack[0]
//			targetPathCount(rt, targetSum, &count)
//			if rt.Left != nil {
//				stack = append(stack, rt.Left)
//			}
//			if rt.Right != nil {
//				stack = append(stack, rt.Right)
//			}
//			stack = stack[1:]
//		}
//		return count
//	}
// func dfs(root *TreeNode, currSum, targetSum int, prefix map[int]int) int {
// 	if root == nil {
// 		return 0
// 	}
// 	currSum += root.Val
// 	count := prefix[currSum-targetSum]
// 	prefix[currSum]++
// 	count += dfs(root.Left, currSum, targetSum, prefix)
// 	count += dfs(root.Right, currSum, targetSum, prefix)
// 	prefix[currSum]--
// 	return count
// }

// func pathSum(root *TreeNode, targetSum int) int {
// 	prefix := map[int]int{0: 1}
// 	return dfs(root, 0, targetSum, prefix)
// }

// func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
// 	if root == nil {
// 		return nil
// 	}
// 	if root == p || root == q {
// 		return root
// 	}
// 	lTree := lowestCommonAncestor(root.Left, p, q)
// 	rTree := lowestCommonAncestor(root.Right, p, q)
// 	if lTree != nil && rTree != nil {
// 		return root
// 	}
// 	if lTree != nil {
// 		return lTree
// 	}
// 	if rTree != nil {
// 		return rTree
// 	}
// 	return nil

// }

// func maxZigZag(root *TreeNode, maxZig *int, direction string) int {
// 	if root == nil {
// 		return 0
// 	}
// 	zigRight := maxZigZag(root.Right, maxZig, "right") + 1
// 	zigLeft := maxZigZag(root.Left, maxZig, "left") + 1
// 	if direction == "right" {
// 		if *maxZig < zigLeft {
// 			*maxZig = zigLeft
// 		}
// 		return zigLeft
// 	}
// 	if direction == "left" {

// 		if *maxZig < zigRight {
// 			*maxZig = zigRight
// 		}
// 		return zigRight
// 	}
// 	return 1

// }

// func longestZigZag(root *TreeNode) int {
// 	maxZig := 0
// 	maxZigZag(root.Left, &maxZig, "left")
// 	maxZigZag(root.Right, &maxZig, "right")
// 	return maxZig
// }
