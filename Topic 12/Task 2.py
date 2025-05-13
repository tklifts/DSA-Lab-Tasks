from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}  # Adjacency list to store graph

    # Method to add a vertex
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    # Method to add an edge
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adj_list:
            self.add_vertex(vertex2)
        
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)  # For undirected graph

    # Method for BFS traversal
    def bfs(self, start):
        visited = set()          # Set to track visited nodes
        queue = deque([start])   # Queue to manage the nodes for BFS
        result = []              # To store the traversal result

        visited.add(start)

        while queue:
            node = queue.popleft()  # Dequeue the front element
            result.append(node)

            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)  # Enqueue neighbors
        
        return result

    # Method for DFS traversal (using recursion)
    def dfs_recursive(self, start):
        visited = set()         # Set to track visited nodes
        result = []             # To store the traversal result
        self._dfs_recursive_helper(start, visited, result)
        return result

    def _dfs_recursive_helper(self, node, visited, result):
        visited.add(node)      # Mark the node as visited
        result.append(node)    # Add to result

        for neighbor in self.adj_list[node]:
            if neighbor not in visited:
                self._dfs_recursive_helper(neighbor, visited, result)

    # Method for DFS traversal (using stack)
    def dfs_stack(self, start):
        visited = set()         # Set to track visited nodes
        stack = [start]         # Stack to manage the nodes for DFS
        result = []             # To store the traversal result

        while stack:
            node = stack.pop()  # Pop the top element from the stack
            if node not in visited:
                visited.add(node)
                result.append(node)

                # Add all unvisited neighbors to the stack
                for neighbor in reversed(self.adj_list[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result


# Test the Graph class and traversal algorithms
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

# BFS Traversal starting from node 0
print("BFS Traversal:", g.bfs(0))  # Output: [0, 1, 2, 3]

# DFS Traversal (using recursion) starting from node 0
print("DFS Traversal (Recursive):", g.dfs_recursive(0))  # Output: [0, 1, 3, 2]

# DFS Traversal (using stack) starting from node 0
print("DFS Traversal (Stack):", g.dfs_stack(0))  # Output: [0, 2, 3, 1]
