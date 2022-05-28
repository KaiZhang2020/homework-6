class Account:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        # fund acounts
        self.zero = 0
        self.one = 0
        self.two = 0
        self.three = 0
        self.four = 0
        self.five = 0
        self.six = 0
        self.seven = 0
        self.eight = 0
        self.nine = 0
        self.transHist = []
        self.transHist.append("O " + "name " + number)
    def total_val(self):
        return (self.zero + self.one + self.two + self.three + 
        self.four + self.five + self.six + self.seven + self.eight +
        self.nine)
    def deposit(self, fund, amount):
        if fund == "1":
            self.one += amount
        elif fund == "2":
            self.two += amount
        elif fund == "3":
            self.three += amount
        elif fund == "4":
            self.four += amount
        elif fund == "5":
            self.five += amount
        elif fund == "6":
            self.six += amount
        elif fund == "7":
            self.seven += amount
        elif fund == "8":
            self.eight += amount
        elif fund == "9":
            self.nine += amount
        else:
            print("error")
    def withdraw(self, fund, amount):
        if amount > self.total_val():
            print("insufficient funds")
        else:
            if fund == "1":
                if amount > fund:
                    amount -= self.one
                    self.one = 0
                    self.withdraw("2", amount)
                else:
                    self.one -= amount 
            elif fund == "2":
                if amount > fund:
                    amount -= self.two
                    self.two = 0
                    self.withdraw("3", amount)
                else:
                    self.two -= amount
            elif fund == "3":
                if amount > fund:
                    amount -= self.three
                    self.three = 0
                    self.withdraw("4", amount)
                else:
                    self.three -= amount
            elif fund == "4":
                if amount > fund:
                    amount -= self.four
                    self.four = 0
                    self.withdraw("5", amount)
                else:
                    self.four -= amount
            elif fund == "5":
                if amount > fund:
                    amount -= self.five
                    self.five = 0
                    self.withdraw("6", amount)
                else:
                    self.five -= amount
            elif fund == "6":
                if amount > fund:
                    amount -= self.six
                    self.six = 0
                    self.withdraw("7", amount)
                else:
                    self.six -= amount
            elif fund == "7":
                if amount > fund:
                    amount -= self.seven
                    self.seven = 0
                    self.withdraw("8", amount)
                else:
                    self.seven -= amount
            elif fund == "8":
                if amount > fund:
                    amount -= self.seven
                    self.seven = 0
                    self.withdraw("9", amount)
                else:
                    self.eight -= amount
            elif fund == "9":
                if amount > fund:
                    amount -= self.nine
                    self.nine = 0
                    self.withdraw("1", amount)
                else:
                    self.nine -= amount
            else:
                print("error")
    def transfer(self, origin, amount, target):

    def history(self):

    def fundHistory(self, fund):

    def __lt__(self, other):
        return self.number < other.number

    def __eq__(self, other):
        return self.number == other.number

    def __gt__(self, other):
        return self.number > other.number

    def __le__(self, other):
        return self.number <= other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __ne__(self, other):
        return self.number != other.number
    

    
