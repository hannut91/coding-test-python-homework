# Uncrackable - https://dmoj.ca/problem/wc17c3j3
# 문제: 주어진 비밀번호가 룰 목록에 모두 통과하는지를 판별하라
# 자료:
#   비밀번호는 문자열이다
#   비밀번호는 8글자와 12글자 사이다
#   비밀번호 영어 소문자, 대문자, 0부터 9까지만 허용한다.
#   적어도 3글자의 영어 소문자가 포함되어야 한다.
#   적어도 2글자의 영어 대문자가 포함되어야 한다.
#   적어도 숫자가 하나 이상 포함되어야 한다.
# 계획:
#   비밀번호를 입력받습니다.
#   비밀번호가 영어 소문자, 대문자, 0~9 외의 문자가 있으면 Invalid를 출력합니다.
#   입력받은 비밀번호가 8글자보다 작으면 Invalid를 출력합니다.
#   입력받은 비밀번호가 12글자보다 크면 Invalid를 출력합니다.
#   입력받은 비밀번호에 영어 소문자가 적어도 3개 이상 포함되지 않으면 Invalid를 출력합니다.
#   입력받은 비밀번호에 영어 대문자가 적어도 2개 이상 포함되지 않으면 Invalid를 출력합니다.
#   입력받은 비밀번호에 숫자가 하나 이상 포함되지 않으면 Invalid를 출력합니다.
#
# 실행:
# 회고:
#   함수를 사용 안하려고 하다보니 프로그램을 빨리 종료시키기가 어려웠음. exit을 썼는데
#   exit을 쓰면 테스트가 통과하지 않아서 시간을 많이 낭비했음

MIN_LOWERCASE_LETTERS = 3
MIN_UPPERCASE_LETTERS = 2
MIN_DIGITS = 1

lowercaseCharacters = "abcdefghijklmnopqrstuvwxyz"
upperCaseCharacters = lowercaseCharacters.upper()
digitCharacters = "0123456789"

passwordInput = input()

lowercaseCharactersCount = 0
upperCaseCharactersCount = 0
digitCharactersCount = 0
otherCharactersCount = 0

for char in passwordInput:
    if char in lowercaseCharacters:
        lowercaseCharactersCount += 1
    elif char in upperCaseCharacters:
        upperCaseCharactersCount += 1
    elif char in digitCharacters:
        digitCharactersCount += 1
    else:
        otherCharactersCount += 1

if not (8 <= len(passwordInput) <= 12):
    print("Invalid")
elif otherCharactersCount > 0:
    print("Invalid")
elif lowercaseCharactersCount < MIN_LOWERCASE_LETTERS:
    print("Invalid")
elif upperCaseCharactersCount < MIN_UPPERCASE_LETTERS:
    print("Invalid")
elif digitCharactersCount < MIN_DIGITS:
    print("Invalid")
else:
    print("Valid")
