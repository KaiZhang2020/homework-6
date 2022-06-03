from Account import Account
from BinarySearch import BinaryTree

class banker:
    def __init__(self, transaction_list):
        self.Tree = BinaryTree()
        self.AccountList = []
        while len(transaction_list) > 0:
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
        if self.Tree.find(acct_num[0:4]) is not None:
            self.Tree.find(acct_num[0:4]).transHist.append("account already exists, open request refused")
        else:
            new_acct = Account(name, acct_num)
            self.Tree.add(new_acct)
            self.AccountList.append(acct_num[0:4])

    def transfer(self, origin, amount, target):
        if self.Tree.find(origin[0:4]) is None or self.Tree.find(target[0:4]) is None:
            self.Tree.find(origin[0:4]).transHist.append("transfer from account " + origin[0:4] + " to account " + target[0:4] + " failed")
        else:
            fund = origin[4]
            self.Tree.find(origin[0:4]).withdraw(fund, amount)
            fund = target[4]
            self.Tree.find(target[0:4]).deposit(fund, amount)

    def transaction(self, order, acct_num, amount):
        int_amount = int(amount)
        if order == 'W':
            if (self.Tree.find(acct_num[0:4]).total_val() < int_amount):
                self.Tree.find(acct_num[0:4]).transHist.append("W " + acct_num[0:4] + " " + amount + "(failed)")
            elif (acct_num[4] == "1" or "0") and (int_amount > self.Tree.find(acct_num[0:4]).cash_val()):
                self.Tree.find(acct_num[0:4]).transHist.append("W " + acct_num[0:4] + " " + amount + "(failed)")
            elif (acct_num[4] == "2" or "3") and (int_amount > self.Tree.find(acct_num[0:4]).bond_val()):
                self.Tree.find(acct_num[0:4]).transHist.append("W " + acct_num[0:4] + " " + amount + "(failed)")
            else:
                fund_number = acct_num[4]
                self.Tree.find(acct_num[0:4]).transHist.append("W " + acct_num[0:4] + " " + amount)
                self.Tree.find(acct_num[0:4]).withdraw(fund_number, int_amount)
        elif order == 'D':
            fund_number = acct_num[4]
            self.Tree.find(acct_num[0:4]).deposit(fund_number, int_amount)
    def history(self, acct_num):
        if int(acct_num[0:4]) <= 9999:
            self.Tree.find(acct_num[0:4]).histOrder.append("ordered")
        else:
            self.Tree.find(acct_num[0:4]).fundHistOrder.append(acct_num)
