'''
LRU Cache
Coding link: programiz or any compiler
Background
An LRU (Least Recently Used) Cache is a data structure that stores a fixed number of items and automatically evicts the least recently used item when it reaches capacity. Think of it like a desk with limited space — when you need to add something new but the desk is full, you remove the item you haven't touched in the longest time.
Common use cases: CPU caches, browser history, database query caching.

Problem
Design a data structure that follows the constraints of an LRU Cache.
Implement the LRUCache class:
Method
Description
LRUCache(int capacity)
Initialize the LRU cache with a positive size capacity
int get(int key)
Return the value of key if it exists, otherwise return -1
void put(int key, int value)
Insert or update key with value. If the cache is at capacity, evict the least recently used key before inserting

Both get and put must run in O(1) average time complexity.

Example
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]

Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]
Step-by-step walkthrough:
LRUCache(2)  → Initialize cache with capacity 2

put(1, 1)    → Cache: {1=1}
put(2, 2)    → Cache: {1=1, 2=2}
get(1)       → Returns 1     | Cache: {2=2, 1=1}  (1 is now most recent) <-- add to gfron and remove here
put(3, 3)    → Evicts key 2  | Cache: {1=1, 3=3}  (2 was least recently used)
get(2)       → Returns -1    (key 2 was evicted)
put(4, 4)    → Evicts key 1  | Cache: {3=3, 4=4}  (1 was least recently used)
get(1)       → Returns -1    (key 1 was evicted)
get(3)       → Returns 3
get(4)       → Returns 4

Constraints
1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
'''


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value 
        self.prev = None 
        self.next = None
        self.expiry 

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.prev = self.head

    def _add_to_the_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._add_to_the_front(node)

        node = Node(key, value)
        self.map[key]= node
        self._add_to_the_front(node)
        if len(self.map) > self.cap:
           lru = self.tail.prev
            # remove 
           self._remove(lru)
           # del
           del self.map[lru.key]

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_to_the_front(node)
        return node.val
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p


                                        ##validate addto fron here
ops = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
arguments = [[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]
cache = None
out = []
for opertation, a in zip(ops, arguments):
    if opertation == "LRUCache":
        cache = LRUCache(a[0])
        out.append(None)
    elif opertation == "put":
        # put logic
        cache.put(a[0],a[1])
        out.append(None)
    else: # get
        out.append(cache.get(a[0]))

# [null, null, null, 1, null, -1, null, -1, 3, 4]
print(out)