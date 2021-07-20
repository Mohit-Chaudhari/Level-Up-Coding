# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 20/07/21
# -----------------------------------------------

# ***** Colorful Number *****
# Problem Description
#
# For Given Number A find if its COLORFUL number or not.
#
# If number A is a COLORFUL number return 1 else return 0.
#
# What is a COLORFUL Number:
#
# A number can be broken into different contiguous sub-subsequence parts.
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
# And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different.
#
#
# Problem Constraints
# 1 <= A <= 2 * 109
#
#
#
# Input Format
# Single Argument which denotes integer A.
#
#
#
# Output Format
# Return 1 if integer A is COLORFUL else return 0.
#
#
#
# Example Input
# Input 1:
#
#  A = 23
# Input 2:
#
#  A = 236
#
#
# Example Output
# Output 1:
#
#  1
# Output 2:
#
#  0
#
#
# Example Explanation
# Explanation 1:
#
#  Possible Sub-sequences: [2, 3, 23] where
#  2 -> 2
#  3 -> 3
#  23 -> 6  (product of digits)
#  This number is a COLORFUL number since product of every digit of a sub-sequence are different.
# Explanation 2:
#
#  Possible Sub-sequences: [2, 3, 6, 23, 36, 236] where
#  2 -> 2
#  3 -> 3
#  6 -> 6
#  23 -> 6  (product of digits)
#  36 -> 18  (product of digits)
#  236 -> 36  (product of digits)
#  This number is not a COLORFUL number since the product sequence 23  and sequence 6 is same.

class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):

        arr = list()
        s = set()
        while A > 0:
            arr.append(A % 10)
            A //= 10

        arr.reverse()
        ln = len(arr)

        if ln == 1:
            return 1

        for i in range(ln):
            if arr[i] in s:
                return 0
            else:
                temp = arr[i]
                s.add(arr[i])
            for j in range(i+1, ln):
                if temp * arr[j] in s:
                    return 0
                else:
                    temp = temp * arr[j]
                    s.add(temp)
        return 1


s = Solution()
print(s.colorful(123))
# OUTPUT: 0
