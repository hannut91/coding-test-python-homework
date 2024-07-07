# Elder - https://dmoj.ca/problem/coci18c4p1
# 문제: 듀얼 끝에 최종적으로 Elder 완드를 획득한 사람과 총 획득했던 사람 수를 구하여라
# 자료:
#   마법사가 다른 마법사를 이기면, 이긴 마법사가 진 마법사의 마법봉을 소유한다
#   Elder 완드는 A가 처음에 소유하고 있다
#   Elder 완드 소유자를 듀얼에서 이기면, 이긴 사람이 Edler 완드를 소유한다.
#   Elder 완드를 소유하지 않은 사람은 듀얼에서 이겨도 변하는 것은 없다.
# 계획:
#   처음 Elder 완드를 소유한 사람을 입력 받는다
#     만약 입력받은 사람이 알파벳 대문자가 아니면 예외를 던진다.
#     입력받은 글자수가 1글자를 초과하면 예외를 던진다.
#   듀얼 수를 입력받는다
#     만약 듀얼수가 정수가 아니면 예외를 던진다
#     만약 듀얼수가 1 <= N <= 100이 아니면 예외를 던진다.
#   듀얼 수 만큼 반복한다
#     패배한 사람이 완드를 가지고 있지 않으면 넘어간다
#     패배한 사람이 완드를 가지고 있으면 소유권을 이긴 사람으로 변경한다
#     이떄 만약 한 번도 소유한 적이 없었다면, 총 소유한 사람 수에 1을 더한다.
#     그리고 소유한 사람 목록에 추가한다
# 실행:
# 회고:
#   영어로 변수를 선언하는 것 자체가 어려웠음. 완드를 소유한 사람을 그냥 owner로 표현할 수 있었지만
#   도메인에서는 완드가 마법사를 섬기는 것으로 표현했기 때무네 변수명에도 동일하게 반영했음.

totalElderWandObeyedWizardCount = 1

elderWandObeyingWizard = input()
if not len(elderWandObeyingWizard) == 1:
    raise "완드를 소유한 사람 글자 수는 1글자여야 합니다"
if not elderWandObeyingWizard.isupper():
    raise "위자드는 영어 대문자 알파벳만 가능합니다"

dualCountInput = input()
if not dualCountInput.isdigit():
    raise "듀얼 횟수는 숫자만 입력 가능합니다"

dualCount = int(dualCountInput)
if not 1 <= dualCount <= 100:
    raise "듀얼 횟수는 1 <= dualCount <= 100이어야 합니다"

elderWandObeyingWizardHistories = elderWandObeyingWizard

for index in range(dualCount):
    dualResult = input()
    winner, looser = dualResult.split(" ")
    if elderWandObeyingWizard == looser:
        elderWandObeyingWizard = winner
        if elderWandObeyingWizard not in elderWandObeyingWizardHistories:
            elderWandObeyingWizardHistories += elderWandObeyingWizard
            totalElderWandObeyedWizardCount += 1

print(elderWandObeyingWizard)
print(totalElderWandObeyedWizardCount)
