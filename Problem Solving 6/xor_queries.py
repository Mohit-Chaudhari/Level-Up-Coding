# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 08/07/21
# -----------------------------------------------

# Xor queries
# Problem Description
#
# You are given an array A (containing only 0 and 1) as element of N length.
# Given L and R, you need to determine value of XOR of all elements from L to R (both inclusive) and
# number of unset bits (0's) in the given range of the array.
#
#
#
# Problem Constraints
# 1<=N,Q<=100000
# 1<=L<=R<=N
#
#
# Input Format
# First argument contains the array of size N containing 0 and 1 only.
# Second argument contains a 2D array with Q rows and 2 columns,
# each row represent a query with 2 columns representing L and R.
#
#
# Output Format
# Return an 2D array of Q rows and 2 columns i.e the xor value and
# number of unset bits in that range respectively for each query.
#
#
# Example Input
# A=[1,0,0,0,1]
# B=[ [2,4],
#     [1,5],
#     [3,5] ]
#
#
# Example Output
# [[0 3]
# [0 3]
# [1 2]]
#
#
# Example Explanation
# In the given case the bit sequence is of length 5 and the sequence is 1 0 0 0 1.
# For query 1 the range is (2,4), and the answer is (array[2] xor array[3] xor array[4]) = 0,
# and number of zeroes are 3, so output is 0 3.
# Similarly for other queries.

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A)
        prefix_xor = list()
        zeroes = list()
        cnt = 0

        # GENERATE PREFIX XOR ARRAY
        for i in range(n):
            if A[i] == 0:
                cnt += 1
            zeroes.append(cnt)
            if i == 0:
                prefix_xor.append(A[i])
            else:
                prefix_xor.append(prefix_xor[i-1] ^ A[i])
        print("PREFIX XOR     : ", prefix_xor)
        print("COUNT OF ZEROS : ", zeroes)

        i = 0
        parent = list()
        while i < len(B):
            child = list()
            left = B[i][0]
            right = B[i][1]
            print("LEFT : ", left-2)
            print("RIGHT : ", right-1)
            # APPEND XOR FROM LEFT TO RIGHT
            if left == 1 or 0 and right == len(A):
                child.append(prefix_xor[right-1])
                child.append(zeroes[right-1])
            else:
                child.append(prefix_xor[right-1] ^ prefix_xor[left-2])
                child.append(zeroes[right-1] - zeroes[left-2])
            parent.append(child)
            i += 1
        return parent


s = Solution()
print(s.solve([1, 0, 0, 0, 1], [[2, 4], [1, 5], [3, 5]]))

