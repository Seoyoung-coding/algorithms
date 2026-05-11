class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0                    # window의 시작 위치
        window_sum = 0              # 현재 window 안의 합
        min_length = float('inf')   # 최소 길이 저장 (처음엔 무한대)

        # right를 한 칸씩 늘려가며 window 확장
        for right in range(len(nums)):

            # 새 숫자를 window에 추가
            window_sum += nums[right]

            # 합이 target 이상이면
            while window_sum >= target:

                # 현재 길이 계산
                current_length = right - left + 1

                # 최소 길이 갱신
                min_length = min(min_length, current_length)

                # 왼쪽 값 제거하면서 window 줄이기
                window_sum -= nums[left]

                # left 한 칸 이동
                left += 1

        # 끝까지 갔는데 못 찾았으면 0 반환
        if min_length == float('inf'):
            return 0

        return min_length