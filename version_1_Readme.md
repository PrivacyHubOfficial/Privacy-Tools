# Version 1 - Foundation (Progress Update)

## Objective

Build a simple system to inspect and remove image metadata using Python (Pillow), and understand how hidden information is stored inside image files.

This version focuses on learning how images behave as objects in Python and how metadata can be accessed, modified, and removed.

---

## Progress Made

### Metadata Reader

The reader loads images and extracts EXIF metadata.

It was tested with real camera images and returns structured metadata such as:

- Device manufacturer
- Phone model
- Camera software
- Capture timestamp
- Image properties (resolution, orientation)

Example output:

```text
271: MANUFACTURER_NAME
272: DEVICE_MODEL
305: CAMERA_APPLICATION
306: 2026:06:23 17:47:28