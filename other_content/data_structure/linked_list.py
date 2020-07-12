class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value



class DoubleLinkedList:


    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def insert(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size +=1
        else:
            self.tail.next = node
            node.prev = self.head
            self.tail = node
            self.size +=1


    def __str__(self):
        val = []
        node = self.head
        while node is not None:
            val.append(str(node.val))
            node = node.next
        return f"Final value [{', '.join(val)}]"







my_list = DoubleLinkedList()
my_list.insert(5)
my_list.insert(50)
my_list.insert(2)