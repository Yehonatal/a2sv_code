class Book:
    def __init__(self, title=None):
        self.title = title


class BookAzori:
    def __init__(self):
        ...

    def push(self, title):
        ...

    def pop(self):
        ...

    def peek(self):
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
