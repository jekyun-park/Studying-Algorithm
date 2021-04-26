# 344. Reverse String 문자열 뒤집기


# 1 swap

class Solution1:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# 2 reverse

class Solution2:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
