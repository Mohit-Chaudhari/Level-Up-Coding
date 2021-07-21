# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 21/07/21
# -----------------------------------------------

# ***** Smaller and Greater *****
# You are given an Array A of size N.
#
# Find for how many elements, there is a strictly smaller element and a strictly greater element.
#
#
#
# Input Format
#
# Given only argument A an Array of Integers.
# Output Format
#
# Return an Integer X, i.e number of elements.
# Constraints
#
# 1 <= N <= 1e5
# 1 <= A[i] <= 1e6
# For Example
#
# Example Input:
#     A = [1, 2, 3]
#
# Example Output:
#     1
#
# Explanation:
#     only 2 have a strictly smaller and strictly greater element, 1 and 3 respectively.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        ln = len(A)
        mini = A[0]
        maxi = A[ln - 1]
        cnt = 0

        for i in range(ln):
            if A[i] == mini or A[i] == maxi:
                cnt += 1
        return ln - cnt


s = Solution()
print(s.solve([1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]))
# OUTPUT: 2
