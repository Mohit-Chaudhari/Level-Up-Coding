# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 14/12/21
# -----------------------------------------------

# GRAPH REPRESENTATION - ADJACENCY MATRIX

class Graph:

    def __init__(self, vertices):
        self._vertices = vertices
        self._adj_matrix = list()
        for _ in range(vertices):
            self._adj_matrix.append([0] * vertices)

        self._visited = [0] * vertices

    def insert_edge(self, u, v, w=1):
        self._adj_matrix[u][v] = w

    def remove_edge(self, u, v):
        self._adj_matrix[u][v] = 0

    def exist_edge(self, u, v):
        return self._adj_matrix[u][v] != 0

    def vertex_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for u in range(self._vertices):
            for v in range(self._vertices):
                if self._adj_matrix[u][v] != 0:
                    count += 1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i, end=" ")
        print()

    def edges(self):
        for u in range(self._vertices):
            for v in range(self._vertices):
                if self._adj_matrix[u][v] != 0:
                    print(u, "--", v)

    def outdegree(self, v):
        count = 0
        for j in range(self._vertices):
            if self._adj_matrix[v][j] != 0:
                count += 1
        return count

    def indegree(self, v):
        count = 0
        for j in range(self._vertices):
            if self._adj_matrix[j][v] != 0:
                count += 1
        return count

    def display_adj_matrix(self):
        # print(self._adj_matrix)
        for i in range(self._vertices):
            print(self._adj_matrix[i])

    def bfs(self, s):
        i = s
        q = list()
        q.append(i)
        print(i, end=" ")

        while q:
            i = q.pop(0)
            self._visited[i] = 1

            for v in range(self._vertices):
                if self._adj_matrix[i][v] != 0 and self._visited[v] == 0:
                    self._visited[v] = 1
                    print(v, end=" ")
                    q.append(v)

    def dfs(self, s):
        if self._visited[s] == 0:
            print(s, end=" ")
            self._visited[s] = 1
            for j in range(self._vertices):
                if self._adj_matrix[s][j] == 1 and self._visited[j] == 0:
                    self.dfs(j)


def undirected_graph():
    G = Graph(4)
    G.display_adj_matrix()
    print("\n - Edges count : ", G.edge_count())
    print("\n - Vertex count : ", G.vertex_count())
    G.insert_edge(0, 1)
    G.insert_edge(0, 2)
    G.insert_edge(1, 0)
    G.insert_edge(1, 2)
    G.insert_edge(2, 0)
    G.insert_edge(2, 1)
    G.insert_edge(2, 3)
    G.insert_edge(3, 2)
    G.display_adj_matrix()
    print("\n - Edges count : ", G.edge_count())
    G.edges()
    print("\n - Edge between 1 - 3 : ", G.exist_edge(1, 3))
    print("\n - Edge between 1 - 2 : ", G.exist_edge(1, 2))
    print("\n - InDegree of 2 : ", G.indegree(2))
    print("\n - OutDegree of 2 : ", G.outdegree(2))
    G.remove_edge(1, 2)
    print("\n - Edge between 1 - 2 : ", G.exist_edge(1, 2))


def weighted_undirected_graph():
    G = Graph(4)
    G.display_adj_matrix()
    print("\n - Edges count : ", G.edge_count())
    print("\n - Vertex count : ", G.vertex_count())
    G.insert_edge(0, 1, 26)
    G.insert_edge(0, 2, 16)
    G.insert_edge(1, 0, 26)
    G.insert_edge(1, 2, 12)
    G.insert_edge(2, 0, 16)
    G.insert_edge(2, 1, 12)
    G.insert_edge(2, 3, 8)
    G.insert_edge(3, 2, 8)
    G.display_adj_matrix()
    print("\n - Edges count : ", G.edge_count())
    G.edges()
    print("\n - Edge between 1 - 3 : ", G.exist_edge(1, 3))
    print("\n - Edge between 1 - 2 : ", G.exist_edge(1, 2))
    print("\n - InDegree of 2 : ", G.indegree(2))
    print("\n - OutDegree of 2 : ", G.outdegree(2))
    G.remove_edge(1, 2)
    print("\n - Edge between 1 - 2 : ", G.exist_edge(1, 2))


