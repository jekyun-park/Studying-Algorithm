from typing import List
import collections

# 49 Group Anagrams 그룹 애너그램


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # KeyError 방지를 위해 항상 디폴트를 생성해주는 defaultdict() 선언
        anagrams = collections.defaultdict(list)

        # strs의 매 단어마다, 정렬한 단어를 키로 하고, 단어를 value 로 하여 딕셔너리에 추가
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()


# test case
test = Solution()

print(test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# join 함수는 '구분자'로 요소를 붙여서 리턴
# sorted에 문자열을 넣을시 정렬하여 리스트로 리턴함.

print(''.join(sorted("jegyun")))
