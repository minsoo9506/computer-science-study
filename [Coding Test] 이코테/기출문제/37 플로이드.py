for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            adj[a][b] = min(adj[a][b], adj[a][k] + adj[k][b])