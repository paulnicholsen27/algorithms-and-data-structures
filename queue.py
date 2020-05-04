class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None


    def is_empty(self):
        return not self.head 

    def peek(self):

        return self.head.data 

    def add(self, node):
        if not self.head:
            self.head = node 
            self.tail = node 
        else:
            self.tail.next = node 
            self.tail = node 

    def remove(self):
        node = self.head
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return node


class Stack:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return not self.head

    def push(self, node):
        if self.head:
            node.next = self.head 
            self.head = node
        else:
            self.head = node 
            self.tail = node

    def pop(self):
        if not self.head:
            return None
        node = self.head 
        self.head = node.next
        node.next = None
        if not self.head:
            self.tail = None
        return node

            

    def peek(self):
        return self.head.data if self.head else None


n1 = Node(5)
n2 = Node(51)

s1 = Stack()

print(s1.is_empty())

s1.push(n1)
print(not s1.is_empty())

print(s1.peek() == n1.data)

s1.push(n2)
print(s1.peek() == n2.data)

print(s1.pop() == n2)
print(s1.peek() == n1.data)
