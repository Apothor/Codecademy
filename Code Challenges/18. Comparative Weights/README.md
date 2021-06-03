# Compartive Weights

This week’s challenge was reported to have been asked in interviews at **Microsoft**.

## Basic difficulty

Suppose you were given eight soccer balls (aka footballs :soccer:), all of them seemingly identical. You are given a balance scale :balance_scale: and told that one of the eight balls is * slightly* heavier than the others (`outlierBall`). What’s the fewest number of times you have to use the scale to find `outlierBall`? Write a function, `scaleOfTruth`, that will determine the minimum number of weighs that you’ll need to find `outlierBall`.

* **Function Name**: `scaleOfTruth`
* **Input**: None
* **Output**: an integer representing the minimum number of weighs needed to find `outlierBall`
* Seven of the footballs have an exactly even weight, only one of the footballs (`outlierBall`) has a greater weight.
* The [balance scale](https://en.wikipedia.org/wiki/Weighing_scale#Balance_scales) is the only way that you can discern any physical difference between the eight footballs.
    * The balance scale did not come with any reference weights – the only weights you have to use on the balance scale are the footballs themselves.
    * The balance scale is very large – you can fit all eight balls on one side of the scale! Thus, you can put multiple footballs on each side when you weigh, if you so choose.
* What if you were given a ninth football with an identical weight to the eight equally heavy balls you have already? What if `outlierBall` was lighter than all the others rather than heavier? Try to write your code so that it is easily maintainable and can be adapted to modifications in the interviewer’s questioning.
* Always remember to * explain* your code and the thought processes behind it!

## Hard difficulty

Write a function, `scaleOfTruthN` that will solve this challenge with any given number of balls, n, and make sure that your function is as *efficient as possible*.

* This function should print out the minimum number of *weighs* needed to find the `outlierBall` in a set of n footballs, where all balls have identical weights apart from one `outlierBall`, which is heavier.
* **Function Name**: `scaleOfTruthN`
* **Input**: n - an integer representing the number of footballs
* **Output**: An integer representing the minium number of *weighs* to find the *outlier ball*.
* Don’t forget to explain your submission just as you would do in a job interview setting!
