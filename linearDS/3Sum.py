nums = [-1, 0, 1, 2, -1, -4, -2]
# 브루트 포스
# 3 수의 합이 0이 되는 3개의 엘리먼트 출력.
"""
def sum(num):
    num.sort()
    answer = []
    for i in range(0, len(num)-2):
        if i > 0 and num[i] == num[i-1]:
            continue
        for j in range(i+1, len(num)-1):
            if j > i+1 and num[j] == num[j-1]:
                continue
            for k in range(j+1, len(num)):
                if k > j+1 and num[k] == num[k-1]:
                    continue
                if num[i] + num[j] + num[k] == 0:
                    answer.append([num[i], num[j], num[k]])
    return answer
"""
# two pointer
def sum(num):
    num.sort()
    answer = []
    for i in range(len(num)):
        if i > 0 and num[i] == num[i - 1]:
            continue
        left, right = i + 1, len(num) - 1
        while left < right:
            sum = num[i] + num[left] + num[right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                answer.append([num[i], num[left], num[right]])
                while left < right and num[left] == num[left + 1]:
                    left += 1
                while left < right and num[right] == num[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return answer

print(sum(nums))
