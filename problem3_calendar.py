from typing import Optional


class Node:
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def insert(self, node: 'Node') -> bool:
        # Check for overlap
        if node.end > self.start and node.start < self.end:
            return False

        # Place in left subtree
        if node.end <= self.start:
            if not self.left_child:
                self.left_child = node
                return True
            return self.left_child.insert(node)

        # Place in right subtree
        if node.start >= self.end:
            if not self.right_child:
                self.right_child = node
                return True
            return self.right_child.insert(node)
        return False


class Calendar:
    def __init__(self):
        self.root: Optional[Node] = None

    def book(self, start: int, end: int) -> bool:
        new_event = Node(start, end)
        if self.root is None:
            self.root = new_event
            return True
        return self.root.insert(new_event)
