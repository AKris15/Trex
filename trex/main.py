from pathlib import Path
import json
from . import state
from trex.fs import create_dir, create_file
from trex.tree import build_tree, apply_tree


def main():
    root = Path("demo-root")
    root.mkdir(exist_ok=True)

    state.root_dir = root
    state.path_stack.append(root)

    # Demo operations (will be removed later)
    src = create_dir(root, "src")
    create_file(src, "main.py")
    create_file(src, "utils.py")

    # SAVE STRUCTURE
    tree = build_tree(root)
    with open("structure.json", "w") as f:
        json.dump(tree, f, indent=2)

    # LOAD STRUCTURE INTO NEW ROOT
    clone = Path("demo-clone")
    clone.mkdir(exist_ok=True)

    with open("structure.json") as f:
        apply_tree(clone, json.load(f))

    print("Works!")

if __name__ == "__main__":
    main()
