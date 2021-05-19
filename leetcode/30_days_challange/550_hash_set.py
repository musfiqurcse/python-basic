class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        #self.data = {}
        

    def add(self, key: int) -> None:
        self.data.append(key)
        #self.data[key]=key
        

    def remove(self, key: int) -> None:
        while key in self.data:
            self.data.remove(key)
        # if key in self.data:
        #    del self.data[key]
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.data
        # return key in self.data
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
