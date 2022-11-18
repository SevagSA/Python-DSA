'''
Linked list reversal algorithm implementation
'''

from typing import Any


class Node:

    def __init__(self, value: Any, next_node: 'Node' = None, prev_node: 'Node' = None) -> None:
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self) -> str:
        return str(self.value)


def reverse_linked_list(node: Node):
    '''
    Reverses a singly linked list

    :param Node node: the node pointing to the linked list that
        will be reversed
    '''
    if not node or not node.next:
        return node

    previous = reverse_linked_list(node.next)
    node.next.next = node
    node.next = None
    return previous
