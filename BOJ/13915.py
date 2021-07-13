import sys

try:
    while True:
        students = []
        N = int(input())

        for _ in range(N):
            skill = sys.stdin.readline().strip()
            skill = sorted(list(set(skill)))

            if (skill in students):
                continue
            else:
                students.append(skill)

        print(len(students))
except EOFError:
    exit()
