class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currStr = ""
        currNum = 0

        for c in s:
            if c.isdigit():
                currNum = currNum * 10 + int(c)

            elif c == "[":
                stack.append((currStr, currNum))
                currStr = ""
                currNum = 0

            elif c == "]":
                prevStr, num = stack.pop()
                currStr = prevStr + currStr * num

            else:
                currStr += c

        return currStr