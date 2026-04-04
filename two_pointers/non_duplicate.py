class Solution:
    def remove(self, arr, key):
        nextElement = 0

        for i in range(len(arr)):
            if arr[i] != key:
                arr[nextElement] = arr[i]
                nextElement += 1

        return nextElement


def main():
    sol = Solution()

    # Test case 1
    print("Array new length: " + str(sol.remove([3, 2, 3, 6, 3, 10, 9, 3], 3)))

main()
