# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 17/11/21
# -----------------------------------------------


# ***** Cycle in Directed Graph *****
#
# Problem Description
#
# Given an directed graph having A nodes. A matrix B of size M x 2 is given which represents the M edges
# such that there is a edge directed from node B[i][0] to node B[i][1].
#
# Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.
#
# NOTE:
#
# The cycle must contain atleast two nodes.
# There are no self-loops in the graph.
# There are no multiple edges between two nodes.
# The graph may or may not be connected.
# Nodes are numbered from 1 to A.
# Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
#
#
# Problem Constraints
#
# 2 <= A <= 105
#
# 1 <= M <= min(200000,A*(A-1))
#
# 1 <= B[i][0], B[i][1] <= A
#
#
#
# Input Format
#
# The first argument given is an integer A representing the number of nodes in the graph.
#
# The second argument given a matrix B of size M x 2 which represents the M edges such that
# there is a edge directed from node B[i][0] to node B[i][1].
#
#
#
# Output Format
#
# Return 1 if cycle is present else return 0.
#
#
#
# Example Input
#
# Input 1:
#
#  A = 5
#  B = [  [1, 2]
#         [4, 1]
#         [2, 4]
#         [3, 4]
#         [5, 2]
#         [1, 3] ]
# Input 2:
#
#  A = 5
#  B = [  [1, 2]
#         [2, 3]
#         [3, 4]
#         [4, 5] ]
#
#
# Example Output
#
# Output 1:
#
#  1
# Output 2:
#
#  0
#
#
# Example Explanation
#
# Explanation 1:
#
#  The given graph contain cycle 1 -> 3 -> 4 -> 1 or the cycle 1 -> 2 -> 4 -> 1
# Explanation 2:
#
#  The given graph doesn't contain any cycle.


from collections import defaultdict
from sys import setrecursionlimit


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):

        visited[v] = True
        recStack[v] = True

        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        recStack[v] = False
        return False

    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return 1
        return 0


class Solution:

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        setrecursionlimit(10 ** 5)
        g = Graph(A)
        for start, end in B:
            g.addEdge(start, end)
        return g.isCyclic()


if __name__ == '__main__':
    A = 5
    B = [[1, 2], [4, 1], [2, 4], [3, 4], [5, 2], [1, 3]]
    s = Solution()
    print(s.solve(A, B))
    # OUTPUT: 1
