class Node:
    """
    Node inside all the double linked Listd
    """
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value
    
    def __str__(self):
        return f'{self.val} \n'



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
            node.prev = self.tail
            self.tail = node
            self.size +=1
        print(f'Current Head -- {self.head} -- Current tail {self.tail}')

    def __remove_node(self, node: Node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        self.size -=1

    def remove_last_element(self):
        if self.tail is not None:
            self.__remove_node(self.tail)




    def delete(self, val):
        node = self.head
        while node is not None:
            if node.val == val:
                self.__remove_node(node)
            node = node.next



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