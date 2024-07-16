# Kemija - https://dmoj.ca/problem/coci08c3p2
# 문제: Luka의 문장을 디코드하라
# 자료:
#   모음은 a, e, i, o, u다
#   Luka는 문장에서 모음이 있으면 모음에 p를 붙이고 그 모음을 뒤에 또 추가한다
#   문자는 소문자 밖에 없다
#   문장들은 빈 칸 하나로만 구별되어 있다
#   문장 앞과 뒤 글자에는 빈 칸이 없다
#   글자수는 100글자를 초과할 수 없다
# 계획:
#   문장을 입력받는다
#     만약 문장 가장 앞에 빈 칸, 가장 뒤에 빈 칸, 연속되는 빈 칸이 있다면 예외를 던진다
#   모음과 p 그리고 모음이 나오는 패턴을 찾는다
#     패턴이 없으면 종료한다
#   패턴이 있으면 대체하고 다시 반복한다
# 실행:
# 회고:
#   반복문 돌면서 모음이 발견되면 2칸 더 전진하는 방법으로 풀 수 있을 것 같은데, 인코딩 방식이
#   변하면 영향을 많이 받을 것 같아서 정규식으로 짜려다보니 아예 반복문이 없어졌다
import re

pattern = r"[aeiou](p[aeiou])"


def replace_vowel(match):
    # 첫 번째 캡처 그룹을 얻음
    return match.group(0)[0]


sentence = input()

result = re.sub(pattern, replace_vowel, sentence)
print(result)
