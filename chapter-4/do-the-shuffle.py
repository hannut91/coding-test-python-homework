# Slot Machines - https://dmoj.ca/problem/ccc00s1
# 문제:
# 자료:
#   mp3는 메모리에 5곡을 저장할 수 있다
#   저장된 곡은 A, B, C, D, E이 있다
#   mp3는 곡 목록을 저장할 수 있다. 이것은 곡의 순서를 결정한다
#   mp3는 버튼이 4개 있다.
#   버튼을 눌러서 곡을 재생할 수 있고, 곡 목록의 순서를 재정렬할 수 있다
#   버튼 1은 첫 번째 곡을 가장 마지막으로 보낸다
#   버튼 2는 가장 마지막 곡을 가장 앞으로 보낸다
#   버튼 3는 첫 번째와 두 번째 곡의 위치를 서로 바꾼다
#   버튼 4는 종료한다.
# 계획:
#   처음에는 버튼을 입력받는다
#     만약 정수가 아니거나 1 <= b <= 4 사이가 아니라면 예외를 던진다
#   버튼을 누를 수를 입력반는다.
#     만약 정수가 아니거나 1 <= n <= 10이 아니라면 예외를 던진다
#   만약 누른 버튼이 종료 버튼인데 누른 수가 1이 아니면 예외를 던진다
#   버튼 1이면 맨 앞에서 하나 빼서 뒤에 추가한다. 버튼을 입력받은 만큼 반복한다
#   버튼 2이면 맨 뒤에서 하나 빼서 앞에 추가한다. 버튼을 입력받은 만큼 반복한다
#   버튼 3이면 처음 곡와 두 번째 곡의 위치를 서로 바꾼다 버튼을 입력받은 만큼 반복한다
#   반복문이 끝나면 곡 목록을 출력한다
# 실행:
# 회고:
#   파이썬에서 사용하는 문법들이 익숙하지 않아서 어려웠음. 익숙한 언어에서 파이썬 문법으로 번역하는
#   느낌이 많이 들었음. 도메인에 대한 분석을 더 많이 해야겠다

playlist = ["A", "B", "C", "D", "E"]


def button1(l):
    arr = l[:]
    arr.append(arr.pop(0))
    return arr


def button2(l):
    arr = l[:]
    arr.insert(0, arr.pop())
    return arr


def button3(l):
    arr = l[:]
    arr[0] = l[1]
    arr[1] = l[0]
    return arr


buttons = {
    "1": button1,
    "2": button2,
    "3": button3,
}

while True:
    command = input()

    clickCountInput = input()
    if not clickCountInput.isdigit():
        raise "버튼은 숫자만 입력 가능합니다"

    clickCount = int(clickCountInput)
    if not 1 <= clickCount <= 10:
        raise "클릭 수는 1 <= n <= 10 이여야 합니다"

    if command == "4":
        if clickCount != 1:
            raise "정지 버튼은 한 번만 누를 수 있습니다"
        break

    for i in range(clickCount):
        playlist = buttons[command](playlist)

print(" ".join(playlist))
