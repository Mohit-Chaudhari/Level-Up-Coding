# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 03/11/21
# -----------------------------------------------

# ***** Reorder List *****
#
# Problem Description
#
# Given a singly linked list A
#
#  A: A0 → A1 → … → An-1 → An
# reorder it to:
#
#  A0 → An → A1 → An-1 → A2 → An-2 → …
# You must do this in-place without altering the nodes' values.
#
#
#
# Problem Constraints
#
# 1 <= |A| <= 106
#
#
#
# Input Format
#
# The first and the only argument of input contains a pointer to the head of the linked list A.
#
#
#
# Output Format
#
# Return a pointer to the head of the modified linked list.
#
#
#
# Example Input
#
# Input 1:
#
#  A = [1, 2, 3, 4, 5]
# Input 2:
#
#  A = [1, 2, 3, 4]
#
#
# Example Output
#
# Output 1:
#
#  [1, 5, 2, 4, 3]
# Output 2:
#
#  [1, 4, 2, 3]
#
#
# Example Explanation
#
# Explanation 1:
#
#  The array will be arranged to [A0, An, A1, An-1, A2].
# Explanation 2:
#
#  The array will be arranged to [A0, An, A1, An-1, A2].

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def get_middle_node(self, node):

        prev = None
        slow = fast = node

        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next

        if fast and fast.next is None:
            prev = slow
            slow = slow.next

        prev.next = None

        return slow

    def reverse_list(self, node):

        current = node
        prev = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev

    def merge_list(self, head_a, head_b):

        dummy_node = ListNode(0)

        tail = dummy_node

        while True:

            if head_a is None:
                tail.next = head_b
                break

            if head_b is None:
                tail.next = head_a
                break

            tail.next = head_a
            head_a = head_a.next
            tail = tail.next
            tail.next = head_b
            head_b = head_b.next

            tail = tail.next

        return dummy_node.next

    def reorderList(self, A):

        mid = self.get_middle_node(A)

        # Reverse the second half.
        mid = self.reverse_list(mid)

        current = self.merge_list(A, mid)

        return current

    def print_list(self, node):
        ptr = node
        while ptr:
            print(ptr.val, end=' —> ')
            ptr = ptr.next

        print('None')


if __name__ == "__main__":

    head = None
    for i in reversed(range(7)):
        curr = ListNode(i)
        curr.next = head
        head = curr

    s = Solution()

    reordered_list = s.reorderList(head)
    s.print_list(reordered_list)
