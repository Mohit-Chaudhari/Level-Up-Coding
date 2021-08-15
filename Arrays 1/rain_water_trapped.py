# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 16/08/21
# -----------------------------------------------

# ***** Rain Water Trapped *****
# Problem Description
#
# Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
#
#
#
# Problem Constraints
# 1 <= |A| <= 100000
#
#
#
# Input Format
# First and only argument is the vector A
#
#
#
# Output Format
# Return one integer, the answer to the question
#
#
#
# Example Input
# Input 1:
#
# A = [0, 1, 0, 2]
# Input 2:
#
# A = [1, 2]
#
#
# Example Output
# Output 1:
#
# 1
# Output 2:
#
# 0
#
#
# Example Explanation
# Explanation 1:
#
# 1 unit is trapped on top of the 3rd element.
# Explanation 2:
#
# No water is trapped.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        ln = len(A)
        front_maxi = -float('inf')
        back_maxi = -float('inf')
        front = [0 for i in range(ln)]
        back = [0 for i in range(ln)]
        cnt = 0

        for i in range(ln):
            if front_maxi < A[i]:
                front_maxi = A[i]
            front[i] = front_maxi

            if back_maxi < A[ln - i - 1]:
                back_maxi = A[ln - i - 1]
            back[ln - i - 1] = back_maxi

        # print(A)
        # print(front)
        # print(back)

        for i in range(1, ln-1):
            temp = min(front[i], back[i])
            cnt += temp - A[i]

        return cnt


s = Solution()
# print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap([0, 1, 0, 2]))
# OUTPUT: 1
