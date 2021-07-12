# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 12/07/21
# -----------------------------------------------

# ***** Remove Duplicates from Sorted Array *****
# Problem Description
#
# Given a sorted array A consisting of duplicate elements.
#
# Your task is to remove all the duplicates and return a sorted array of distinct elements consisting of all distinct elements present in A.
#
# NOTE: The input format has been changed from previous versions.
#
#
#
# Problem Constraints
# 1 <= |A| <= 106
#
# 1 <= A[i] <= 2*109
#
#
#
# Input Format
# First and only argurment containing the integer array A.
#
#
#
# Output Format
# Return an array/vector from the function as per the question.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 1, 2]
# Input 2:
#
# A = [1, 2, 2, 3, 3]
#
#
# Example Output
# Output 1:
#
# [1, 2]
# Output 2:
#
# [1, 2, 3]
#
#
# Example Explanation
# Explanation 1:
#
# Updated Array: [1, 2] after removing the 2nd element.
# Explanation 2:
#
# Updated Array: [1, 2, 3] after removing the 3rd and 5th element.


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        len_a = len(A)
        arr = [A[0]]
        i = 1
        while i < len_a:
            if A[i] != A[i-1]:
                arr.append(A[i])
            i += 1

        return arr


s = Solution()
print(s.solve([5000, 5000, 5000]))
# OUTPUT: [5000]
