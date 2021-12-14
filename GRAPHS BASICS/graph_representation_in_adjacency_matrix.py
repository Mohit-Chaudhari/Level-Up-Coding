# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 14/12/21
# -----------------------------------------------

# GRAPH REPRESENTATION - ADJACENCY MATRIX

class Vertex:

    def __init__(self, node):
        self.id = node
        self.visited = False

    def set_vertex_id(self, ids):
        self.id = ids

    def get_vertex_id(self):
        return self.id

    def add_neighbour(self, neighbour):
        G.add_edge(self.id, neighbour)

    def set_visited(self):
        self.visited = True


class Graph:

    def __init__(self, num_vertices, cost=0):
        self.adj_matrix = [[-1] * num_vertices for _ in range(num_vertices)]
        self.num_vertices = num_vertices
        self.vertices = []
        for i in range(0, num_vertices):
            new_vertex = Vertex(i)
            self.vertices.append(new_vertex)

    def set_vertex(self, vtx, ids):
        if 0 <= vtx < self.num_vertices:
            self.vertices[vtx].set_vertex_id(ids)

    def get_vertex(self, n):
        for vertex_in in range(0, self.num_vertices):
            if n == self.vertices[vertex_in].get_vertex_id():
                return vertex_in
        return -1

    def add_edge(self, frm, to, cost=0):
        if self.get_vertex(frm) != -1 and self.get_vertex(to) != -1:
            self.adj_matrix[self.get_vertex(frm)][self.get_vertex(to)] = cost
            # FOR DIRECTED GRAPH - DO NOT ADD THIS
            self.adj_matrix[self.get_vertex(to)][self.get_vertex(frm)] = cost

    def print_matrix(self):
        for u in range(0, self.num_vertices):
            row = []
            for v in range(0, self.num_vertices):
                row.append(self.adj_matrix[u][v])
            print(row)

    def get_edges(self):
        edges = []
        for v in range(0, self.num_vertices):
            for u in range(0, self.num_vertices):
                if self.adj_matrix[u][v] != -1:
                    vid = self.vertices[v].get_vertex_id()
                    wid = self.vertices[u].get_vertex_id()
                    edges.append((vid, wid, self.adj_matrix[u][v]))
        return edges

    def get_vertices(self):
        vertices = []
        for vertex_in in range(0, self.num_vertices):
            vertices.append(self.vertices[vertex_in].get_vertex_id())
        return vertices


if __name__ == "__main__":
    G = Graph(6)
    G.set_vertex(0, 'a')
    G.set_vertex(1, 'b')
    G.set_vertex(2, 'c')
    G.set_vertex(3, 'd')
    G.set_vertex(4, 'e')
    G.set_vertex(5, 'f')
    print(" - Graph data : ")
    G.add_edge('a', 'e', 10)
    G.add_edge('a', 'c', 20)
    G.add_edge('c', 'b', 30)
    G.add_edge('b', 'e', 40)
    G.add_edge('e', 'd', 50)
    G.add_edge('f', 'e', 60)
    G.print_matrix()
    print(" - GET EDGES : ")
    print(G.get_edges())
    print(" - GET VERTICES : ")
    print(G.get_vertices())
