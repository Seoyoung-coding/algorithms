class Solution:
    def findAverages(self, K, arr):
        result = []
        for i in range(len(arr)-K+1):

            _sum = 0.0
            for j in range(i, i+K):
                _sum += arr[j]
            result.append(_sum/K) # calculate average

        return result

def main():
    sol = Solution()
    result = sol.findAverages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))

main()