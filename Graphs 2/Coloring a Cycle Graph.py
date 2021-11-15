# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 15/11/21
# -----------------------------------------------

# ***** Coloring a Cycle Graph *****
# Problem Description
#
# Given the number of vertices A in a Cyclic Graph.
#
# Your task is to determine the number of colors required to color the
# graph so that no two Adjacent vertices have the same color.
#
#
#
# Problem Constraints
#
# 3 <= A <= 109
#
#
#
# Input Format
#
# First argument is an integer A denoting the number of vertices in the Cyclic Graph.
#
#
#
# Output Format
#
# Return an single integer denoting the number of colors required to color the graph so that no two Adjacent vertices have the same color.
#
#
#
# Example Input
#
# Input 1:
#
#  5
# Input 2:
#
#  4
#
#
# Example Output
#
# Output 1:
#
#  3
# Output 2:
#
#  2

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        if A % 2 == 0:
            return 2
        return 3


if __name__ == '__main__':
    s = Solution()
    print(s.solve(5))
    # OUTPUT : 3
    print(s.solve(6))
    # OUTPUT: 2
