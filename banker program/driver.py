from Banker import banker

transaction_list = []

with open('BankTransIn.txt') as f:
    for line in f:
        transaction_list.append(line)

banker(transaction_list)
