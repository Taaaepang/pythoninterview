from collections import deque
import re


# 일반 for 문

sentence = str(input())
onlyChar = []
for char in sentence:
    if char.isalnum():
        onlyChar.append(char.lower())

while len(onlyChar) > 1:
    if onlyChar.pop(0) != onlyChar.pop():
        print('False')


# deque 선언.
onlyChar = deque()

# slicing 이용. 정규표현식
sentence = sentence.lower()
s = re.sun('[^a-z0-9]','', sentence)

#return sentence == sentence[::-1]
