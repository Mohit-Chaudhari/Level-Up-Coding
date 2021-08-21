# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 21/08/21
# -----------------------------------------------

# ***** Single Element in a Sorted Array *****
# Problem Description
#
# Given a sorted array of integers A where every element appears twice except for one element which appears once,
# find and return this single element that appears only once.
#
# NOTE: Users are expected to solve this in O(log(N)) time.
#
#
#
# Problem Constraints
# 1 <= |A| <= 100000
#
# 1 <= A[i] <= 10^9
#
#
#
# Input Format
# The only argument given is the integer array A.
#
#
#
# Output Format
# Return the single element that appears only once.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 1, 7]
# Input 2:
#
# A = [2, 3, 3]
#
#
# Example Output
# Output 1:
#
#  7
# Output 2:
#
#  2
#
#
# Example Explanation
# Explanation 1:
#
#  7 appears once
# Explanation 2:
#
#  2 appears once

class Solution:

    def helper(self, arr, start, end):

        pivot = (start + end) // 2

        # a = arr[start:end + 1]
        # start_element = arr[start]
        # end_element = arr[end]
        # pivot_element = arr[pivot]

        if start == end:
            return arr[pivot]

        elif arr[pivot] != arr[pivot + 1] and arr[pivot] != arr[pivot - 1]:
            return arr[pivot]
        elif pivot % 2 == 0 and arr[pivot] != arr[pivot + 1]:
            return self.helper(arr, start, pivot)
        elif pivot % 2 == 0 and arr[pivot] == arr[pivot + 1]:
            return self.helper(arr, pivot + 2, end)
        elif pivot % 2 != 0 and arr[pivot] != arr[pivot - 1]:
            return self.helper(arr, start, pivot - 1)
        elif pivot % 2 != 0 and arr[pivot] == arr[pivot - 1]:
            return self.helper(arr, pivot + 1, end)

    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ln = len(A)
        start = 0
        end = ln - 1

        if ln == 1 or A[0] != A[1]:
            return A[0]
        else:
            start = 2

        if A[ln-1] != A[ln-2]:
            if (ln - 1) % 2 == 0:
                return A[ln-1]
        else:
            end = ln - 3

        return self.helper(A, start, end)


s = Solution()
print(s.solve([1, 1, 7]))
# OUTPUT: 7
