class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        target = len(nums) // 3

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        res = []

        for n, count in freq.items():
            if count > target:
                res.append(n)

        return res