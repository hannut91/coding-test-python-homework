# Happy or Sad - https://dmoj.ca/problem/ccc15j2

HAPPY_FACE_CHARACTER = ":-)"
SAD_FACE_CHARACTER = ":-("

text = input()

happyFaceCharacterCount = text.count(HAPPY_FACE_CHARACTER)
sadFaceCharacterCount = text.count(SAD_FACE_CHARACTER)

if happyFaceCharacterCount == 0 and sadFaceCharacterCount == 0:
    print("none")
elif happyFaceCharacterCount == sadFaceCharacterCount:
    print("unsure")
elif happyFaceCharacterCount > sadFaceCharacterCount:
    print("happy")
else:
    print("sad")
