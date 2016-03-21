#!/usr/bin/env python3
import time
import random

#I chose these letters becase it was the first image I saw, and linked to stackoverflow. 
class Board:

	def BoardGen():
		die0 = [ 'R','I','F','O','B','X']
		die1 = ['I','F','E','H','E','Y']
		die2 = ['D','E','N','O','W','S']
		die3 = ['U','T','O','K','N','D']
		die4 = ['H','M','S','R','A','O']
		die5 = ['L','U','P','E','T','S']
		die6 = ['A','C','I','T','O','A']
		die7 = ['Y','L','G','K','U','E']
		die8 = ['Qu','B','M','J','O','A']
		die9 = ['E','H','I','S','P','N']
		die10 = ['V','E','T','I','G','N']
		die11 = ['B','A','L','I','Y','T']
		die12 = ['E','Z','A','V','N','D']
		die13 = ['R','A','L','E','S','C']
		die14 = ['U','W','I','L','R','G']
		die15 = ['P','A','C','E','M','D']

		BoardToEndAllBoards = [die0,die1,die2,die3,die4,die5,
					die6,die7,die8,die9,die10,
					die11,die12,die13,die14,die15]
	
		Board = []
		
		while BoardToEndAllBoards:
			die = random.choice(BoardToEndAllBoards)
			Board.append(random.choice(die))
			BoardToEndAllBoards.remove(die)
		
		return Board
#	self.endTime = time.time()+180 # 3 minute counter
