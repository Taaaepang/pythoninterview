from collections import deque
class node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self, data):
        self.head = node(data)
    def add(self, data):
        if self.head is None:
            self.head = node(data)
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = node(data)
    def view(self):
        n = self.head
        while n is not None:
            print(n.data)
            n = n.next
    def linkedToList(self):
        a = []
        n = self.head
        while n is not None:
            a.append(n.data)
            n = n.next
        return a
link1 = linkedlist(1)
link1.add(2)

link2 = linkedlist(1)
link2.add(2)
link2.add(2)
link2.add(1)

# list 변환
'''
def palindrome(link):
    q = []

    if link.head is None:
        return True

    q = link.linkedToList()

    while len(q)>1:
        if q.pop(0) != q.pop():
            return False
    return True
'''
# deque 활용.
'''
def palindrome(link):
    q = deque(link.linkedToList())

    while len(q) >1:
        if q.popleft() != q.pop():
            return False
    return True
'''

# runner 활용
def palindrome(link):
    rev = None
    fast = slow = link.head

    if link.head is None:
        return True

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    while rev and rev.data == slow.data:
        slow, rev = slow.next, rev.next
    return not rev

print(palindrome(link1))
print(palindrome(link2))