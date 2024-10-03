# Making Change

This project implements a solution to the "Making Change" problem, where we determine the fewest number of coins needed to meet a given amount total, given a list of coin denominations.

## Problem Description

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

### Function Prototype

```python
def makeChange(coins, total)
```

### Parameters

- `coins`: A list of integers representing the values of the coins in your possession.
- `total`: An integer representing the total amount to make change for.

### Return Value

- The function returns the fewest number of coins needed to meet `total`.
- If `total` is 0 or less, the function returns 0.
- If `total` cannot be met by any number of coins you have, the function returns -1.

### Constraints

- The value of a coin will always be an integer greater than 0.
- You can assume you have an infinite number of each denomination of coin in the list.

## Implementation Details

The solution uses a dynamic programming approach to efficiently solve the problem. The implementation can be found in the `0-making_change.py` file.

## Usage

To use this function, import it into your Python script:

```python
from making_change import makeChange

result = makeChange([1, 2, 25], 37)
print(result)  # Output: 7
```

## Requirements

- Python 3.4.3 or later
- Ubuntu 20.04 LTS

## File Structure

- `0-making_change.py`: Contains the implementation of the `makeChange` function.
- `0-main.py`: A main file for testing the `makeChange` function.

## Coding Style

This project adheres to the PEP 8 style guide (version 1.7.x).

## Testing

You can test the implementation using the provided `0-main.py` file:

```bash
./0-main.py
```

Expected output:
```
7
-1
```

## Author

[Your Name]

## License

[Specify the license here, if applicable]
