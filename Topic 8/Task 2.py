from collections import deque

class Graph:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.adj_list = {i: [] for i in range(num_vertices)}

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        if not self.directed:
            self.adj_list[v2].append(v1)

    def bfs(self, start):
        visited = [False] * self.num_vertices
        queue = deque([start])
        visited[start] = True
        traversal = []

        while queue:
            node = queue.popleft()
            traversal.append(node)

            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return traversal

    def dfs(self, start):
        visited = [False] * self.num_vertices
        traversal = []

        def dfs_recursive(node):
            visited[node] = True
            traversal.append(node)

            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return traversal

    def display(self):
        print("\nAdjacency List:")
        for key in self.adj_list:
            print(f"{key}: {self.adj_list[key]}")
