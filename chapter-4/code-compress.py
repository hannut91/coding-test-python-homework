# Cold Compress - https://dmoj.ca/problem/ccc19j3
count = int(input())

for i in range(count):
    text = input()

    currentChar = ""
    count = 0
    output = ''

    for char in text:
        if char != currentChar:
            before = currentChar
            currentChar = char
            if count == 0:
                count = 1
                continue
            else:
                output += f" {count} {before}"
                count = 1
        else:
            count += 1
    if count > 0:
        output += f" {count} {currentChar}"
    print(output[1:])
