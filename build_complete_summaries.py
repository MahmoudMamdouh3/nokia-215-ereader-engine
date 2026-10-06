"""
Comprehensive Bilingual Summaries Generator
Generates executive study guides for the ENTIRETY of the library (66 books)
in both English (summaries/english/) and Arabic (summaries/arabic/).
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

SUMMARIES_BASE = r"E:\nokia\summaries"
EN_DIR = os.path.join(SUMMARIES_BASE, "english")
AR_DIR = os.path.join(SUMMARIES_BASE, "arabic")

os.makedirs(EN_DIR, exist_ok=True)
os.makedirs(AR_DIR, exist_ok=True)

# Helper function to save a summary pair
def save_summary(file_id, title_en, author, title_ar, thesis_en, thesis_ar, points_en, points_ar, takeaways_en, takeaways_ar, quotes_en=None, quotes_ar=None):
    # English formatting
    en_content = f"""# {title_en}
**Author:** {author}

## Executive Summary & Core Premise
{thesis_en.strip()}

## Key Structural Breakdown & Analysis
{points_en.strip()}

## Actionable Takeaways & Lessons
{takeaways_en.strip()}
"""
    if quotes_en:
        en_content += f"\n## Memorable Quotes\n{quotes_en.strip()}\n"

    # Arabic formatting
    ar_content = f"""# ملخص كتاب: {title_ar}
**المؤلف:** {author}

## الفكرة الجوهرية والملخص التنفيذي
{thesis_ar.strip()}

## التحليل البنيوي والمحاور الرئيسية
{points_ar.strip()}

## الدروس المستفادة والخلاصة العملية
{takeaways_ar.strip()}
"""
    if quotes_ar:
        ar_content += f"\n## اقتباسات خالدة\n{quotes_ar.strip()}\n"

    with open(os.path.join(EN_DIR, f"{file_id}.md"), "w", encoding="utf-8") as f:
        f.write(en_content.strip() + "\n")

    with open(os.path.join(AR_DIR, f"{file_id}_Arabic.md"), "w", encoding="utf-8") as f:
        f.write(ar_content.strip() + "\n")

    print(f"  [✓] Built: {file_id}")
