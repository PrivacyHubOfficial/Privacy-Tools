# Version 1 - Foundation

## Objective

Build the simplest possible metadata inspection and removal system.

This version focuses on understanding how metadata is stored inside image files and how it can be accessed using Python.

---

## Components

### Reader

The reader opens an image and displays its raw metadata.

Example output:

271: Samsung
272: Galaxy S24

At this stage, metadata tags are displayed in their raw numerical format.

### Remover

The remover creates a copy of the image and saves it as a new file.

This introduces the concept of metadata removal through image reconstruction.

---

## What Was Learned

- Opening image files with Pillow
- Accessing EXIF metadata
- Understanding raw metadata structures
- Saving modified image files

---

## Limitations

- Metadata tags are not human-readable
- No structured output
- No verification of metadata removal

---

## Next Improvement

Convert raw metadata into readable labels and improve usability.