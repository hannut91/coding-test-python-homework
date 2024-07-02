# Telemarketer or not? - https://dmoj.ca/problem/ccc18j1

import re

pattern = re.compile(r'^[0-9]$')


def inputDigit():
    value = input()
    if pattern.match(value):
        return int(value)
    else:
        raise "0-9 정수만 입력 가능합니다"


digit1 = inputDigit()
digit2 = inputDigit()
digit3 = inputDigit()
digit4 = inputDigit()

if (digit1 == 8 or digit1 == 9) and (digit2 == digit3) and (digit4 == 8 or digit4 == 9):
    print("ignore")
else:
    print("answer")
