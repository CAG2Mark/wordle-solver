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

Word list is from: http://www.mieliestronk.com/wordlist.html
