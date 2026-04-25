class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left , right = 0 , n - 1
        index = n - 1
        square = [0] * n

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                square[index] = nums[left] * nums[left]
                left += 1

            else:
                square[index] = nums[right] * nums[right]
                right -= 1
            index -= 1

        return square

def main():
    sol = Solution()
    nums1 = [-4, -1, 0, 3, 10]
    print(sol.sortedSquares(nums1))