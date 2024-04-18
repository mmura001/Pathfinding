import heapq
import sys

# Define the maze and weighted edges (your `maze` and `weightedList`)
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 0, 0, 0, 0]
]

# Weighted edges
edges = [[0, 1, 1], [0, 8, 0.5], [1, 2, 1], [1, 9, 0.5], [2, 3, 1], [2, 10, 0.5], [3, 4, 1], [3, 11, 0.5], [4, 5, 1], [4, 12, 0.5], [5, 6, 1], [5, 13, 4], [6, 7, 1], [6, 14, 4], [7, 15, 4], [8, 9, 1], [8, 16, 4], [9, 10, 1], [9, 17, 4], [10, 11, 1], [10, 18, 4], [11, 12, 1], [11, 19, 4], [12, 13, 4], [12, 20, 4], [13, 14, 4], [13, 21, 4], [14, 15, 4], [14, 22, 4], [15, 23, 4], [16, 17, 4], [16, 24, 0.5], [17, 18, 4], [17, 25, 0.5], [18, 19, 4], [18, 26, 0.5], [19, 20, 4], [19, 27, 0.5], [20, 21, 4], [20, 28, 0.5], [21, 22, 4], [21, 29, 0.5], [22, 23, 4], [22, 30, 0.5], [23, 31, 0.5], [24, 25, 1], [24, 32, 0.5], [25, 26, 1], [25, 33, 0.5], [26, 27, 1], [26, 34, 0.5], [27, 28, 1], [27, 35, 0.5], [28, 29, 1], [28, 36, 0.5], [29, 30, 1], [29, 37, 0.5], [30, 31, 1], [30, 38, 0.5], [31, 39, 0.5], [32, 33, 1], [32, 40, 0.5], [33, 34, 1], [33, 41, 4], [34, 35, 1], [34, 42, 4], [35, 36, 1], [35, 43, 4], [36, 37, 1], [36, 44, 4], [37, 38, 1], [37, 45, 4], [38, 39, 1], [38, 46, 4], [39, 47, 4], [40, 41, 4], [40, 48, 4], [41, 42, 4], [41, 49, 4], [42, 43, 4], [42, 50, 4], [43, 44, 4], [43, 51, 4], [44, 45, 4], [44, 52, 0.5], [45, 46, 4], [45, 53, 0.5], [46, 47, 4], [46, 54, 0.5], [47, 55, 0.5], [48, 49, 4], [49, 50, 4], [50, 51, 4], [51, 52, 1], [52, 53, 1], [53, 54, 1], [54, 55, 1]]
# Define a function to find the shortest path using Dijkstra's Algorithm

# Define a function to find the shortest path using Dijkstra's Algorithm
def dijkstra(maze, edges, start, end):
    if start < 0 or start >= len(maze) or end < 0 or end >= len(maze):
        return None  # Invalid start or end points

    # Create a dictionary to store the distances from the start node to other nodes
    distances = {node: sys.maxsize for node in range(len(maze))}

    distances[start] = 0

    # Create a dictionary to store the previous node in the shortest path
    previous_nodes = {}

    # Create a priority queue (min heap) to select nodes with the smallest distance
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we've reached the end node, reconstruct the path and return it
        if current_node == end:
            path = []
            while current_node in previous_nodes:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            path.insert(0, start)
            return path

        # If the current distance is greater than what we have in `distances`, skip
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in get_neighbors(current_node, edges):
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return None  # No path found

# Define a function to get neighbors of a node from the edges
def get_neighbors(node, edges):
    neighbors = []
    for edge in edges:
        if edge[0] == node:
            neighbors.append((edge[1], edge[2]))
        elif edge[1] == node:
            neighbors.append((edge[0], edge[2]))
    return neighbors

# Input: Start and end points
start_point = 54  # Replace with your actual start point
end_point = 5     # Replace with your actual end point

# Find the shortest path
shortest_path = dijkstra(maze, edges, start_point, end_point)

if shortest_path:
    print(f"Shortest path from {start_point} to {end_point}: {shortest_path}")
else:
    print(f"No valid path found from {start_point} to {end_point}")