#! /usr/bin/env python3

import BoggleClasses

import curses


Board = BoggleClasses.Board.BoardGen()
wordList = BoggleClasses.Board.ValidWords(Board)
x = 0
for each in Board:
        x+=1
        if x % 4 == 1:
                print("\n"+each,end=' ')
        else:
                print(each, end=' ')

print("\n\n\n")
print(wordList)


