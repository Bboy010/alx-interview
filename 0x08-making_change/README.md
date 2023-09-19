# Change Comes from Within

This is a Python function that calculates the fewest number of coins needed to meet a given amount total using a pile of coins with different values.

## Problem Statement

Given a pile of coins of different values and a target total amount, you need to determine the fewest number of coins needed to meet that total. If it's impossible to reach the target total using the available coins, the function returns -1.

### Function Prototype

```python
def makeChange(coins, total):
    # Your code here
```
--- 
> Follow these intructions

- Prototype: def makeChange(coins, total)
- Return: fewest number of coins needed to meet total
1. If total is 0 or less, return 0
2. If total cannot be met by any number of coins you have, return -1
- coins is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task

> cat 0-main.py
```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))
```
---
> ./0.main.py

`
7
-1
`

*Find the file there* [Making Change](./0-making_change.py)
