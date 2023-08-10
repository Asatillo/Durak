class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# TODO: node delition
# TODO: node insertion

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.current_val = None
        self.previous_node = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("...")

    def next(self):
        if not self.head:
            return None

        if self.current_val is None:
            self.current_val = self.head

        self.previous_node = self.current_val
        self.current_val = self.current_val.next
        return self.current_val.data
    
    def get_next_node(self):
        if self.current_val is None:
            return None

        return self.current_val.next.data

    def get_previous_node(self):
        if self.previous_node is None:
            return None

        return self.previous_node.data
