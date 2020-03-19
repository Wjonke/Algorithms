#!/usr/bin/python

import argparse

#first pass solution

# def find_max_profit(prices):
#     def merge(a, b):
#         x = y = 0
#         result = []
#         while x < len(a) and y < len(b):
#             if a[x] < b[y]:
#                 result.append(a[x])
#                 x += 1
#             else:
#                 result.append(b[y])
#                 y += 1
#
#         result.extend(a[x:])
#         result.extend(b[y:])
#
#         return result
#
#     def merge_sort(arr):
#         if len(arr) <= 1:
#             return arr
#
#         point = len(arr) // 2
#
#         lhs = merge_sort(arr[point:])
#         rhs = merge_sort(arr[:point])
#
#         return merge(lhs, rhs)
##################################################################################################
##################################################################################################

#second pass, abstract helper functions
# def merge(a, b):
#     x = y = 0
#     result = []
#     while x < len(a) and y < len(b):
#         if a[x] < b[y]:
#             result.append(a[x])
#             x += 1
#         else:
#             result.append(b[y])
#             y += 1
#
#     result.extend(a[x:])
#     result.extend(b[y:])
#
#     return result
#
#
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     point = len(arr) // 2
#
#     lhs = merge_sort(arr[point:])
#     rhs = merge_sort(arr[:point])
#
#     return merge(lhs, rhs)

#second pass implimentation

# def find_max_profit(prices):
#     # set Min Value
#     min_value = prices[0]
#     # Set the Difference List
#     difference = []
#     # Loop through List starting at index 1 and subtract list[i] - list[i - 1]
#     for i in range(1, len(prices)):
#         # Get Result of Current Price minus Min Value
#         result = prices[i] - min_value
#         # Set Min Value if it is the new Min Value
#         if min_value > prices[i]:
#             min_value = prices[i]
#         # Append The Result
#         difference.append(result)
#     # Sort the Difference List with Merge Sort Algorithm
#     sorted_difference = merge_sort(difference)
#     # Return the last index of the sorted Array
#     return sorted_difference[-1]

##################################################################################################
##################################################################################################

# Third Pass Solution
def find_max_profit(prices, min_value=0, cur_profit=0, index=1):
    if index >= len(prices):
        return cur_profit

    if min_value == 0:
        min_value = prices[0]
        cur_profit = prices[index] - prices[0]

    if prices[index] - min_value > cur_profit:
        cur_profit = prices[index] - min_value

    if min_value > prices[index]:
        min_value = prices[index]

    return find_max_profit(prices, min_value, cur_profit, index + 1)


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
