from Banker import banker

transaction_list = []

with open('BankTransIn.txt') as f:
    for line in f:
        transact_item = line.split(" ")
        transaction_list.append(transact_item)

banker(transaction_list)
