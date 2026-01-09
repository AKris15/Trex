from pathlib import Path
from . import state
from trex.fs import create_dir, create_file, undo_last


def main():
    root = Path("demo-root")
    root.mkdir(exist_ok=True)

    state.root_dir = root
    state.path_stack.append(root)

    # Demo operations (will be removed later)
    src = create_dir(root, "src")
    create_file(src, "main.py")
    create_file(src, "utils.py")

    undo_last()  # removes utils.py
    print("Works!")

if __name__ == "__main__":
    main()

