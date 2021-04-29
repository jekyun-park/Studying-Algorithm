# 819 Most Common Word 가장 흔한 단어
import re
import collections
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # 정규 표현식을 이용하여 paragraph를 소문자 단어 단위로 짜르고, banned에 해당 단어가 없다면, 배열에 추가한다.
        words = [word for word in re.sub(
            r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        # 카운터를 이용하여 단어가 몇번 나왔는지 조회할 수 있다.
        counted = collections.Counter(words)

        # 가장 많이 나온 단어를 return 한다.
        return counted.most_common(1)[0][0]


# test case

t = Solution()
p = "Bob hit a ball, the hit BALL flew far after it was hit."
b = ["hit"]
print(t.mostCommonWord(
    "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
