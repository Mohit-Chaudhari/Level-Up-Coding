# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 19/09/21
# -----------------------------------------------

# ***** Largest Rectangle in Histogram *****
# Problem Description
#
# Given an array of integers A .
#
# A represents a histogram i.e A[i] denotes height of the ith histogram's bar. Width of each bar is 1.
#
# Find the area of the largest rectangle formed by the histogram.
#
#
#
# Problem Constraints
# 1 <= |A| <= 100000
#
# 1 <= A[i] <= 1000000000
#
#
#
# Input Format
# The only argument given is the integer array A.
#
#
#
# Output Format
# Return the area of largest rectangle in the histogram.
#
#
#
# Example Input
# Input 1:
#
#  A = [2, 1, 5, 6, 2, 3]
# Input 2:
#
#  A = [2]
#
#
# Example Output
# Output 1:
#
#  10
# Output 2:
#
#  2
#
#
# Example Explanation
# Explanation 1:
#
# The largest rectangle has area = 10 unit. Formed by A[3] to A[4].
# Explanation 2:
#
# Largest rectangle has area 2.

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):

        i, n = 0, len(A)

        max_area, stack = 0, []
        while i < n:
            if not stack or A[stack[-1]] <= A[i]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()

                area = (A[top]) * (i - stack[-1] - 1 if stack else i)

                max_area = max(max_area, area)

        while stack:
            top = stack.pop()

            area = (A[top]) * (i - stack[-1] - 1 if stack else i)
            max_area = max(max_area, area)

        return max_area


s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
# OUTPUT: 10
