# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 21/09/21
# -----------------------------------------------

# ***** Level Order *****
# Problem Description
#
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
#
#
# Problem Constraints
# 1 <= number of nodes <= 105
#
#
#
# Input Format
# First and only argument is root node of the binary tree, A.
#
#
#
# Output Format
# Return a 2D integer array denoting the zigzag level order traversal of the given binary tree.
#
#
#
# Example Input
# Input 1:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Input 2:
#
#    1
#   / \
#  6   2
#     /
#    3
#
#
# Example Output
# Output 1:
#
#  [
#    [3],
#    [9, 20],
#    [15, 7]
#  ]
# Output 2:
#
#  [
#    [1]
#    [6, 2]
#    [3]
#  ]
#
#
# Example Explanation
# Explanation 1:
#
#  Return the 2D array. Each row denotes the traversal of each level.

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, root):

        # Base case
        if root is None:
            return
        # Create an empty queue for level order traversal
        q = list()
        ans = list()

        # Enqueue root and initialize height
        q.append(root)

        while q:

            # nodeCount (queue size) indicates number
            # of nodes at current level.
            count = len(q)
            level = list()

            # Dequeue all nodes of current level and
            # Enqueue all nodes of next level
            while count > 0:
                temp = q.pop(0)
                level.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)

                count -= 1
            ans.append(level)

        return ans
