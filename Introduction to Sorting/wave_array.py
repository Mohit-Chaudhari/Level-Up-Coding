# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 01/10/21
# -----------------------------------------------

# ***** Wave Array *****
# Problem Description
#
# Given an array of integers A, sort the array into a wave like array and return it,
# In other words, arrange the elements into a sequence such that
#
# a1 >= a2 <= a3 >= a4 <= a5.....
# NOTE : If there are multiple answers possible, return the one that's lexicographically smallest.
#
#
#
# Problem Constraints
# 1 <= len(A) <= 106
# 1 <= A[i] <= 106
#
#
#
# Input Format
# First argument is an integer array A.
#
#
#
# Output Format
# Return an array arranged in the sequence as described.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 2, 3, 4]
# Input 2:
#
# A = [1, 2]
#
#
# Example Output
# Output 1:
#
# [2, 1, 4, 3]
# Output 2:
#
# [2, 1]
#
#
# Example Explanation
# Explanation 1:
#
# One possible answer : [2, 1, 4, 3]
# Another possible answer : [4, 1, 3, 2]
# First answer is lexicographically smallest. So, return [2, 1, 4, 3].
# Explanation 1:
#
# Only possible answer is [2, 1].

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, arr):
        n = len(arr)
        # sort the array

        arr.sort()

        # Swap adjacent elements
        for i in range(0, n - 1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr


s = Solution()
print(s.wave([1, 2, 3, 4]))
# OUTPUT: [2, 1, 4, 3]
