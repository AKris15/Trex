import curses
from pathlib import Path

from . import state
from .render import render_tree

MENU_ITEMS = [
    "Create Directory",
    "Create File",
    "Undo",
    "Load Preset",
    "Save Structure",
    "Load Structure",
    "Quit",
]


def draw_menu(stdscr, selected: int):
    h, w = stdscr.getmaxyx()
    start_y = 2

    stdscr.addstr(start_y - 1, w - 20, "Actions", curses.A_BOLD)

    for i, item in enumerate(MENU_ITEMS):
        attr = curses.A_REVERSE if i == selected else curses.A_NORMAL
        stdscr.addstr(start_y + i, w - 20, item, attr)


def draw_tree(stdscr, root: Path, current: Path):
    stdscr.addstr(0, 0, root.name, curses.A_BOLD)

    lines = render_tree(root, current=current)
    for idx, line in enumerate(lines, start=1):
        stdscr.addstr(idx, 0, line)


def tui_main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)

    root = state.root_dir
    current = state.path_stack[-1]

    selected = 0

    while True:
        stdscr.clear()

        draw_tree(stdscr, root, current)
        draw_menu(stdscr, selected)

        key = stdscr.getch()

        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(MENU_ITEMS) - 1:
            selected += 1
        elif key in (10, 13):  # Enter
            if MENU_ITEMS[selected] == "Quit":
                break

        stdscr.refresh()
