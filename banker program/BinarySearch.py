# To finish:
# Modify the BinarySearch so that i can find the account using just
# the account number

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.rightight = Node(data)

    def find(self, data):
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, target, node):
        if target == node.data.number:
            return node
        elif (target < node.data.number and node.left is not None):
            return self._find(target, node.left)
        elif (target > node.data.number and node.right is not None):
            return self._find(target, node.right)