from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

Auction_Time = False
Bid = {}

def Highest_Bidder(bidding_record):
  #bidding_record = {"Angela": 123, "James": 321}
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not Auction_Time:
  print("Welcome to the secret auction program")
  Name = input("What is your name?: ")
  Price = int(input("What's your bid?: $"))
  Bid[Name] = Price
  Continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if Continue == 'no':
    Auction_Time = True
    Highest_Bidder(Bid)
  elif Continue == 'yes':
    clear()

print(Bid)