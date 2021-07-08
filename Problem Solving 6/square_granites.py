# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 08/07/21
# -----------------------------------------------

# Square granites
# Problem Description
#
# A city is of rectangular shape with the size A * B meters. On the occasion of the city's anniversary, a decision was taken to pave the city with square granite flagstones. Each flagstone is of the size C * C. What is the least number of flagstones needed to pave the city?
#
# NOTE: It's allowed to cover the surface larger than the city, but the city has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the city.
#
#
#
# Problem Constraints
# 1 <= A <= 109
#
# 1 <= B <= 109
#
# 1 <= C <= 109
#
#
#
# Input Format
# First argument is an integer A as per the question.
#
# Second argument is an integer B as per the question.
#
# Third argument is an integer C as per the question.
#
#
#
# Output Format
# Return an integer showing least number of flagstones needed.
#
#
#
# Example Input
# Input 1:
#
# A=6, B=6, C=4
#
#
# Example Output
# Output 1:
#
# 4
#
#
# Example Explanation
# Explanation 1:
#
# If we use 4 flagstones(2 rows and 2 columns) then it will cover the whole city.

import math


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        return math.ceil(A / C) * math.ceil(B / C)


s = Solution()
print(s.solve(6, 6, 4))
