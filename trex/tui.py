import curses
from pathlib import Path

from . import state
from .fs import create_dir, create_file, undo_last
from .presets import load_preset
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


def prompt(stdscr, message: str) -> str:
    h, w = stdscr.getmaxyx()
    stdscr.addstr(h - 2, 0, " " * (w - 1))
    stdscr.addstr(h - 2, 0, message)
    stdscr.refresh()

    curses.echo()
    value = stdscr.getstr(h - 2, len(message)).decode().strip()
    curses.noecho()

    return value


def tui_main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)

    root = state.root_dir
    selected = 0

    while True:
        current = state.path_stack[-1]

        stdscr.clear()
        draw_tree(stdscr, root, current)
        draw_menu(stdscr, selected)

        key = stdscr.getch()

        if key == curses.KEY_UP and selected > 0:
            selected -= 1

        elif key == curses.KEY_DOWN and selected < len(MENU_ITEMS) - 1:
            selected += 1

        elif key in (10, 13):  # Enter
            action = MENU_ITEMS[selected]

            if action == "Create Directory":
                name = prompt(stdscr, "Directory name: ")
                if name:
                    new_dir = create_dir(current, name)
                    if new_dir:
                        state.path_stack.append(new_dir)

            elif action == "Create File":
                name = prompt(stdscr, "File name: ")
                if name:
                    create_file(current, name)

            elif action == "Undo":
                undone = undo_last()
                if undone and not current.exists():
                    state.path_stack.pop()

            elif action == "Load Preset":
                value = prompt(stdscr, "Preset name or path: ")
                if value:
                    try:
                        load_preset(value, current)
                    except Exception as e:
                        prompt(stdscr, f"Error: {e} (press Enter)")

            elif action == "Quit":
                break

        stdscr.refresh()
