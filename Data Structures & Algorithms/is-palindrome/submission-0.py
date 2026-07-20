class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        for c in s:
            if c.isalnum():
                clean += c.lower()

        start = 0
        end = len(clean) - 1

        while start < end:
            if clean[start] != clean[end]:
                return False

            start += 1
            end -= 1

        return True