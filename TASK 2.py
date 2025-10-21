from sys import maxsize

def travellingSalesmanDP(graph):
    V = len(graph)
    dp = [[maxsize] * V for _ in range(1 << V)]
    
    # Starting point: only at node 0 with cost 0
    dp[1][0] = 0

    for mask in range(1 << V):
        for u in range(V):
            if not (mask & (1 << u)):
                continue
            for v in range(V):
                if mask & (1 << v) or u == v:
                    continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + graph[u][v])

    # Close the tour by returning to starting node (0)
    min_cost = maxsize
    for i in range(1, V):
        if graph[i][0] != 0:
            min_cost = min(min_cost, dp[(1 << V) - 1][i] + graph[i][0])
    
    return min_cost

if __name__ == "__main__":
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]
    
    print("Minimum cost of TSP:", travellingSalesmanDP(graph))
