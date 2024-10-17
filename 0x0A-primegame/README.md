0x0A. Prime Game

# Prime Game

## Description
This project implements a two-player game called "Prime Game" where players take turns choosing prime numbers from a set of consecutive integers. The game is played for multiple rounds, and the overall winner is determined based on who wins the most rounds.

## Rules of the Game
1. The game starts with a set of consecutive integers from 1 to n (inclusive).
2. Players take turns choosing a prime number from the set.
3. When a prime number is chosen, that number and its multiples are removed from the set.
4. The player who cannot make a move (no prime numbers left) loses the round.
5. Multiple rounds are played with different values of n.
6. The player who wins the most rounds is the overall winner.

## Implementation Details
- File: `0-prime_game.py`
- Main function: `isWinner(x, nums)`
  - `x`: number of rounds
  - `nums`: array of n values for each round
  - Returns: name of the player that won the most rounds ("Maria" or "Ben"), or None if it's a tie

## Requirements
- Python 3.4.3 or later
- Ubuntu 20.04 LTS

## Usage
To use this implementation, import the `isWinner` function from the `0-prime_game.py` file:

```python
from 0-prime_game import isWinner

# Example usage
x = 5
nums = [2, 5, 1, 4, 3]
winner = isWinner(x, nums)
print(f"The winner is: {winner}")
```

## Example
```python
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

Output:
```
Winner: Ben
```

## Performance
The implementation uses the Sieve of Eratosthenes algorithm for efficient prime number generation, allowing it to handle large values of n (up to 10000) without significant performance issues.

## Limitations
- The implementation assumes that n and x will not be larger than 10000.
- No external packages are used or allowed in this implementation.

## Contributing
This is a practice project and is not open for contributions. However, feel free to use and modify the code for your own learning purposes.

## License
This project is released under the MIT License. See the LICENSE file for details.
