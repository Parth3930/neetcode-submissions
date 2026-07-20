class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        answer = right

        while left <= right:

            mid = (left + right) // 2

            hours = 0

            # Calculate total hours needed at speed = mid
            for pile in piles:
                hours += (pile + mid - 1) // mid

            # If speed works, try a smaller speed
            if hours <= h:
                answer = mid
                right = mid - 1

            # Too slow, need a faster speed
            else:
                left = mid + 1

        return answer