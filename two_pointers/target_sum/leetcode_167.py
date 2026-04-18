class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left , right = 0, len(numbers) - 1

        while left < right:
            current_sum = int(numbers[left] + numbers[right])   # while 안에서 계산해야 하는 이유는 left, right이 계속 바뀌어서 계속 새로운 계산이 필요함

            if current_sum == target:
                return [left + 1 , right + 1]

            if target > current_sum:
                left += 1
            else:
                right -= 1
        return [-1 , 1] # 끝까지 다 확인했는데도 없을때 출력 = 정답 없음

def main():
    sol = Solution()
    print(sol.twoSum([2,7,11,15],9))
    print(sol.twoSum([2,3,4],6))
    print(sol.twoSum([-1,0],-1))

main()