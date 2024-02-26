# Creating the nodes where are going to link
class Node:
    def __init__(self, data=None):
        self.data = data  # Data: Information to be stored in the list
        self.next = None  # Pointer: To point to the next node in the list


""" 
    [Node: |D|next|] -> [Node: |D|next|] -> [Node: |D|next|] 
    (Head)                                  (Tail)
"""


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)  # creating the new node
        if not self.head:  # If the list is empty then the new node will be the head
            self.head = new_node
            return
        # If the're nodes in the list then you will need to traverse to the end before appending the new node, you do that by creating a last_node at the start of the list(head) then walk it until theres no next node then make that node the new node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        # Intended to insert the first node to the list which is why we're not checking if there is a node beforehand
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAt(self, data, idx):
        if idx == 0 or idx == 1:
            self.prepend(data)
            return

        new_node = Node(data)

        i = 1
        current_node = self.head
        # walking the list until you pointing at the element at the desired idx
        while current_node.next:
            if i >= idx - 1:
                break
            current_node = current_node.next
            i += 1
        # Then the new node will point to that node and the node before it will point to the new node which effectively places the new node between the current_node(1 node behind idx) and current_node.next(node at idx) which makes the new node the new element at idx position. Even if the idx is beyond the current size I'll just append it to the end cause ill always check if there is a next before figuring out if the position exists
        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, data):
        ...

    def removeAt(self, data):
        ...

    def get(self, idx):
        ...

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print('None')


singly_linked = SingleLinkedList()
# Append elements
singly_linked.append(1)
singly_linked.append(2)
singly_linked.append(3)
singly_linked.append(4)
singly_linked.append(5)
singly_linked.prepend(0)
singly_linked.insertAt(69, 0)

singly_linked.print_list()
