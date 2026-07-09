class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create a dictionary to store the frequency of each character
        freq = {}

        # Traverse the string to populate the dictionary with character frequencies
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        # Traverse the string again to find the first unique character
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i

        # If no unique character is found, return -1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("apple"))  # Expected: 0
    print(sol.firstUniqChar("abcab"))  # Expected: 2
    print(sol.firstUniqChar("abab"))   # Expected: -1
