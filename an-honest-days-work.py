# An Honest Day's Work - https://dmoj.ca/problem/wc18c3j1

p = int(input())
b = int(input())
d = int(input())

badgeCount = p // b
remainPaint = p % b

print(badgeCount * d + remainPaint)
