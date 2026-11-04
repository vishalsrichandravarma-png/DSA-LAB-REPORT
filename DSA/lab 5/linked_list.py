class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input("Enter the number of the nodes: "))
        for i in range(n):
            data = int(input("enter the data for node : "))
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"Total number of nodes: {count}")

    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next:
                current = current.next  
            current.next = new_node

    def insert_at_index(self, index, data):
        if index < 0:
            print("Index cannot be negative.")
            return
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(index - 1):
            if current is None:
                print("Index out of bounds.")
                return
            current = current.next
        if current is None:
            print("Index out of bounds.")
            return
        new_node.next = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_index(self, index):
        if index < 0:
            print("Index cannot be negative.")
            return
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            if current is None or current.next is None:
                print("Index out of bounds.")
                return
            current = current.next
        if current.next is None:
            print("Index out of bounds.")
            return
        current.next = current.next.next

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def searching(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                print(f"Data {data} found at index {index}.")
                return
            current = current.next
            index += 1
        print(f"Data {data} not found in the list.")

    def sorting(self):
        if self.head is None:
            return
        current = self.head
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next

def main():
    linked_list = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Create Linked List")
        print("2. Display Linked List")
        print("3. Insert at Beginning")
        print("4. Insert at End")
        print("5. Insert at Index")
        print("6. Delete at Beginning")
        print("7. Delete at End")
        print("8. Delete at Index")
        print("9. Search for an Element")
        print("10. Count Nodes")
        print("11. Delete a specific element")
        print("12. Sort the linked list")
        print("13. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            linked_list.create()
        elif choice == 2:
            linked_list.display()
        elif choice == 3:
            data = int(input("Enter data to insert at beginning: "))
            linked_list.insert_at_beginning(data)
        elif choice == 4:
            data = int(input("Enter data to insert at end: "))
            linked_list.insert_at_end(data)
        elif choice == 5:
            index = int(input("Enter index to insert at: "))
            data = int(input("Enter data to insert: "))
            linked_list.insert_at_index(index, data)
        elif choice == 6:
            linked_list.delete_at_beginning()
        elif choice == 7:
            linked_list.delete_at_end()
        elif choice == 8:
            index = int(input("Enter index to delete at: "))
            linked_list.delete_at_index(index)
        elif choice == 9:
            data = int(input("Enter data to search for: "))
            linked_list.searching(data)
        elif choice == 10:
            linked_list.count()
        elif choice == 11:
            data = int(input("Enter data to delete: "))
            linked_list.delete(data)
        elif choice == 12:
            linked_list.sorting()
        elif choice == 13:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()