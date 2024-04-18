# import heapq

# def find_path_with_distance(maze, start, end):
#     def get_neighbours(cell):
#         x, y = cell
#         neighbours = []

#         # Check each direction
#         if x > 0:  # check top
#             neighbours.append((x - 1, y))
#         if x < len(maze) - 1:  # check bottom
#             neighbours.append((x + 1, y))
#         if y > 0:  # check left
#             neighbours.append((x, y - 1))
#         if y < len(maze[0]) - 1:  # check right
#             neighbours.append((x, y + 1))

#         return [(x, y) for x, y in neighbours]

#     def heuristic(cell, goal):
#         x1, y1 = cell
#         x2, y2 = goal
#         return abs(x1 - x2) + abs(y1 - y2)

#     def cost_to_cell(current, cell):
#         return maze[cell[0]][cell[1]]

#     def reconstruct_path(came_from, current):
#         path = []
#         while current in came_from:
#             path.append(current)
#             current = came_from[current]
#         path.reverse()
#         return path

#     queue = [(0, start)]
#     came_from = {}
#     cost_so_far = {start: 0}

#     while queue:
#         _, current = heapq.heappop(queue)

#         if current == end:
#             path = reconstruct_path(came_from, current)
#             distance = cost_so_far[current]
#             return path, distance

#         for neighbour in get_neighbours(current):
#             new_cost = cost_so_far[current] + cost_to_cell(current, neighbour)
#             if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
#                 cost_so_far[neighbour] = new_cost
#                 priority = new_cost + heuristic(neighbour, end)
#                 heapq.heappush(queue, (priority, neighbour))
#                 came_from[neighbour] = current

#     return None, float('inf')

# # Example usage:
# maze = [[1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 1, 0, 1, 0, 0]]
# start = (7, 7)
# end = (0, 0)

# path, distance = find_path_with_distance(maze, start, end)
# print("Path:", path)
# print("Distance:", distance)

import heapq

maze = [[1, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0],
 [1, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 1],
 [1, 0, 0, 1, 0, 1, 0, 0]]


start = (7, 7)
end = (0, 0) 

def get_neighbours(maze, cell):
    x, y = cell
    neighbours = []

    # Check each direction
    if x > 0:  # check top
        neighbours.append((x - 1, y))
    if x < len(maze) - 1:  # check bottom
        neighbours.append((x + 1, y))
    if y > 0:  # check left
        neighbours.append((x, y - 1))
    if y < len(maze[0]) - 1:  # check right
        neighbours.append((x, y + 1))

    return [(x, y) for x, y in neighbours]

def heuristic(cell, goal):
    x1, y1 = cell
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def cost_to_cell(maze, current, cell):
    return maze[cell[0]][cell[1]]

def find_path(maze, start, end):
    queue = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while queue:
        _, current = heapq.heappop(queue)

        if current == end:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbour in get_neighbours(maze, current):
            new_cost = cost_so_far[current] + cost_to_cell(maze, current, neighbour)
            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                priority = new_cost + heuristic(neighbour, end)
                heapq.heappush(queue, (priority, neighbour))
                came_from[neighbour] = current

    return None

# Define functions to count the number of 0s and 1s in a path
def count_zeros(path):
    return sum(1 for cell in path if maze[cell[0]][cell[1]] == 0)

def count_ones(path):
    return sum(1 for cell in path if maze[cell[0]][cell[1]] == 1)

# Find paths considering 0s and 1s
shortest_path = find_path(maze, start, end)
shortest_path_with_ones = find_path(maze, start, end)
while shortest_path_with_ones and count_ones(shortest_path_with_ones) < 2:
    shortest_path_with_ones = find_path(maze, start, end)

# Choose the path based on your criteria
if shortest_path and (not shortest_path_with_ones or count_zeros(shortest_path) <= count_ones(shortest_path_with_ones)):
    print("Shortest path using 0s:", shortest_path)
else:
    print("Path with minimal 1s:", shortest_path_with_ones)
