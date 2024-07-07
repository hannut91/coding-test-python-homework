# Multiple Choice - https://dmoj.ca/problem/ccc11s2
# 문제: 선생님이 객관식 문제에서 등급을 매길 수 있도록 프로그램을 작성하라
# 자료:
#   답변은 A, B, C, D, E중에 하나다.
#   답변한 순서가 문제를 나타낸다.
#   주어진 정답의 순서가 문제를 나타낸다.
# 계획:
#   문제수를 입력받는다.
#     만약 문제수가 정수를 입력받지 않으면 예외를 던진다.
#     문제수가 0 < N < 10000 사이에 있지 않으면 예외를 던진다.
#   문제수만큼 학생의 답변을 입력받는다.
#     이때 답변이 ABCDE중에 없다면 예외를 던진다.
#   문제수만큼 정답을 입력받는다.
#     이때 정답이 ABCDE중에 없다면 예외를 던진다.
#     답변과 비교하여 같으면 정답 개수를 증가시킨다
# 실행:
# 회고:
#   변수 이름을 구체적으로 적으니 뒤에 s하나 안붙여서 헷갈리게 됨. 도메인에 눈여겨 봐야하는 부분만
#   명확하게 표현하고 로컬 변수는 간단하게 하는 것도 실험해 봐야겠음

ANSWER_CHARACTERS = "ABCDE"

choicesCountInput = input()
if not choicesCountInput.isdigit():
    print(choicesCountInput)
    raise "문제 수는 정수만 입력 가능합니다"

choicesCount = int(choicesCountInput)
if not 0 < choicesCount < 10000:
    print(choicesCount)
    raise "문제 수는 0 < N < 10000 수만 입력 가능합니다"

answers = []
for index in range(choicesCount):
    answer = input()
    if answer not in ANSWER_CHARACTERS:
        print(answer)
        raise "학생의 답변은 ABCDE중에만 입력 가능합니다"
    answers.append(answer)

correctAnswers = []
for index in range(choicesCount):
    correctAnswer = input()
    if correctAnswer not in ANSWER_CHARACTERS:
        print(correctAnswer)
        raise "정답은 ABCDE중에만 입력 가능합니다"
    correctAnswers.append(correctAnswer)

answerCount = 0
for index in range(choicesCount):
    if answers[index] == correctAnswers[index]:
        answerCount = answerCount + 1

print(answerCount)
