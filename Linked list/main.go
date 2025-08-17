package main

// import (
// 	"fmt"
// )

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteMiddle(head *ListNode) *ListNode {
	dummy := &ListNode{Next: head}
	fast := head
	prev := dummy
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		prev = prev.Next
	}
	prev.Next = prev.Next.Next
	return dummy.Next
}

func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	var prev *ListNode = nil
	curr := head
	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}
	return prev
}

func pairSum(head *ListNode) int {
	fast := head
	curr := head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		curr = curr.Next
	}
	var prev *ListNode = nil

	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}
	maxTwinSum := 0
	for prev != nil && head != nil {
		twinSum := prev.Val + head.Val
		if maxTwinSum < twinSum {
			maxTwinSum = twinSum
		}
		prev = prev.Next
		head = head.Next
	}
	return maxTwinSum

}

func oddEvenList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	odd := head
	even := head.Next
	evenHead := head.Next

	for odd != nil && odd.Next != nil && even != nil && even.Next != nil {
		odd.Next = even.Next
		odd = odd.Next
		even.Next = odd.Next
		even = even.Next
	}
	odd.Next = evenHead
	return head

}

func main() {

}
