# 937. Reorder Log Files 로그 파일 재정렬


# 숫자 로그는 입력 순서대로
# 문자 로그는 숫자 로그보다 앞에 온다
# 식별자는 순서에 영향이 없지만, 문자가 같은경우 식별자 순으로 한다.

# 람다함수

class Solution:

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let, dig = [], []

        for log in logs:
            if log.split()[1].isdigit():  # split()으로 식별자 제거, 숫자 로그라면, log를 dig에 추가
                dig.append(log)
            else:  # 문자 로그라면, log를 let 에 추가
                let.append(log)

        let.sort(key=lambda x: (x.split()[1:], x.split()[0]))  # 람다 표현식으로 정렬

        return let + dig  # 문자 로그가 숫자 로그보다 앞에 오기 때문에 let + dig

# 람다표현식에 대한 이해 필요
