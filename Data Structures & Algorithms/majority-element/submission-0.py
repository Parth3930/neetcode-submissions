class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        target = len(nums) // 2

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

            if freq[n] > target:
                return n
