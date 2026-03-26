class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()

        for x in nums:
            if x in unique_set:
                return True
            unique_set.add(x)
        return False

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1,2,3,1]
    print(sol.containsDuplicate(nums1))

    nums2 = [1,2,3,4]
    print(sol.containsDuplicate(nums2))

    nums3 = [1,1,1,3,3,4,3,2,4,2]
    print(sol.containsDuplicate(nums3))