import heapq

def dijkstra(graph, start):
    # Initialize all distances as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to get the node with the smallest distance
    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        # Skip processing if we already have a better distance
        if current_dist > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight

            # Update the shortest distance if a new one is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# ---------- Test Case ----------
if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 1},
        'B': {'A': 4, 'C': 2, 'D': 5},
        'C': {'A': 1, 'B': 2, 'D': 8},
        'D': {'B': 5, 'C': 8}
    }

    start_node = 'A'
    result = dijkstra(graph, start_node)

    print(f"Shortest distances from {start_node}:")
    for node in sorted(result):
        print(f"  {node}: {result[node]}")
