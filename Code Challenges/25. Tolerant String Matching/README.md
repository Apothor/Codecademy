# Tolerant String Matching

 ## Basic difficulty

You have two strings message and snippet with `len(message) >= len(snippet)` and the length of the message can be orders of magnitude bigger than the snippet. Write a function, `basicMatch`, that will return true if the `snippet` is present in the `message` (case insensitive).

* **Function Name**: `basicMatch`
* **Input**: two strings `message` and `snippet`
* **Output**: boolean showing if `snippet` is in `message`
* **Examples**:
  * `basicMatch("Codecademy taught me to code", "code") => True`
  * `basicMatch("A really long string", "on") => True`
  * `basicMatch("Welcome to the internet", "hello") => False`
  * `basicMatch("CaseInsEnSiTiVE", "caseinsensitive") => True`
** Always remember to *explain* your code and the thought processes behind it!
** What if your interviewer had follow-up questions or extensions to this challenge? Don’t anticipate what exactly those follow-ups or changes may be, but try to write your code so that it is easily read, easily maintained, and can be adapted to potential modifications in the interviewer’s questioning.


## Intermediate difficulty

You are told the input `message` went through a decoding step and could be malformed with the wrong characters due to text encoding errors (whereas `snippet` will never be malformed). I.e. the `message` was incorrectly decoded and still contains the string “%65” which should have been decoded as an “A”. Write a function, `intermediateMatch`, that will say if a tolerant matching is present, given two strings and an array of possible decodings.

* **Function Name**: `intermediateMatch`
* **Input**: two strings `message` and `snippet` and a 2D array of possible decodings [["%65", “a”], …]
* **Output**: boolean showing if `snippet` is tolerantly in `message`
* **Examples**:
    * `intermediateMatch("Codecademy is great", "codecademy", []) => True`
    * `intermediateMatch("Codec%65demy is great", "codecademy", [["%65", "A"]]) => True`
    * `intermediateMatch("Codec%65demy is great", "codec%65demy", [["%65", "A"]]) => True`
    * `intermediateMatch("Codec%65demy is great", "codecademy", [["%65", "A"], ["%67", "D"]]) => True`
    * `intermediateMatch("Co%67ec%65demy is great", "codec%65demy", [["%65", "A"], ["%67", "D"]]) => True`
    * `intermediateMatch("Co%67eca%68emy is great", "codecademy", [["%67", "D"], ["%68", "D"]]) => True`
    * `intermediateMatch("Co%67eca%67emy is great", "co%67ecademy", [ ["%67", "D"]]) => True`
    * `intermediateMatch("Codecademy is great", "codec%65demy", [["%65", "A"]]) => False`
    * `intermediateMatch("abc%6efg", "abcdefg", [["e", "d"], ["%6", "e"]]) => False`
* Please note the following:
    * `snippet` will never be wrong. I.e. if it includes the string “%65” this is the literal string
    * `message` may or may not be decoded wrong. I.e. “%65” could be the literal string or could be decoded as an “A”
    * the decoding function is a many-to-one mapping, so given the decoding `[a, b]` a can only ever decode to b, but multiple a’s could give you the same b. I.e. `[["%67", "D"], ["%68", "D"]]` is valid but `[["%67", "D"], ["%67", "C"]]` is an invalid mapping.
    For any mapping `[a, b]` a can be any number of characters but b will always be a single character. I.e. `["%68", "D"]` is valid but `["%67", "CODE"]` isn’t
        
## Hard difficulty

Your chief network engineer tells you the `message` is even more garbled than it first seemed. He can’t remember how many times the message was encoded, which means we will have to decode the message an unknown number of times! He’s promised that there are no cycles in the encoding though, so there is no chain that leads back to itself i.e. this is invalid `[a, b], [b,c], [c, d] .... [X, a]`

* **Function Name**: `hardMatch`
* **Input**: two strings `message` and `snippet` and a 2D array of possible decodings `[["%65", “a”], …]`
* **Output**: boolean showing if snippet is tolerantly in message
* **Examples**:
    * `hardMatch("Codecademy is great", "codecademy", []) => True`
    * `hardMatch("Codec%65demy is great", "codecademy", [["%65", "A"]]) => True`
    * `hardMatch("Codec%65demy is great", "codecademy", [["%65", "$"], ["$", "A"]]) => True`
    * `hardMatch("Codec%65demy is great", "codecademy", [["%65", "$"], ["$", "B"]]) => False`
* Don’t forget to explain your submission just as you would do in a job interview setting
* Also consider the Big O complexity of your code and comment on it

## Extreme difficulty

As with Hard but most of our three assumptions are no longer valid. In a decode `[a, b]` b can be an arbitrary length. `[a, b]` now has a many to many relationship (one a can go to multiple bs now). Your chief engineer has realised that there may indeed by a cycle in the decoding!

* **Function Name**: `extremeMatch`
* **Input**: two strings `message` and `snippet` and a 2D array of possible decodings `[["%65", “a”], …]`
* **Output**: boolean showing if `snippet` is tolerantly in `message`
* **Examples**:
    * `extremeMatch("$1cademy is great", "codecademy", [["$2", "co"], ["$1", "code"]]) => True`
    * `extremeMatch("$2decademy is great", "codecademy", [["$1", "code"], ["$2", "co"]]) => True`
    * `extremeMatch("%1 is great", "codecademy", [["%1", "codecademy"], ["%68", "D"]]) => True`
    * `extremeMatch("%1 is great", "codecademy", [["%1", "codecademy"], ["codecademy", "%2"], ["%2", "%1"]]) => True`
    * `extremeMatch("%1 is great", "code", [["%1", "codecademy"], ["%68", "D"]]) => True`
    * `extremeMatch("dbcd%6fg", "abc%6efg", [["%6", "d"], ["d", "e"], ["e", "%6"], ["d", "a"]]) => True`
    * `extremeMatch("%1 is great", "code", [["%1", "co"], ["%68", "D"]]) => False`
    * `* `extremeMatch("%1 is great", "code", [["%1", "co"], ["co", "d"], ["d", "%1"]]) => False`

## Bonus (for any level)

Your chief network engineer is amazed you have managed to get this far, and is extremely grateful that you’ve helped him fix his mistakes. However, he realised he also needs to know the start and end index of the snippet within the message. Redo the first three tasks including start and end indices.

* **Function Name**: `bonusMatch`
* **Input**: two strings `message` and `snippet` and a 2D array of possible decodings `[["%65", “a”], …]`
* **Output**: boolean showing if `snippet` is tolerantly in `message`
* **Examples**:
    * `bonusMatch("Codecademy is great", "codecademy", []) => True, 0, 10`
    * `bonusMatch("Codec%65demy is great", "codecademy", [["%65", "A"]]) => True, 0, 12`
    * `bonusMatch("Codec%65demy is great", "codecademy", [["%65", "$10"], ["$10", "A"]]) => True, 0, 12`
    * `bonusMatch("Co%67ecademy teaches me to code", "code", [["%67", "d"], ["d", "a"]]) => True, 0, 6`
    * `bonusMatch("Codec%65demy is great", "codecademy", [["%65", "$10"], ["$10", "B"]]) => False, 0, 0`
* You must return the indices of the first possible match
