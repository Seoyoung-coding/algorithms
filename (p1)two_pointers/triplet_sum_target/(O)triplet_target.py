import math

class Solution:
    def searchTriplet(self, arr, target_sum):
        arr.sort()
        smallest_difference = math.inf
        for i in range(len(arr)-2):
            left = i + 1
            right = len(arr) - 1
            while (left < right):
                target_diff = target_sum - arr[i] - arr[left] - arr[right]
                if target_diff == 0:
                    return target_sum

                # the second part of the following 'if' is to handle the smallest sum when we have
                # more than one solution
                if abs(target_diff) < abs(smallest_difference) \
                        or (abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
                    smallest_difference = target_diff  # save the closest and the biggest difference

                if target_diff > 0:
                    left += 1
                else:
                    right -= 1

        return target_sum - smallest_difference


def main():
    sol = Solution()
    print(sol.searchTriplet([-1, 0, 2, 3], 2))
    print(sol.searchTriplet([-3, -1, 1, 2], 1))
    print(sol.searchTriplet([1, 0, 1, 1], 100))
    print(sol.searchTriplet([0, 0, 1, 1, 2, 6], 5))


main()

