# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 08/07/21
# -----------------------------------------------

# ***** SUB ARRAY OR *****
# Problem Description
#
# Given an array of integers A of size N.
#
# Value of a subarray is defined as BITWISE OR of all elements in it.
#
# Return the sum of Value of all subarrays of A % 109 + 7.
#
#
#
# Problem Constraints
# 1 <= N <= 105
#
# 1 <= A[i] <= 108
#
#
#
# Input Format
# The first argument given is the integer array A.
#
#
#
# Output Format
# Return the sum of Value of all subarrays of A % 109 + 7.
#
#
#
# Example Input
# Input 1:
#
#  A = [1, 2, 3, 4, 5]
# Input 2:
#
#  A = [7, 8, 9, 10]
#
#
# Example Output
# Output 1:
#
#  71
# Output 2:
#
#  110
#
#
# Example Explanation
# Explanation 1:
#
#  Value([1]) = 1
#  Value([1, 2]) = 3
#  Value([1, 2, 3]) = 3
#  Value([1, 2, 3, 4]) = 7
#  Value([1, 2, 3, 4, 5]) = 7
#  Value([2]) = 2
#  Value([2, 3]) = 3
#  Value([2, 3, 4]) = 7
#  Value([2, 3, 4, 5]) = 7
#  Value([3]) = 3
#  Value([3, 4]) = 7
#  Value([3, 4, 5]) = 7
#  Value([4]) = 4
#  Value([4, 5]) = 5
#  Value([5]) = 5
#  Sum of all these values = 71
# Explanation 2:
#
#  Sum of value of all sub array is 110.

from math import log2


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        # Find max element of the array
        max_element = max(A)

        # Find the max bit position set in
        # the array
        maxBit = int(log2(max_element)) + 1

        totalSubarrays = n * (n + 1) // 2

        s = 0

        # Traverse from 1st bit to last bit which
        # can be set in any element of the array
        for i in range(maxBit):
            c1 = 0

            # List to store indexes of the array
            # with i-th bit not set
            vec = []

            sum = 0

            # Traverse the array
            for j in range(n):

                # Check if ith bit is not set in A[j]
                a = A[j] >> i

                if (not (a & 1)):
                    vec.append(j)

            # Variable to store count of subarrays
            # whose bitwise OR will have i-th bit
            # not set
            cntSubarrNotSet = 0

            cnt = 1

            for j in range(1, len(vec)):

                if (vec[j] - vec[j - 1] == 1):
                    cnt += 1

                else:

                    cntSubarrNotSet += cnt * (cnt + 1) // 2

                    cnt = 1

            # For last element of vec
            cntSubarrNotSet += cnt * (cnt + 1) // 2

            # If vec is empty then cntSubarrNotSet
            # should be 0 and not 1
            if len(vec) == 0:
                cntSubarrNotSet = 0

                # Variable to store count of subarrays
            # whose bitwise OR will have i-th bit set
            cntSubarrIthSet = totalSubarrays - cntSubarrNotSet

            s += cntSubarrIthSet * pow(2, i)

        return s % (10 ** 9 + 7)


s = Solution()
print(s.solve([1, 2, 3, 4, 5]))
# OUTPUT: 71
