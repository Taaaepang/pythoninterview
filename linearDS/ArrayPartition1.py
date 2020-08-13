# 오름차순.

# n개의 페어에서 min(a,b) 의 합이 최대가 되게.
"""
num = [1, 4, 3, 2]
num.sort()

sum_num = []

for i in range(0, len(num)-1, 2):
    sum_num.append(min(num[i], num[i+1]))
print(sum(sum_num))
"""
# 짝수번째 수를 더하자.
"""
num = [1, 4, 3, 2]
num.sort()

even = []

for i in range(0, len(num), 2):
    even.append(num[i])
print(sum(even))
"""

# python 답게.

num = [1, 4, 3, 2]
print(sum(sorted(num)[::2]))






