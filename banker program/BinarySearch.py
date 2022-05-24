class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

class BinarySearchTree: