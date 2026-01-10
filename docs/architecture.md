# Architecture Overview

trex follows a layered architecture:

## Layers

1. Filesystem Layer (`fs.py`)
   - Safe create and undo operations

2. Tree Model (`tree.py`)
   - Serialize and apply directory structures

3. Preset Loader (`presets.py`)
   - Load declarative layouts

4. Renderer (`render.py`)
   - Convert filesystem into visual tree

5. TUI (`tui.py`)
   - Curses-based UI orchestration

## Design Decisions

- No recursion for navigation (stack-based)
- No filesystem mutation from UI
- Presets are data, not logic
