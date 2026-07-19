class Solution:
    def findLength(self, str1, k):
        window_start = 0
        max_length = 0
        char_frequency = {}

        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char not in char_frequency:
                char_frequency[right_char] = 0
                char_frequency[right_char] += 1