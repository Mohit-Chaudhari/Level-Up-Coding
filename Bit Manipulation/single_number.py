# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 05/08/21
# -----------------------------------------------

# ***** Single Number *****
# Problem Description
#
# Given an array of integers A, every element appears twice except for one. Find that single one.
#
# NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
#
#
# Problem Constraints
# 2 <= |A| <= 2000000
#
# 0 <= A[i] <= INTMAX
#
#
#
# Input Format
# First and only argument of input contains an integer array A.
#
#
#
# Output Format
# Return a single integer denoting the single element.
#
#
#
# Example Input
# Input 1:
#
#  A = [1, 2, 2, 3, 1]
# Input 2:
#
#  A = [1, 2, 2]
#
#
# Example Output
# Output 1:
#
#  3
# Output 2:
#
#  1
#
#
# Example Explanation
# Explanation 1:
#
# 3 occurs once.
# Explanation 2:
#
# 1 occurs once.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ln = len(A)
        ans = A[0]

        for i in range(1, ln):
            ans ^= A[i]

        return ans


s = Solution()
print(s.singleNumber([1, 2, 2, 3, 1]))
# OUTPUT: 3
