#!/usr/bin/python

import sys

def making_change(amount, denominations):
  my_cache = {i: 0 for i in range(amount + 1)}
  my_cache[0] = 1
  for x in denominations:
    for y in range(1, amount + 1):
      if y - x >= 0:
        my_cache[y] = my_cache[y - x] + my_cache[y]
  return my_cache[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")