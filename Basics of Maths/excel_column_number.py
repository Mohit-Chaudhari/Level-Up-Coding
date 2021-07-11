# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 11/07/21
# -----------------------------------------------

# ***** Excel Column Number *****
# Problem Description
#
# Given a column title as appears in an Excel sheet, return its corresponding column number.
#
#
#
# Problem Constraints
# 1 <= length of the column title <= 5
#
#
#
# Input Format
# Input a string which represents the column title in excel sheet.
#
#
#
# Output Format
# Return a single integer which represents the corresponding column number.
#
#
#
# Example Input
# Input 1:
#
#  AB
# Input 2:
#
#  ABCD
#
#
# Example Output
# Output 1:
#
#  28
# Output 2:
#
#  19010
#
#
# Example Explanation
# Explanation 1:
#
#  A -> 1
#  B -> 2
#  C -> 3
#  ...
#  Z -> 26
#  AA -> 27
#  AB -> 28

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        Alphabet = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
            "J": 10,
            "K": 11,
            "L": 12,
            "M": 13,
            "N": 14,
            "O": 15,
            "P": 16,
            "Q": 17,
            "R": 18,
            "S": 19,
            "T": 20,
            "U": 21,
            "V": 22,
            "W": 23,
            "X": 24,
            "Y": 25,
            "Z": 26
        }
        n = len(A)
        power = n - 1
        index = 0
        for i in range(n):
            index = index + ((26 ** power) * Alphabet[A[i]])
            if power >= 0:
                power -= 1
        return index


s = Solution()
print(s.titleToNumber("ABCD"))
# OUTPUT: 19010
