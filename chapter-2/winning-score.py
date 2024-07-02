# Winning Score - https://dmoj.ca/problem/ccc19j1

def inputDigit():
    value = input()
    if not value.isdigit():
        raise "정수만 입력 가능합니다"

    number = int(value)
    if number < 0:
        raise "횟수는 0보다 커야합니다"

    return number


appleThree = inputDigit()
appleTwo = inputDigit()
appleOne = inputDigit()
bananaThree = inputDigit()
bananaTwo = inputDigit()
bananaOne = inputDigit()

appleScore = appleThree * 3 + appleTwo * 2 + appleOne
bananaScore = bananaThree * 3 + bananaTwo * 2 + bananaOne

if appleScore > bananaScore:
    print("A")
elif appleScore < bananaScore:
    print("B")
else:
    print("T")
