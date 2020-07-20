class Node:
    def __init__(self, val, next = None):
        self.next = next
        self.val = val




class SingleLinkedList:

    def __init__(self, head = None):
        self.head = head
        self.node = None

    def __repr__(self) :
        """
        Return a string representation of the list
        Takes O(n) times.
        """
        nodes = []
        recent = self.head
        while recent:
            nodes.append(str(recent.val))
            recent = recent.next
        return ' ,'.join(nodes)

    
    def append(self, val: int):
        """
        Appending value in linked list
        """
        new_node = Node(val)
        head_item = self.head
        if head_item:
            while head_item.next:
                head_item = head_item.next
            head_item.next = new_node
        else:
            self.head = new_node


    def pop(self, val: int):
        head_item = self.head
        prev =  None
        while head_item:
            if head_item.val == val:
                if prev == None:
                    self.head =head_item.next
                else:
                    prev.next = head_item.next
                    head_item = prev
            prev = head_item
            head_item = head_item.next
        




if __name__ == "__main__":
    nd = SingleLinkedList()
    nd.append(10)
    print(repr(nd))
    nd.pop(10)
    print(repr(nd))
    nd.append(10)
    nd.append(11)
    nd.append(12)
    print(repr(nd))
    nd.pop(11)
    print(repr(nd))
    nd.append(13)
    nd.append(14)
    nd.append(10)
    print(repr(nd))
    nd.pop(10)
    print(repr(nd))
