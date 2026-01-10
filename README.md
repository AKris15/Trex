# KTrex 

**KTrex** is an interactive, terminal-based directory and file structure builder.  
It lets you visually create, navigate, undo, save, load, and reuse project layouts
directly from a curses-based TUI — safely and deterministically.

> Think: `mkdir` + `tree` + `undo` + `presets` + `resume`, all in one tool.

---

## Features

- Interactive terminal UI (arrow-key driven)
- Create directories and files visually
- Safe undo (never deletes non-empty directories)
- Presets (builtin or external JSON)
- Save project structure to JSON
- Load and resume saved structures
- Non-destructive by design (no overwrites, no forced deletes)
- Works offline, zero runtime dependencies
- Scrollable tree view (keyboard + mouse)

---

## Installation

### Using pip (recommended)

```bash
pip install KTrex
````

### Editable install (for development)

```bash
git clone https://github.com/akris15/KTrex.git
cd KTrex
pip install -e .
```

---

## ▶️ Usage

Run KTrex inside any directory:

```bash
KTrex
```

You’ll be dropped into an interactive TUI showing your project tree and available actions.

---

## Controls

| Key                   | Action                         |
|-----------------------|--------------------------------|
| ↑ / ↓                 | Navigate menu                  |
| Enter                 | Select highlighted action      |
| PageUp / PageDown     | Scroll tree view               |
| Ctrl + U / Ctrl + D   | Scroll tree view               |
| Mouse Wheel           | Scroll tree view               |
| Any key               | Dismiss messages / dialogs     |
| Quit                  | Exit KTrex safely               |

---

## Actions Explained

### Create Directory

* Creates a new directory in the current location
* Automatically enters the directory

### Create File

* Creates a file in the current directory
* Does **not** change navigation

### Undo

* Reverts the most recent create action
* Only removes files or **empty directories**
* Never deletes non-empty directories

### Load Preset

* Load a predefined structure by name or file path
* Presets are **additive**, never destructive

### Save Structure

* Serialize the entire project tree to a JSON file
* Useful for reuse, backups, or AI-assisted generation

### Load Structure

* Load a previously saved structure JSON
* Applies safely without removing existing files

### Go Back

* Navigate to parent directory
* Cannot escape project root

### Help

* View built-in documentation and keybindings

---

## Presets

### Built-in presets

```text
ml_project
```

Usage:

```
Load Preset → ml_project
```

### External presets

```text
Load Preset → /path/to/custom_preset.json
```

Preset format is documented below.

---

## Preset / Structure Format

KTrex uses a simple, declarative JSON format:

```json
{
  "name": "project",
  "type": "dir",
  "children": [
    {
      "name": "src",
      "type": "dir",
      "children": [
        { "name": "main.py", "type": "file" }
      ]
    }
  ]
}
```

This format is shared by:

* presets
* saved structures
* AI-generated layouts

---

## Safety Guarantees

KTrex is designed to be **safe by default**:

* ❌ Never overwrites files
* ❌ Never deletes non-empty directories
* ❌ Never escapes project root
* ✅ Undo is leaf-only and predictable
* ✅ All destructive actions are explicit

---

Nice question — README polish matters a lot, especially if you want your repo to look **professional + sponsor-friendly**.

Below are **clean, modern ways** to upgrade both the **License** and **Sponsor** sections without overdoing it.

---

## 📜 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this software with proper attribution.

See the [LICENSE](./LICENSE) file for details.


## 💖 Sponsor

If you find this project useful and want to support its development:

[![Ko-Fi](https://img.shields.io/badge/☕%20Buy%20Me%20a%20Coffee-ko--fi-red)](https://ko-fi.com/akris)

Your support helps keep this project alive and actively maintained.
