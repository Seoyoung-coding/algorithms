class Solution: # complement를 찾는 방식 (two-pointer X)
    def pair_with_targetsum(self, arr, target_sum):
        nums = {}
        for i, num in enumerate(arr):   # 배열은 정렬되어 있기 때문
            if target_sum - num in nums:
                return [nums[target_sum - num], i]
            else:
                nums[num] = i
        return [-1, -1]


def main():
    sol = Solution()
    print(sol.pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(sol.pair_with_targetsum([2, 5, 9, 11], 11))


main()