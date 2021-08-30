class Node:
    def __init__(self, val: int = None) -> None:
        self.val: int = val
        self.next: Node = None

class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def traverse(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next
        print("\n")
    
    def insertAtTheTop(self, val: int) -> None:
        n = Node(val=val)
        n.next = self.head
        self.head = n

    def insertAtTheEnd(self, val: int) -> None:
        n = Node(val=val)
        temp = self.head
        if not temp:
            self.head = n
            return
        while temp.next is not None:
            temp = temp.next
        temp.next = n
    
    def addNodeToTop(self, n: Node) -> None:
        if not self.head:
            self.head = n
        else:
            n.next = self.head
            self.head = n
    
    def insertBetweenNodes(self, nodeAfter: Node, val: int) -> None:
        if not nodeAfter:
            return
        n = Node(val=val)
        n.next = nodeAfter.next
        nodeAfter.next = n
    
    def remove(self, val: int) -> None:
        if not self.head:
            return
        if self.head.val == val:
            self.head = None
            return
        temp = self.head
        prev = None
        while temp is not None:
            if temp.val == val:
                break
            prev = temp
            temp = temp.next
        if temp and temp.val == val and prev:
            prev.next = temp.next


slist = SingleLinkedList()
slist.insertAtTheTop(3)
slist.insertAtTheTop(2)
slist.insertAtTheEnd(5)
slist.insertAtTheEnd(10)
slist.insertAtTheTop(7)
slist.traverse()
slist.remove(5)
slist.traverse()
slist.remove(-1)
slist.traverse()
n1 = Node(val=13)
slist.addNodeToTop(n1)
n2 = Node(val=21)
slist.addNodeToTop(n2)
slist.traverse()
slist.insertBetweenNodes(nodeAfter=n2, val=65)
slist.traverse()
