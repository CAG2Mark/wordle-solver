# wordle-solver
A smart wordle solver in Python.

The way it works is it first guesses words containing the most
common characters in the English language. Once it has pinned
down 3 of the 5 letters, it will then enter "elimination mode".
It will detect the discriminating characters in the remaining 
possible words, and ask words to eliminate as many of those
characters as possible.

Once it is confident enough it has enough attempts remaining
so that it can solve the problem by just guessing, it does 
exactly that.

(NOTE: this was built completely using my own ideas. I did
not watch any tutorial or any video to get the idea. It was
only after I showed it to some friends that they showed me
a 3Blue1Brown video on it :P)

# How to use
Simply type in the word it gives you each time into Wordle.

Then, type in the feedback Wordle gives you:
* If it is the **right position and character**, type `2`.
* If it is the **wrong position but right character**, type `1`.
* If it is the **wrong character**, type `0` for that position.

For example, if the answer (which you can't yet see) 
is `crews` and you typed `tries`, according to the Wordle
feedback, you should type `02012`. Press enter and it will
give you the next guess. If the next guess seems off,
then it's because it's in elimination mode.
