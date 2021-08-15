# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 15/08/21
# -----------------------------------------------

# ***** Primal Power *****
# Problem Description
#
# "Primal Power" of an array is defined as the count of prime numbers present in it.
#
# Given an array of integers A of length N, you have to calculate its Primal Power.
#
#
#
# Problem Constraints
# 1 <= N <= 103
#
# -106 <= A[i] <= 106
#
#
#
# Input Format
# First and only argument is an integer array A.
#
#
#
# Output Format
# Return the Primal Power of array A.
#
#
#
# Example Input
# Input 1:
#
#  A = [-6, 10, 12]
# Input 2:
#
#  A = [-11, 7, 8, 9, 10, 11]
#
#
# Example Output
# Output 1:
#
#  0
# Output 2:
#
#  2
#
#
# Example Explanation
# Explanation 1:
#
#  -6 is not a prime number, as prime numbers are always natural numbers(by definition).
#   Also, both 10 and 12 are composite numbers.
# Explanation 2:
#
#  7 and 11 are prime numbers. Hence, Primal Power = 2.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxi = max(A)
        ln = len(A)
        spf = [float('inf') for i in range(maxi+1)]
        cnt = 0

        # CREATE SPF ARRAY
        for i in range(maxi + 1):
            if i == 0 or i == 1:
                continue
            if spf[i] == float('inf'):
                divisor_range = i
                while divisor_range <= maxi:
                    if spf[divisor_range] > i:
                        spf[divisor_range] = i
                    divisor_range += i
            else:
                continue

        # print(spf)
        for i in range(ln):
            if spf[A[i]] == A[i]:
                cnt += 1

        return cnt


s = Solution()
print(s.solve([-11, 7, 8, 9, 10, 11]))
# OUTPUT: 2
