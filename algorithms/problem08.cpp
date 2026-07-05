/**
This problem can be solved using a graph traversal 
algorithm such as breadth-first search (BFS) or depth-first search (DFS). 
The infinite coordinate grid can be represented as a graph, with cells as nodes 
and edges connecting neighboring cells.
This code will start from the cell (1000, 1000) and use the
BFS algorithm to visit all the accessible cells, 
and it will return the number of cells ant can visit.
Note that this solution is not optimal due to the usage
of the infinite grid, it can cause a large amount of
 memory, also the solution is a bit slow.
*/

#include <iostream>
#include <queue>
#include <unordered_set>
using namespace std;

const int dx[] = {0, 0, 1, -1}; // possible moves in x direction
const int dy[] = {1, -1, 0, 0}; // possible moves in y direction

bool isAccessible(int x, int y) {
    int sum = 0;
    while (x > 0) {
        sum += x % 10;
        x /= 10;
    }
    while (y > 0) {
        sum += y % 10;
        y /= 10;
    }
    return sum <= 25;
}

int BFS(int startX, int startY) {
    queue<pair<int, int>> q;
    unordered_set<int> visited;
    q.push({startX, startY});
    visited.insert(startX * 1000 + startY);
    int count = 1;
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();
        for (int i = 0; i < 4; i++) {
            int newX = x + dx[i];
            int newY = y + dy[i];
            if (isAccessible(newX, newY) && visited.find(newX * 1000 + newY) == visited.end()) {
                q.push({newX, newY});
                visited.insert(newX * 1000 + newY);
                count++;
            }
        }
    }
    return count;
}

int main() {
    int startX = 1000, startY = 1000;
    cout << "Number of cells visited: " << BFS(startX, startY) << endl;
    return 0;
}



/*
there are several ways to optimize this solution.

Pruning: Instead of checking all the cells, you can use a heuristic to prune the search tree and avoid visiting cells that are not likely to contain a solution. For example, you can use a function that calculates the sum of the digits in the x and y coordinates and prune any cells that have a sum greater than 25.

Memoization: You can use memoization to keep track of the cells that have been visited and avoid revisiting them. This can be done by using a hash table to store the coordinates of the visited cells, where the key is the concatenation of the x and y coordinates and the value is a Boolean indicating whether the cell has been visited.

Bounded search space: Instead of searching the entire infinite grid, you can limit the search space to a specific region around the starting cell. For example, you can define a bounding box around the starting cell, such that all cells outside of the bounding box are not searched.

Using Iterative deepening DFS, so it will not cause a large amount of memory, it can stop searching when the depth that it's at has reached the bounding box or the number of cells, the ant can visit

Here is an example of how you might implement the optimized DFS algorithm using these techniques in C++:
#include <iostream>
#include <unordered_set>
#include <algorithm>
using namespace std;

bool isAccessible(int x, int y, int depth) {
    if( depth>25 ) return false;
    int sum = 0;
    while (x > 0) {
        sum += x % 10;
        x /= 10;
    }
    while (y > 0) {
        sum += y % 10;
        y /= 10;
    }
    return sum <= 25;
}

int DFS(int x, int y, int depth, unordered_set<int> &visited, int boundX, int boundY, int &count) {
    if (x<0 || x> boundX || y < 0 || y> boundY) return count;
    int hash = (1e6 * x + y);
    if (visited.find(hash) != visited.end()) return count;
    visited.insert(hash);
    if( isAccessible(x,y,depth) ) {
        count++;
        DFS(x - 1, y, depth+1, visited, boundX, boundY, count);
        DFS(x + 1, y, depth+1, visited, boundX, boundY, count);
        DFS(x, y - 1, depth+1, visited, boundX, boundY, count);
        DFS(x, y + 1, depth+1, visited, boundX, boundY, count);
    }
    return count;
}

int IDDFS(int startX, int startY, int boundX, int boundY) {
    int depth = 0;
    int count = 0;
    while(true) {
        unordered_set<int> visited;
        int result = DFS(startX, startY, depth, visited, boundX, boundY, count);
        if(result > 0 || depth > 25) break;
        depth++;
    }
    return count;

*/
