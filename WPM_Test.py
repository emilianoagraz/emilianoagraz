import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

def main(stdscr):

    # Definir Colores
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    
    BLACK_AND_WHITE = curses.color_pair(1)
    BLACK_AND_YELLOW = curses.color_pair(2)
    WHITE_AND_YELLOW = curses.color_pair(2)

    win = curses.newwin(10, 60, 3, 8)
    box = Textbox(win)

    rectangle(stdscr, 1, 4, 14, 71)

    stdscr.refresh()

    # gather & print
    box.edit()
    text = box.gather().strip().replace("\n", "")
    stdscr.addstr(10, 40, text)

    stdscr.getch()

wrapper(main)