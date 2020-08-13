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

    def reverselist(self):
        def reverse(node, prev=None):
            if not node:
                 return prev
            n, node.next = node.next, prev
            return reverse(n,node)
        self.head = reverse(self.head)

link = linkedlist(1)
link.add(2)
link.add(3)
link.add(4)

# 값만 교환
'''
def swapPairs(head):
    cur = head

    while cur and cur.next:
        cur.data, cur.next.data = cur.next.data, cur.data
        cur = cur.next.next
    return head
'''

def swapPairs(head):
    root = prev = node(None)
    prev.next = head
    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head

        prev.next = b

        head = head.next
        prev = prev.next.next
    return root.next


answer = swapPairs(link.head)

while answer:
    print(answer.data, end=' ')
    answer = answer.next