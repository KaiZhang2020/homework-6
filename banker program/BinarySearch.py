class Node:
    def __init__(self, data, account_info):
        self.left = None
        self.right = None
        self.data = data
        self.account = account_info
    def insert(self, data, account_info):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data, account_info)
            else:
               self.left.insert(data, account_info)
         elif data > self.data:
            if self.right is None:
               self.right = Node(data, account_info)
            else:

               self.right.insert(data, account_info)
      else:
         self.data = data
         self.account_info = account_info
