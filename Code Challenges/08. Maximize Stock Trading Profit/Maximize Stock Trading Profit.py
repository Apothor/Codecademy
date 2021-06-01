# Maximize Stock Trading Profit

'''
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

Your function should be called `bestDays` and take `one array of integers` as an input. `bestDays` should output a 2D array of the form `[[buyDay1, sellDay1],[buyDay2, sellDay2], ..... , [buyDayN, sellDayN]]`, where `buyDayX` and `sellDayX` are integers corresponding to the days in the input array.

## Hard Difficulty

Solve the basic and intermediate versions of this challenge as efficiently as possible.
'''

# Basic Difficulty

# bestDay(price) identifies and returns a buy and sell date for a single trade
# of a sepcific stock for maximum profit from historical prices.
def bestDay(price):   
    buy_day = 0
    sell_day = 0
    # profit calculates the profit of the trade originating on buy_date
    profit = 0
    # provisional_profitcalculates the profit of a hypothetical trade on provisional_buy_date
    provisional_profit = 0
    # provisional_buy_day tracks the buy_day of the aforemntioned hypothetical trade
    provisional_buy_day = 0
    no_days = len(price)
    for current_day in range(no_days):
        next_day = current_day + 1
        if price[current_day] > price[sell_day]:
            sell_day = current_day
            profit = price[sell_day] - price[buy_day]
            provisional_profit = price[sell_day] - price[provisional_buy_day]
        if provisional_profit > profit:
            buy_day = provisional_buy_day
            profit = provisional_profit
        if price[current_day] < price[buy_day]:
            provisional_buy_day = current_day
    if profit == 0:
        return "No profit was to be made."
    else:
        return "Buy your stock on day {} and sell on day {}".format(buy_day+1, sell_day+1)

# Tests
# No results
price = [17, 11, 10, 9, 6, 3, 2, 1]
print(bestDay(price))
# Day 2 and 4
price = [17, 16, 18, 20, 6, 3, 2, 1]
print(bestDay(price))
# Day 2 and 5
price = [17, 11, 60, 25, 150, 75, 31, 120]
print(bestDay(price))
# Day 5 and 7
price = [180, 170, 250, 300, 30, 525, 685, 90, 100]
print(bestDay(price))
import random
# Days unknown
price = random.sample(range(0, 1000), 365)
print(bestDay(price))

# Intermediate difficulty

# bestDay(price) identifies and returns buy and sell dates for subsequent trades
# of a specific stock for maximum profit from historical prices.
def bestDay(price):   
    trading_days = []
    position = False
    for current_day in range(len(price) -1):
        next_day = current_day + 1
        if position:
            if price[current_day] > price[sell_day]:
                sell_day = current_day
                # update the stored sell_day of the current trade
                trading_days[-1][1] = sell_day + 1
            if price[current_day] > price[next_day]:
                position = False
        if not position:
            if price[current_day] < price[next_day]:
                position = True
                buy_day = current_day
                sell_day = next_day
                # update trading_days with the addition of a new trade
                trading_days.append([current_day + 1, next_day+ 1])
    if not trading_days:
        return "No profit was to be made."        
    else:
        return "Your subsequent trading days are:\n" + "\n".join(["Buy on day {} and sell on day {}".format(*trade) for trade in trading_days])

# Tests
# No results
price = [17, 11, 10, 9, 6, 3, 2, 1]
print(bestDay(price))
# Day (2,4)
price = [17, 16, 18, 20, 6, 3, 2, 1]
print(bestDay(price))
# Day (2,3), (4,5), (7,8)
price = [17, 11, 60, 25, 150, 75, 31, 120]
print(bestDay(price))   
# Day (2,4), (5,7), (8,9)
price = [180, 170, 250, 300, 30, 525, 685, 90, 100]
print(bestDay(price))
# Days unknown
import random
price = random.sample(range(0, 1000), 10)
print(bestDay(price))