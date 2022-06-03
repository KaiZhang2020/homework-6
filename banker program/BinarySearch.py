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
                node.right = Node(data)

    def find(self, data):
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, target, node):
        if target == node.data.number:
            return node.data
        elif target < node.data.number and node.left is not None:
            return self._find(target, node.left)
        elif target > node.data.number and node.right is not None:
            return self._find(target, node.right)
        else:
            return None

    def succesorHelper(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.data
    
    def predecessorHelper(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.data

    def removeNode(self, root, key):
        if not root:
            return root
        
        if key < root.data:
            root.left = self.removeNode(root.left, key)
        
        elif key > root.data:
            root.right = self.removeNode(root.right, key)

        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.data = self.succesorHelper(root)
                root.right = self.removeNode(root.right, root.data)
            else:
                root.data = self.predecessorHelper(root)
                root.left = self.removeNode(root.left, root.data)
        return root