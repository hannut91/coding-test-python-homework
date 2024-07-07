# Trik - https://dmoj.ca/problem/coci06c5p1
# 문제: 컵을 움직였을 때 볼의 위치를 판별하라
# 자료:
#   컵은 불투명하다.
#   컵은 3개가 있다.
#   컵은 입구가 아래로 놓여있다.
#   공의 처음 위치는 보는 사람 입장에서 가장 왼쪽이다. 즉 1이다.
#   공의 위치는 왼쪽 부터 오른쪽으로 1, 2, 3 선형적으로 증가한다.
#   컵의 위치 변경은 두 컵 사이밖에 안된다.
#   50번 밖에 움직일 수 없다.
#   컵의 위치 변경은 영향을 받는 공의 위치와 관련이 있다.
#   A는
# 계획:
#   문자열을 입력받는다.
#     만약 문자열이 ABC안에 없으면 경고를 보여주고 종료합니다.
#     만약 문자열이 비어있거나 50글자를 넘으면 경고를 보여주고 종료합니다.
#   볼의 처음 위치를 가장 왼쪽으로 설정합니다.
#   문자열을 순회하며 주어진 문자열에 따라 컵을 교환합니다.
#   A는 공이 1 혹은 2 위치에 있으면 교환합니다.
#   B는 공이 2 혹은 3 위치에 있으면 교환합니다.
#   C는 공이 1 혹은 3 위치에 있으면 교환합니다.
# 실행:
# 회고:
#   컵의 위치 변경이라는 사실을 어떻게 표현할지 정하지 않고 계획을 세웠음. 그러다보니
#   실행할 때 대충 변경이라는 것을 만들려고 했다는 것을 꺠달았음. 그래서 컵의 교환이라는 것은
#   영향을 받는 두 위치의 점이라고 생각하고, 이 영향권에 있을 때 반대편 쪽으로 이동하는 것이라고 정의했음
#   대충 넘어가지 말고 `정의`라는 것을 해야겠음

import re

MOVE_CHARACTERS = "ABC"

pattern_string = f'^[{MOVE_CHARACTERS}]+$'
pattern = re.compile(pattern_string)

swaps = {
    'A': [1, 2],
    'B': [2, 3],
    'C': [1, 3],
}

moveCharacters = input()
if len(moveCharacters) < 1 or len(moveCharacters) > 50:
    raise "moveCharacters는 길이 1 이상 50이하여야 합니다."

if not pattern.match(moveCharacters):
    raise f"moveCharacters는 {MOVE_CHARACTERS}만 입력 가능합니다."

ballPosition = 1

for move in moveCharacters:
    if swaps[move][0] == ballPosition:
        ballPosition = swaps[move][1]
    elif swaps[move][1] == ballPosition:
        ballPosition = swaps[move][0]
    else:
        # 볼의 위치가 컵의 변경과 상관이 없는 경우에 여기가 실행됩니다. 이때는 아무런 조작을 하지 않습니다.
        pass

print(ballPosition)
