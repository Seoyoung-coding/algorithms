class Solution:
    def searchTriplets(self, arr):
        arr.sort()
        triplets = []
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
                continue
            self.searchPair(arr, -arr[i], i+1, triplets)

        return triplets