from collections import defaultdict, deque

def bfs(graph, start, n):
    visited = [False] * n
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
    return visited

def is_strongly_connected(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = bfs(graph, 0, n)
    if not all(visited):
        return False
    transpose = defaultdict(list)
    for u, v in edges:
        transpose[v].append(u)

    visited_transpose = bfs(transpose, 0, n)
    return all(visited_transpose)

n = 4
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
print("Strongly connected?", is_strongly_connected(n, edges))