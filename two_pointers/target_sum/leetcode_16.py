class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums)):
            left, right = i + 1 , len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if abs(target - s) < abs(target - closest): # closest는 지금까지 찾은 값중 가장 가까운 합
                    closest = s

                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return s

        return closest