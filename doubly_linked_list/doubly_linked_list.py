class Node:
    def __init__(self, data, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
    def __repr__(self) -> str:
        return self.data                
    
class Linked_list:
    def __init__(self) :
        self.head = None
        self.tail = None
    def insert_at_tail(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data, None, node) 
            self.tail = node.next
        
    def insert_at_head(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data, self.head)
            self.head.prev = node
            self.head = node
    def insert_after(self, next, data):
        node = self.head
        if next == self.tail.data:
            self.insert_at_tail(data)
            return
        elif next == self.head.data:
            self.insert_at_head(data)
            return
        while node is not None:
            if (node.next).data == next:
                node = node.next
                node.next = Node(data, node.next,node)
                return
            else:
                node = node.next

        raise Exception("Node does not exist")

    def print_all(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def print_all_reverse(self):
        node = self.tail
        while node is not None:
            print(node.data)
            node = node.prev
example = Linked_list()
example.insert_at_tail(3)
example.insert_at_tail(2)
example.insert_at_head(1)
example.print_all()
example.insert_after(1, 10)
example.print_all()
