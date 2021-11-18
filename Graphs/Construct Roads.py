# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 18/11/21
# -----------------------------------------------


# ***** Construct Roads *****
#
# Problem Description
#
# A country consist of N cities connected by N - 1 roads. King of that country want to construct maximum number of roads
# such that the new country formed remains bipartite country.
#
# Bipartite country is a country, whose cities can be partitioned into 2 sets in such a way, that for each road (u, v)
# that belongs to the country, u and v belong to different sets. Also, there should be no multiple roads between
# two cities and no self loops.
#
# Return the maximum number of roads king can construct. Since the answer could be large return answer % 109 + 7.
#
# NOTE: All cities can be visited from any city.
#
#
#
# Problem Constraints
#
# 1 <= A <= 105
#
# 1 <= B[i][0], B[i][1] <= N
#
#
#
# Input Format
#
# First argument is an integer A denoting the number of cities, N.
#
# Second argument is a 2D array B of size (N-1) x 2 denoting the initial roads i.e. there is a road between
# cities B[i][0] and B[1][1] .
#
#
#
# Output Format
#
# Return an integer denoting the maximum number of roads king can construct.
#
#
#
# Example Input
#
# Input 1:
#
#  A = 3
#  B = [
#        [1, 2]
#        [1, 3]
#      ]
# Input 2:
#
#  A = 5
#  B = [
#        [1, 3]
#        [1, 4]
#        [3, 2]
#        [3, 5]
#      ]
#
#
# Example Output
#
# Output 1:
#
#  0
# Output 2:
#
#  2
#
#
# Example Explanation
#
# Explanation 1:
#
#  We can't construct any new roads such that the country remains bipartite.
# Explanation 2:
#
#  We can add two roads between cities (4, 2) and (4, 5).

from collections import defaultdict


class Solution:

    def __init__(self):
        self.v = None
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self):
        visited = [False] * (self.v + 1)
        sets = [0] * (self.v + 1)
        first = list(self.graph.keys())[0]
        queue = [first]
        visited[first] = True
        sets[first] = 1
        s1 = 0
        s2 = 0

        while queue:

            n = queue.pop(0)

            for i in self.graph[n]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    if sets[n] == 1:
                        sets[i] = 2
                    else:
                        sets[i] = 1

        visited.pop(0)
        sets.pop(0)
        for i in sets:
            if i == 1:
                s1 += 1
            elif i == 2:
                s2 += 1

        # print("S1 : ", s1)
        # print("S2 : ", s2)
        # print("Sets : ", sets)
        # print("visited: ", visited)

        return ((s1 * s2) - (self.v - 1)) % ((10 ** 9) + 7)

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        if len(B) == 0:
            return 0

        self.v = A
        for start, end in B:
            self.add_edge(start, end)
            self.add_edge(end, start)
            # print(self.graph)

        return self.bfs()


if __name__ == "__main__":
    A = 15
    B = [[7, 5], [15, 14], [11, 2], [8, 7], [10, 3], [5, 3], [4, 2], [6, 4], [13, 2], [3, 2], [14, 11], [12, 9], [2, 1], [9, 2]]
    # OUTPUT: 42
    # A = 1
    # B = [[]]
    s = Solution()
    print(s.solve(A, B))

