class Solution:
    def sort(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        return nums

def main():
    sol = Solution()
    print(sol.sort([3, 1, 5, 4, 2]))
    print(sol.sort([2, 6, 4, 3, 1, 5]))
    print(sol.sort([1, 5, 6, 4, 3, 2]))

main()