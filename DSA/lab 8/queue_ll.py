class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(data, "inserted into queue")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            print(data, "deleted from queue")

    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

q = Queue()
while True:
    print("\n1.Enqueue  2.Dequeue  3.Peek  4.Display  5.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        q.enqueue(int(input("Enter item: ")))
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.peek()
    elif choice == 4:
        q.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
