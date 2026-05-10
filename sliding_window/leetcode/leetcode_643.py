class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # 처음 k개의 합을 먼저 구한다
        window_sum = sum(nums[:k])

        # 현재 최대 합도 처음 window 값으로 시작
        max_sum = window_sum

        # k번째 인덱스부터 끝까지 이동
        for right in range(k, len(nums)):

            # 새로 들어오는 값 추가
            window_sum += nums[right]

            # window에서 빠지는 값 제거
            window_sum -= nums[right - k]

            # 최대 합 갱신
            max_sum = max(max_sum, window_sum)

        # 평균 반환
        return max_sum / k