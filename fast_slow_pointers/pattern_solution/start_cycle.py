class Solution:
    def findCycleStart(self, head):
        cycle_length = 0

        slow, fast = head, head
        while (fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                cycle_length = self.calculate_cycle_length(slow)
                break

        return self.find_start(head, cycle_length)

    def calculate_cycle_length(self, slow):
        current = slow
        cycle_length = 0

        while True:
            current = current.next
            cycle_length += 1
            if current == slow:
                break

        return cycle_length

    def find_start(self, head, cycle_length):
        pointer1 = head
        pointer2 = head

        while cycle_length > 0:
            pointer2 = pointer2.next
            cycle_length -= 1

        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1

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
