# Presets

Presets define reusable directory structures in JSON format.

## Built-in Presets

KTrex ships with builtin presets located inside the package.

Example:
- ml_project

Usage:
```

Load Preset → ml_project

```

## External Presets

You can load presets from any file path:

```

Load Preset → /path/to/preset.json

````

## Preset Format

```json
{
  "name": "example",
  "type": "dir",
  "children": [
    { "name": "file.txt", "type": "file" }
  ]
}
````

Rules:

* Only `dir` and `file` types are allowed
* Children are optional
* Presets are additive
