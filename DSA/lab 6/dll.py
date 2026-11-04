class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create(self):
        n = int(input("Enter number of nodes: "))
        for i in range(n):
            data = int(input("Enter data: "))
            new_node = Node(data)
            if self.head is None:
                self.head = self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index")
            return
        if index == 0:
            self.insert_at_beginning(data)
            return
        temp = self.head
        for i in range(index - 1):
            if temp is None:
                print("Invalid index")
                return
            temp = temp.next
        if temp is None:
            print("Invalid index")
            return
        if temp.next is None:
            self.insert_at_end(data)
            return
        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

    def delete_at_index(self, index):
        if self.head is None or index < 0:
            print("Invalid index")
            return
        temp = self.head
        for i in range(index):
            if temp is None:
                print("Invalid index")
                return
            temp = temp.next
        if temp is None:
            print("Invalid index")
            return
        if temp.prev is None:
            self.head = temp.next
        else:
            temp.prev.next = temp.next
        if temp.next is None:
            self.tail = temp.prev
        else:
            temp.next.prev = temp.prev

    def delete_value(self, data):
        temp = self.head
        index = 0
        while temp is not None and temp.data != data:
            temp = temp.next
            index += 1
        if temp is None:
            print("Value not found")
            return
        self.delete_at_index(index)

    def count(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        print("Total number of nodes:", count)

    def display_forward(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.tail
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

def main():
    dll = DoublyLinkedList()
    while True:
        print("\n1.Create  2.Insert beginning  3.Insert end  4.Insert index")
        print("5.Delete value  6.Delete index  7.Count  8.Display forward")
        print("9.Display backward  10.Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            dll.create()
        elif choice == 2:
            dll.insert_at_beginning(int(input("Enter data: ")))
        elif choice == 3:
            dll.insert_at_end(int(input("Enter data: ")))
        elif choice == 4:
            dll.insert_at_index(int(input("Enter index: ")), int(input("Enter data: ")))
        elif choice == 5:
            dll.delete_value(int(input("Enter value: ")))
        elif choice == 6:
            dll.delete_at_index(int(input("Enter index: ")))
        elif choice == 7:
            dll.count()
        elif choice == 8:
            dll.display_forward()
        elif choice == 9:
            dll.display_backward()
        elif choice == 10:
            break
        else:
            print("Invalid choice")

main()
