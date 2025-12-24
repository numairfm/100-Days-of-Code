# TODO-1: Ask the user for input

auction = {}
i = 0
max = 0
winner = ''
running = True
while running:
    i += 1
    name = input("Enter your name: ")
    bid = input("Enter your bid: ")
    bid = int(bid)
    # TODO-2: Save data into dictionary {name: price}

    auction[name] = bid
    print(auction)
    # TODO-3: Whether if new bids need to be added
    if input("Are there any more bidders? yes or no: ").lower() == "no":
        running = False
    else:
        continue
    # TODO-4: Compare bids in dictionary
for bidder in auction:
    bidder_amount = auction[bidder]

    if bidder_amount > max:
        max = bidder_amount
        winner = bidder

print(f"auction winner is {winner} with bid of {max}")