def directed_graph():
    G = Graph(4)
    G.display_adj_matrix()
    print("\n - Edges count : ", G.edge_count())
    print("\n - Vertex count : ", G.vertex_count())
    G.insert_edge(0, 1)
    G.insert_edge(0, 2)
    G.insert_edge(1, 2)
    G.insert_edge(2, 3)
    G.display_adj_matrix()
    print("\n - Edges count : ", G.edge_count())
    G.edges()
    print("\n - Edge between 1 - 3 : ", G.exist_edge(1, 3))
    print("\n - Edge between 1 - 2 : ", G.exist_edge(1, 2))
    print("\n - InDegree of 2 : ", G.indegree(2))
    print("\n - OutDegree of 2 : ", G.outdegree(2))
    G.remove_edge(1, 2)
    print("\n - Edge between 1 - 2 : ", G.exist_edge(1, 2))


def weighted_directed_graph():
    G = Graph(4)
    G.display_adj_matrix()
    print("\n - Edges count : ", G.edge_count())
    print("\n - Vertex count : ", G.vertex_count())
    G.insert_edge(0, 1, 26)
    G.insert_edge(0, 2, 16)
    G.insert_edge(1, 2, 12)
    G.insert_edge(2, 3, 8)
    G.display_adj_matrix()
    print("\n - Edges count : ", G.edge_count())
    G.edges()
    print("\n - Edge between 1 - 3 : ", G.exist_edge(1, 3))
    print("\n - Edge between 1 - 2 : ", G.exist_edge(1, 2))
    print("\n - InDegree of 2 : ", G.indegree(2))
    print("\n - OutDegree of 2 : ", G.outdegree(2))
    G.remove_edge(1, 2)
    print("\n - Edge between 1 - 2 : ", G.exist_edge(1, 2))


def breadth_first_search():
    G = Graph(7)
    G.insert_edge(0, 1)
    G.insert_edge(0, 6)
    G.insert_edge(0, 5)
    G.insert_edge(1, 0)
    G.insert_edge(1, 6)
    G.insert_edge(1, 2)
    G.insert_edge(1, 5)
    G.insert_edge(2, 6)
    G.insert_edge(2, 4)
    G.insert_edge(2, 3)
    G.insert_edge(3, 4)
    G.insert_edge(4, 2)
    G.insert_edge(4, 5)
    G.insert_edge(5, 2)
    G.insert_edge(5, 3)
    G.insert_edge(6, 3)
    G.display_adj_matrix()
    print("\n - InDegree of 5 : ", G.indegree(5))
    print("\n - OutDegree of 5 : ", G.outdegree(5))
    print("\n - BFS FROM NODE 1 : ", end=" ")
    G.bfs(1)
    print()


def depth_first_search():
    G = Graph(7)
    G.insert_edge(0, 1)
    G.insert_edge(0, 6)
    G.insert_edge(0, 5)
    G.insert_edge(1, 0)
    G.insert_edge(1, 6)
    G.insert_edge(1, 2)
    G.insert_edge(1, 5)
    G.insert_edge(2, 6)
    G.insert_edge(2, 4)
    G.insert_edge(2, 3)
    G.insert_edge(3, 4)
    G.insert_edge(4, 2)
    G.insert_edge(4, 5)
    G.insert_edge(5, 2)
    G.insert_edge(5, 3)
    G.insert_edge(6, 3)
    G.display_adj_matrix()
    print("\n - InDegree of 5 : ", G.indegree(5))
    print("\n - OutDegree of 5 : ", G.outdegree(5))
    print("\n - DFS FROM NODE 1 : ", end=" ")
    G.dfs(1)
    print()


if __name__ == '__main__':
    print("-" * 20, " UNDIRECTED GRAPH ", "-" * 20)
    undirected_graph()
    print("-" * 20, " UNDIRECTED GRAPH END ", "-" * 20)
    print("\n")

    print("-" * 20, " WEIGHTED UNDIRECTED GRAPH ", "-" * 20)
    weighted_undirected_graph()
    print("-" * 20, " WEIGHTED UNDIRECTED GRAPH END ", "-" * 20)
    print("\n")

    print("-" * 20, " DIRECTED GRAPH ", "-" * 20)
    directed_graph()
    print("-" * 20, " DIRECTED GRAPH END ", "-" * 20)
    print("\n")

    print("-" * 20, " WEIGHTED DIRECTED GRAPH ", "-" * 20)
    weighted_directed_graph()
    print("-" * 20, " WEIGHTED DIRECTED GRAPH END ", "-" * 20)
    print("\n")

    print("-" * 20, " BREADTH FIRST SEARCH ", "-" * 20)
    breadth_first_search()
    print("-" * 20, " BREADTH FIRST SEARCH END ", "-" * 20)
    print("\n")

    print("-" * 20, " DEPTH FIRST SEARCH ", "-" * 20)
    depth_first_search()
    print("-" * 20, " DEPTH FIRST SEARCH END ", "-" * 20)
    print("\n")

