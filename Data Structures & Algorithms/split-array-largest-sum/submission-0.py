class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        left = max(nums)
        right = sum(nums)

        answer = right

        while left <= right:

            mid = (left + right) // 2

            groups = 1
            current_sum = 0

            for num in nums:

                if current_sum + num > mid:
                    groups += 1
                    current_sum = num
                else:
                    current_sum += num

            if groups <= k:
                answer = mid
                right = mid - 1

            else:
                left = mid + 1

        return answer