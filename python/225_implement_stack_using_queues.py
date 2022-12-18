"""
# 225. Implement Stack using Queues

Easy

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
- `void push(int x)` Pushes element x to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns true if the stack is empty, false otherwise.

Notes:
- You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
"""

from collections import deque


class MyStack:
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def push(self, x: int) -> None:
        self.right.append(x)
        while len(self.left) > 0:
            self.right.append(self.left.popleft())

        self.left, self.right = self.right, self.left

    def pop(self) -> int:
        return self.left.popleft()

    def top(self) -> int:
        return self.left[0]

    def empty(self) -> bool:
        return len(self.left) == 0
