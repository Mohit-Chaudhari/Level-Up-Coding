# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 22/08/21
# -----------------------------------------------

# ***** Find a peak element *****
# Problem Description
#
# Given an array of integers A, find and return the peak element in it.
# An array element is peak if it is NOT smaller than its neighbors.
#
# For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.
#
# NOTE: Users are expected to solve this in O(log(N)) time.
#
#
#
# Problem Constraints
# 1 <= |A| <= 100000
#
# 1 <= A[i] <= 109
#
#
#
# Input Format
# The only argument given is the integer array A.
#
#
#
# Output Format
# Return the peak element.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 2, 3, 4, 5]
# Input 2:
#
# A = [5, 17, 100, 11]
#
#
# Example Output
# Output 1:
#
#  5
# Output 2:
#
#  100
#
#
# Example Explanation
# Explanation 1:
#
#  5 is the peak.
# Explanation 2:
#
#  100 is the peak.

class Solution:

    def helper(self, arr, start, end):

        pivot = (start + end) // 2

        if arr[pivot] > arr[pivot - 1] and arr[pivot] > arr[pivot + 1]:
            return arr[pivot]
        elif arr[pivot] < arr[pivot - 1]:
            return self.helper(arr, start, pivot - 1)
        elif arr[pivot] < arr[pivot + 1]:
            return self.helper(arr, pivot + 1, end)
        elif arr[pivot - 1] < arr[pivot] <= arr[pivot + 1]:
            return arr[pivot]

    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ln = len(A)
        if ln == 1:
            return A[0]
        else:
            if A[0] > A[1]:
                return A[0]
            if A[ln - 1] > A[ln - 2]:
                return A[ln - 1]

        return self.helper(A, 0, ln - 1)


s = Solution()
print(s.solve([1, 1000000000, 1000000000]))
# print(s.solve([5, 17, 100, 11]))
# OUTPUT: 100
