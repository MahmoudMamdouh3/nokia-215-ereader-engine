# -*- coding: utf-8 -*-
"""
Nokia 215 4G (2024) - Screen & Page Rendering Specifications
=============================================================

Empirical Calibration Result (verified on physical device 2026-10-07):
---------------------------------------------------------------------
- Hardware TFT LCD Resolution: 240 x 320 (QVGA)
- Persistent System UI Overhead: 40 pixels total
    - Top Status Bar (Battery, Signal, Time): ~20 px
    - Bottom Softkey Bar ("Options" / "Back"): ~20 px
- Exact Usable Image Viewer Area: 240 x 280 pixels
    - Verified via calibration test image `FIT_240x280.jpg` (Image #6)
    - Completely eliminates horizontal & vertical black letterbox bars.
    - Eliminates scaling blurriness and header/footer UI clipping.
"""

# Screen Dimensions
WIDTH = 240
HEIGHT = 280

# Horizontal Layout
MARGIN_X = 12
USABLE_WIDTH = WIDTH - (2 * MARGIN_X)  # 216 px

# Vertical Layout (Height = 280 px)
HEADER_Y = 7
HEADER_LINE_Y = 23
BODY_TOP_Y = 29

FOOTER_LINE_Y = 257  # 23 px above bottom (280 - 23 = 257)
FOOTER_Y = 262       # 18 px above bottom (280 - 18 = 262)

# Available vertical height for body text lines
USABLE_HEIGHT = FOOTER_LINE_Y - BODY_TOP_Y - 4  # 224 px

# Colors (TFT High-Contrast Optimized)
COLOR_BG = (255, 255, 255)
COLOR_TEXT = (15, 15, 15)
COLOR_HEADER = (100, 100, 100)
COLOR_FOOTER = (120, 120, 120)
COLOR_DIVIDER = (225, 225, 225)
COLOR_CODE_BG = (245, 245, 245)
COLOR_AR_AYAH = (0, 65, 35)

def draw_page_chrome(draw, header_text, page_num, total_pages, font_head, font_foot):
    """
    Renders standardized header divider, truncated header title,
    footer divider, and centered page counter string on a 240x280 page.
    """
    # Header Title (truncate with ellipsis if it overflows)
    h_text = header_text
    bbox_head = draw.textbbox((0, 0), h_text, font=font_head)
    while (bbox_head[2] - bbox_head[0]) > (USABLE_WIDTH + 4) and len(h_text) > 8:
        h_text = h_text[:-4] + "..."
        bbox_head = draw.textbbox((0, 0), h_text, font=font_head)
        
    draw.text((MARGIN_X, HEADER_Y), h_text, fill=COLOR_HEADER, font=font_head)
    draw.line([(MARGIN_X, HEADER_LINE_Y), (WIDTH - MARGIN_X, HEADER_LINE_Y)], fill=COLOR_DIVIDER, width=1)
    
    # Footer
    draw.line([(MARGIN_X, FOOTER_LINE_Y), (WIDTH - MARGIN_X, FOOTER_LINE_Y)], fill=COLOR_DIVIDER, width=1)
    foot_str = f"{page_num} / {total_pages}"
    bbox_foot = draw.textbbox((0, 0), foot_str, font=font_foot)
    foot_w = bbox_foot[2] - bbox_foot[0]
    draw.text(((WIDTH - foot_w) // 2, FOOTER_Y), foot_str, fill=COLOR_FOOTER, font=font_foot)
