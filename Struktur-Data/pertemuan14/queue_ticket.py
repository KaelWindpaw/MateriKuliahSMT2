"""
Queue implementation untuk sistem antrian tiket
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """
    Implementasi Queue menggunakan Linked List
    untuk sistem antrian tiket
    """
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def enqueue(self, data):
        """Tambahkan pembeli ke dalam antrian"""
        new_node = Node(data)
        
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1

    def enqueue_sorted(self, data, key):
        """Tambahkan pembeli ke dalam antrian berdasarkan prioritas."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        insertion_value = key(data)
        current = self.head
        previous = None
        while current is not None and key(current.data) <= insertion_value:
            previous = current
            current = current.next

        if previous is None:
            new_node.next = self.head
            self.head = new_node
        else:
            previous.next = new_node
            new_node.next = current
            if current is None:
                self.tail = new_node
        self.size += 1
    
    def dequeue(self):
        """Keluarkan pembeli dari antrian"""
        if self.head is None:
            return None
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        
        if self.head is None:
            self.tail = None
        
        return data
    
    def peek(self):
        """Lihat data pembeli paling depan tanpa mengeluarkannya"""
        if self.head is None:
            return None
        return self.head.data
    
    def is_empty(self):
        """Cek apakah antrian kosong"""
        return self.size == 0
    
    def get_size(self):
        """Dapatkan jumlah pembeli dalam antrian"""
        return self.size
    
    def get_all_queue(self):
        """Dapatkan semua data pembeli dalam antrian"""
        queue_list = []
        current = self.head
        
        while current is not None:
            queue_list.append(current.data)
            current = current.next
        
        return queue_list
    
    def clear(self):
        """Kosongkan antrian"""
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        """String representation dari queue"""
        if self.is_empty():
            return "Queue kosong"
        
        result = "Antrian: "
        current = self.head
        items = []
        
        while current is not None:
            items.append(str(current.data))
            current = current.next
        
        return result + " -> ".join(items)
