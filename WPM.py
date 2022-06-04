import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time
import random

# START SCREEN
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 2, "PROGRAMA DE ENTRENAMIENTO PARA ESCRITORES DESASOSEGADOS", curses.color_pair(3))
    stdscr.addstr(2, 22, "de BAN BAN")
    stdscr.addstr(4, 9, "Pulse cualquier tecla para empezar")
    stdscr.refresh()
    stdscr.getkey()

# DISPLAY
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(10, 2, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)
        
# LOAD FRASES
def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

# TEST
def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)   

        

# MAIN
def main(stdscr):

    # COLOR
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    BLACK_AND_WHITE = curses.color_pair(1)
    BLACK_AND_YELLOW = curses.color_pair(2)
    WHITE_AND_YELLOW = curses.color_pair(2)

    start_screen(stdscr)
    
    while True:
        wpm_test(stdscr)
        stdscr.addstr(4, 2, "FIN")
        stdscr.addstr(6, 2, "Pulse cualquier tecla para repetir")
        stdscr.addstr(8, 2, "ESC", curses.color_pair(3))
        stdscr.addstr(8, 6, "para salir")
        key = stdscr.getkey()

        if ord(key) == 27:
            break
   

wrapper(main)