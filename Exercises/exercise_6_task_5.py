def print_notes_and_bills(amount):
    remaining = amount

    denominations_notes = [1000, 500, 200, 100, 50, 20]
    # Each item correcsponds to a denomination in the list above
    note_amounts = [0, 0, 0, 0, 0, 0]
    denominations_coins = [10, 5, 2, 1]
    # Each item correcsponds to a denomination in the list above
    coin_amounts = [0, 0, 0, 0]

    for index, denomination in enumerate(denominations_notes):
        note_amounts[index] = remaining // denomination
        remaining = remaining % denomination

    for index, denomination in enumerate(denominations_coins):
        coin_amounts[index] = remaining // denomination
        remaining = remaining % denomination

    print(f"{amount} kr blir:")
    # print notes
    for index, denomination in enumerate(denominations_notes):
        note_amount = note_amounts[index]
        if note_amount == 1:
            print(f"{note_amount} st {denomination}-lapp")
        elif note_amount > 1:
            print(f"{note_amount} st {denomination}-lappar")
    # print coins
    for index, denomination in enumerate(denominations_coins):
        coin_amount = coin_amounts[index]
        if coin_amount == 1:
            print(f"{coin_amount} st {denomination}-krona")
        elif coin_amount > 1:
            print(f"{coin_amount} st {denomination}-kronor")
    



amount = input("Ange antal kronor: ")
amount = int(amount)
print_notes_and_bills(amount)