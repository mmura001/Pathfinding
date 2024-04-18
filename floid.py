import sys

def floydWarshall(graph):
    n = len(graph)
    distance = [[sys.maxsize] * n for _ in range(n)]
    next_vertex = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                distance[i][j] = 0
            elif graph[i][j] is not None:
                distance[i][j] = graph[i][j]
                next_vertex[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    next_vertex[i][j] = next_vertex[i][k]

    # Detect negative cycles
    for i in range(n):
        if distance[i][i] < 0:
            return None, None

    return distance, next_vertex

def reconstructPath(next_vertex, start, end):
    path = []
    while start != end:
        if next_vertex[start][end] is None:
            return None
        path.append(start)
        start = next_vertex[start][end]
    path.append(end)
    return path

if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0.5, None, None, None, None],
        [0.5, 0, 1, 0.5, None, None, None, None],
        [1, 1, 0, 0.5, None, None, None, None],
        [0.5, 0.5, 0.5, 0, -1, None, None, None],
        [None, None, None, -1, 0, 1, 1, 1],
        [None, None, None, None, 1, 0, 4, None],
        [None, None, None, None, 1, 4, 0, None],
        [None, None, None, None, 1, None, None, 0]
    ]

    distances, next_vertex = floydWarshall(graph)
    start = 0  # Replace with your actual source vertex
    end = 5    # Replace with your actual destination vertex

    if distances is None:
        print("Negative cycle detected.")
    else:
        path = reconstructPath(next_vertex, start, end)
        if path is None:
            print("No path from", start, "to", end)
        else:
            print("Shortest path from", start, "to", end, ":", path)
            print("Shortest distance:", distances[start][end])
