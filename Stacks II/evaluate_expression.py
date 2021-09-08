# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 08/09/21
# -----------------------------------------------

# ***** Evaluate Expression *****
# Problem Description
#
# An arithmetic expression is given by a charater array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each character may be an integer or an operator.
#
#
#
# Problem Constraints
# 1 <= N <= 105
#
#
#
# Input Format
# The only argument given is character array A.
#
#
#
# Output Format
# Return the value of arithmetic expression formed using reverse Polish Notation.
#
#
#
# Example Input
# Input 1:
#     A =   ["2", "1", "+", "3", "*"]
# Input 2:
#     A = ["4", "13", "5", "/", "+"]
#
#
# Example Output
# Output 1:
#     9
# Output 2:
#     6
#
#
# Example Explanation
# Explaination 1:
#     starting from backside:
#     * : () * ()
#     3 : () * (3)
#     + : (() + ()) * (3)
#     1 : (() + (1)) * (3)
#     2 : ((2) + (1)) * (3)
#     ((2) + (1)) * (3) = 9
# Explaination 2:
#     + : () + ()
#     / : () + (() / ())
#     5 : () + (() / (5))
#     1 : () + ((13) / (5))
#     4 : (4) + ((13) / (5))
#     (4) + ((13) / (5)) = 6

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        ln = len(A)
        arr = list()

        for i in range(ln):
            if A[i] == "+":
                b = arr.pop()
                a = arr.pop()
                arr.append(int(b) + int(a))
            elif A[i] == "-":
                b = arr.pop()
                a = arr.pop()
                arr.append(int(a) - int(b))
            elif A[i] == "/":
                b = arr.pop()
                a = arr.pop()
                arr.append(int(a) // int(b))
            elif A[i] == "*":
                b = arr.pop()
                a = arr.pop()
                arr.append(int(b) * int(a))
            else:
                arr.append(int(A[i]))
        return arr.pop()


s = Solution()
print(s.evalRPN(["4", "13", "5", "/", "+"]))
# print(s.evalRPN(["2", "1", "+", "3", "*"]))
# OUTPUT: 9
