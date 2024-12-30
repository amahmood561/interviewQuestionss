'''
dijkstra algorithm
'''
import heapq

def dijkstra(graph, source):
    # Initialize distances dictionary with infinity for all nodes except the source
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0

    # Priority queue to track the node with the smallest distance
    priority_queue = [(0, source)]  # (distance, node)

    while priority_queue:
        # Extract the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if the current distance is greater than the already known distance
        if current_distance > distances[current_node]:
            continue

        # Update distances to neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path is found, update the distance and push to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 3)],
    'D': []
}

# Run Dijkstra's algorithm from source node 'A'
shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)
# Output: {'A': 0, 'B': 1, 'C': 3, 'D': 6}
