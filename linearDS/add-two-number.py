from functools import reduce

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
link1 = linkedlist(2)
link1.add(4)
link1.add(3)

link2 = linkedlist(5)
link2.add(6)
link2.add(4)

link1.reverselist()
link2.reverselist()

l1 = link1.linkedToList()
l2 = link2.linkedToList()

#answer = int(''.join(str(e) for e in l1)) + int(''.join(str(e) for e in l2))
answer = reduce(lambda x, y: 10*x+y, l1, 0) + reduce(lambda x, y: 10*x+y, l2, 0)
print(answer)




