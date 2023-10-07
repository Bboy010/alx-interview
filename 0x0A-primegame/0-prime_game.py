#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine the winner of the game
    where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
"""
    def sieve(n):
        # Sieve of Eratosthenes to generate prime numbers up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        primes = []
        for p in range(2, n + 1):
            if is_prime[p]:
                primes.append(p)
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
        return primes

    def canWin(n, primes):
        """ Dynamic programming to check if
        the current player can win for a given n
        """
        if n == 1:
            return False  # Maria cannot make a move, so she loses

        for prime in primes:
            if prime > n:
                break
            if not canWin(n - prime, primes):
                return True
            """If there's a move leading to the opponent's
            loss, Maria wins
            """
        return False

    # Initialize the list of prime numbers up to the maximum n
    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if canWin(n, primes):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
