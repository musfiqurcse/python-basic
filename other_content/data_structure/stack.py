# python stack program
# Author Musfiqur Rahma
class Stack:
    def __init__(self, length: int) -> None:
        self.top_point =  -1
        self.stack = [None for i in range(length)]

    def push(self, element):
        self.top_point = self.top_point + 1
        self.stack[self.top_point] = element

    def pop(self):
        last_element = self.stack[self.top_point]
        self.top_point = self.top_point - 1
        return last_element

    def peek(self):
        return self.stack[self.top_point]
    
    def is_empty(self):
        return self.top_point == -1