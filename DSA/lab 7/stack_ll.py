class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed into stack")

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            item = self.top.data
            self.top = self.top.next
            print(item, "popped from stack")

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

s = Stack()
while True:
    print("\n1.Push  2.Pop  3.Peek  4.Display  5.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        s.push(int(input("Enter item: ")))
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 4:
        s.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
