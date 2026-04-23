class Solution:
    def searchTriplets(self, arr):
        triplets = []
        arr.sort()

        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue # 같은 값이면 넘어감
            self.searchPair(arr, -arr[i], i+1, triplets) # 현재 숫자 arr[i]를 기준으로 나머지 두 수의 합이 -arr[i] 가 되도록 찾는다

        return triplets


# 아래부터는 고정된것 외 2개의 수를 찾는 함수 시작
def searchPair(self, arr, target_sum, left, triplets):
    right = len(arr) - 1

    while(left < right):  # 두 포인터가 만날 때까지 반복
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]]) # 세 숫자 합이 0이 되는 조합 저장 후 이동
            left += 1
            right -= 1

            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif target_sum > current_sum:
            left += 1

        else:
            right -= 1