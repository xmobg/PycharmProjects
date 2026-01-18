def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with bid ${highest_bid}")
bids = {}
continue_bids = True
while continue_bids:
    name = input("Please enter your name: ")
    price = float(input("Please enter your price: "))
    bids[name] = price
    should_continue = input("Would you like to continue? (y/n): ").lower()
    if should_continue == "n":
        continue_bids = False
        find_highest_bidder(bids)

    elif should_continue == "y":
        print("\n" * 100)



