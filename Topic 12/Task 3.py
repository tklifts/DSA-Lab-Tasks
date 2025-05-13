import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    # Add a vertex to the graph
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    # Add an edge to the graph with a weight
    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.adj_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adj_list:
            self.add_vertex(vertex2)
        
        self.adj_list[vertex1].append((vertex2, weight))
        self.adj_list[vertex2].append((vertex1, weight))  # For undirected graph

    # Dijkstra's algorithm to find the shortest path from the starting node
    def dijkstra(self, start):
        # Initialize distances and the priority queue
        distances = {vertex: float('inf') for vertex in self.adj_list}
        distances[start] = 0  # Distance to start node is 0
        pq = [(0, start)]  # Priority queue (min-heap), (distance, vertex)
        
        while pq:
            # Get the vertex with the smallest distance
            current_distance, current_vertex = heapq.heappop(pq)

            # If the current distance is greater than the already found distance, skip processing
            if current_distance > distances[current_vertex]:
                continue
            
            # Process each neighbor of the current vertex
            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight

                # If the newly calculated distance is shorter, update the distance and add to the queue
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances

# Test the Graph class and Dijkstra's algorithm
g = Graph()
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 1)
g.add_edge("C", "B", 2)
g.add_edge("B", "D", 1)

# Run Dijkstra's algorithm starting from node "A"
print(g.dijkstra("A"))
