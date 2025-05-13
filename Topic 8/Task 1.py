class Graph:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

        # Initialize empty adjacency list
        self.adj_list = {i: [] for i in range(num_vertices)}

        # Initialize empty adjacency matrix (2D list of 0s)
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices:
            print("Invalid vertices")
            return

        # Add edge to adjacency list
        self.adj_list[v1].append(v2)
        if not self.directed:
            self.adj_list[v2].append(v1)

        # Add edge to adjacency matrix
        self.adj_matrix[v1][v2] = 1
        if not self.directed:
            self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
        if not self.directed and v1 in self.adj_list[v2]:
            self.adj_list[v2].remove(v1)

        # Remove edge from adjacency matrix
        self.adj_matrix[v1][v2] = 0
        if not self.directed:
            self.adj_matrix[v2][v1] = 0

    def display(self):
        print("\nAdjacency List:")
        for key in self.adj_list:
            print(f"{key}: {self.adj_list[key]}")

        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(row)

# ------------------------
# ✅ Test Case Example
# ------------------------

# Undirected Graph with 5 vertices
g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

# Display both representations
g.display()

# Remove an edge and display again
print("\nRemoving edge (0, 2)...")
g.remove_edge(0, 2)
g.display()
