class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addAtHead(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def findNode(self, val):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.val == val:
                return cur_node
            cur_node = cur_node.next

    def findPrevNode(self, val):
        cur_node = self.head
        while cur_node.next is not None:
            if cur_node.next.val == val:
                return cur_node
            cur_node = cur_node.next
        return None

    def append(self, val):
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = Node(val)

    def addAfter(self, prev_val, val):
        prev_node = self.findNode(prev_val)
        new_node = Node(val)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, val):
        prev_node = self.findPrevNode(val)
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next

    def printNodes(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.val, end=' ')
            cur_node = cur_node.next
        print()
    
    
lst = LinkedList()
lst.addAtHead(5)
lst.append(3)
lst.addAfter(5, 2)
lst.printNodes()
lst.delete(2)
lst.printNodes()
lst.addAfter(5, 7)
lst.printNodes()