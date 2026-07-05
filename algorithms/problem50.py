'''
Union-Find (Disjoint Set Union): Efficient data structure for connectivity and Kruskal's algorithm.

'''
class UnionFind:
    def __init__(self, size):
        # Initialize parent and rank arrays
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        # Path compression: make the found root the parent of the node
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        # Union by rank: attach smaller tree under larger tree
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

    def connected(self, node1, node2):
        # Check if two nodes are in the same component
        return self.find(node1) == self.find(node2)


# Example usage
uf = UnionFind(10)  # Create a Union-Find for 10 elements (0 to 9)

# Perform some unions
uf.union(1, 2)
uf.union(2, 3)
uf.union(4, 5)

# Check connectivity
print(uf.connected(1, 3))  # True
print(uf.connected(1, 4))  # False

# Find the root of a node
print(uf.find(3))  # 1 (or equivalent root based on path compression)
