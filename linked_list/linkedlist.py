class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next
    def __repr__(self) -> str:
        return self.data                
    
class Linked_list:
    def __init__(self) :
        self.head = None

    def insert_at_tail(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data) 
        
    def insert_at_head(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = Node(data, self.head)
            self.head = node
    def insert_after(self, next, data):
        node = self.head
        while node is not None:
            if (node.next).data == next:
                node = node.next
                node.next = Node(data, node.next)
                return
            raise Exception("Node does not exist")

    def print_all(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
example = Linked_list()
example.insert_at_head(4)
example.insert_at_tail(3)

example.insert_after(3,2)

example.print_all()# 4, 3, 2
