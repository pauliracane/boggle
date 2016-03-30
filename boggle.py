#! /usr/bin/env python3

import BoggleClasses
import warnings
import time
import curses
import random
import sys
from test import box

def main(stdscr):
    Board = BoggleClasses.Board.BoardGen()
    wordList = BoggleClasses.Board.ValidWords(Board)

    begin_x = 0
    begin_y = 0
    height = 50
    width = 70
    win = curses.newwin(height, width, begin_y, begin_x)

    x = 0
    z = 0
    y = 0
    for each in Board:
        x += 1
        if x % 4 == 1:
            y += 2
            z = 0
            box(stdscr, z, y, each)
        else:
            z += 4
            box(stdscr, z, y, each)
    endTime = time.time() + 180  # make game 3 minutes long (180 seconds)
    guess = ""
    guessedWords = []
    CompWords = []
    points = 0
    comppoints = 0
    curses.echo()
    y = 16   # computer Y input Line
    hY = 13  # Humans Y input line
    compguess = time.time() + 7
    while time.time() < endTime and wordList:
        stdscr.nodelay(True)
        stdscr.addstr(0,0," "*20) # Wipe remaining time, then Print
        stdscr.addstr(0,0,(str(int(endTime - time.time()))+" seconds"))
        stdscr.move(hY,len(guess))       # Move to Human Input Y
        s = stdscr.getch()
        if s != -1:
            if chr(s) == '\n':  # 10 is the carrage return sent by enter.
                for x in range(0, len(guess) + 20):  # Wipe line of long word
                    stdscr.addstr(hY, x, " ")
                    stdscr.addstr(hY+1, x, " ")
                stdscr.move(hY, 0)          # move back to start of the line
                if guess in wordList:       # if guess in list of words
                    wordList.remove(guess)  # Remove it from the list
                    wordlen = len(guess)    # Get length once, less checks
                    if wordlen <= 4:        # If word is 3 or 4 letters
                        points += 1         # give 1 point
                    elif wordlen == 5:      # if 5 letters
                        points += 2         # give 2 points
                    elif wordlen == 6:      # if 6 letters
                        points += 3         # give 3 points
                    elif wordlen == 7:      # if 7 letters
                        points += 5         # give 5 poitns
                    else:                   # if more than 7
                        points += 11        # give 11 points
                    guessedWords.append(guess)    # add guess to used words
                    guess = ""              # reset guess to be null
                elif guess == 'q':
                    endTime = time.time()
                else:
                    guess = ""
            elif s == curses.KEY_BACKSPACE:  # catch backspace wipe last char
                if guess:
                    stdscr.addstr(hY, 0, " " * len(guess))
                    guess = guess[:-1]

                    stdscr.addstr(hY, 0, guess)
                    stdscr.move(hY, len(guess))
            elif s < 256:    # for each instance of character being passed in.
                if len(guess) < 17:
                    guess += str(chr(s)).lower()
                else:
                    stdscr.addstr(hY+1, 0, "Guess is too long.")

        if time.time() > compguess:
            compguess = time.time() + 7
            computerGuess = random.choice(list(wordList))
            wordList.remove(computerGuess)
            CompWords.append(computerGuess)
            stdscr.addstr(y, 0, ' ' * 42)
            stdscr.addstr(y, 0, 'Computer has guessed: ')
            stdscr.addstr(computerGuess)
            stdscr.move(hY, len(guess))
            wordlen = len(computerGuess)  # Get length, less comparisons
            if wordlen <= 4:              # If word is 3 or 4 letters
                comppoints += 1           # give 1 point
            elif wordlen == 5:            # if 5 letters
                comppoints += 2           # give 2 points
            elif wordlen == 6:            # if 6 letters
                comppoints += 3           # give 3 points
            elif wordlen == 7:            # if 7 letters
                comppoints += 5           # give 5 poitns
            else:                         # if more than 7
                comppoints += 11          # give 11 points

            computerGuess = ""

    stdscr.clear()
    stdscr.move(0,0)
    stdscr.nodelay(False)
    stdscr.addstr("\nYou correctly guessed:\n" + ' '.join(guessedWords))
    stdscr.addstr("\nfor a total of "+str(points) + " points\n")
    stdscr.addstr("\nThe computer guessed: \n" + ' '.join(CompWords))
    stdscr.addstr("\nfor a total of "+str(comppoints)+" points")

    stdscr.addstr("\nFinish typing your word.\n\n")
    while s != 10:
        s = stdscr.getch()

    stdscr.addstr(' '.join(wordList))
    stdscr.addstr("\n\nPress any Button.")
    stdscr.getch()



if __name__ == '__main__':
    warnings.simplefilter('error')
    if sys.version_info[0] < 3:
        try:
            raise DeprecationWarning("This program only works in python3")
        except DeprecationWarning:
            print("DeprecationWarning: This program only works in Python3")
            exit(15)
#        print("Error; program must be run in Python v3.")
    try:
        curses.wrapper(main)
    except:
        exit(5)
