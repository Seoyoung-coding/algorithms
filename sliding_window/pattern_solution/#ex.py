class Solution:
    def max_sub_array_of_size_k(self, k, arr):
        max_sum = 0  # Initialize the maximum sum.
        window_sum = 0  # Initialize the current window sum.

        for i in range(len(arr) - k + 1):
            window_sum = 0  # Reset the window sum for each new window.
            for j in range(i, i+k):
                window_sum += arr[j]  # Calculate the sum of the current window.
            max_sum = max(max_sum, window_sum)  # Update the maximum sum.
        return max_sum


def main():
    sol = Solution()
    print("Maximum sum of a subarray of size K: " +
          str(sol.max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(sol.max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
