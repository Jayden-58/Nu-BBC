class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("head node created: ", self.head.value)
            return
        
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node
        print("Appended new Node with value: ", node.next.value)

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Head Node created: ", self.head.value)
            return
        self.head.prev = new_node
        self.head = new_node
        print("success! prepended a new head node with value: ", self.head.value)

llist = LinkedList()
llist.prepend("first node")
llist.prepend("Inserted new first node")
