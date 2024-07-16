# Ptice - https://dmoj.ca/problem/coci08c1p2
# 문제: 누가 가장 많은 정답을 맞췄는지 구하라
# 자료:
#   아드리안, 브루노, 고란은 새 애호가 클럽에 들어가려고 한다
#   시험에 합격한 사람만 클럽에 들어갈 수 있다
#   각 시험에는 A, B, C중에 정답이 있다
#   아드리안은 A,B,C 순서대로 찍을려고 한다
#   브루노는 B,A,B,C 순서대로 찍을려고 한다
#   고란은 C,C,A,A,B,B 순서대로 찍을려고 한다
# 계획:
#   문제에 대한 질문 수를 입력받는다
#     정수가 아니거나 1 <= N <= 100이 아니면 예외
#   문제의 정답을 입력받는다
#     질문 수와 다르면 예외
#     A,B,C중에 없으면 예외
#   질문을 순회한다.
#     각 사람들의 시퀀스와 비교해서 같으면 정답 수를 증가시킨다
#
# 실행:
# 회고:
#   계획을 세우는게 귀찮아서 자꾸 코드를 바로 작성하려고 한다. 체계적으로 문제 푸는 연습을 더 해야겠다

import re

ALLOWED_ANSWERS = "ABC"

applicants = [
    {
        "name": "Adrian",
        "pattern": "ABC",
        "correctAnswerCount": 0,
    },
    {
        "name": "Bruno",
        "pattern": "BABC",
        "correctAnswerCount": 0,
    },
    {
        "name": "Goran",
        "pattern": "CCAABB",
        "correctAnswerCount": 0,
    },
]

questionsCountInput = input()
if not questionsCountInput.isdigit():
    raise "문제 수는 정수만 입력 가능합니다"

questionsCount = int(questionsCountInput)
if not 1 <= questionsCount <= 100:
    raise "문제 수는 1 <= N <= 100 이여야 합니다"

answers = input()
if len(answers) != questionsCount:
    raise "정답의 수는 문제 수와 같아야 합니다"

if not re.compile(f"[^{ALLOWED_ANSWERS}]").match(answers) is None:
    raise f"정답은 {ALLOWED_ANSWERS}만 허용합니다"

for index in range(len(answers)):
    answer = answers[index]
    for applicant in applicants:
        patternLength = len(applicant["pattern"])
        if applicant["pattern"][index % patternLength] == answer:
            applicant["correctAnswerCount"] += 1

sortedApplicants = sorted(applicants, key=lambda x: x['correctAnswerCount'],
                          reverse=True)
max = sortedApplicants[0]["correctAnswerCount"]

print(max)
for applicant in sortedApplicants:
    if applicant["correctAnswerCount"] == max:
        print(applicant["name"])
    else:
        break
