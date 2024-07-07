# Riječi - https://dmoj.ca/problem/coci13c3p1
# 문제: 버튼을 눌렀을 때 스크린에 각 문자가 얼마나 출력되는지 계산하라
# 자료:
#   기계는 큰 스크린과 버튼 하나를 가지고 있다
#   기계는 처음에는 A글자를 보여준다
#   버튼을 누르면 A는 B가 되고, B는 BA가 된다
# 계획:
#   버튼을 클릭할 횟수를 입력받는다
#     만약 정수가 아니라면 예외를 던진다
#     만약 횟수가 1 <= K <= 45가 아니라면 예외를 던진다
#   클릭한 횟수만큼 반복한다
#     현재 문자열을 순회하면서 변환하고 변환된 문자열을 다음 문자열로 덮어쓴다
#   A와 B의 글자수를 세서 출력한다
# 실행:
# 회고:
#   테스트 케이스를 로컬에서 충분히 실행해보지 않아서 왜 실패가 났는지 몰랐음.
#   입력값의 경계값은 반드시 테스트해보고 제출해야겠음

clickCountInput = input()
if not clickCountInput.isdigit():
    raise "버튼 클릭 수는 정수만 입력 가능합니다"

clickCount = int(clickCountInput)
if not 1 <= clickCount <= 45:
    raise "버튼 클릭 수는 1 <= K <= 45여야 합니다"

screen = "A"
aCount = 0
bCount = 1

for index in range(clickCount - 1):
    temp = bCount
    bCount = aCount + bCount
    aCount = temp

print(f'{aCount} {bCount}')

# 도메인으로 푼 문제
# for index in range(clickCount - 1):
# aCount = 0
# bCount = 0
# nextScreen = ""
# # O(K)
# for char in screen:
#     if char == "A":
#         nextScreen = nextScreen + "B"
#         bCount = bCount + 1
#     elif char == "B":
#         nextScreen = nextScreen + "BA"
#         aCount = aCount + 1
#         bCount = bCount + 1
#     else:
#         raise "스크린에는 A, B만 출력 가능합니다"
# screen = nextScreen
# print(f'{aCount} {bCount}')
