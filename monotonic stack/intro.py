#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
    def removeNodes(self, head):
        stack = []  # Create an empty stack to store nodes in descending order

        cur = head
        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()  # Remove nodes from the stack that are smaller than the current node
            if stack:
                stack[-1].next = cur  # Update the next pointer of the top node in the stack
            stack.append(cur)  # Push the current node onto the stack
            cur = cur.next

        return stack[0] if stack else None  # Return the head of the modified list, or None if the stack is empty

# Testing the solution
solution = Solution()

# Creating the linked list 5 -> 3 -> 7 -> 4 -> 2 -> 1
head1 = Node(5)
head1.next = Node(3)
head1.next.next = Node(7)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(2)
head1.next.next.next.next.next = Node(1)
head1 = solution.removeNodes(head1)

# Printing the modified list: 7 -> 4 -> 2 -> 1
node = head1
while node:
    print(node.val, end=" -> " if node.next else "\n")
    node = node.next
