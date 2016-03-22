#! /usr/bin/env python3

import BoggleClasses


Board = BoggleClasses.Board.BoardGen()
wordList = BoggleClasses.Board.ValidWords()
x = 0
for each in Board:
        x+=1
        if x % 4 == 1:
                print("\n"+each,end=' ')
        else:
                print(each, end=' ')
print()
print(wordList)


