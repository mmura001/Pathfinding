import sys
from enum import Enum, IntEnum

class Cell(IntEnum):
    EMPTY = 0  # indicates empty cell where the agent can move to
    ANTIJAMMED = 3
    OCCUPIED = 1  # indicates cell which contains a wall and cannot be entered
    CURRENT = 2 

maze = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
]

def findNegativeCycles(edges, n):
    # Initialize the distance and parent arrays
    distance = [sys.maxsize] * n
    parent = [-1] * n

    # Initially, all vertices have weight 0
    start_vertex = 0
    distance[start_vertex] = 0

    # Relaxation step (run V-1 times)
    for k in range(n - 1):
        for (u, v, w) in edges:
            if distance[u] != sys.maxsize and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u

    # Run one more iteration to check for negative-weight cycles
    negative_cycle = None
    for (u, v, w) in edges:
        if distance[u] != sys.maxsize and distance[u] + w < distance[v]:
            # Negative cycle found
            negative_cycle = getPath(parent, u)
            break

    return negative_cycle

def WeghtList(maze):
    a = len(maze)
    b = len(maze[0])

    list_1 = []
    x = 0

    for i in range(0, a):
        for j in range(0, b):
            if j + 1 < b:
                # if maze[i][j+1] == Cell.OCCUPIED or maze[i][j+1] == Cell.OCCUPIED_1:
                if maze[i][j + 1] == Cell.OCCUPIED:

                    list_1.append([x, x + 1, (maze[i][j + 1] + 2)])
                elif maze[i][j+1] == Cell.ANTIJAMMED:
                    list_1.append([x, x + 1, (maze[i][j + 1] - 1.5)])
                else:
                    list_1.append([x, x + 1, (maze[i][j + 1] + 0.5)])
            if i + 1 < a:
                # if maze[i + 1][j] == Cell.OCCUPIED or maze[i + 1][j] == Cell.OCCUPIED_1:
                if maze[i + 1][j] == Cell.OCCUPIED:

                    list_1.append([x, x + b, (maze[i + 1][j])])
                elif maze[i + 1][j] == Cell.ANTIJAMMED:
                    list_1.append([x, x + b, (maze[i + 1][j] - 3.5)])
                else:
                    list_1.append([x, x + b, (maze[i + 1][j] + 0.5)])
            x = x + 1

    return list_1


weightedList = WeghtList(maze)



def getPath(parent, vertex):
    if vertex < 0:
        return []
    return getPath(parent, parent[vertex]) + [vertex]


# Function to run the Bellman–Ford algorithm from a given source
def bellmanFord(edges, source, destination, n):
    # distance[] and parent[] stores the shortest path (least cost/path) info
    distance = [sys.maxsize] * n
    parent = [-1] * n

    # Initially, all vertices except source vertex weight INFINITY and no parent
    distance[source] = 0

    # relaxation step (run V-1 times)
    for k in range(n - 1):
        # edge from `u` to `v` having weight `w`
        for (u, v, w) in edges:
            # if the distance to destination `v` can be shortened by taking edge (u, v)
            if distance[u] != sys.maxsize and distance[u] + w < distance[v]:
                # update distance to the new lower value
                distance[v] = distance[u] + w
                # set v's parent as `u`
                parent[v] = u

    # run relaxation step once more for n'th time to check for negative-weight cycles
    for (u, v, w) in edges:  # edge from `u` to `v` having weight `w`
        # if the distance to destination `u` can be shortened by taking edge (u, v)
        if distance[u] != sys.maxsize and distance[u] + w < distance[v]:
            print('Negative-weight cycle is found!!')
            return

    # for i in range(n):
    #     if i != source and distance[i] < sys.maxsize:
    #         print(f'The distance of vertex {i} from vertex {source} is {distance[i]}. '
    #               f'Its path is', getPath(parent, i))

    path = getPath(parent,destination)
    if destination != source and distance[destination] < sys.maxsize:
     print(f'The distance of vertex {destination} from vertex {source} is {distance[destination]}. '
           f'Its path is', getPath(parent, destination))


    return path , distance[destination]


if __name__ == '__main__':

   
    # set the maximum number of nodes in the graph
    n = 729


    edges = weightedList
    print("gfhjfhgn",edges)

    negative_cycle = findNegativeCycles(edges, n)
    if negative_cycle:
        print("Negative cycle found:", negative_cycle)
    else:
        print("No negative cycle found.")



    # run the Bellman–Ford algorithm from every node
    # for source in range(n):



    source = int(input("Enter source: "))
    destination = int(input("Enter destination: "))
    path, dist = bellmanFord(edges,source,destination, n)
    print("path1 dist1", path, dist)
    if dist == 9223372036854775807:
        path, dist = bellmanFord(edges,destination,source, n)
        print("path2 dist2", path, dist)
    