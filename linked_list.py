"""
Corey Verkouteren
12/2024
singly vs double linked list
"""
class SNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class DNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.back = None


class SinglyLinkedList:
    def __init__(self):
        self.header = None

    def insert(self, value):
        new_node = SNode(value)
        next = self.header

        while next:
            next = next.next

        next.next = new_node

    def delete(self, value):
        n_node = self.header
        l_node = None
        while n_node.value != value and n_node:
            l_node = n_node
            n_node = n_node.next

        if not n_node:
            return False

        l_node.next = n_node.next


class DoublyLinkedList:
    def __init__(self):
        self.header = None
        self.footer = None

    def insert_back(self, value):
        new_node = DNode(value)
        self.footer.next = new_node
        self.footer = new_node

    def insert_front(self, value):
        new_node = DNode(value)
        new_node.next = self.header
        self.header = new_node

    def delete(self, value):
        n_node = self.header
        l_node = None
        while n_node.value != value and n_node:
            l_node = n_node
            n_node = n_node.next

        if not n_node:
            return False

        l_node.next = n_node.next
        n_node.next.back = l_node

    def extract_front(self):
        hold = self.header
        self.header = self.header.next
        self.header.back = None

        return hold

    def extract_last(self):
        hold = self.footer
        self.footer = self.footer.back
        self.footer.next = None

        return hold