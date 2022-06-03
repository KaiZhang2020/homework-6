class Account:
    def __init__(self, name, number):
        self.open(name, number)

    def open(self, name, number):
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

        self.histOrder = []
        self.fundHistOrder = []
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

    def total_val(self):
        return (int(self.zero) + int(self.one) + int(self.two) + int(self.three) + 
        int(self.four) + int(self.five) + int(self.six) + int(self.seven) + int(self.eight) +
        int(self.nine))

    def cash_val(self):
        return self.zero + self.one

    def bond_val(self):
        return self.two + self.three

    def deposit(self, fund, amount):
        amount = int(amount)
        if fund == "1":
            self.one += amount
            self.oneHist.append("D " + self.number + fund + " " + str(amount))
        elif fund == "2":
            self.two += amount
            self.twoHist.append("D " + self.number + fund + " " + str(amount))
        elif fund == "3":
            self.three += amount
            self.threeHist.append("D " + self.number + fund + " " + str(amount))
        elif fund == "4":
            self.four += amount
            self.fourHist.append("D " + self.number + fund + " " + str(amount))
        elif fund == "5":
            self.five += amount
            self.fiveHist.append("D " + self.number + fund + " " + str(amount))
        elif fund == "6":
            self.six += amount
            self.sixHist.append("D " + self.number + fund + " " + str(amount))
        elif fund == "7":
            self.seven += amount
            self.sevenHist.append("D " + self.number + fund + " " + str(amount))
        elif fund == "8":
            self.eight += amount
            self.eightHist.append("D " + self.number + fund + " " + str(amount))
        elif fund == "9":
            self.nine += amount
            self.nineHist.append("D " + self.number + fund + " " + str(amount))
        elif fund == "0":
            self.zero += amount
            self.zeroHist.append("D " + self.number + fund + " " + str(amount))
        else:
            print("deposit error")

    def withdraw(self, fund, amount):
        amount = int(amount)
        if fund == "1":
            if amount > self.one:
                self.oneHist.append("W " + self.number + fund + " " + str(self.one))
                amount -= self.one
                self.one = 0
                self.withdraw("0", amount)
            else:
                self.oneHist.append("W " + self.number + fund + " " + str(amount))
                self.one -= amount 
        elif fund == "2":
            if amount > self.two:
                self.twoHist.append("W " + self.number + fund + " " + str(self.two))
                amount -= self.two
                self.two = 0
                self.withdraw("3", amount)
            else:
                self.twoHist.append("W " + self.number + fund + " " + str(amount))
                self.two -= amount
        elif fund == "3":
            if amount > self.three:
                self.threeHist.append("W " + self.number + fund + " " + str(self.three))
                amount -= self.three
                self.one = 0
                self.withdraw("2", amount)
            else:
                self.threeHist.append("W " + self.number + fund + " " + str(amount))
                self.three -= amount
        elif fund == "4":
            if amount > self.four:
                self.nineHist.append("W " + self.number + fund + " " + str(amount) + "(failed)")
                print("insufficent fund in acct 4")
            else:
                self.fourHist.append("W " + self.number + fund + " " + str(amount))
                self.four -= amount
        elif fund == "5":
            if amount > self.five:
                self.nineHist.append("W " + self.number + fund + " " + str(amount) + "(failed)")
                print("insufficent fund in acct 5")
            else:
                self.fiveHist.append("W " + self.number + fund + " " + str(amount))
                self.five -= amount
        elif fund == "6":
            if amount > self.six:
                self.nineHist.append("W " + self.number + fund + " " + str(amount) + "(failed)")
                print("insufficent fund in acct 6")
            else:
                self.sixHist.append("W " + self.number + fund + " " + str(amount))
                self.six -= amount
        elif fund == "7":
            if amount > self.seven:
                self.sevenHist.append("W " + self.number + fund + " " + str(amount) + "(failed)")
                print("insufficent fund in acct 7")
            else:
                self.sevenHist.append("W " + self.number + fund + " " + str(amount))
                self.seven -= amount
        elif fund == "8":
            if amount > self.eight:
                self.nineHist.append("W " + self.number + fund + " " + str(amount) + "(failed)")
                print("insufficent fund in acct 8")
            else:
                self.eightHist.append("W " + self.number + fund + " " + str(amount))
                self.eight -= amount
        elif fund == "9":
            if amount > self.nine:
                self.nineHist.append("W " + self.number + fund + " " + str(amount) + "(failed)")
                print("insufficent fund in acct 9")
            else:
                self.nineHist.append("W " + self.number + fund + " " + str(amount))
                self.nine -= amount
        elif fund == "0":
            if amount > self.zero:
                self.zeroHist.append("W " + self.number + fund + " " + str(self.zero))
                amount -= self.zero
                self.zero = 0
                self.withdraw("1", amount)
            else:
                self.zeroHist.append("W " + self.number + fund + " " + str(amount))
                self.zero -= amount
        else:
            print("withdraw error")

    def history(self, output):
        output.write("Transaction History for " + self.name + "\n")
        for item in self.transHist:
            output.write("   " + item + "\n")
        self.fundHistory("0", output)
        self.fundHistory("1", output)
        self.fundHistory("2", output)
        self.fundHistory("3", output)
        self.fundHistory("4", output)
        self.fundHistory("5", output)
        self.fundHistory("6", output)
        self.fundHistory("7", output)
        self.fundHistory("8", output)
        self.fundHistory("9", output)

    def fundHistory(self, fund, output):
        if fund == "1":
            output.write("Prime Money Market: $" + str(self.one) + "\n")
            for item in self.oneHist:
                output.write("   " + item + "\n")
        elif fund == "2":
            output.write("Long-Term Bond: $" + str(self.two) + "\n")
            for item in self.twoHist:
                output.write("   " + item + "\n")
        elif fund == "3":
            output.write("Short-Term Bond: $" + str(self.three) + "\n")
            for item in self.threeHist:
                output.write("   " + item + "\n")
        elif fund == "4":
            output.write("500 Index Fund: $" + str(self.four) + "\n")
            for item in self.fourHist:
                output.write("   " + item + "\n")
        elif fund == "5":
            output.write("Capital Value Fund: $" + str(self.five) + "\n")
            for item in self.fiveHist:
                output.write("   " + item + "\n")
        elif fund == "6":
            output.write("Growth Equity Fund: $" + str(self.six) + "\n")
            for item in self.sixHist:
                output.write("   " + item + "\n")
        elif fund == "7":
            output.write("Growth Index Fund: $" + str(self.seven) + "\n")
            for item in self.sevenHist:
                output.write("   " + item + "\n")
        elif fund == "8":
            output.write("Value Fund: $" + str(self.eight) + "\n")
            for item in self.eightHist:
                output.write("   " + item + "\n")
        elif fund == "9":
            output.write("Value Stock Index: $" + str(self.nine) + "\n")
            for item in self.nineHist:
                output.write("   " + item + "\n")
        elif fund == "0":
            output.write("Money Market: $" + str(self.zero) + "\n")
            for item in self.zeroHist:
                output.write("   " + item + "\n")
        else:
            print("fund history error")

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
    

    
