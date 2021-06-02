# Change Please

This week’s challenge was reported to have been asked in interviews at **Google**.

## Basic difficulty

You’re building an ATM and want to know how many ways you can “break” a given amount of money into cash or change.
To do so, write a function, `changeOptions`, that when fed an amount of money n and a list of values S = { S1, S2, .. , Sm} (representing the possible coin or note denominations), will return the number of all the possible ways in which one can break down n into change.

* **Function Name**: `changeOptions`
* **Input**: n, an integer ≥0 and an integer array S which is the list of all denominations.
* **Output**: an integer, the number of all of the possible combinations of coins and notes that add up to n
* **Example**: `changeOptions(5, [1, 2, 5, 10, .., 50000]) => 4`
* Where the amount is 5¢ (n=5) and the denominations are S = [1, 2, 5, 10, .., 50000], the possible combinations of coins and notes that add up to 5 are 1+1+1+1+1, 1+1+1+2, 1+2+2, 5, so your function would return 4.
* The order of the coins and notes doesn’t matter – 2¢+1¢+2¢ is the same amount of money as 2¢+2¢+1¢.
n and S both represent the number of cents – for example do not use €2.50 as an input, use 250 instead.
use as your sample problem n = 26730 and S = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]

## Hard difficulty

Write `changeOptions` as *efficiently as possible*.
