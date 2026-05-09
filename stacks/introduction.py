# Stack implementation using an array
class Solution:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [0] * capacity
        self.top = -1  # Stack is initially empty

    # Push operation
    def push(self, value):
        if self.top == self.capacity - 1:
            print(f"Stack Overflow! Cannot push {value}")
            return
        self.top += 1
        self.stack[self.top] = value
        print(f"{value} pushed to stack.")

    # Pop operation
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow! No elements to pop.")
            return -1  # Return -1 to indicate error
        value = self.stack[self.top]
        self.top -= 1
        return value

    # Peek operation
    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
            return -1
        return self.stack[self.top]
