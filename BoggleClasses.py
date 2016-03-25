#!/usr/bin/env python3
import time
import random

# I chose these letters becase it was the first image on google images
# Further reading :
# http://www.boardgamegeek.com/thread/300565/
# This program is for educational purposes.
# states c1976, yellow box.


class Board:

    def BoardGen():
        die0 = ['R', 'I', 'F', 'O', 'B', 'X']
        die1 = ['I', 'F', 'E', 'H', 'E', 'Y']
        die2 = ['D', 'E', 'N', 'O', 'W', 'S']
        die3 = ['U', 'T', 'O', 'K', 'N', 'D']
        die4 = ['H', 'M', 'S', 'R', 'A', 'O']
        die5 = ['L', 'U', 'P', 'E', 'T', 'S']
        die6 = ['A', 'C', 'I', 'T', 'O', 'A']
        die7 = ['Y', 'L', 'G', 'K', 'U', 'E']
        die8 = ['Q', 'B', 'M', 'J', 'O', 'A']
        die9 = ['E', 'H', 'I', 'S', 'P', 'N']
        die10 = ['V', 'E', 'T', 'I', 'G', 'N']
        die11 = ['B', 'A', 'L', 'I', 'Y', 'T']
        die12 = ['E', 'Z', 'A', 'V', 'N', 'D']
        die13 = ['R', 'A', 'L', 'E', 'S', 'C']
        die14 = ['U', 'W', 'I', 'L', 'R', 'G']
        die15 = ['P', 'A', 'C', 'E', 'M', 'D']

        BoardToEndAllBoards = [
                                die0, die1, die2, die3, die4, die5,
                                die6, die7, die8, die9, die10,
                                die11, die12, die13, die14, die15
                              ]

        Board = []

        while BoardToEndAllBoards:
            die = random.choice(BoardToEndAllBoards)
            Board.append(random.choice(die))
            BoardToEndAllBoards.remove(die)

        return Board

    def ValidWords(board):
        '''
        pulled from :
        http://stackoverflow.com/questions/746082/how-to-find-list-of-possible-words-from-a-letter-matrix-boggle-solver#750012
        converted to Python3...
        '''

        x = 0
        grid = ""
        # Generate board in pattern: "abcd efgh ijkl mnop"
        for letter in board:
            x += 1
            if x % 4 == 1:
                grid += ' ' + letter.lower()
            else:
                grid += letter.lower()

        grid = grid.split()
        # Number of rows, columns
        nrows, ncols = len(grid), len(grid[0])

        # A dictionary word that could be a solution must use only the grid's
        # letters and have length >= 3. (With a case-insensitive match.)
        import re
        # Make alphabet based on letters in grid.  (in comment example, a-p)
        alphabet = ''.join(set(''.join(grid)))
        # Set bogglable matches if a set of 3 characters from Alphabet
        bogglable = re.compile('[' + alphabet + ']{3,}$', re.I).match

        # Walk through dictionary looking for matches on 'bogglable'
        words = set(word.rstrip('\n') for word in
                    open('/usr/share/dict/american-english')
                    if bogglable(word.lower()))
        prefixes = set(word[:i] for word in words
                       for i in range(2, len(word) + 1))

        def solve():
            for y, row in enumerate(grid):
                for x, letter in enumerate(row):
                    for result in extending(letter, ((x, y),)):
                        yield result

        def extending(prefix, path):
            if prefix in words:
                yield (prefix, path)
            for (nx, ny) in neighbors(path[-1]):
                if (nx, ny) not in path:
                    prefix1 = prefix + grid[ny][nx]
                    if prefix1 in prefixes:
                        for result in extending(prefix1, path + ((nx, ny),)):
                            yield result

        def neighbors(coords):
            (x, y) = coords
            for nx in range(max(0, x - 1), min(x + 2, ncols)):
                for ny in range(max(0, y - 1), min(y + 2, nrows)):
                    yield (nx, ny)

        return (sorted(set(word for (word, path) in solve())))

