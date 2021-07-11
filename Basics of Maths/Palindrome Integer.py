# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 11/07/21
# -----------------------------------------------

# ***** Palindrome Integer *****
# Determine whether an integer is a palindrome. Do this without extra space.
#
# A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
# Negative numbers are not palindromic.
#
# Example :
#
# Input : 12121
# Output : True
#
# Input : 123
# Output : False

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        A = str(A)
        n = len(str(A))
        for i in range(n//2):
            if A[i] != A[n-i-1]:
                return 0
        return 1


s = Solution()
print(s.isPalindrome(12121))
# OUTPUT: True
