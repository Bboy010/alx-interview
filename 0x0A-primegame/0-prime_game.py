#!/usr/bin/python3

def isWinner(x, nums):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def canWin(n):
        if n == 1:
            return False
        if n in memo:
            return memo[n]

        for i in range(2, n + 1):
            if isPrime(i) and n % i == 0:
                if not canWin(n - i):
                    memo[n] = True
                    return True

        memo[n] = False
        return False

    memo = {}
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if canWin(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
