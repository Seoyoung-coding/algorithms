class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_map = {}
        for i in range(len(s)):
            if s[i] in freq_map:
                freq_map[s[i]] += 1
            else:
                freq_map[s[i]] = 1

            if t[i] in freq_map:
                freq_map[t[i]] -= 1
            else:
                freq_map[t[i]] = -1

        for char in freq_map:
            if freq_map[char] != 0:
                return False
        return True

sol = Solution()
if __name__ == '__main__':
    s1 = "anagram"
    t1 = "nagaram"
    print(sol.isAnagram(s1,t1))

    s2 = "rat"
    t2 = "car"
    print(sol.isAnagram(s2,t2))