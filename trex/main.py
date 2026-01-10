import curses
from pathlib import Path

from trex import state
from trex.tui import tui_main


def main():
    root_name = input("Project directory name: ").strip()

    if not root_name:
        print("Error: project directory name cannot be empty.")
        return

    root = Path(root_name).expanduser().resolve()

    root.mkdir(parents=True, exist_ok=True)

    state.root_dir = root
    state.path_stack = [root]
    state.history.clear()

    curses.wrapper(tui_main)


if __name__ == "__main__":
    main()
