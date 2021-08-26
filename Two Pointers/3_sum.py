# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 26/08/21
# -----------------------------------------------


# ***** 3 Sum *****
# Problem Description
#
# Given an array A of N integers, find three integers in A such that the sum is closest to a given number B.
# Return the sum of those three integers.
#
# Assume that there will only be one solution.
#
# Problem Constraints
# -108 <= B <= 108
# 1 <= N <= 104
# -108 <= A[i] <= 108
#
# Input Format
# First argument is an integer array A of size N.
#
# Second argument is an integer B denoting the sum you need to get close to.
#
# Output Format
# Return a single integer denoting the sum of three integers which is closest to B.
#
# Example Input
# Input
# 1:
#
# A = [-1, 2, 1, -4]
# B = 1
# Input
# 2:
#
# A = [1, 2, 3]
# B = 6
#
# Example Output
#
# Output 1:
#
# 2
# Output 2:
#
# 6
#
# Example Explanation
# Explanation 1:
#
#  The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
# Explanation 2:
#
#  Take all elements to get exactly 6.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        ln = len(A)
        curr = float('inf')

        A.sort()

        for i in range(ln - 2):
            a = i
            b = i + 1
            c = ln - 1

            while b < c:

                s = A[a] + A[b] + A[c]

                if abs(s - B) < abs(curr - B):
                    curr = s

                if s > B:
                    c -= 1

                if s < B:
                    b += 1

                if s == B:
                    return B
        return curr


s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], -1))
# OUTPUT: 2
