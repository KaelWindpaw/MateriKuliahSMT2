# Mmebuat QUEUE DARI LINKDE LIST
# 1 BUAT KELAS NODE
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Membuat kelas MyQueue
class MyQueue:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0
# Mmebuat Method enqueue
    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty() is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print (f"Enqueued {data}")
# Membuat Metode Dequeue
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            print("Queue is empty")
            return data
# Metode untuk mengecek apakah queue kosong atau tidak
    def isEmpty(self):
        return self.size == 0
# Metode untuk mengecek queue
    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        current = self.head
        print("Queue: ", end="")
        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")