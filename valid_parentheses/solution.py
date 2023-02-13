from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        openers = deque()
        last_opener = -1
        for char in (ord(c) for c in s):
            if char in {40, 91, 123}:
                last_opener += 1
                openers.append(char)
                continue
            if not openers:
                return False

            op = openers[last_opener]
            if char == (op + 1 if op == 40 else op + 2):
                openers.pop()
                last_opener -= 1
                continue

            return False

        return not openers
