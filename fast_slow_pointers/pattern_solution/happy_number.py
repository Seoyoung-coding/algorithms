class Solution:
    def find(self, num):
        slow, fast = num, num
        while True:
            slow = self.find_square_sum(slow)
            fast = self.find_square_sum(self.find_square_sum(fast))
            if slow == fast:
                break
        return slow == 1