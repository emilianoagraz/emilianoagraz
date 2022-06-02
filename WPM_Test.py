import curses
from curses import wrapper
import time

def main(stdscr):

    # Definir Colores
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    
    BLACK_AND_WHITE = curses.color_pair(1)
    BLACK_AND_YELLOW = curses.color_pair(2)
    WHITE_AND_YELLOW = curses.color_pair(2)

    # Screen
    stdscr.addstr("Hello World")
    stdscr.refresh()

    # Window
    counter_win = curses.newwin(1, 20, 10, 10)

    for i in range(100):
        counter_win.clear()
        color = BLACK_AND_WHITE

        if i % 2 == 0:
            color = BLACK_AND_YELLOW

        counter_win.addstr(f"Count: {i}", color)    
        counter_win.refresh()
        time.sleep(0.1)

    stdscr.getch()


wrapper(main)