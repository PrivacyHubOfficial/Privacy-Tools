# Case 001: Photo Metadata Leak

## Overview

Many people share photos online without knowing that hidden metadata is included in the file.

This metadata can contain sensitive information such as:

- GPS location
- Device type
- Time and date
- Software used

---

## What Happened

A user shared an image online.

The image looked harmless.

However, the file contained metadata that exposed:

- Exact location where the photo was taken
- Device information
- Time of capture

---

## The Risk

Even though the image itself was safe to share, the metadata created a privacy leak.

This could allow someone to:

- Identify the user’s location
- Track movement patterns
- Link images to a specific device
- Infer personal routines

---

## Root Cause

The issue was not the image itself.

It was the hidden metadata inside the file that was never removed before sharing.

---

## How It Could Have Been Prevented

- Remove metadata before uploading images
- Use metadata stripping tools
- Avoid sharing original files directly
- Use privacy-focused export methods

---

## Technical Insight

This is exactly the problem that metadata removal tools solve:

- Extract hidden metadata
- Identify sensitive fields
- Remove or sanitize data
- Export clean files

---

## Lesson Learned

Privacy risks are often invisible.

What is not seen is sometimes more dangerous than what is seen.