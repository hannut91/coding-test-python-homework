# Epidemiology - https://dmoj.ca/problem/ccc20j2
# 문제: 예상하는 감염자수가 몇일만에 도달하는지를 구하여라
# 자료:
#   한 사람이 질병에 걸리면 다음 날에 R만큼 감염을 시킨다
# 계획:
#   예상 감염자 수를 입력받는다
#     정수가 아니면 에외
#     0보다 크고 10000000보다 작지 않으면 예외
#   처음 감염자 수를 입력받는다
#     정수가 아니면 에외
#     0보다 크고 예상 감염자 수 보다 작거나 같지 않으면 예외
#   하루에 감염시키는 수를 입력받는다
#     정수가 아니면 예외
#     0보다 크고 10보다 작거나 같지 않으면 예외
#   현재 감염자수가 예상 감염자 수를 넘지 않을때까지 반복한다
#     날짜를 하나 증가시킨다
#     현재 감염자 수에 하루에 감염시키는 수를 곱한다
#   지난 날짜를 출력한다
# 실행:
# 회고:

targetInfectedPeopleCountInput = input()
if not targetInfectedPeopleCountInput.isdigit():
    raise "목표 감염자 수는 정수만 입력 가능합니다"

targetInfectedPeopleCount = int(targetInfectedPeopleCountInput)
if not 0 < targetInfectedPeopleCount <= (10 ** 7):
    raise "목표 감염자 수는 0보다 크고 10 ** 7보다 작거나 같아야 합니다"

infectedPeopleCountInput = input()
if not infectedPeopleCountInput.isdigit():
    raise "현재 감염자 수는 정수만 입력 가능합니다"

infectedPeopleCount = int(infectedPeopleCountInput)
if not 0 < infectedPeopleCount <= targetInfectedPeopleCount:
    raise "현재 감염자 수는 0보다 크고 예상 감염자수 보다 작거나 같아야 합니다"

infectingCountPerDayInput = input()
if not infectingCountPerDayInput.isdigit():
    raise "하루에 감염시키는 수는 정수만 입력 가능합니다"

infectingCountPerDay = int(infectingCountPerDayInput)
if not 0 < infectingCountPerDay <= 10:
    raise "하루에 감염시키는 수의 범위는 0 < R <= 10입니다"

initalCount = infectedPeopleCount
day = 0

if infectingCountPerDay == 1:
    initalCount * day
else:
    (initalCount * (infectingCountPerDay ** day) //
     (infectingCountPerDay - 1))
