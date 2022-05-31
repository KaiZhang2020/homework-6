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
            if transact[0] == "O":
                self.open(transact[2] + " " + transact[1], transact[3][0:4])
            elif transact[0] == "W" or transact[0] == "D":
                self.transaction(transact[0], transact[1], transact[2])
            elif transact[0] == "H":
                self.history(transact[1])
            elif transact[0] == "T":
                self.transfer(transact[1], transact[2], transact[3])

        # print the results
    # Open
    def open(self, name, acct_num):
        new_acct = Account(name, acct_num)
        self.Tree.add(new_acct)

    def transfer(self, origin, amount, target):
        # break origin string
        origin_acct = self.Tree.find(origin[0:4])
        # target the fund account
        fund = origin[4]
        origin_acct.withdraw(fund, amount)
        # break target string
        target_acct = self.Tree.find(target[0:4])
        # target the fund account for target
        fund = origin[4]
        target_acct.withdraw(fund, amount)

    def transaction(self, order, acct_num, amount):
        int_amount = int(amount)
        if order == 'W':
            fund_number = acct_num[4]
            self.Tree.find(acct_num[0:4]).transHist.append("W " + acct_num + amount)
            self.Tree.find(acct_num[0:4]).withdraw(fund_number, int_amount)
        elif order == 'D':
            fund_number = acct_num[4]
            self.Tree.find(acct_num[0:4]).deposit(fund_number, int_amount)
    def history(self, acct_num):
        if acct_num > 9999:
            self.Tree.find(acct_num).history()
        else:
            account_number = acct_num[0:4]
            fund_number = acct_num[4]
            self.Tree.find(account_number).fundHistory(fund_number)
