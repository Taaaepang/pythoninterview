import sys

num = [7, 1, 5, 3, 6, 4]
# 브루트 포스
'''
max_price = 0
for idx, price in enumerate(num):
    for j in range(idx, len(num)):
        max_price = max(max_price, num[j] - price)
'''
# 저점과 현재 값의 계산.
profit = 0
min_price = sys.maxsize
for i in range(len(num)):
    min_price = min(min_price, num[i])
    profit = max(profit, num[i] - min_price)
print(profit)