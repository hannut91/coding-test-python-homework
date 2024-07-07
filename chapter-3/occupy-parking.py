# Occupy parking - https://dmoj.ca/problem/ccc18j2
# 문제: 어제와 오늘 주차 공간이 모두 사용된 곳의 개수를 계산하라
# 자료:
#   N개의 주차 공간이 있다.
#   주차 공간에는 차가 주차되어있을 수 있다.
#   주차 공간에는 비어있을 수 있다.
#   입력으로 어제와 오늘 주차한 기록을 입력한다.
#   같은 공간에 어제와 오늘 모두 주차하면, 모두 사용된 곳으로 친다.
# 계획:
#   주차 공간 수를 입력받는다.
#     만약 입력한 수가 정수가 아니면 예외를 던진다.
#     만약 수가 1 <= N <= 100이 아니면 예외를 던진다.
#   어제 주차 기록을 입력받는다.
#     문자열의 길이가 N과 같지 않으면 예외를 던진다.
#     문자열에 C 혹은 .이 아니면 예외를 던진다.
#   오늘 주차 기록을 입력받는다.
#     문자열의 길이가 N과 같지 않으면 예외를 던진다.
#     문자열에 C 혹은 .이 아니면 예외를 던진다.
#   어제 주차 기록을 순회한다.
#     이때 인덱스는 주차 공간의 위치에 해당한다.
#     어제 주차 기록과 오늘 기록 주차한 기록이 모두 있으면 개수를 더한다.
# 실행:
# 회고:
#   어제 주차 기록과 오늘 주차 기록이 모두 주차로 되어있는 경우를 명확하게 정의하지 않아서
#   코드를 작성할 때 정의했음. 도메인에서 정의한 내용대로 판단하는 연습을 더 해야될 것 같음

import re

PARKING_HISTORY_CHARACTER = "C."

pattern_string = f'^[{PARKING_HISTORY_CHARACTER}]+$'
pattern = re.compile(pattern_string)

value = input()
if not value.isdigit():
    raise "정수만 입력 가능합니다"

parkingSpacesCount = int(value)
if not 1 <= parkingSpacesCount <= 100:
    raise "주차 공간은 1 <= N <= 100 사이여야 합니다"

yesterdayParkingHistory = input()
if not len(yesterdayParkingHistory) == parkingSpacesCount:
    raise "주차기록 수는 주차공간의 수와 일치해야 합니다"
if not pattern.match(yesterdayParkingHistory):
    raise f"주차기록은 {PARKING_HISTORY_CHARACTER}만 입력 가능합니다"

todayParkingHistory = input()
if not len(todayParkingHistory) == parkingSpacesCount:
    raise "주차기록 수는 주차공간의 수와 일치해야 합니다"
if not pattern.match(todayParkingHistory):
    raise f"주차기록은 {PARKING_HISTORY_CHARACTER}만 입력 가능합니다"

bothOccupiedParkingSpacesCount = 0

for parkingSpacePosition in range(len(yesterdayParkingHistory)):
    if yesterdayParkingHistory[parkingSpacePosition] == 'C' and todayParkingHistory[parkingSpacePosition] == 'C':
        bothOccupiedParkingSpacesCount += 1

print(bothOccupiedParkingSpacesCount)
