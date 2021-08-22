# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 22/08/21
# -----------------------------------------------


# ***** Permutations *****
# Problem Description
#
# Given an integer array A of size N denoting collection of numbers , return all possible permutations.
#
# NOTE:
#
# No two entries in the permutation sequence should be the same.
# For the purpose of this problem, assume that all the numbers in the collection are unique.
# Return the answer in any order
# WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS.
# Example : next_permutations in C++ / itertools.permutations in python.
# If you do, we will disqualify your submission retroactively and give you penalty points.
#
#
# Problem Constraints
# 1 <= N <= 9
#
#
#
# Input Format
# Only argument is an integer array A of size N.
#
#
#
# Output Format
# Return a 2-D array denoting all possible permutation of the array.
#
#
#
# Example Input
# A = [1, 2, 3]
#
#
# Example Output
# [ [1, 2, 3]
#   [1, 3, 2]
#   [2, 1, 3]
#   [2, 3, 1]
#   [3, 1, 2]
#   [3, 2, 1] ]
#
#
# Example Explanation
# All the possible permutation of array [1, 2, 3].
import are as are


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        result = list()

        if len(A) == 1:
            return [A[:]]

        for i in range(len(A)):
            n = A.pop(0)
            perms = self.permute(A)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            A.append(n)

        return result


s = Solution()
print(s.permute([1, 2, 3]))
# OUTPUT:
