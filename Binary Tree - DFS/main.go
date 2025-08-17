package main

// * Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	leftDepth := maxDepth(root.Left)
	rightDepth := maxDepth(root.Right)
	if leftDepth > rightDepth {
		return leftDepth + 1
	} else {
		return rightDepth + 1
	}

}
func dfs(root *TreeNode, nodeVals *[]int) {
	if root == nil {
		return
	}
	if root.Left == nil && root.Right == nil {
		*nodeVals = append(*nodeVals, root.Val)
		return
	}
	dfs(root.Left, nodeVals)
	dfs(root.Right, nodeVals)
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	nodeVals1, nodeVals2 := []int{}, []int{}
	dfs(root1, &nodeVals1)
	dfs(root2, &nodeVals2)

	if len(nodeVals1) != len(nodeVals2) {
		return false
	}
	for i, _ := range nodeVals1 {
		if nodeVals1[i] != nodeVals2[i] {
			return false
		}
	}
	return true
}
