# Who is in the Middle - https://dmoj.ca/problem/ccc07j1

def inputBowlWeight():
    value = input()
    if not value.isdigit():
        raise "정수만 입력 가능합니다"

    number = int(value)
    if number < 1 or number > 99:
        raise "1~99까지만 입력 가능합니다"

    return number


bowl1 = inputBowlWeight()
bowl2 = inputBowlWeight()
bowl3 = inputBowlWeight()

if (bowl1 >= bowl2 and bowl2 >= bowl3) or (bowl1 <= bowl2 and bowl2 <= bowl3):
    print(bowl2)
elif (bowl2 >= bowl1 and bowl1 >= bowl3) or (bowl2 <= bowl1 and bowl1 <= bowl3):
    print(bowl1)
else:
    print(bowl3)
