class Human:
    def __init__(self, name=None):
        self.name = name
        self.next = None

        # Queue specific pointers
        self.front = None
        self.tail = None


class DaboQueue:
    def __init__(self):
        self.head = None

    def dequeue(self):
        if not self.head:
            return
        removed_human = self.head
        self.head = removed_human.next
        self.front = self.head

    def enqueue(self, name):
        new_human = Human(name)
        if not self.head:
            self.head = new_human
            self.front = new_human
            self.tail = new_human
            return

        else:
            self.tail.next = new_human
            self.tail = new_human

    def peek(self):
        if self.head:
            print(self.head.name)
            return
        print("None")

    def see_self(self):
        current_human = self.head
        while current_human:
            print(current_human.name, end=" --> ")
            current_human = current_human.next
        print("None")


dabo_self = DaboQueue()

dabo_self.enqueue("Mathew")
dabo_self.enqueue("Mark")
dabo_self.enqueue("Luke")
dabo_self.enqueue("John")

dabo_self.dequeue()
dabo_self.see_self()
dabo_self.dequeue()
dabo_self.see_self()
dabo_self.dequeue()
dabo_self.see_self()
