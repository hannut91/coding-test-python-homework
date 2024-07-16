# When You Eat Your Smarties - https://dmoj.ca/problem/ecoo15r1p1
# 빨간건 마지막에 먹음
# 오렌지부터 시작해서 하나씩 먹음
# 오렌지 블루 그린 엘로 핑크 바이올렛 브라운 그리고 레드 순으로 먹는다
# 최대 7개까지 들고 있을 수 있음
# 다른 색깔은 걍 바로 먹음
# 먹을 때는 같은 색깔은 한 번에 전부 먹는다
# 먹을 때 항상 13초가 걸린다 단 red가 있으면 16초가 걸린다

TEST_COUNT = 10
RED_TIME_PER_SINGLE = 16
NON_RED_TIME_PER_HANDFUL = 13
HANDFUL_SIZE = 7

order = [
    "orange", "blue", "green", "yellow", "pink", "violet", "brown", "red"
]

group = {
    "orange": 0,
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "pink": 0,
    "violet": 0,
    "brown": 0,
    "red": 0,
}

for i in range(TEST_COUNT):
    totalTime = 0

    while True:
        smartie = input()
        if smartie == "end of box":
            break

        group[smartie] += 1
    while True:
        if all(value == 0 for value in group.values()):
            break

        for it in order:
            if it == "red" and group[it] > 0:
                totalTime += 16
                group[it] -= 1
            else:
                if group[it] > 0:
                    totalTime += NON_RED_TIME_PER_HANDFUL
                    if group[it] > HANDFUL_SIZE:
                        group[it] -= HANDFUL_SIZE
                    else:
                        group[it] = 0

    print(totalTime)
