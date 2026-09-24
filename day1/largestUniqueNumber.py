from collections import defaultdict
from typing import List

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        freq = defaultdict(int)

        for num in A:
            freq[num] += 1

        maxUnique = -1
        for key, value in freq.items():
            if value == 1:
                maxUnique = max(maxUnique, key)

        return maxUnique

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestUniqueNumber([5, 7, 3, 7, 5, 8]))  # Expected: 8
    print(sol.largestUniqueNumber([1, 2, 3, 2, 1, 4, 4]))  # Expected: 3
    print(sol.largestUniqueNumber([9, 9, 8, 8, 7, 7]))   # Expected: -1
