from Banker import banker

transaction_list = []
final_list = []

with open('BankTransIn.txt') as f:
    for line in f:
        transact_item = line.split(" ")
        transaction_list.append(transact_item)

b = banker(transaction_list)

output = open('BankTransOut.txt', 'w')

output.write("Processing Done. Final Balances \n")

while len(b.AccountList) > 0:
    account_to_get = b.AccountList.pop(0)
    final_list.append(account_to_get)
    act = b.Tree.find(account_to_get)
    while len(act.histOrder) > 0:
        act.histOrder.pop(0)
        output.write("Transaction History for " + act.name + " by fund")
        act.history(output)
    while len(act.fundHistOrder) > 0:
        fundNum = act.fundHistOrder.pop(0)
        act.fundHist(fundNum, output)

    output.write("\n")

while len(final_list) > 0:
    acct_to_get = final_list.pop(0)
    act = b.Tree.find(acct_to_get)
    output.write(act.name + " Account ID: " + act.number[0:4] + "\n")
    output.write("   Money Market: $" + str(act.zero) + "\n")
    output.write("   Prime Money Market: $" + str(act.one) + "\n")
    output.write("   Long-Term Bond: $" + str(act.two) + "\n")
    output.write("   Short-Term Bond: $" + str(act.three) + "\n")
    output.write("   500 Index Fund: $" + str(act.four) + "\n")
    output.write("   Capital Value Fund: $" + str(act.five) + "\n")
    output.write("   Growth Equity Fund: $" + str(act.six) + "\n")
    output.write("   Growth Index Fund: $" + str(act.seven) + "\n")
    output.write("   Value Fund: $" + str(act.eight) + "\n")
    output.write("   Value Stock Index: $" + str(act.nine) + "\n")

print("Bank operation successful, check BankTransOut.txt for more infomation")
"""
while len(b.AccountList) > 0:
    account_to_get = b.AccountList.pop(0)
    final_list.append(account_to_get)
    act = b.Tree.find(account_to_get)
    output.write("Transaction History for " + act.name + "\n")
    output.write("Money Market: $" + str(act.zero) + "\n")
    while len(act.zeroHist) != 0:
        lines = act.zeroHist.pop(0)
        output.write(lines + "\n")
    output.write("Prime Money Market: $" + str(act.one) + "\n")
    while len(act.oneHist) != 0:
        lines = act.oneHist.pop(0)
        output.write(lines + "\n")
    output.write("Long-Term Bond: $" + str(act.two) + "\n")
    while len(act.twoHist) != 0:
        lines = act.twoHist.pop(0)
        output.write(lines + "\n")
    output.write("Short-Term Bond: $" + str(act.three) + "\n")
    while len(act.threeHist) != 0:
        lines = act.threeHist.pop(0)
        output.write(lines + "\n")
    output.write("500 Index Fund: $" + str(act.four) + "\n")
    while len(act.fourHist) != 0:
        lines = act.fourHist.pop(0)
        output.write(lines + "\n")
    output.write("Capital Value Fund: $" + str(act.five) + "\n")
    while len(act.fiveHist) != 0:
        lines = act.fiveHist.pop(0)
        output.write(lines + "\n")
    output.write("Growth Equity Fund: $" + str(act.six) + "\n")
    while len(act.sixHist) != 0:
        lines = act.sixHist.pop(0)
        output.write(lines + "\n")
    output.write("Growth Index Fund: $" + str(act.seven) + "\n")
    while len(act.sevenHist) != 0:
        lines = act.sevenHist.pop(0)
        output.write(lines + "\n")
    output.write("Value Fund: $" + str(act.eight) + "\n")
    while len(act.eightHist) != 0:
        lines = act.eightHist.pop(0)
        output.write(lines + "\n")
    output.write("Value Stock Index: $" + str(act.nine) + "\n")
    while len(act.nineHist) != 0:
        lines = act.nineHist.pop(0)
        output.write(lines + "\n")

"""