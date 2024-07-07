# Ljestvica - https://dmoj.ca/problem/coci12c5p1
# 문제: 악보가 주어졌을 때 C major인지 A minor인지 판별하라
# 자료:
#   C Major의 주요음은 C F G다
#   A Minor의 주요음은 A D E다
#   악보에 C Maior의 주요음의 개수가 A Minor의 주요음 개수보다 많다면 C Major다
#   반대로 악보에 A Minord의 주요음 개수가 더 많다면 A Minor다
#   만약 주요음 개수가 같다면 마지막 음이 A이면 A Minor, C라면 C Major다
#   강조된 음은 각 마디로 구분된 음에서 가장 앞의 음이다.
# 계획:
#   악보를 입력받는다.
#     만약 A, B, C, D, E, F, G, |중에 없으면 예외를 던진다
#     만약 가장 앞에 혹은 가장 뒤에 | 가 있으면 예외를 던진다
#     입력한 글자수가 2 <= N <= 100이 아니면 예외를 던진다
#   입력한 문자열을 | 문자열로 구분해서 문자열에 담는다.
#   가장 앞에 글자가 C Major중에 있으면 C Major 주요음 개수를 증가시킨다
#   가장 앞에 글자가 A Minor중에 있으면 A Minor 주요음 개수를 증가시킨다
#   만약 C Major주요음 개수가 A Minor주요음 개수보다 많다면 C-dur를 출력한다
#   만약 A Minor주요음 개수가 더 많다면 A-mol을 출력한다.
#   만약 수가 같다면 가장 마지막 음이 C라면 C-dur를 출력한다
#     가장 마지막 음이 A라면 A-mol을 출력한다
#     만약 둘다 아니라면 예외를 출력한다
# 실행:
# 회고:
#   도메인 자체가 복잡해서 이해하는데 어려웠음. 각 단어가 부르는 말을 문제에서 찾느라
#   시간이 오래 걸렸음.

TONES = "ABCDEFG"
C_MAJOR_MAIN_TONES = "CFG"
A_MINOR_MAIN_TONES = "ADE"
SEPERATOR = "|"

sheet = input()
if sheet[0] not in TONES and sheet[-1] not in TONES:
    raise "악보 맨 앞과 맨 뒤는 음이 와야 합니다."
if not 2 <= len(sheet) <= 100:
    raise "악보의 글자수는 2 <= N <= 100여야 합니다."
for char in sheet:
    if not char in TONES and char != SEPERATOR:
        raise "문자열은 A, B, C, D, E, F, G, |만 입력 가능합니다"

cMajorMainTonesCount = 0
aMinorMainTonesCount = 0

measures = sheet.split(SEPERATOR)
for measure in measures:
    accentedTone = measure[0]
    if accentedTone in C_MAJOR_MAIN_TONES:
        cMajorMainTonesCount = cMajorMainTonesCount + 1
    elif accentedTone in A_MINOR_MAIN_TONES:
        aMinorMainTonesCount = aMinorMainTonesCount + 1
    else:
        pass

if cMajorMainTonesCount > aMinorMainTonesCount:
    print("C-dur")
elif cMajorMainTonesCount < aMinorMainTonesCount:
    print("A-mol")
else:
    if measures[-1][-1] == "C":
        print("C-dur")
    elif measures[-1][-1] == "A":
        print("A-mol")
    else:
        raise "주어진 악보가 C Major도 아니고 A Minor도 아닙니다"
