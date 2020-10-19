# countdown-numbers

This python script solves the Countdown numbers game. 
https://en.wikipedia.org/wiki/Countdown_(game_show)#Numbers_round

# Usage

You will need Python 3 installed (all classes used are part of the standard library). Other than that, it's just a simple case of...

```shell
python countdown_numbers.py --numbers 1 2 3 4 5 100 --target 123
```
and you will recieve an output on the terminal like..

```
Finding solution for 123...
1 + 2 = 3
3 + 100 = 103
4 * 5 = 20
103 + 20 = 123
Found 123.
```
---
# Notes

There are different approaches to this problem, and many (faster!) implementations already available online. For me, it was just an afternoon exercise for fun, and an interesting algorithm problem to tackle. The approach that came most naturally to me was to first contain all the numbers in a (multi)set. Then 
1. Pick two numbers and remove them from the set
2. Pick an arithmetic operation to use on these two numbers to create a new number
3. Add the new number to the set
4. Repeat

This will continue until either the target is found within the set, or there is only one number remaining in the set. It avoids the issue of ordering operations and using brackets. 

In terms of runtime - as a very crude measure - it exhausts all posibilities (i.e. worst case) in about 8 seconds on my 2014 i5 Macbook. So plenty of time before the countdown clock hits 30!
