# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 04/07/21
# -----------------------------------------------

# Majority Element
# Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example :
#
# Input : [2, 1, 2]
# Return  : 2 which occurs 2 times which is greater than 3/2.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def MajorityElement(self, A):
        cnd = float('inf')

        cnt = 0
        n = len(A)

        for i in range(n):
            if cnd is None:
                cnt += 1
                cnd = A[i]
            elif i == 0:
                cnd = A[i]
                cnt = 1
            else:
                if cnd == A[i]:
                    cnt += 1
                else:
                    cnt -= 1
                    if cnt == 0:
                        cnd = None

        cnt = 0
        for i in range(n):
            if cnd == A[i]:
                cnt += 1

        return cnd


s = Solution()
s.MajorityElement([2, 1, 2])
