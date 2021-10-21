# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 22/10/21
# -----------------------------------------------

# ***** Stairs *****
# Problem Description
#
# You are climbing a stair case and it takes A steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
#
# Problem Constraints
# 1 <= A <= 36
#
#
#
# Input Format
# The first and the only argument contains an integer A, the number of steps.
#
#
#
# Output Format
# Return an integer, representing the number of ways to reach the top.
#
#
#
# Example Input
# Input 1:
#
#  A = 2
# Input 2:
#
#  A = 3
#
#
# Example Output
# Output 1:
#
#  2
# Output 2:
#
#  3
#
#
# Example Explanation
# Explanation 1:
#
#  Distinct ways to reach top: [1, 1], [2].
# Explanation 2:
#
#  Distinct ways to reach top: [1 1 1], [1 2], [2 1].

class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        arr = [0 for i in range(A + 2)]
        arr[1] = 1

        for i in range(2, A + 2):
            arr[i] = arr[i - 1] + arr[i - 2]

        return arr[A + 1]


s = Solution()
s.climbStairs(3)
# OUTPUT: 3
