#!/usr/bin/python3
""" Making change file"""


def makeChange(coins, total):
    """ Create table and initialize"""
    dp = [float('inf')]*(total + 1)

    # number of coins to have 0
    dp[0] = 0

    # boucle from 1 to total
    for i in range(1, total + 1):
        # browse all coins
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
