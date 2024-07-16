# AmeriCanadian - https://dmoj.ca/problem/ccc02j2
# 문제: 아메리칸 스펠링으로 된 단어들을 캐네디언 스펠링으로 변경하라
# 자료:
#   아메리칸과 캐네디언은 다르게 발음한다
#   단어가 4글자가 넘고, 자음뒤에 or로 끝나면 아메리칸 스펠링이다
#   아메리칸스펠링에서 or는 캐네디안스펠링에서 our와 같다
#   모음은 a, e, i, o, u, y다
# 계획:
#   계속해서 단어를 입력받는다
#     만약 단어가 64글자를 넘으면 예외를 던진다
#     만약 단어가 `quit!`이면 반복을 종료한다
#     4글자 보다 작으면 출력 목록에 넣고 반복을 계속한다
#     만약 단어에 자음 바로뒤에 or이 있으면 or을 our로 바꾼다. 바꾼 단어를 출력 목록에 넣는다
#   출력목록을 하나씩 전부 출력한다
# 실행:
# 회고:
#   역시 문제가 생기면 도메인을 제대로 파악하지 않아서 생긴 문제다. suffix라는 단어를 제대로 해석하지
#   않아서 문제도 복잡하게 푼 것 같다. 하나하나 자세히 봐야겠다
import re

CONSONANT = "bcdfghjklmnpqrstvwxz"
VOWEL = "aeiouy"
MAX_WORD_LENGTH = 64
TERMINAL_WORD = "quit!"

transformedWords = []

while True:
    word = input()
    if len(word) > MAX_WORD_LENGTH:
        raise f"단어의 글자수는 {MAX_WORD_LENGTH}입니다"

    if word == TERMINAL_WORD:
        break

    if len(word) < 4:
        transformedWords.append(word)
        continue
    pattern = re.compile(f"[{CONSONANT}]or$")

    newWord = re.sub(pattern,
                     lambda match: match.group().replace("or", "our"), word)
    transformedWords.append(newWord)

for it in transformedWords:
    print(it)
