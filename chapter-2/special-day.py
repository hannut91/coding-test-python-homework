# Special Day - https://dmoj.ca/problem/ccc15j1

def inputMonth():
    value = input()
    if not value.isdigit():
        raise "정수만 입력 가능합니다"

    number = int(value)
    if number < 0 or number > 12:
        raise "1~12만 입력 가능합니다"

    return number


def inputDay():
    value = input()
    if not value.isdigit():
        raise "정수만 입력 가능합니다"

    number = int(value)
    if number < 0 or number > 31:
        raise "1~31만 입력 가능합니다"

    return number


month = inputMonth()
day = inputDay()

if month < 2:
    print("Before")
elif month > 2:
    print("After")
else:
    if day < 18:
        print("Before")
    elif day > 18:
        print("After")
    else:
        print("Special")
