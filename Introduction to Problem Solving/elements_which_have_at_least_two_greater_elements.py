# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 20/07/21
# -----------------------------------------------

# ***** Elements which have at-least two greater elements *****
# Problem Description
#
# You are given an array of distinct integers A, you have to find and return all elements in array which have at-least
# two greater elements than themselves.
#
# NOTE: The result should have the order in which they are present in the original array.
#
#
#
# Problem Constraints
# 3 <= |A| <= 105
#
# -109 <= A[i] <= 109
#
#
#
# Input Format
# First and only argument is an integer array A.
#
#
#
# Output Format
# Return an integer array containing the elements of A which have at-least two greater elements than themselves in A.
#
#
#
# Example Input
# Input 1:
#
#  A = [1, 2, 3, 4, 5]
# Input 2:
#
#  A = [11, 17, 100, 5]
#
#
# Example Output
# Output 1:
#
#  [1, 2, 3]
# Output 2:
#
#  [11, 5]
#
#
# Example Explanation
# Explanation 1:
#
#  Number of elements greater than 1: 4
#  Number of elements greater than 2: 3
#  Number of elements greater than 3: 2
#  Number of elements greater than 4: 1
#  Number of elements greater than 5: 0
#  Elements 1, 2 and 3 have atleast 2 elements strictly greater than themselves.
# Explanation 2:
#
#  Number of elements greater than 11: 2
#  Number of elements greater than 17: 1
#  Number of elements greater than 100: 0
#  Number of elements greater than 5: 3
#  Elements 5 and 11 have atleast 2 elements strictly greater than themselves.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        B = A.copy()
        A.sort()
        lst = A[len(A)-2:]
        new_lst = [x for x in B if x not in lst]
        return new_lst


s = Solution()
print(s.solve([1, 2, 3, 4, 5]))
# OUTPUT: [1, 2, 3]
