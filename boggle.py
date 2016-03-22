#! /usr/bin/env python3

import BoggleClasses
import time
import curses


def main(stdscr):
	Board = BoggleClasses.Board.BoardGen()
	wordList = BoggleClasses.Board.ValidWords(Board)

	begin_x = 0; begin_y = 0
	height = 50; width = 70
	win = curses.newwin(height, width, begin_y, begin_x)

	x = 0
	for each in Board:
		x+=1
		if x % 4 == 1:
			stdscr.addstr("\n"+each+ " ")
		else:
			stdscr.addstr(each + " ")
	stdscr.addstr("\n\n\n")
	endTime = time.time()+30
	guess = ""
	guessedWords = []
	points = 0
	curses.echo()
	while time.time() < endTime and wordList:
		stdscr.nodelay(True)
		s = stdscr.getch()
		if s != -1:
			chr(s)
			if s == 10:
				for x in range(0,len(guess)):
					stdscr.addstr(" ")
				stdscr.move(7,0)
				if guess in wordList:
					wordList.remove(guess)
					wordlen = len(guess)
					if wordlen <= 4:
						points += 1
					elif wordlen == 5:
						points += 2
					elif wordlen == 6:
						points +=3
					elif wordlen == 7:
						points +=5
					else:
						points +=11
					guessedWords.append(guess)
					guess = ""
				else:
					guess = ""
			elif s == 263:
				guess = guess.replace(guess[-1],"")
			elif s < 256:
				guess+=str(chr(s))
		


	stdscr.nodelay(False)
	stdscr.addstr(guess+"\n")
	stdscr.addstr(' '.join(wordList))
	stdscr.addstr("\nYou correctly guessed:\n" + ' '.join(guessedWords) +"\nfor a total of "+str(points)+" points")
	stdscr.getkey()

curses.wrapper(main)
