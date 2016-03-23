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
			stdscr.addstr("\n"+each+ "  ")
		else:
			stdscr.addstr(each + "  ")
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
			if s == 10: # 10 is the carrage return sent by enter.
				for x in range(0,len(guess)):		#Wipe the line
					stdscr.addstr(" ")
				stdscr.move(7,0)			#move back to the start of the line
				if guess in wordList:			#check if the guess is in the list of valid words
					wordList.remove(guess)		#Remove it from the list
					wordlen = len(guess)		#Get the length once, so it's less comparisons
					if wordlen <= 4:		#If word is 3 or 4 letters
						points += 1		#give 1 point
					elif wordlen == 5:		#if 5 letters
						points += 2		#give 2 points
					elif wordlen == 6:		#if 6 letters
						points +=3		#give 3 points
					elif wordlen == 7:		#if 7 letters
						points +=5		#give 5 poitns
					else:				#if more than 7
						points +=11		#give 11 points
					guessedWords.append(guess)	#add the guess to a list of human guessed words
					guess = ""			#reset guess to be null
				else:
					guess = ""			
			elif s == 263:	#catch backspace character, remove last character passed in
				if guess:
					guess = guess.replace(guess[-1],"")
				else:
					pass
			elif s < 256:	#for each instance of a character being passed in.
				guess+=str(chr(s))


	stdscr.nodelay(False)
	stdscr.addstr(guess+"\n")
	stdscr.addstr(' '.join(wordList))
	stdscr.addstr("\nYou correctly guessed:\n" + ' '.join(guessedWords) +"\nfor a total of "+str(points)+" points\n")
	#stdscr.addstr("\nThe computer guessed: \n" + ' '.join(CompWords) + "\nfor a total of "+str(comppoints)+" points")
	
	stdscr.addstr("\nFinish typing your word.\n")
	while s != 10:
		s = stdscr.getch()


	stdscr.addstr("Press any Button.")
	stdscr.getch()
curses.wrapper(main)
