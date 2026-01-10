from pathlib import Path

from trex import state
from trex.presets import load_preset
from trex.render import render_tree


def main():
    root = Path("demo-render")
    root.mkdir(exist_ok=True)

    state.root_dir = root
    state.path_stack = [root]

    load_preset("ml_project", root)

    print(root.name)
    for line in render_tree(root, current=root / "src"):
        print(line)

    print("\nWorks!")


if __name__ == "__main__":
    main()
