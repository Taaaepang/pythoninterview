import re
from collections import Counter


'''
banned에 있는 문자열을 제외한 가장 많은 문자열.
정규식을 이용하여 문자가 아닌 부분을 다 공백으로 만든후,
리프리헨션으로 banned에 있지 않은 문자열을 뽑아낸 후,
카운터로 계산하자.
'''
paragraph = "Bob hit a ball, the hit Ball flow far after it was hit."
banned = ["hit"]
words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

answer = Counter(words).most_common()[0][0]
print(answer)