class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.size == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")

print("pass" if (q.size() == 3) else "fail")
q.enqueue("d")
print("pass " if (q.size() == 4) else "fail")

print("pass " if (q.dequeue() == "a") else "fail")
print("pass " if (q.dequeue() == "d") else "fail")
print("pass " if (q.size() == 2) else "fail")

q.show_queue()
