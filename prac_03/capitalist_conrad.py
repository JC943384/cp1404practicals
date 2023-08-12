"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAX_INCREASE = 0.175  # 17.5%
MIN_PRICE = 1
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
NUMBER_OF_DAYS = 425
OUTPUT_FILE = "price_simulation.txt"

out_file = open(OUTPUT_FILE, 'w')
price = INITIAL_PRICE
print(f"Initial price: ${price:,.2f}",file=out_file)
print(f"Initial price: ${price:,.2f}")

for day in range(1,NUMBER_OF_DAYS + 1):
    price_change = random.uniform(0,0.175)
    new_price = (1+price_change) * price
    price = new_price
    print(f"On {day} price is: ${price:,.2f}", file=out_file)
    print(f"On {day} price is: ${price:,.2f}")
    if price >= MAX_PRICE or price <= MIN_PRICE:
        break
out_file.close()



