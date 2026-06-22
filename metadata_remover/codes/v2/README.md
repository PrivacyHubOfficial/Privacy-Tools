# Version 2 - Usability Improvements

## Objective

Improve the readability and usability of the metadata inspection and removal process.

This version focuses on making metadata understandable to users.

---

## Components

### Reader

The reader converts EXIF tag numbers into meaningful labels.

Example:

Make: Samsung
Model: Galaxy S24
DateTime: 2026:06:22 10:15:30

Metadata is now easier to interpret.

### Remover

The remover introduces a safer image reconstruction process before exporting the cleaned image.

This reduces the likelihood of preserving hidden metadata.

---

## What Was Learned

- EXIF tag decoding
- Metadata interpretation
- Image reconstruction techniques
- Cleaner code organization

---

## Improvements Over Version 1

- Human-readable metadata
- Better user experience
- Safer metadata removal approach

---

## Limitations

- Code is still difficult to reuse
- No verification stage
- Limited scalability

---

## Next Improvement

Refactor the code into reusable functions and introduce metadata verification.