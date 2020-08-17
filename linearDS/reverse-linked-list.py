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

link = linkedlist(1)
link.add(2)
link.add(3)
link.add(4)
link.add(5)
'''
def reverselist(linkhead):
    def reverse(node, prev=None):
        if not node:
            return prev
        n, node.next = node.next, prev
        return reverse(n, node)

    return reverse(linkhead)
'''
'''
node = 1, prev=None   n : 2   node.next = None
node = 2, prev=1     
'''
def reverselist(linkhead):
    node, prev = linkhead, None

    while node:
        n, node.next = node.next, prev
        prev, node = node, n

    return prev

link = reverselist(link.head)

while link is not None:
    print(link.data, end=' ')
    link = link.next