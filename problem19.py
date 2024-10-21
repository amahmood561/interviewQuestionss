'''

Microsoft.

The transitive closure of a graph is a measure of which vertices are reachable from other vertices. It can be represented as a matrix M, where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.

For example, suppose we are given the following graph in adjacency list form:

graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
The transitive closure of this graph would be:

[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
Given a graph, find its transitive closure.



'''
def floyd_warshall_transitive_closure(graph):
    """
    Computes the transitive closure of a directed graph using the Floyd-Warshall algorithm.

    Parameters:
    graph (List[List[int]]): Adjacency list representation of the graph where graph[i] contains
                             all vertices that are directly reachable from vertex i.

    Returns:
    List[List[int]]: A matrix representing the transitive closure of the graph where closure[i][j] == 1
                     if vertex j is reachable from vertex i, otherwise 0.
    """
    
    # Determine the number of vertices in the graph
    N = len(graph)
    
    # Initialize the reachability matrix with all entries set to 0
    # closure[i][j] will be 1 if there is a path from vertex i to vertex j
    closure = [[0 for _ in range(N)] for _ in range(N)]
    
    # Populate the initial reachability based on direct edges
    for i in range(N):
        # Iterate through all vertices directly reachable from vertex i
        for j in graph[i]:
            closure[i][j] = 1  # Mark as reachable
        
        closure[i][i] = 1  # Every vertex is reachable from itself
    
    # Apply the Floyd-Warshall algorithm to compute transitive closure
    # Consider each vertex as an intermediate point in potential paths
    for k in range(N):
        # For each possible intermediate vertex k
        for i in range(N):
            # For each source vertex i
            for j in range(N):
                # For each destination vertex j
                if closure[i][k] and closure[k][j]:
                    # If vertex k is reachable from i and j is reachable from k,
                    # then j is reachable from i via k
                    closure[i][j] = 1  # Update reachability
    
    # Return the final reachability matrix representing the transitive closure
    return closure

# Example Usage
if __name__ == "__main__":
    # Define the graph as an adjacency list
    # Each sublist represents the vertices reachable directly from the vertex at that index
    graph = [
        [0, 1, 3],  # Vertex 0 is connected to itself, 1, and 3
        [1, 2],     # Vertex 1 is connected to itself and 2
        [2],        # Vertex 2 is connected to itself
        [3]         # Vertex 3 is connected to itself
    ]
    
    # Compute the transitive closure of the graph
    closure = floyd_warshall_transitive_closure(graph)
    
    # Print the transitive closure matrix
    print("Transitive Closure Matrix:")
    for row in closure:
        print(row)

'''
[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
'''

'''

The Floyd-Warshall algorithmmm is a dynamic programming approach that efficiently computes the shortest paths between all pairs of vertices.

It can be adapted to compute the transitive closure by simply tracking reachability instead of path lengths.

Algorithm Steps:
Initialize the Reachability Matrix:

Create an N x N matrix M where M[i][j] = 1 if there is a direct edge from vertex i to vertex j, otherwise 0.
Set M[i][i] = 1 for all vertices i since every vertex is reachable from itself.
Update the Matrix:

For each intermediate vertex k from 0 to N-1:
For each pair of vertices (i, j):
If M[i][k] and M[k][j] are both 1, set M[i][j] = 1.
Time Complexity:
O(N³), where N is the number of vertices.



'''