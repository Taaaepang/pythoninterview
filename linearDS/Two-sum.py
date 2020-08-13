nums = [2, 7, 11, 15]
target = 9
# 두 수의 합이 target
# bruteforce
'''
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
'''

# in 을 이용한 탐색.
'''
def twoSum(nums, target):
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in nums[i+1:]:
            return i, nums[i+1:].index(complement) + (i+1)
'''

# 첫번째 수를 뺀 결과 키 조회.
dic = {}
for i, num in enumerate(nums):
    dic[num] = i

for i in range(len(nums)):
    if target - nums[i] in dic and i != dic[target-nums[i]]:
        print(i, dic[target-nums[i]])
        break





