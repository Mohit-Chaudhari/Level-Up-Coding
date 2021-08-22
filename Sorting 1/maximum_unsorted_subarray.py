# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 23/08/21
# -----------------------------------------------

# ***** Maximum Unsorted Subarray *****
# Problem Description
#
# Given an array A of non-negative integers of size N. Find the minimum sub-array Al, Al+1 ,...,
# Ar such that if we sort(in ascending order) that sub-array, then the whole array should get sorted. If A is already sorted, output -1.
#
#
#
# Problem Constraints
# 1 <= N <= 1000000
# 1 <= A[i] <= 1000000
#
#
#
# Input Format
# First and only argument is an array of non-negative integers of size N.
#
#
#
# Output Format
# Return an array of length 2 where First element denotes the starting index(0-based) and
# second element denotes the ending index(0-based) of the sub-array. If the array is already sorted,
# return an array containing only one element i.e. -1.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 3, 2, 4, 5]
# Input 2:
#
# A = [1, 2, 3, 4, 5]
#
#
# Example Output
# Output 1:
#
# [1, 2]
# Output 2:
#
# [-1]
#
#
# Example Explanation
# Explanation 1:
#
# If we sort the sub-array A1, A2, then the whole array A gets sorted.
# Explanation 2:
#
# A is already sorted.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        arr = A[:]
        A.sort()
        index = list()

        ln = len(A)
        front = True
        rear = True
        i = 0

        while (front or rear) and i < ln:
            if front:
                if A[i] != arr[i]:
                    front = False
                    index.append(i)
            if rear:
                if A[ln - i - 1] != arr[ln - i - 1]:
                    rear = False
                    index.append(ln - i - 1)
            i += 1
        if len(index) > 1:
            index.sort()
            return index
        else:
            return [-1]


s = Solution()
print(s.subUnsort([1,2,3,4,5]))
# print(s.subUnsort([1, 3, 2, 4, 5]))
# OUTPUT: [1, 2]
