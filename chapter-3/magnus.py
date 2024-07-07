# Magnus - https://dmoj.ca/problem/coci18c3p1
# 문제: HONI-blocks의 최대 수를 구하여라
# 자료:
#   HONI-block은 HONI로 연속된 문자열을 만들 수 있는 단어를 말한다.
# 계획:
#   단어를 입력 받는다.
#     만약 단어에 대문자 영어가 아닌 문자가 있다면 종료한다.
#     만약 단어의 길이가 1 <= N <= 100000범위가 아니라면 종료한다.
#   단어를 순회하면서 처음에는 H를 찾는다.
#   H를 찾으면 그 다음에는 O를 찾는다.
#   O를 찾으면 N을 찾는다
#   I를 찾으면 HONI-block 횟수를 1 증가 시키고 다시 H를 찾길 반복한다.
# 실행:
# 회고:
#   입력 검증을 했는데, 이것 때문에 테스트가 통과되지 않아서 시간을 많이 해맸다.
#   다행히도 DMOJ는 입력값을 출력해서 확인할 수 있으니, 만약 의심되는 것이 있다면
#   빠르게 확인해 봐야겠다. 그리고 예외를 던질 경우 Type Error가 출력된다는 사실도 확인했다.
#   앞으로 이 에러가 나오면 예외에 걸렸다는 사실로 빠르게 유추할 수 있을 것 같다.

word = input()
if not 1 <= len(word) <= 100000:
    raise "단어의 글자수는 1 ~ 100000 사이여야 합니다."

for char in word:
    if not char.isupper():
        print(word)
        # raise "단어는 모두 대문자 영어 알파벳이어야 합니다."

HONIBlock = "HONI"
index = 0
HONIBlockCount = 0
remainWord = ""

for char in word:
    if char == HONIBlock[index]:
        index += 1
        if index == len(HONIBlock):
            HONIBlockCount += 1
            index = 0

print(HONIBlockCount)
