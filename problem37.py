'''

 Amazon.

Implement a stack API using only a heap. A stack implements the following methods:

push(item), which adds an element to the stack
pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
Recall that a heap has the following operations:

push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap
'''

import heapq

class HeapStackEmptyError(Exception):
    """Custom exception to indicate that the stack is empty."""
    pass

class HeapStack:
    def __init__(self):
        """
        Initialize the HeapStack with an empty heap and a counter.
        """
        self.heap = []
        self.counter = 0  # To keep track of the insertion order

    def push(self, item):
        """
        Push an item onto the stack.

        :param item: The item to be pushed onto the stack.
        """
        # Invert the counter to simulate a max-heap using Python's min-heap
        heapq.heappush(self.heap, (-self.counter, item))
        print(f"Pushed: {item} with counter: {self.counter}")
        self.counter += 1

    def pop(self):
        """
        Pop the most recently added item from the stack.

        :return: The most recently added item.
        :raises HeapStackEmptyError: If the stack is empty.
        """
        if not self.heap:
            raise HeapStackEmptyError("Pop from an empty stack")

        # Pop the item with the highest counter (i.e., most recently added)
        counter, item = heapq.heappop(self.heap)
        print(f"Popped: {item} with counter: {-counter}")
        return item

    def is_empty(self):
        """
        Check if the stack is empty.

        :return: True if the stack is empty, False otherwise.
        """
        return len(self.heap) == 0

    def __len__(self):
        """
        Get the number of items in the stack.

        :return: The number of items in the stack.
        """
        return len(self.heap)

    def peek(self):
        """
        Peek at the most recently added item without removing it.

        :return: The most recently added item.
        :raises HeapStackEmptyError: If the stack is empty.
        """
        if not self.heap:
            raise HeapStackEmptyError("Peek from an empty stack")
        return self.heap[0][1]


def main():
    stack = HeapStack()

    # Push items onto the stack
    stack.push('apple')
    stack.push('banana')
    stack.push('cherry')

    # Peek at the top item
    try:
        top_item = stack.peek()
        print(f"Top item: {top_item}")
    except HeapStackEmptyError as e:
        print(e)

    # Pop items from the stack
    try:
        while not stack.is_empty():
            item = stack.pop()
            print(f"Removed item: {item}")
    except HeapStackEmptyError as e:
        print(e)

    # Attempt to pop from an empty stack
    try:
        stack.pop()
    except HeapStackEmptyError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
