## Simple from Shapiro

A very easy solution by just taking a random (or next) question from a
list of posible questions left in the game

## YASM from Barteld Kooi

Building on Simple by filtering the posible questions
and compairing them to find the question that has to
most diverse result (answer).

#### reflection

Altough the algorithm doesn't perform very bad I would have expected it
to be better (it probably is). I think I might have implemented it wrong
but I am not sure what is wrong.

## Custom from Xander

Building on Simple trying to improve results by trying to select a beter
question instead of picking 'random'. Results are selected based on
information given (Black * 2 + White), this solution wins less games
than the simple variant.

#### reflection
There are 2 main issues with my custom solution,
the first is that the results are filtered based on the black and white pegs but
this is not actually a great strategy, for example getting 0 pegs gives way more
information about the secret code than (2, 1).
Another issue is that because it is so slow to calculate the selection will only
start when there is less than 100 solutions left, this results in some games
being lost before the 'optimisation' has started. 