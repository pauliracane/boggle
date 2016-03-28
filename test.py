#!/usr/bin/env python3

import curses


def box(screen, begin_x, begin_y, letter):
    TL_win = screen.subwin(3, 5, begin_y, begin_x)
    
    TL_win.addstr(1,2,letter)

    TL_win.border(
        ord('|'), ord('|'),
        ord('-'), ord('-'),
        ord('+'), ord('+'),
        ord('+'), ord('+')
    )
    
    TL_win.refresh()
    return TL_win

def main(stdscr):
    stdscr = curses.initscr()

#    test1 = box(0,0,'E')
#    test2 = box(4,0,'Q')
#    test3 = box(8,0,'U')
#    test4 = box(0,2,'M')
#    test5 = box(4,2,'P')
#    test6 = box(8,2,'I')
#    test7 = box(0,4,'E')
#    test8 = box(4,4,'N')
#    test9 = box(8,4,'T')
    stdscr.addstr("Hit enter when Ready.")   
    stdscr.getkey()
    stdscr.addstr(0,0,"                            ")
if __name__ == '__main__':
    curses.wrapper(main)
