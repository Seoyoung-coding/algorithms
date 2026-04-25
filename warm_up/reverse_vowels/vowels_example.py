class Solution:
    vowels = "aeiouAEIOU"

    def reverseVowels(self, s: str) -> str:
        first, last = 0, len(s) - 1
        array = list(s)

        while first < last:
            while first < last and self.vowels.find(array[first]) == -1:
                first += 1

            while first < last and self.vowels.find(array[last]) == -1:
                last -= 1

            array[first], array[last] = array[last], array[first]

            first += 1
            last -= 1

        return "".join(array)


if __name__ == "__main__":
    solution = Solution()

    s1 = "hello"
    expected_output1 = "holle"
    actual_output1 = solution.reverseVowels(s1)
    print("Test Case 1: ", expected_output1 == actual_output1)

    s2 = "DesignGUrus"
    expected_output2 = "DusUgnGires"
    actual_output2 = solution.reverseVowels(s2)
    print("Test Case 2: ", expected_output2 == actual_output2)