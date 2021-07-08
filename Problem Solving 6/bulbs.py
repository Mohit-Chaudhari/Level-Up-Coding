# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 08/07/21
# -----------------------------------------------

# Bulbs
# Problem Description
#
# N light bulbs are connected by a wire.
#
# Each bulb has a switch associated with it,
# however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb.
#
# Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.
#
# You can press the same switch multiple times.
#
# Note: 0 represents the bulb is off and 1 represents the bulb is on.
#
#
#
# Problem Constraints
# 1 <= N <= 5*105
# 0 <= A[i] <= 1
#
#
#
# Input Format
# The first and the only argument contains an integer array A, of size N.
#
#
#
# Output Format
# Return an integer representing the minimum number of switches required.
#
#
#
# Example Input
# Input 1:
#
#  A = [0, 1, 0, 1]
# Input 2:
#
#  A = [1, 1, 1, 1]
#
#
# Example Output
# Output 1:
#
#  4
# Output 2:
#
#  0
#
#
# Example Explanation
# Explanation 1:
#
#  press switch 0 : [1 0 1 0]
#  press switch 1 : [1 1 0 1]
#  press switch 2 : [1 1 1 0]
#  press switch 3 : [1 1 1 1]
# Explanation 2:
#
#  There is no need to turn any switches as all the bulbs are already on.

class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        n = len(A)
        if n == 0:
            return 0
        cnt = 0
        cnd = A[0]
        addition = 1 if A[0] == 0 else 0

        for i in range(n):
            if cnd == 0:
                if A[i] == 1:
                    cnd = 1
                    cnt += 1
            elif cnd == 1:
                if A[i] == 0:
                    cnd = 0
                    cnt += 1
        return cnt + addition


s = Solution()
print(s.bulbs([1, 1, 1, 1]))
# OUTPUT : 0
