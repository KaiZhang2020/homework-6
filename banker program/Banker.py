from Account import Account
from BinarySearch import Node
from BinarySearch import BinaryTree

class banker:
    def __init__(self, transaction_list):
        self.Tree = BinaryTree()
        while transaction_list != None:
            transact = transaction_list.pop(0)
            #divide string
            if transact[0] == 'O':
                self.open(transact[1], transact[2])
            elif transact[0] == 'W' or transact[0] == 'D':
                self.transaction(transact[0], transact[1], transact[2])
            elif transact[0] == 'H':
                self.history(transact[1])
            elif transact[0] == 'T':
                self.transfer(transact[1], transact[2], transact[3])

        # print the results
    # Open
    def open(self, name, acct_num):
        new_acct = Account(name, acct_num)
        self.Tree.add(new_acct)

    def transfer(self, origin, amount, target):
        origin_acct = self.Tree.find(origin)

    def transaction(self, order, acct_num, amount):
        if order == 'W':
            # do stuff
        else:
            # do stuff

    def history(self, acct_num):
        if acct_num > 9999:
            # do stuff
        else:
            # do stuff
