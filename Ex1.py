from collections import deque
import sys

def bfs(grid, start, n):
    dist = [[sys.maxsize] * n for _ in range(n)]
    q = deque()
    x, y = start
    dist[x][y] = 0
    q.append((x, y))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

def find_best_meeting_point(grid, robot_positions):
    n = len(grid)
    total_dist = [[0]*n for _ in range(n)]
    count_reached = [[0]*n for _ in range(n)]

    for robot in robot_positions:
        dist = bfs(grid, robot, n)
        for i in range(n):
            for j in range(n):
                if dist[i][j] != sys.maxsize:
                    total_dist[i][j] += dist[i][j]
                    count_reached[i][j] += 1

    min_total = sys.maxsize
    best_cell = (-1, -1)
    for i in range(n):
        for j in range(n):
            if count_reached[i][j] == len(robot_positions):
                if total_dist[i][j] < min_total:
                    min_total = total_dist[i][j]
                    best_cell = (i, j)

    return best_cell, min_total


grid = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1]
]

robots = [(0,0), (1,6), (4,1)]
meeting_point, steps = find_best_meeting_point(grid, robots)
print("Best meeting point:", meeting_point)
print("Minimal total steps:", steps)