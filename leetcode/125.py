# 125. Valid Palindrome

# 1 List

import collections
import re


class Solution:

    def isPalindrome(self, s: str) -> bool:
        strs = []

        for char in s:
            if char.isalnum():
                strs.append(char.lower())
            else:
                pass

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

# 2 Deque


class Solution2:

    def isPalindrome(self, s: str) -> bool:

        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())
            else:
                pass

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

# 3 Slicing


class Solution3:

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]
