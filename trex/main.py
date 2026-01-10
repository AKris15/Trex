from pathlib import Path

from trex.presets import load_preset

from . import state


def main():
    root = Path("demo-preset")
    root.mkdir(exist_ok=True)

    state.root_dir = root
    state.path_stack.append(root)

    load_preset("ml_project", root)

    print("Works!")


if __name__ == "__main__":
    main()
