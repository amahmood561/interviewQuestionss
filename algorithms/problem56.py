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

def transitive_closure(adj):
    """
    Compute the transitive closure of a directed graph.
    
    adj: adjacency list representation of the graph.
         Example: adj[0] = [0, 1, 3] means there are edges from 0→0, 0→1, and 0→3.
         
    Returns: a matrix M (list of lists),
             where M[i][j] = 1 if there is a path from i to j, else 0.
    """
    
    n = len(adj)                       # number of vertices
    M = [[0] * n for _ in range(n)]    # initialize matrix with all 0s

    def dfs(src):
        """
        Explore all vertices reachable from 'src'
        and mark them in the matrix M.
        """
        stack = [src]                  # we use a stack for DFS
        while stack:
            u = stack.pop()            # take the last vertex added
            for v in adj[u]:           # check all neighbors of u
                # If src can reach v and we haven't marked it yet:
                if M[src][v] == 0:
                    M[src][v] = 1      # mark reachable
                    stack.append(v)    # continue exploring from v

    # Run DFS starting from every vertex
    for i in range(n):
        M[i][i] = 1   # every node is trivially reachable from itself
        dfs(i)        # explore all nodes reachable from i

    return M


# Example usage:
graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]

result = transitive_closure(graph)
for row in result:
    print(row)
