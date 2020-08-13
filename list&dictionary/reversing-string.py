'''
two pointer
def reverseString(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
'''

'''
python reverse

def reversString(s):
    s.reverse()
'''