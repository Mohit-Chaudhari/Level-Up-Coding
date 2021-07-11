# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 11/07/21
# -----------------------------------------------

# ***** Intersection Of Sorted Arrays *****
# Find the intersection of two sorted arrays.
# OR in other words, Given 2 sorted arrays, find all the elements which occur in both the arrays.
#
# Example :
#
# Input :
#     A : [1 2 3 3 4 5 6]
#     B : [3 3 5]
#
# Output : [3 3 5]
#
# Input :
#     A : [1 2 3 3 4 5 6]
#     B : [3 5]
#
# Output : [3 5]
import sys


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):

        len_a = len(A)
        len_b = len(B)
        ai = 0
        bi = 0
        arr = list()

        while len_a > 0 and len_b > 0:
            if A[ai] == B[bi]:
                arr.append(B[bi])
                ai += 1
                bi += 1
                len_a -= 1
                len_b -= 1
            elif A[ai] < B[bi]:
                ai += 1
                len_a -= 1
            elif A[ai] > B[bi]:
                bi += 1
                len_b -= 1
        return arr


s = Solution()
A = [1, 3, 8, 10, 13, 13, 16, 16, 16, 18, 21, 23, 24, 31, 31, 31, 33, 35, 35, 37, 37, 38, 40, 41, 43, 47, 47, 48, 48, 52, 52, 53, 53, 55, 56, 60, 60, 61, 61, 63, 63, 64, 66, 67, 67, 68, 69, 71, 80, 80, 80, 80, 80, 80, 81, 85, 87, 87, 88, 89, 90, 94, 95, 97, 98, 98, 100, 101 ]
B = [5, 7, 14, 14, 25, 28, 28, 34, 35, 38, 38, 39, 46, 53, 65, 67, 69, 70, 78, 82, 94, 94, 98 ]
print(s.intersect(A, B))
# OUTPUT: [35, 38, 53, 67, 69, 94, 98]
