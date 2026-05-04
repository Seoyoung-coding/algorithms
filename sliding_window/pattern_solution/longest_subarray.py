class Solution:
    def findLength(self, str1, k):
        window_start, max_length, max_repeat_letter_count = 0, 0, 0
        frequency_map = {}

        # Try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char not in frequency_map:
                frequency_map[right_char] = 0
            frequency_map[right_char] += 1