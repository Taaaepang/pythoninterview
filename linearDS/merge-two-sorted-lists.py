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
link1.add(4)

link2 = linkedlist(1)
link2.add(3)
link2.add(4)

def merge_two_link(l1, l2):
    if not l1 or l2 and l1.data > l2.data:
        l1, l2 = l2, l1
    if l1:
        l1.next = merge_two_link(l1.next, l2)
    return l1

link = merge_two_link(link1.head, link2.head)

while link is not None:
    print(link.data, end=' ')
    link = link.next
