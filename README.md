# Random Number Generator

# A function that lets the computer pick a number within a range

### Formula
```python
# Import the random library

import random

# Pick a number randomly within a range

variable = random.randint(startNum, endNum)
```

startNum and endNum are inclusive, meaning thos numbers are part of the options for the computer to choose from.

### Rules
In order to set a range, check how many options are needed. For example, a coin has 2 sides, so a coin flipper generator would have 2 options.

*Ex.
```python
import random

coin = random.randint(0,1)

if(coin == 1):
  print("heads)
else:
  print("tails")
```
> heads *or* tails

