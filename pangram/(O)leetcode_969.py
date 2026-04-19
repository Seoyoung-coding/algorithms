class Solution:
    def checkIfPangram(self, sentence):
        import string

        lower_sentence = sentence.lower()

        if set(lower_sentence) == set(string.ascii_lowercase):
            return True
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    sentence1 = "TheQuickBrownFoxJumpsOverTheLazyDog"
    print(sol.checkIfPangram(sentence1))

    sentence2 = "This is not a pangram"
    print(sol.checkIfPangram(sentence2))