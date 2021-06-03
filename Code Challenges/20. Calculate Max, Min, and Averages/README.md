# Calculate Max, Min, and Averages

Variations of week’s challenge were reported to have been asked in interviews at **Amazon**.

## Basic difficulty
You’re training for a marathon and have a list of times in which you’ve completed your training runs. Write a function, `averageFinder` that will return the [mean](https://en.wikipedia.org/wiki/Arithmetic_mean) and [mode](https://en.wikipedia.org/wiki/Mode_(statistics) of your race times. Make sure that you write your functions and find these answers `from scratch` – don’t use imported tools!

* **Function name**: `averageFinder`
* **Input**: an array with race times, each a natural number representing the minutes it took you to finish your run (you can presume that race times are rounded up to the nearest minute so we do not have to deal with seconds)
* **Output**: an array, with mean time and mode time (in that order)
* **Example**: `averageFinder([500, 450, 400, 400, 375, 350, 325, 300]) => [387.5, 400]`
    * Please include the above sample input array in your submission as a test.
* Always remember to *explain* your code and the thought processes behind it!
* As always solutions using imports to do all the heavy lifting such as itertools will not be considered for the winner (and are not what interviewers are looking for) – you should write your functions from scratch.
* What if your interviewer had follow-up questions, for example asking for maximum, median, and minimum times instead of mean and mode? What if your input array did not have duplicate values? Don’t anticipate what exactly those follow-ups or changes may be, but try to write your code so that it is easily read, easily maintained, and can be adapted to potential modifications in the interviewer’s questioning.


## Intermediate difficulty

You’re not satisfied with just looking at the historical data for your marathon training – you want your program to reflect your *continued* progress, returning your best, worst, and average run times. Write a function, `timeKeeper` that will help you out. `timeKeeper` will take an input, n a positive integer representing the number of minutes it took you to complete your latest run, and then return an array of the following vital statistics about all of your runs to date:

* the longest time you’ve taken to date (`maxTime`)
* the shortest (best) time you’ve taken to date (`minTime`)
* the mean of all of your race times (`meanTime`)
* the mode of all of your race times (`modeTime`)
* the [median](https://en.wikipedia.org/wiki/Median) of all of your race times (`medianTime`)

* **function name**: `timeKeeper`
* **Input**: a race time n, a natural number in minutes (you can presume that race times are rounded up to the nearest minute so we do not have to deal with seconds). Each time you insert a new time, n, it is added to an array that contains all of your historical race times.
* **Output**: an array, with longest time, shortest time, mean time, mode time and median time (in that order)
* **Example**: with an existing array of `[500, 450, 400, 400, 375, 350, 325, 300]` for your historical times and your new time of 320 to insert, `timeKeeper(320) => [500, 300, 380, 400, 375]`
    Please include this example array and insertion in your test submission to make it easier for others to assess.
* Always remember to *explain* your code and the thought processes behind it!
* Make sure to write everything from scratch!
* Interviewers often ask you for extra features or revisions after you’ve made the program, so for bonus points – can you also return whether or not (and by how much) your times are improving over time? You can presume that your array of race times is sorted by the time in which they were logged, with the first time you trained as the first entry in the array and the most recent time as the last entry in the array. You would show the value for improvements (or deterioration) of your times as the last entry in your results array, after the median.
* If you’d prefer to use a class that is acceptable too

## Hard difficulty

Write `timeKeeper` *as efficiently as possible* (and try to include the bonus points question).
Don’t forget to explain your submission just as you would do in a job interview setting!
