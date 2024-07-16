# Slot Machines - https://dmoj.ca/problem/ccc00s1
# 문제: 마르타가 파산할 때 까지 플레이한 횟수를 출력하라
# 자료:
#   마르타는 부자가 되기 위해 카지노에 간다
#   마르타는 한 번에 3개의 기계를 플레이한다
#   기계는 완전히 예측 가능하다.
#   마르타는 기계가 완전히 예측 가능하다는 사실을 모른다
#   기계를 플레이 하는데 1 quarter가 든다
#   첫 번째 기계는 35번째 플레이 마다 30 quarter를 얻는다
#   두 번째 기계는 100번째 플레이 마다 60 quarter를 얻는다
#   세 번째 기계는 10번째 플레이 마다 9 quarter를 얻는다
# 계획:
#   마르타의 잔액을 동전 수를 입력받는다
#     만약 정수가 아니면 예외를 던진다
#     만약 1 <= 잔액 < 1000 이면 예외를 던진다
#   첫 번째 기계 이전 플레이 횟수를 입력받는다
#     만약 정수가 아니면 예외를 던진다
#     만약 0 <= qaurter < 35 quarter 이 아니면 예외를 던진다
#   두 번째 기계 이전 플레이 횟수를 입력받는다
#     만약 정수가 아니면 예외를 던진다
#     만약 0 <= qaurter < 100 quarter 이 아니면 예외를 던진다
#   세 번째 기계 이전 플레이 횟수를 입력받는다
#     만약 정수가 아니면 예외를 던진다
#     만약 0 <= qaurter < 10 quarter 이 아니면 예외를 던진다
#   동전의 개수가 0이 될때까지 반복한다
#     첫 번째 기계에 동전을 넣는다.
#     만약 첫 번째 기계에 현재 플레이한 횟수가 보상 횟수와 같다면, 잔액을 보상만큼 증가시키고 플레이한
#       횟수는 0으로 초기화한다.
#
# 실행:
# 회고:
#   한 번에 연속으로 머신을 돌린다는 것을 for 반복문으로 표현했는데 이게 잘 맞는지는 모르겠다.
#   나중에 기계를 연속으로 실행을 안 할수 도 있고 기계가 추가될 수 있을탠데, 기계가 늘어나는 것은
#   기계 목록에만 추가되면 쉽게 추가가 되지만, 만약 기계를 실행하는 순서가 변경에는 코드가 변경이 어려울
#   것 같다.

machines = [
    {
        "payQuartersCount": 35,
        "reward": 30,
        "currentCount": 0,
    },
    {
        "payQuartersCount": 100,
        "reward": 60,
        "currentCount": 0,
    },
    {
        "payQuartersCount": 10,
        "reward": 9,
        "currentCount": 0,
    }
]

quartersCountInput = input()
if not quartersCountInput.isdigit():
    raise "동전 개수는 정수만 입력 가능합니다"

quartersCount = int(quartersCountInput)
if not 1 <= quartersCount < 1000:
    raise "동전은 1 <= quartersCount < 1000 이어야 합니다"

for machine in machines:
    playedCountInput = input()
    if not playedCountInput.isdigit():
        raise "머신의 플레이 횟수는 정수만 입력 가능합니다"

    playedCount = int(playedCountInput)
    if not 0 <= playedCount < machine["payQuartersCount"]:
        raise "머신의 플레이 횟수는 0 이상 보상 개수 이하여야 합니다"

    machine["currentCount"] = playedCount

totalPlayedCount = 0
while quartersCount > 0:
    for machine in machines:
        if quartersCount <= 0:
            break

        totalPlayedCount += 1
        quartersCount -= 1
        machine["currentCount"] += 1
        if machine["currentCount"] == machine["payQuartersCount"]:
            quartersCount += machine["reward"]
            machine["currentCount"] = 0

print(f"Martha plays {totalPlayedCount} times before going broke.")
