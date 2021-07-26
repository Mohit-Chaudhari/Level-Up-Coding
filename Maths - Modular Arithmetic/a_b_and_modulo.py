# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 27/07/21
# -----------------------------------------------

# ***** A, B and Modulo *****
# Problem Description
#
# Given two integers A and B, find the greatest possible positive M, such that A % M = B % M.
#
#
#
# Problem Constraints
# 1 <= A, B <= 109
# A != B
#
#
#
# Input Format
# The first argument given is the integer, A.
# The second argument given is the integer, B.
#
#
#
# Output Format
# Return an integer denoting greatest possible positive M.
#
#
#
# Example Input
# Input 1:
#
# A = 1
# B = 2
# Input 2:
#
# A = 5
# B = 10
#
#
# Example Output
# Output 1:
#
# 1
# Output 2:
#
# 5
#
#
# Example Explanation
# Explanation 1:
#
# 1 is the largest value of M such that A % M == B % M.
# Explanation 2:
#
# For M = 5, A % M = 0 and B % M = 0.
#
# No value greater than M = 5, satisfies the condition.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A - B > B - A:
            return A - B
        return B - A


s = Solution()
print(s.solve(5, 10))
# OUTPUT: 5
