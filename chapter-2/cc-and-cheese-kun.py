# C.C. and Cheese-kun - https://dmoj.ca/problem/dmopc16c1p0
def inputW():
    value = input()
    if not value.isdigit():
        raise "정수만 입력 가능합니다"

    number = int(value)
    if number < 1 or number > 3:
        raise "1~3까지만 입력 가능합니다"

    return number


def inputC():
    value = input()
    if not value.isdigit():
        raise "정수만 입력 가능합니다"

    number = int(value)
    if number < 0 or number > 100:
        raise "0~100까지만 입력 가능합니다"

    return number


w = inputW()
c = inputC()

result = "very"
if w == 3 and c >= 95:
    result = "absolutely"

if w == 1 and c <= 50:
    result = "fairly"

print(f"C.C. is {result} satisfied with her pizza.")
