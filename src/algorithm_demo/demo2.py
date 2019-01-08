class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def peek(self):
        if self.node != None:
            val = self.node.val
            self.top
        else:
            return None

    def push(self, val):
        node = Node(val=val)
        node.next = self.top
