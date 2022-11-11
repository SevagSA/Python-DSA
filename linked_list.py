'''
Singly and doubly linked list implementation
'''
from typing import Iterator, Generator, Any, List


class Node:

    def __init__(self, value: Any, next_node: 'Node' = None, prev_node: 'Node' = None) -> None:
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self) -> str:
        return str(self.value)


class LinkedList:

    def __init__(self, values: Node = None) -> None:
        self.head = None
        self.tail = None
        self.length = 0
        if values is not None:
            self.add_multiple_nodes(values)

    def __str__(self) -> str:
        return ' -> '.join([str(node) for node in self])

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> Generator[Node, None, None]:
        current = self.head
        while current:
            yield current
            current = current.next

    @property
    def values(self) -> List[Node]:
        return [node.values for node in self]

    def add_head(self, value: Node) -> Node:
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        self.length += 1
        return self.head

    def add_tail(self, value: Node) -> Node:
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.length += 1
        return self.tail


def add_multiple_nodes(self, values) -> None:
    for value in values:
        self.add_node(value)


class DoublyLinkedList(LinkedList):
    def add_head(self, value: Node) -> Node:
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            current_head = self.head
            self.head = Node(value, current_head)
            current_head.prev = self.head
        return self.head

    def add_tail(self, value: Node) -> Node:
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
