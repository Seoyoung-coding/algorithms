# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        # while문이 끝났다는건 끝(None)에 도달했다는 뜻 = 사이클 없음
        return False