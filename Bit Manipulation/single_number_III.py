# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 06/08/21
# -----------------------------------------------

# ***** Single Number III *****
# Problem Description
#
# Given an array of numbers A , in which exactly two elements appear only once and all the other elements appear
# exactly twice. Find the two elements that appear only once.
#
# Note: Output array must be sorted.
#
#
#
# Problem Constraints
# 2 <= |A| <= 100000
# 1 <= A[i] <= 109
#
#
#
# Input Format
# First argument is an array of interger of size N.
#
#
#
# Output Format
# Return an array of two integers that appear only once.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 2, 3, 1, 2, 4]
# Input 2:
#
# A = [1, 2]
#
#
# Example Output
# Output 1:
#
# [3, 4]
# Output 2:
#
# [1, 2]
#
#
# Example Explanation
# Explanation 1:
#
#  3 and 4 appear only once.
# Explanation 2:
#
#  1 and 2 appear only once.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ln = len(A)
        A.sort()
        arr = list()
        i = 0

        while i < ln:
            if i == ln-1:
                arr.append(A[i])
                break
            if A[i] == A[i+1]:
                i += 2
            else:
                arr.append(A[i])
                i += 1

        return arr


s = Solution()
print(s.solve([1, 2, 3, 1, 2, 4]))
# OUTPUT: [3, 4]
