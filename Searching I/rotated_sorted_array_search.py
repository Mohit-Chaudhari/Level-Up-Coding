# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 21/08/21
# -----------------------------------------------

# ***** Rotated Sorted Array Search *****
# Problem Description
#
# Given a sorted array of integers A of size N and an integer B.
#
# array A is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).
#
# You are given a target value B to search. If found in the array, return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# NOTE: Users are expected to solve this in O(log(N)) time.
#
# Problem Constraints
# 1 <= N <= 1000000
#
# 1 <= A[i] <= 10^9
#
# all elements in A are disitinct.
#
# Input Format
# The first argument given is the integer array A.
#
# The second argument given is the integer B.
#
# Output Format
# Return index of B in array A, otherwise return -1
#
#
#
# Example Input
# Input 1:
#
# A = [4, 5, 6, 7, 0, 1, 2, 3]
# B = 4
# Input 2:
#
# A = [1]
# B = 1
#
# Example Output
# Output 1:
#
#  0
# Output 2:
#
#  0
#
# Example Explanation
#
# Explanation
# 1:
#
# Target 4 is found at index 0 in A.
#
# Explanation
# 2:
#
# Target
# 1 is found at index 0 in A.

class Solution:

    def searchHelper(self, arr, start, end, key):

        pivot = (start + end) // 2

        if arr[pivot] == key:
            return pivot

        elif start == end:
            if arr[start] == key:
                return start
            return -1

        elif arr[start] == key:
            return start

        elif arr[end] == key:
            return end

        elif arr[start] <= key < arr[pivot]:
            return self.searchHelper(arr, start, pivot - 1, key)

        elif arr[pivot] < key <= arr[end]:
            return self.searchHelper(arr, pivot + 1, end, key)

        elif arr[start] - arr[pivot] > 0:
            return self.searchHelper(arr, start, pivot - 1, key)

        elif arr[pivot] - arr[end] > 0:
            return self.searchHelper(arr, pivot + 1, end, key)

        else:
            return -1

    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        ln = len(A)
        return self.searchHelper(A, 0, ln - 1, B)


s = Solution()
A = [ 19, 20, 21, 22, 28, 29, 32, 36, 39, 40, 41, 42, 43, 45, 48, 49, 51, 54, 55, 56, 58, 60, 61, 62, 65, 67, 69, 71, 72, 74, 75, 78, 81, 84, 85, 87, 89, 92, 94, 95, 96, 97, 98, 99, 100, 105, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 130, 131, 133, 134, 135, 136, 137, 138, 139, 141, 142, 144, 146, 147, 148, 149, 150, 153, 155, 157, 159, 161, 163, 164, 169, 170, 175, 176, 179, 180, 185, 187, 188, 189, 192, 196, 199, 201, 203, 205, 3, 7, 9, 10, 12, 13, 17 ]
print(s.search(A, 6))
# print(s.search([4, 5, 6, 7, 0, 1, 2, 3], 4))
# OUTPUT: 0
