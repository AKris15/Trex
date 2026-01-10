import curses
from pathlib import Path

from trex import state
from trex.presets import load_preset
from trex.tui import tui_main


def main():
    root = Path("demo-tui")
    root.mkdir(exist_ok=True)

    state.root_dir = root
    state.path_stack = [root]

    load_preset("ml_project", root)

    curses.wrapper(tui_main)


if __name__ == "__main__":
    main()
