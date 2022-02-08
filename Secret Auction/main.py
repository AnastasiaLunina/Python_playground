from replit import clear
from art import logo

print(logo)

all_bids = {}
bidding_done = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')


while not bidding_done:
    user_name = input('What is your name? ')
    bid_price = int(input('What is your bid? $'))
    all_bids[user_name] = bid_price
    any_other_bidders = input('Are there any other bidders? Please type "yes" or "no" ')
    if any_other_bidders == 'no':
        bidding_done = True
        find_highest_bidder(all_bids)
    elif any_other_bidders == 'yes':
        clear()