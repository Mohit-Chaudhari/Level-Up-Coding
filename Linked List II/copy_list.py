# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 15/09/21
# -----------------------------------------------

# ***** Copy List *****
# Problem Description
#
# A linked list A is given such that each node contains an additional random pointer
# which could point to any node in the list or NULL.
#
# Return a deep copy of the list.
#
# Problem Constraints
# 0 <= |A| <= 106
#
#
#
# Input Format
# The first argument of input contains a pointer to the head of linked list A.
#
# Output Format
# Return a pointer to the head of the required linked list.
#
# Example Input
# Given list
#    1 -> 2 -> 3
# with random pointers going from
#   1 -> 3
#   2 -> 1
#   3 -> 1
#
# Example Output
#    1 -> 2 -> 3
# with random pointers going from
#   1 -> 3
#   2 -> 1
#   3 -> 1
#
# Example Explanation
# You should return a deep copy of the list. The returned answer should not contain the same node as the original list,
# but a copy of them. The pointers in the returned list should not link to any node in the original input list.

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):

        itr = head

        while itr:
            node = RandomListNode(itr.label)

            node.next = itr.next

            itr.next = node

            itr = node.next

        orig = head

        copy = head.next

        while orig and orig.next:

            if orig.random:
                orig.next.random = orig.random.next

            orig = orig.next.next

        orig = head

        while orig and orig.next:

            temp = orig.next

            orig.next = temp.next

            orig = orig.next

            if orig:
                temp.next = orig.next

        return copy






