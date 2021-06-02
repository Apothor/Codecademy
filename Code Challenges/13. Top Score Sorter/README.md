# Top Score Sorter

This week’s challenge was reported to have been asked in interviews at **Amazon**.

## Basic difficulty

You’ve spent decades setting high scores on Donkey Kong but now, a challenger approaches. Write a function, `scoreSettler`, that will definitively show who is the King of Kong. `scoreSettler` will take a list of unsorted scores plus the highest possible score and return a sorted list of all of the scores, in descending order from high score to low score.

* **Function Name**: `scoreSettler`
* *** **Input**: `list of integers` representing scores and a single integer for the highest possible score
* **Output**: A sorted `list of integers` in descending order
* **Example**: `scoreSettler([ 1, 2, 3, 999999], 1000000) => [999999, 3, 2, 1]`
* In your submission, please use as a test of your function the maximum value of 1218000, with a list of scores `[874300, 879200, 1172100, 1141800, 933900, 1177200, 1190200, 1110100, 1158400, 985600, 1047200, 1049100, 1138600, 1170500, 1064500, 1190000, 1050200, 1090400, 1062800, 1061700, 1218000, 1068000, 1127700, 1144800, 1195100]`
* You’re expected to create and implement your own sorting algorithms, not to simply use an in-built sort function.


## Hard difficulty

You wouldn’t be much of a King of Kong if your settling of the scores didn’t itself set records. Write `scoreSettler` as *efficiently as possible*.

* If you can’t make your program any more efficient explain why.
* If you need an additional challenge, try to solve this problem in a more unconventional or artful way, or perhaps try a different language!
