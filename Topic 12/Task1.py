class Graph:
    def __init__(self, directed=False):
        self.directed = directed  # Flag to determine if the graph is directed or undirected
        self.vertices = []        # List to store all vertices
        self.adj_list = {}        # Adjacency List representation
        self.adj_matrix = []      # Adjacency Matrix representation (2D list)

    # Method to add a vertex
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.adj_list[vertex] = []  # Initialize adjacency list for the vertex
            # Extend the adjacency matrix
            for row in self.adj_matrix:
                row.append(0)  # Add a new column (edge)
            self.adj_matrix.append([0] * len(self.vertices))  # Add a new row (vertex)

    # Method to add an edge between two vertices
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            print("Vertices not found in graph.")
            return
        
        # Add the edge in adjacency list
        self.adj_list[vertex1].append(vertex2)
        
        # Add the edge in adjacency matrix (directed or undirected)
        index1 = self.vertices.index(vertex1)
        index2 = self.vertices.index(vertex2)
        self.adj_matrix[index1][index2] = 1  # Set the matrix cell to 1 for an edge

        # For undirected graphs, we also need to add the reverse edge
        if not self.directed:
            self.adj_matrix[index2][index1] = 1

    # Method to display the graph using adjacency list representation
    def display_adj_list(self):
        print("Adjacency List:", self.adj_list)

    # Method to display the graph using adjacency matrix representation
    def display_adj_matrix(self):
        print("Adjacency Matrix:")
        # Print column labels
        print("  ", end="")
        for vertex in self.vertices:
            print(vertex, end=" ")
        print()
        
        # Print rows for the adjacency matrix
        for i, row in enumerate(self.adj_matrix):
            print(self.vertices[i], row)

# Test the Graph class
g = Graph(directed=False)
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")

g.display_adj_list()
g.display_adj_matrix()
