class Book:
    def __init__(self, title=None):
        self.title = title
        self.prev = None


class BookAzori:
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, title):
        new_title = Book(title)
        self.size += 1
        if not self.head:
            self.head = new_title
            return

        new_title.prev = self.head
        self.head = new_title

    def pop(self):
        self.size = max(0, self.size - 1)

        if self.size == 0:
            current_top = self.head
            self.head = None
            return

        current_top = self.head
        del self.head
        self.head = current_top.prev

    def peek(self):
        if self.head:
            print(self.head.title)
        else:
            print("None")
        ...

    def see_books(self):
        ...


book_stack = BookAzori()

book_stack.push("Dune")
book_stack.push("Dune 2")
book_stack.push("Dune 3")
book_stack.peek()
book_stack.pop()
book_stack.peek()
book_stack.push("Dune 4")
book_stack.push("Dune 5")
book_stack.peek()
book_stack.see_books()
