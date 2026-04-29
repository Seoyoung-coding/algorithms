# class Node:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def findCycleStart(self, head):
        if head is None:
            return None

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if fast is None or fast.next is None:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

def main():
    sol = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

main()