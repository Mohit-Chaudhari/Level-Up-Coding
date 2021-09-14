# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 14/09/21
# -----------------------------------------------

# ***** Remove Nth Node from List End *****
# Problem Description
#
# Given a linked list A, remove the B-th node from the end of list and return its head.
#
# For example, Given linked list: 1->2->3->4->5, and B = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
#
# NOTE: If B is greater than the size of the list, remove the first node of the list.
#
# NOTE: Try doing it using constant additional space.
#
#
#
# Problem Constraints
# 1 <= |A| <= 106
#
#
#
# Input Format
# The first argument of input contains a pointer to the head of the linked list.
#
# The second argument of input contains the integer B.
#
#
#
# Output Format
# Return the head of the linked list after deleting the B-th element from the end.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 2, 3, 4, 5]
# B = 2
# Input 2:
#
# A = [1]
# B = 1
#
#
# Example Output
# Output 1:
#
# [1, 2, 3, 5]
# Output 2:
#
#  []
#
#
# Example Explanation
# Explanation 1:
#
# In the first example, 4 is the second last element.
# Explanation 2:
#
# In the second example, 1 is the first and the last element.

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:

    def getSize(self, A):
        i = 0
        while A is not None:
            A = A.next
            i += 1
        return i

    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        size = self.getSize(A)
        size = size - B - 1

        if size <= 0:
            return A.next

        head = A
        i = 0
        while A is not None and i < size:
            A = A.next
            i += 1

        if B != 1:
            A.next = A.next.next
        else:
            A.next = None

        return head


s = Solution()
print(s.removeNthFromEnd([1, 2, 3, 4, 5], 2))
# OUTPUT: [1, 2, 3, 5]
# NOTE: You have to create linked list, the passed parameter is consider as an array.
