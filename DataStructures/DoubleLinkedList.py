class Node:
    def __init__(self, val: int = None) -> None:
        self.val = val
        self.left = None
        self.right = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def traverse(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.right
        print("\n")
    
    def insertAtTheTop(self, val) -> None:
        n = Node(val=val)
        if not self.head:
            self.head = n
        else:
            self.head.left = n
            n.right = self.head
            self.head = n
    
    def insertAtTheEnd(self, val) -> None:
        n = Node(val)
        if not self.head:
            self.head = n
        else:
            temp = self.head
            while temp.right is not None:
                temp = temp.right
            temp.right = n
            n.left = temp
            
    
    def insertAfterNode(self, node, val) -> None:
        n = Node(val)
        if not self.head:
            return
        temp = self.head
        while temp != node or temp is not None:
            temp = temp.right
        if not temp:
            return
        temp.right.left = n
        temp.right = n
        n.right = temp.right
        n.left = temp
    
    def insertBeforeNode(self, node, val) -> None:
        n = Node(val)
        if not self.head:
            return
        temp = self.head
        while temp.right != node or temp.right is not None:
            temp = temp.right
        if not temp.right:
            return
        n.right = temp.right
        n.left = temp
        temp.right.left = n
        temp.right = n
    
    def deleteByVal(self, val) -> None:
        if not self.head:
            return
        if self.head.val == val:
            self.head.right.left = None
            self.head = self.head.right
            return
        temp = self.head
        while temp.right is not None:
            if temp.val == val:
                break
            temp = temp.right
        if temp.val != val:
            return
        temp.left.right = temp.right
        if temp.right:
            temp.right.left = temp.left

    def reverse(self) -> Node:
        if not self.head or not self.head.right:
            return
        p = self.head
        q = p.right
        p.right = None
        p.left = q
        while q is not None:
            q.left, q.right = q.right, p
            p, q = q, q.left
        self.head = p


dl = DoubleLinkedList()
dl.insertAtTheTop(2)
dl.insertAtTheTop(3)
dl.insertAtTheTop(5)
dl.insertAtTheEnd(10)
dl.insertAtTheEnd(12)
dl.insertAtTheTop(15)
dl.insertAtTheEnd(20)
dl.traverse()
dl.deleteByVal(10)
dl.traverse()
dl.deleteByVal(15)
dl.deleteByVal(20)
dl.traverse()
dl.reverse()
dl.traverse()