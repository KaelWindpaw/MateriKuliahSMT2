# membuat quite sederhana dengan menggunakan list

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

# membuat metode enqueue
    def enqueue(self, data):
        new_node = node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print(f"Enqueued: {data}")

# membuat metode dequeue
    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        print(f"Dequeued: {data}")
        return data

    def peek(self):
        if self.head is None:
            print("Queue is empty")
            return None
        return self.head.data

    def is_empty(self):
        return self.size == 0

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        queue_elements = []
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


antrian = MyQueue()
antrian.enqueue("Andi")
antrian.enqueue("Budi")
antrian.enqueue("Caca")
antrian.print_queue()
antrian.peek()
antrian.dequeue()