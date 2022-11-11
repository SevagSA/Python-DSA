'''
Binary search tree (BST) implementation
'''
from typing import Any


class Node():

    def __init__(self, data: Any) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree():

    def __init__(self) -> None:
        self.root = None

    def insert(self, data: Any) -> None:
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data: Any, cur_node: Node) -> None:
        '''
        Insert a node by respecting the order of the BST (smaller value to the left,
        grater value to the right, insert where it's null).
        This is a helper function for `insert()`.

        :param Any data: the data that is being inserted.
        :param Node cur_node: the node being evaluated against `data` to determine if it
            is greater or smaller.
        '''
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            raise ValueError('Value is already present in the tree.')

    def find(self, data: Any) -> bool:
        '''
        Find node with the given `data` element

        :returns bool: `True` if found, `False` if not found or tree is empty
        '''
        if self.root:
            return self._find(data, self.root)
        return False

    def _find(self, data: Any, cur_node: Node) -> bool:
        '''
        Find a node with a given value.
        This is a helper function for `find()`.

        :param Any data: the data that is being found.
        :param Node cur_node: the node being evaluated against `data`.
        :returns bool: `True` if found, `False` otherwise
        '''
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True  # Alternatively, return cur_node

    def print_tree(self, traversal_type: str) -> None:
        if traversal_type == 'preorder':
            self.preorder_print(self.root)
        elif traversal_type == 'inorder':
            self.inorder_print(self.root)
        elif traversal_type == 'postorder':
            self.postorder_print(self.root)
        else:
            raise ValueError(
                'Invalid print type. Choose from "preorder", "inorder" or "postorder"')
        print()

    def preorder_print(self, start: Node) -> None:
        '''Root -> Left -> Right'''
        if start:
            print(f'{start.data} ', end='')
            self.preorder_print(start.left)
            self.preorder_print(start.right)

    def inorder_print(self, start: Node) -> None:
        '''Left -> Root -> Right'''
        if start:
            self.inorder_print(start.left)
            print(str(start.data) + ' ', end='')
            self.inorder_print(start.right)

    def postorder_print(self, start: Node) -> None:
        '''Left -> Right -> Root'''
        if start:
            self.inorder_print(start.left)
            self.inorder_print(start.right)
            print(str(start.data) + ' ', end='')


bst = BinarySearchTree()
bst.insert(64)
bst.insert(657)
bst.insert(23)
bst.insert(7)
bst.insert(35)
bst.insert(75)
bst.insert(10)
bst.print_tree("inorder")
bst.print_tree("postorder")
bst.print_tree("preorder")
print(bst.find(64))
print(bst.find(657))
print(bst.find(23))
print(bst.find(7))
print(bst.find(35))
print(bst.find(75))
print(bst.find(10))
