def transitive_closure(adj):
    n = len(adj)
    M = [[0]*n for _ in range(n)]

    def dfs(src):
        stack = [src]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if M[src][v] == 0:
                    M[src][v] = 1
                    stack.append(v)

    for i in range(n):
        M[i][i] = 1          # a node reaches itself
        dfs(i)
    return M

# Example
graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]

for row in transitive_closure(graph):
    print(row)



## dfs questiuobns 