# 📐 Screen-Area Issue — Persistent S30+ UI & 240×280 Calibration

> **Status: 🟢 RESOLVED, CALIBRATED & DEPLOYED (2026-10-07).**
> Empirically verified on physical Nokia 215 4G (2024) hardware via calibration kit.
> Target Resolution: **240 × 280 pixels**.

---

## 1. Problem Statement: The Persistent UI Overlay

When viewing images in the Nokia 215 4G (2024) S30+ Gallery / Photo Viewer, the system enforces **persistent on-screen system UI bars** that cannot be hidden by any button shortcut or configuration:
1. **Top Status Bar**: Battery percentage/icon, cellular signal, and system clock (~20 px).
2. **Bottom Softkey Bar**: Contextual softkey actions ("Options" on left, "Back" on right) (~20 px).

Together, these system UI bars consume **40 vertical pixels** of the hardware 240×320 TFT LCD display.

```
+------------------------------------+  y = 0
|  📶 [Time]             🔋 [Status] |  (20 px Status Bar)
+====================================+  y = 20
|                                    |
|                                    |
|       ACTIVE VIEWER CANVAS         |
|                                    |
|          240 x 280 pixels          |
|                                    |
|                                    |
+====================================+  y = 300
|  Options                      Back |  (20 px Softkey Bar)
+------------------------------------+  y = 320
```

---

## 2. Mathematical Root Cause of the Letterboxing Bug

In early iterations of this project, book and manga pages were rendered at the hardware display resolution of **240 × 320 pixels**.

When the S30+ image viewer renders an image:
- The viewer window height is only **280 pixels** ($320 - 40 = 280$).
- Because the image was 320 pixels tall, the viewer performed proportional *fit-to-screen* scaling:
  $$\text{Scale Factor} = \frac{280}{320} = 0.875$$
- The scaled width became:
  $$\text{Scaled Width} = 240 \times 0.875 = 210\text{ px}$$
- As a consequence, the 210 px scaled image was centered horizontally on the 240 px display, leaving **15 pixels of black letterboxing bars on both the left and right sides** ($240 - 210 = 30\text{ px total padding}$, 15 px each side).
- Worse, the fractional downscaling caused typography interpolation blur, reducing readability of Georgia body text and Arabic Tashkeel diacritics.

---

## 3. Empirical Calibration Kit

To discover the exact pixel boundaries of the active viewing window, [`screen_calibration.py`](../screen_calibration.py) generated a series of 6 targeted test patterns:
- Image 1: `RULER_VERTICAL_240x320.jpg` — Dual 10-pixel tick rulers to read covered pixel counts directly.
- Image 2: `RULER_HORIZONTAL_240x320.jpg` — Horizontal edge alignment guides.
- Image 3: `GRID_240x320.jpg` — 10x10 colored grid with numeric coordinate anchors.
- Image 4: `FIT_240x240.jpg` — 1:1 aspect ratio square.
- Image 5: `FIT_240x260.jpg` — Conservative 60 px UI allowance.
- Image 6: `FIT_240x280.jpg` — **Calculated 40 px UI allowance (20 px top + 20 px bottom)**.

---

## 4. Hardware Verification & Calibration Results

The user tested the calibration suite on the physical device:

| Metric | Measured Value | Device Observation |
| :--- | :--- | :--- |
| **Viewer Scaling Behaviour** | Fit-to-screen (proportional) | Any image taller than 280 px induces width downscaling & black side bars |
| **Optimal Geometry** | **240 × 280 pixels (Image #6)** | **Confirmed**: Black side bars are 100% eliminated, edge-to-edge width |
| **Top Status Bar Height** | **20 pixels** | Exactly matches calculated boundary |
| **Bottom Softkey Bar Height** | **20 pixels** | Exactly matches calculated boundary |
| **Hardware LCD Resolution** | **240 × 320 pixels** | QVGA TFT LCD |
| **Total Persistent UI Overhead** | **40 pixels** | 20 px top + 20 px bottom |
| **True Usable Canvas** | **240 × 280 pixels** | **100% maximum screen real estate** |

---

## 5. Architectural Implementation: `screen_spec.py`

To prevent future regression, all rendering dimensions are centralized in [`screen_spec.py`](../screen_spec.py):

```python
WIDTH = 240
HEIGHT = 280

MARGIN_X = 12
USABLE_WIDTH = WIDTH - (2 * MARGIN_X)  # 216 px

HEADER_Y = 7
HEADER_LINE_Y = 23
BODY_TOP_Y = 29

FOOTER_LINE_Y = 257  # 23 px above bottom
FOOTER_Y = 262       # 18 px above bottom
USABLE_HEIGHT = FOOTER_LINE_Y - BODY_TOP_Y - 4  # 224 px
```

### Pipelines Migrated:
1. [`book_pipeline.py`](../book_pipeline.py): Literary Classics (`05`), Productivity & Finance (`02`), Quran Arabic & English (`01`).
2. [`robert_greene_pipeline.py`](../robert_greene_pipeline.py): 7 Power & Strategy books (`03`).
3. [`build_programming_books.py`](../build_programming_books.py): Pragmatic Programmer & C++ Principles 3rd Ed (`04`).
4. [`tafsir_pipeline.py`](../tafsir_pipeline.py): Tafsir Al-Mukhtasar Arabic & English 114 Surahs (`01`).
5. [`sync_books_to_phone.py`](../sync_books_to_phone.py): Buffered FAT32 transfer to `F:\Books`.

---

## 6. Developer Guidelines for Future Nokia Media Pipelines

1. **Never hard-code 240×320 for Gallery-based renderers.** Always use `screen_spec.py` (`240x280`).
2. **"Screen Resolution" ≠ "Viewer Canvas".** Firmware UI bars restrict the viewport.
3. **If targeting different Nokia firmware/models** (e.g., Nokia 225 4G, 6300 4G), run `screen_calibration.py` first to determine the model's status and softkey bar dimensions.
