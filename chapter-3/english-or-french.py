# English or French? - https://dmoj.ca/problem/ccc11s1
# 문제: 주어진 문장이 영어인지 프랑스어인지 판별하라
# 자료:
#   NLP는 기계를 사용해서 인간 언어를 인식하는 것이다.
#   t, T 문자의 수가 s S보다 많다면 영어로 작성된 텍스트다.
#   s, S 문자의 수가 t T보다 많다면 프랑스어 텍스트다.
#   t, T 문자의 수와 s S문자의 수가 같다면 프랑스어 텍스트다.
#   텍스트는 1개 이상 10,000개 미만 텍스트가 주어진다.
#   텍스트는 입력은 단어 1개 이상 100개 이하의 텍스트가 주어진다.
# 계획:
#   텍스트 라인 수를 입력 받는다.
#     만약 정수가 아니라면 예외를 던진다.
#     만약 1개 미만이거나, 10,000개 이상이라면 예외를 던진다.
#   입력한 라인수 만큼 반복한다.
#     텍스트를 입력받는다.
#       만약 텍스트의 길이가 1이상 100이하가 아니라면 예외를 던진다.
#     t, T 문자 개수를 세서 저장한다.
#       만약 입력받은 모든 문자가 s혹은S여도 t, T가 많다면 종료한다.
#     s, S 문자 개수를 세서 저장한다.
#       만약 입력받은 모든 문자가 t혹은T여도 s, S가 많다면 종료한다.
#   만약 tT가 sS보다 많다면 English를 출력한다
#   만약 sS가 tT보다 많다면 French를 출력한다.
#   만약 같다면 French를 출력한다.
# 실행:
# 회고:
#   문자를 매직 리터럴로 처리해서 값이 잘못되었는지 찾기 어려웠다. 처음에 자료를 정의할 때
#   상수로 처리해서 바뀔 수 있는 부분들을 미리 정의해놓고 하는게 좋겠다.

MIN_TEXT_LENGTH = 1
MAX_TEXT_LENGTH = 100
ENGLISH_CHARACTER_LOWER = "t"
ENGLISH_CHARACTER_UPPER = ENGLISH_CHARACTER_LOWER.upper()
FRENCH_CHARACTER_LOWER = "s"
FRENCH_CHARACTER_UPPER = FRENCH_CHARACTER_LOWER.upper()

textLinesCountInput = input()
if not textLinesCountInput.isdigit():
    raise "텍스트 라인 수는 정수만 입력 가능합니다."

textLinesCount = int(textLinesCountInput)
if not 0 < textLinesCount < 10000:
    raise "텍스트 라인 수는 0 < N < 10000만 입력 가능합니다."

englishOccurrencesCount = 0
frenchOccurrencesCount = 0

for index in range(textLinesCount):
    text = input()
    if not MIN_TEXT_LENGTH <= len(text) <= MAX_TEXT_LENGTH:
        raise "텍스트의 글자수는 {MIN_TEXT_LENGTH} <= length <= {MAX_TEXT_LENGTH}이어야 합니다"

    englishOccurrencesCount = (
            englishOccurrencesCount
            + text.count(ENGLISH_CHARACTER_LOWER)
            + text.count(ENGLISH_CHARACTER_UPPER))
    frenchOccurrencesCount = (
            frenchOccurrencesCount
            + text.count(FRENCH_CHARACTER_LOWER)
            + text.count(FRENCH_CHARACTER_UPPER))
    if englishOccurrencesCount > (frenchOccurrencesCount + ((textLinesCount - (index + 1)) * MAX_TEXT_LENGTH)):
        break

if englishOccurrencesCount > frenchOccurrencesCount:
    print("English")
elif englishOccurrencesCount < frenchOccurrencesCount:
    print("French")
else:
    print("French")
