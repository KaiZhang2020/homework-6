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
        self.zeroHist = []
        self.oneHist = []
        self.twoHist = []
        self.threeHist = []
        self.fourHist = []
        self.fiveHist = []
        self.sixHist = []
        self.sevenHist = []
        self.eightHist = []
        self.nineHist = []

        self.transHist.append("O " + "name " + number)
    def total_val(self):
        return (self.zero + self.one + self.two + self.three + 
        self.four + self.five + self.six + self.seven + self.eight +
        self.nine)
    def deposit(self, fund, amount):
        self.transHist.append("D " + self.number + fund + " " + amount)
        if fund == "1":
            self.one += amount
            self.oneHist.append("D " + fund + amount)
        elif fund == "2":
            self.two += amount
            self.twoHist.append("D " + fund + amount)
        elif fund == "3":
            self.three += amount
            self.threeHist.append("D " + fund + amount)
        elif fund == "4":
            self.fourHist.append("D " + fund + amount)
            self.four += amount
        elif fund == "5":
            self.fiveHist.append("D " + fund + amount)
            self.five += amount
        elif fund == "6":
            self.sixHist.append("D " + fund + amount)
            self.six += amount
        elif fund == "7":
            self.sevenHist.append("D " + fund + amount)
            self.seven += amount
        elif fund == "8":
            self.eightHist.append("D " + fund + amount)
            self.eight += amount
        elif fund == "9":
            self.nineHist.append("D " + fund + amount)
            self.nine += amount
        elif fund == "0":
            self.zeroHist.append("D " + fund + amount)
            self.zero += amount
        else:
            print("error")
    def withdraw(self, fund, amount):
        if amount > self.total_val():
            print("insufficient funds")
        else:
            if fund == "1":
                if amount > self.one:
                    self.oneHist.append("W " + fund + self.one)
                    amount -= self.one
                    self.one = 0
                    self.withdraw("2", amount)
                else:
                    self.oneHist.append("W " + fund + amount)
                    self.one -= amount 
            elif fund == "2":
                if amount > self.two:
                    self.twoHist.append("W" + fund + self.two)
                    amount -= self.two
                    self.two = 0
                    self.withdraw("3", amount)
                else:
                    self.twoHist.append("W" + fund + amount)
                    self.two -= amount
            elif fund == "3":
                if amount > self.three:
                    self.threeHist.append("W" + fund + self.three)
                    amount -= self.three
                    self.three = 0
                    self.withdraw("4", amount)
                else:
                    self.threeHist.append("W" + fund + amount)
                    self.three -= amount
            elif fund == "4":
                if amount > self.four:
                    self.fourHist.append("W" + fund + self.four)
                    amount -= self.four
                    self.four = 0
                    self.withdraw("5", amount)
                else:
                    self.fourHist.append("W" + fund + amount)
                    self.four -= amount
            elif fund == "5":
                if amount > self.five:
                    self.fiveHist.append("W" + fund + self.five)
                    amount -= self.five
                    self.five = 0
                    self.withdraw("6", amount)
                else:
                    self.fiveHist.append("W" + fund + amount)
                    self.five -= amount
            elif fund == "6":
                if amount > self.six:
                    self.sixHist.append("W" + fund + self.six)
                    amount -= self.six
                    self.six = 0
                    self.withdraw("7", amount)
                else:
                    self.sixHist.append("W" + fund + amount)
                    self.six -= amount
            elif fund == "7":
                if amount > self.seven:
                    amount -= self.seven
                    self.seven = 0
                    self.withdraw("8", amount)
                else:
                    self.seven -= amount
            elif fund == "8":
                if amount > self.eight:
                    self.eightHist.append("W" + fund + self.eight)
                    amount -= self.seven
                    self.seven = 0
                    self.withdraw("9", amount)
                else:
                    self.eightHist.append("W" + fund + amount)
                    self.eight -= amount
            elif fund == "9":
                if amount > self.nine:
                    self.nineHist.append("W" + fund + self.nine)
                    amount -= self.nine
                    self.nine = 0
                    self.withdraw("0", amount)
                else:
                    self.nineHist.append("W" + fund + amount)
                    self.nine -= amount
            elif fund == "0":
                if amount > self.zero:
                    self.zeroHist.append("W" + fund + self.zero)
                    amount -= self.zero
                    self.zero = 0
                    self.withdraw("1", amount)
                else:
                    self.zeroHist.append("W" + fund + amount)
                    self.zero -= amount
            else:
                print("error")
    def history(self):
        print(*self.transHist, sep = "\n")
    def fundHistory(self, fund):
        if fund == 1:
            print(*self.oneHist, sep = "\n")
        elif fund == 2:
            print(*self.twoHist, sep = "\n")
        elif fund == 3:
            print(*self.threeHist, sep = "\n")
        elif fund == 4:
            print(*self.fourHist, sep = "\n")
        elif fund == 5:
            print(*self.fiveHist, sep = "\n")
        elif fund == 6:
            print(*self.sixHist, sep = "\n")
        elif fund == 7:
            print(*self.sevenHist, "\n")
        elif fund == 8:
            print(*self.eightHist, sep = "\n")
        elif fund == 9:
            print(*self.nineHist, sep = "\n")
        elif fund == 0:
            print(*self.zeroHist, sep = "\n")
        else:
            print("error")
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
    

    
