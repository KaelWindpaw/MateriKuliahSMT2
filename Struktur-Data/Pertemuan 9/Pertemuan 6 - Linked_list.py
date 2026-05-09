#membuat single linked list (SLI) dengan python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
    def tambah_belakang(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
    def hapus_depan(self):
        if self.head is None:
            print("single linked list kosong")
            return
        self.head = self.head.next

    def hapus_data(self, data):
        current_node = self.head
        previous_node = None

        while current_node:
            if current_node.data == data:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node
                return
            previous_node = current_node
            current_node = current_node.next
        print(f"Data {data} tidak ditemukan.")

# Contoh penggunaan
s11= SingleLinkedList()
s11.tambah_belakang(10)
s11.tambah_belakang(20)  
s11.tambah_belakang(30)
s11.hapus_depan()
s11.hapus_data(21)
print("Isi Linked List:")
s11.display()