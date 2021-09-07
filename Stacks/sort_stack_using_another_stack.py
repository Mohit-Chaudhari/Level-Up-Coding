# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 07/09/21
# -----------------------------------------------

# ***** Sort stack using another stack *****
# Problem Description
#
# Given a stack of integers A, sort it using another stack.
#
# Return the array of integers after sorting the stack using another stack.
#
#
#
# Problem Constraints
# 1 <= |A| <= 5000
#
# 0 <= A[i] <= 1000000000
#
#
#
# Input Format
# The only argument given is the integer array A.
#
#
#
# Output Format
# Return the array of integers after sorting the stack using another stack.
#
#
#
# Example Input
# Input 1:
#
#  A = [5, 4, 3, 2, 1]
# Input 2:
#
#  A = [5, 17, 100, 11]
#
#
# Example Output
# Output 1:
#
#  [1, 2, 3, 4, 5]
# Output 2:
#
#  [5, 11, 17, 100]
#
#
# Example Explanation
# Explanation 1:
#
#  Just sort the given numbers.
# Explanation 2:
#
#  Just sort the given numbers.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        temp = None
        arr = list()
        while A:
            temp = A.pop()
            if arr:
                if arr[-1] < temp:
                    arr.append(temp)
                else:
                    while arr:
                        if arr[-1] > temp:
                            A.append(arr.pop())
                        else:
                            break
                    arr.append(temp)
            else:
                arr.append(temp)
        return arr


s = Solution()
print(s.solve([66, 96, 43, 28, 14, 1, 41, 76, 70, 81, 22, 11, 42, 78, 4, 88, 70, 43, 90, 6, 12]))
# print(s.solve([5, 4, 3, 2, 1]))
# OUTPUT: [1, 2, 3, 4, 5]
