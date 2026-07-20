class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        answer = right

        while left <= right:

            mid = (left + right) // 2

            days_used = 1
            current_weight = 0

            for weight in weights:

                if current_weight + weight > mid:
                    days_used += 1
                    current_weight = weight

                else:
                    current_weight += weight

            if days_used <= days:
                answer = mid
                right = mid - 1

            else:
                left = mid + 1

        return answer
