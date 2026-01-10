# Safety Model

KTrex is designed to prevent accidental data loss.

## What KTrex will never do

- Delete non-empty directories
- Overwrite existing files
- Modify files without explicit action
- Escape the project root

## Undo Rules

- Only the most recent action can be undone
- Undo applies only to files or empty directories
- Undo fails safely if an operation is unsafe
