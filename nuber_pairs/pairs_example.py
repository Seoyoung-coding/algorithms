class Solution:
    def numGoodPairs(self, nums):
        pairCount = 0
        map = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1
            pairCount += map[n] - 1
        return pairCount

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2, 3, 1, 1, 3]
    result1 = sol.numGoodPairs(nums1)
    print("Result 1:", result1, "(Expected: 4)")
