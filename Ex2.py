from collections import deque

def bfs_farthest_node(adj, start):
    n = len(adj)
    dist = [-1] * n
    q = deque([start])
    dist[start] = 0
    farthest_node = start

    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                if dist[v] > dist[farthest_node]:
                    farthest_node = v

    return farthest_node, dist[farthest_node]

def tree_diameter(adj):
    x, _ = bfs_farthest_node(adj, 0) # BFS to find the farthest node x
    y, diameter = bfs_farthest_node(adj, x) # BFS from x to find diameter
    return diameter

adjacency_list = [
    [1],
    [0, 2, 3],
    [1],
    [1, 4],
    [3]
]

print("Tree diameter:", tree_diameter(adjacency_list))