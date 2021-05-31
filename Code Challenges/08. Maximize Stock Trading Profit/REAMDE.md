# Maximize Stock Trading Profit

This week’s challenge was reportedly asked in interviews at Google:

## Basic Difficulty

Given the daily values of a stock, write a program that will find how you can gain the most with a single buy-sell trade.

You may assume …

* Your function should be called `bestDays` and take one array of integers as an input.
* Daily stock values will be represented in an array of integers (`arr[]`) representing the stock price at the beginning or “opening bell” of each day.
* You may use the following as a test array, from day 0 through day 7: `{17, 11, 60, 25, 150, 75, 31, 120}`. In this case, purchasing on day one and selling on day four would yield the most profit.
* `bestDays` analyses historical data and returns when one should have bought and sold to maximize profit, it is not designed to predict the future. If you do manage to write a program that accurately predicts future stock market trends, congratulations, you’ll be very very rich.
* You are required to buy and sell only once.
* For the sake of this exercise, you will only ever be purchasing, owning, or selling one share.
* `bestDays` should return the day on which one should buy a share, followed by the day on which one should sell a share, as integers.

## Intermediate difficulty

Given the daily values of a stock over a number of days n, write a program that will find how you can gain the most with a combination of buy-sell trades.

* You can only make one transaction per day, and new transactions can take place only after the previous transaction is complete (e.g. buy :arrow_forward: sell :arrow_forward: buy :arrow_forward: sell). For example, if you sold on day 3 you could not also buy on day 3, you would have to wait until day 4 or later to purchase again.
* You may use the following as a test array, from day 0 through day 7: `{90, 170, 250, 300, 30, 525, 685, 90}`. In this case, purchasing on day zero and selling on day three, then buying again on day four before selling on day six would yield the most profit.

Your function should be called `bestDays` and take `one array of integers` as an input. `bestDays` should output a 2D array of the form [[buyDay1, sellDay1],[buyDay2, sellDay2], ..... , [buyDayN, sellDayN]], where `buyDayX` and `sellDayX` are integers corresponding to the days in the input array.

## Hard Difficulty

Solve the basic and intermediate versions of this challenge as efficiently as possible.

Find out more about hard challenges and Big O
