# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

# Example 1:
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node.


# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(next=head)
#         fast = head
#         prev = dummy
#         while fast and fast.next:
#             fast = fast.next.next
#             prev = prev.next
#         prev.next = prev.next.next
#         return dummy.next


# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         prev = None
#         curr = head
#         while curr:
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next
#         return prev


# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]


# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         odd = head
#         even = head.next
#         even_head = head.next

#         while odd and odd.next and even and even.next:
#             odd.next = even.next
#             odd = odd.next
#             even = odd.next
#             even = even.next
#         odd.next = even_head
#         return head


# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

# Example 1:

# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 

# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         if not head and not head.next:
#             return head
#         fast = head
#         curr = head

#         while fast and fast.next:
#             fast = fast.next.next 
#             curr = curr.next
#         prev = None 
#         max_twin_sum = 0 

#         while curr:
#             next = curr.next 
#             curr.next = prev
#             prev = curr
#             curr = next 

#         while prev:
#             twin_sum = prev.val + head.val 
#             max_twin_sum = max(twin_sum,max_twin_sum)
#             prev = prev.next
#             head = head.next
#         return max_twin_sum
