class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        first, last = 0, len(s) - 1
        array = list(s)

        while first < last:
            while first < last and vowels.find(array[first]) == -1:
                first += 1

            while first < last and vowels.find(array[last]) == -1:
                last -= 1

            array[first], array[last] = array[last], array[first]
            first += 1
            last -= 1

        return "".join(array)


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseVowels("IceCreAm"))
    print(sol.reverseVowels("leetcode"))