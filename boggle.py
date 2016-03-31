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
                    points = score(guess, points)

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

            comppoints = score(computerGuess, comppoints)

            computerGuess = ""

    # When game is over
    stdscr.clear()          # Clear Screen
    stdscr.move(0,0)        # Go to top left corner
    stdscr.nodelay(False)   # Reset delay
    # Print scores + words guessed
    stdscr.addstr("\nYou correctly guessed:\n" + ' '.join(guessedWords))
    stdscr.addstr("\nfor a total of "+str(points) + " points\n")
    stdscr.addstr("\nThe computer guessed: \n" + ' '.join(CompWords))
    stdscr.addstr("\nfor a total of "+str(comppoints)+" points")
    # Print Winner
    stdscr.addstr("\nThe ")
    if(comppoints>points):
        stdscr.addstr("Computer ")
    elif(comppoints == points):
        stdscr.addstr("Cat ")
    else:
        stdscr.addstr("Player ")
    stdscr.addstr("has won.")

    # Prevent accidental exits if they're still typing when game ends
    stdscr.addstr("\nPress Enter to continue.\n\n")
    while chr(abs(s)) != '\n':  # Chr poops the bed when given a -1.
        s = stdscr.getch()
    stdscr.addstr("\nThe unguessed words were:\n")
    stdscr.addstr(' '.join(wordList))
    stdscr.addstr("\n\nPress any Button to exit.")
    stdscr.getch()


def score(guess, PointStorage):
    wordlen = len(guess)
    if wordlen <= 4:       # If word is 3 or 4 letters
        PointStorage += 1  # give 1 point
    elif wordlen == 5:     # if 5 letters
        PointStorage += 2  # give 2 points
    elif wordlen == 6:     # if 6 letters
        PointStorage += 3  # give 3 points
    elif wordlen == 7:     # if 7 letters
        PointStorage += 5  # give 5 poitns
    else:                  # if more than 7
        PointStorage += 11 # give 11 points
    
    return PointStorage

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
    except KeyboardInterrupt:
        print("Try just sending in 'q' next time.")
    '''
    except:
        print("Something went wrong.")
        print("Try increasing the size of your terminal.\n")
        exit(5)
    '''
