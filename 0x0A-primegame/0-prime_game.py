#!/usr/bin/python3
"""
Prime Game Implementation
"""


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game for multiple rounds.
    
    :param x: number of rounds
    :param nums: array of n for each round
    :return: name of the player that won the most rounds, or None if it's a tie
    """
    def sieve_of_eratosthenes(n):
        """Generate primes up to n using the Sieve of Eratosthenes."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n + 1, i):
                    primes[j] = False
        return primes

    def play_round(n):
        """
        Play a single round of the game.
        
        :param n: the upper limit of the set of consecutive integers
        :return: True if Maria wins, False if Ben wins
        """
        primes = sieve_of_eratosthenes(n)
        player_turn = True  # True for Maria, False for Ben
        
        for i in range(2, n + 1):
            if primes[i]:
                player_turn = not player_turn
        
        return not player_turn  # The last player to make a move wins

    if x <= 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums[:x]:  # Ensure we don't exceed x rounds
        if n <= 1:
            ben_wins += 1
        elif play_round(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
