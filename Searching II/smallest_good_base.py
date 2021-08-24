# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 25/08/21
# -----------------------------------------------

# ***** Smallest Good Base *****
# Given an integer A, we call k >= 2 a good base of A, if all digits of A base k are 1.
# Now given a string representing A, you should return the smallest good base of A in string format.
#
#
# Input Format
#
# The only argument given is the string representing A.
# Output Format
#
# Return the smallest good base of A in string format.
# Constraints
#
# 3 <= A <= 10^18
# For Example
#
# Input 1:
#     A = "13"
# Output 1:
#     "3"     (13 in base 3 is 111)
#
# Input 2:
#     A = "4681"
# Output 2:
#     "8"     (4681 in base 8 is 11111).
import math


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, n):
        n = int(n)
        for m in range(2, 61):
            k = int(math.pow(n, 1.0/m))
            if k ==1 or k== n-1:
                continue
            sum = 1
            current_k = k
            for _ in range(1,m+1):
                sum += current_k
                current_k *=k
            if sum ==n :
                return str(k)
        return str(n-1)


s = Solution()
print(s.solve("13"))
# OUTPUT: 3
