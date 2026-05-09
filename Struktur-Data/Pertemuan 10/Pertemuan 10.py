# Implementasi Stack dengan Linked List
#1 Membuat kelas Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
# Metode cek is Empty
    def is_empty(self):
        return self.top is None
# Metode push
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
# Metode pop 
    def pop(self):
        return None
    popped_node = self.top
    self.top = self.top.next
    self.size -= 1
    return popped_node.data
# Metode peek / Top
    def peek(self):
    if self.is_empty():
        return None
    return self.top.data
# Metode Display / cetal Tumupukan
    def Display(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next
myStack = Stack()
myStack.is_empty()