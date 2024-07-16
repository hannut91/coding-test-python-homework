# Take a Number - https://dmoj.ca/problem/ecoo13r1p1

nextNumber = int(input())
waitingStudentsCount = 0
takenStudentsCount = 0
lateStudentsCount = 0

while True:
    v = input()
    if v == "TAKE":
        lateStudentsCount += 1
        waitingStudentsCount += 1
        if nextNumber == 999:
            nextNumber = 1
        else:
            nextNumber += 1
    elif v == "SERVE":
        waitingStudentsCount -= 1
        takenStudentsCount += 1

    elif v == "CLOSE":
        print(f"{lateStudentsCount} {waitingStudentsCount} {nextNumber}")
        waitingStudentsCount = 0
        lateStudentsCount = 0
    elif v == "EOF":
        break
