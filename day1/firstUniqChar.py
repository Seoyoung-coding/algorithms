class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        for i, c in enumerate(s):
            if freq[c] == 1:
                return i

        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("apple"))  # Expected: 0
    print(sol.firstUniqChar("abcab"))  # Expected: 2
    print(sol.firstUniqChar("abab"))   # Expected: -1
