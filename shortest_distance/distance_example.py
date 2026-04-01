import math

class Solution:
    def shortestDistance(selfself, words, word1, word2):
        shortestDistance = len(words)
        position1, position2 = -1, -1

        for i, word in enumerate(words):
            if word == word1:
                position1 = i
            elif word == word2:
                position2 = i

            if position1 != -1 and position2 != -1:
                shortestDistance = min(shortestDistance, abs(position1 - position2))

        return shortestDistance

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    words1 = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    word11 = "fox"
    word21 = "dog"
    expected_output1 = 5
    actual_output1 = solution.shortestDistance(words1, word11, word21)
    print("Test case 1:", expected_output1 == actual_output1)

    # Test case 2
    words2 = ["a", "b", "c", "d", "a", "b"]
    word12 = "a"
    word22 = "b"
    expected_output2 = 1
    actual_output2 = solution.shortestDistance(words2, word12, word22)
    print("Test case 2:", expected_output2 == actual_output2)

    # Test case 3
    words3 = ["a", "c", "d", "b", "a"]
    word13 = "a"
    word23 = "b"
    expected_output3 = 1
    actual_output3 = solution.shortestDistance(words3, word13, word23)
    print("Test case 3:", expected_output3 == actual_output3)

    # Test case 4
    words4 = ["a", "b", "c", "d", "e"]
    word14 = "a"
    word24 = "e"
    expected_output4 = 4
    actual_output4 = solution.shortestDistance(words4, word14, word24)
    print("Test case 4:", expected_output4 == actual_output4)
