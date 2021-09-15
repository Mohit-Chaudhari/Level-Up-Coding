# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 15/09/21
# -----------------------------------------------

# ***** K reverse linked list *****
# Problem Description
#
# Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and
# return modified linked list.
#
#
#
# Problem Constraints
# 1 <= |A| <= 103
#
# B always divides A
#
#
#
# Input Format
# The first argument of input contains a pointer to the head of the linked list.
#
# The second arugment of input contains the integer, B.
#
#
#
# Output Format
# Return a pointer to the head of the modified linked list.
#
#
#
# Example Input
# Input 1:
#
#  A = [1, 2, 3, 4, 5, 6]
#  B = 2
# Input 2:
#
#  A = [1, 2, 3, 4, 5, 6]
#  B = 3
#
#
# Example Output
# Output 1:
#
#  [2, 1, 4, 3, 6, 5]
# Output 2:
#
#  [3, 2, 1, 6, 5, 4]
#
#
# Example Explanation
# Explanation 1:
#
#  For the first example, the list can be reversed in groups of 2.
#     [[1, 2], [3, 4], [5, 6]]
#  After reversing the K-linked list
#     [[2, 1], [4, 3], [6, 5]]
# Explanation 2:
#
#  For the second example, the list can be reversed in groups of 3.
#     [[1, 2, 3], [4, 5, 6]]
#  After reversing the K-linked list
#     [[3, 2, 1], [6, 5, 4]]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self):
        self.head = None

    def insert(self, element):
        new_node = ListNode(element)
        if self.head is None:
            self.head = new_node
            return
        lst = self.head
        while lst.next is not None:
            lst = lst.next
        lst.next = new_node

    def print_linked_list(self, A):
        head = A
        arr = list()
        while head is not None:
            arr.append(head.val)
            head = head.next
        return arr

    def helper(self, A, B):
        for i in A:
            self.insert(i)
        return self.print_linked_list(self.reverseList(self.head, B))

    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):

        curr = A
        nxt = None
        prev = None
        count = 0

        while curr is not None and count < B:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1
        if nxt is not None:
            A.next = self.reverseList(nxt, B)

        return prev


A = [1, 2, 3, 4, 5, 6]
B = 2
s = Solution()
print(s.helper(A, B))
# OUTPUT: [2, 1, 4, 3, 6, 5]
