"""
To Complete:
    - divide and read string, and put that in the transaction class
"""

from Account import Account
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
        # break origin string
        origin_acct = self.Tree.find(origin)
        # target the fund account
        fund = origin.charAt(4)
        origin_acct.withdraw(fund, amount)
        # break target string
        target_acct = self.Tree.find(target)
        # target the fund account for target
        fund = origin.charAt(4)
        target_acct.withdraw(fund, amount)

    def transaction(self, order, acct_num, amount):
        if order == 'W':
            self.Tree.find(acct_num).transHist.append("W " + acct_num + amount)
            # do stuff
        elif order == 'D':
            account_number = acct_num[0:4]
            fund_number = acct_num.charAt(4)
            self.Tree.find(account_number).deposit(fund_number, amount)

    def history(self, acct_num):
        if acct_num > 9999:
            self.Tree.find(acct_num).history()
        else:
            account_number = acct_num[0:4]
            fund_number = acct_num.charAt(4)
            self.Tree.find(account_number).fundHistory(fund_number)
