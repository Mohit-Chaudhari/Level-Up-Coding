# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 28/07/21
# -----------------------------------------------

# ***** String operations *****
# Problem Description
#
# Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:
#
# Concatenate the string with itself.
# Delete all the uppercase letters.
# Replace each vowel with '#'.
# You are given a string A of size N consisting of lowercase and uppercase alphabets.
# Return the resultant string after applying the above operations.
#
# NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
#
#
#
# Problem Constraints
# 1<=N<=100000
#
#
# Input Format
# First argument is a string A of size N.
#
#
#
# Output Format
# Return the resultant string.
#
#
#
# Example Input
# A="AbcaZeoB"
#
#
#
# Example Output
# "bc###bc###"
#
#
#
# Example Explanation
# First concatenate the string with itself so string A becomes "AbcaZeoBAbcaZeoB".
# Delete all the uppercase letters so string A becomes "bcaeobcaeo".
# Now replace vowel with '#'.
# A becomes "bc###bc###".

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A += A
        ln = len(A)
        str = ""
        for i in range(ln):
            if 65 <= ord(A[i]) <= 90:
                continue
            elif A[i] in ['a', 'e', 'i', 'o', 'u']:
                str += '#'
            else:
                str += A[i]
        return str


s = Solution()
print(s.solve("AbcaZeoB"))
# OUTPUT: bc###bc###
