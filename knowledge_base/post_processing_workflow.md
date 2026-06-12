# Post-Processing Workflow Guide

## Purpose

This guide outlines a typical post-processing workflow from import to export,
covering culling, basic adjustments, color grading, and output settings.

## Workflow Overview

1. **Import & Backup** — Copy files from the memory card to your computer and a
   backup drive before doing anything else.
2. **Cull** — Quickly review images and flag/rate the best ones; reject obvious
   misses (out of focus, duplicates, blinks).
3. **Basic Adjustments** — Exposure, white balance, contrast, highlights/shadows.
4. **Color Grading** — Adjust hue/saturation/luminance per color, apply a
   consistent look across a set of images.
5. **Local Adjustments** — Dodge/burn, spot removal, graduated filters for skies.
6. **Sharpening & Noise Reduction** — Applied last, tailored to the output size
   and medium.
7. **Export** — Resize and format appropriately for the destination (web, print,
   social media).

## Basic Adjustments Explained

* **Exposure**: Overall brightness. Aim for a balanced histogram without clipped
  highlights or shadows (unless intentional, e.g. silhouettes).
* **White Balance**: Corrects color casts. Use a neutral gray/white reference in
  the frame if available, or adjust by eye until skin tones and neutrals look
  natural.
* **Contrast**: Difference between darks and lights. Increase for punchier images,
  decrease for a flatter, more "filmic" look.
* **Highlights/Shadows**: Recover detail in blown-out skies or dark shadow areas —
  RAW files have much more recovery latitude than JPEGs.

## Color Grading Basics

* Use HSL (Hue/Saturation/Luminance) panels to fine-tune individual colors (e.g.
  make greens less yellow, deepen blue skies).
* Split-toning or color-grading tools let you add distinct tones to shadows and
  highlights (e.g. cool shadows, warm highlights) for a cinematic look.
* Apply a consistent preset or look across a set of images from the same shoot for
  cohesion.

## Sharpening and Noise Reduction

* Apply sharpening based on output: web images need less sharpening than large
  prints viewed up close.
* Noise reduction is especially important for high-ISO images — apply luminance
  noise reduction to smooth grain, and color noise reduction to remove colored
  speckling, while preserving detail in the subject.

## Export Settings

| Destination | Resolution | Format | Color Space |
|---|---|---|---|
| Web / Social Media | 1080-2048px long edge | JPEG, quality 70-85% | sRGB |
| Email / Quick Share | 1200-1600px long edge | JPEG, quality 70% | sRGB |
| Print | Full resolution / per print size & DPI | TIFF or high-quality JPEG | sRGB or Adobe RGB (per printer spec) |

## Common Issue: Edited Photos Look Different on Other Devices/Screens

### Symptoms

* Colors or brightness look correct on the editing screen but appear off
  (too dark, too saturated, color-shifted) when viewed elsewhere

### Resolution

1. Check your monitor's calibration — uncalibrated monitors are a common cause of
   this mismatch. Consider a hardware calibration tool for serious editing work.
2. Ensure your export color space is sRGB for web/social media — most browsers and
   phones assume sRGB, and Adobe RGB images can look desaturated if
   misinterpreted.
3. Check ambient lighting in your editing space — bright or colored ambient light
   affects perceived brightness and color on screen.
4. View your edited image on multiple devices (phone, another monitor) before
   finalizing major edits.

## Escalation Criteria

* If color management issues persist across calibrated displays and correct color
  space exports, the issue may be with the output device itself (e.g. an
  uncalibrated printer profile) — consult the printer/lab's color profile
  documentation.
