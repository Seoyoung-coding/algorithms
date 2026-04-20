class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        squares = [0] * n
        left, right = 0, n - 1
        index = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                squares[index] = nums[left] * nums[left]
                left += 1
            else:
                squares[index] = nums[right] * nums[right]
                right -= 1
            index -= 1

        return squares