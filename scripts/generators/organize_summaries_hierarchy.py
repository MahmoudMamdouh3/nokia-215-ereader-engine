"""
Organizes summaries into 9 ergonomic, keypad-friendly categories:
01_Computer_Science
02_Productivity_And_Finance
03_Power_And_Strategy
04_Spiritual_And_Religious
05_Russian_Literature
06_French_Literature
07_British_And_Irish_Literature
08_American_Literature
09_World_Classics_And_SciFi
"""

import os
import shutil

BASE_DIR = r"E:\nokia\summaries"

CATEGORY_MAPPING = {
    "01_Computer_Science": [
        "01_The_Pragmatic_Programmer",
        "02_Programming_Principles_And_Practice_Using_CPP"
    ],
    "02_Productivity_And_Finance": [
        "03_Atomic_Habits",
        "04_The_Psychology_Of_Money",
        "05_How_To_Win_Friends_And_Influence_People"
    ],
    "03_Power_And_Strategy": [
        "06_The_48_Laws_Of_Power",
        "07_The_33_Strategies_Of_War",
        "08_Mastery",
        "09_The_Laws_Of_Human_Nature",
        "10_The_Art_Of_Seduction",
        "11_The_50th_Law",
        "12_The_Daily_Laws"
    ],
    "04_Spiritual_And_Religious": [
        "13_The_Holy_Quran",
        "14_Tafsir_Al_Mukhtasar",
        "15_The_Holy_Bible"
    ],
    "05_Russian_Literature": [
        "16_Crime_And_Punishment",
        "17_The_Brothers_Karamazov",
        "18_White_Nights",
        "19_War_And_Peace",
        "20_Anna_Karenina",
        "21_The_Master_And_Margarita"
    ],
    "06_French_Literature": [
        "22_In_Search_Of_Lost_Time_Swanns_Way",
        "23_Les_Miserables",
        "24_Madame_Bovary",
        "25_The_Stranger",
        "26_The_Little_Prince",
        "27_The_Red_And_The_Black",
        "66_Journey_To_The_End_Of_The_Night"
    ],
    "07_British_And_Irish_Literature": [
        "28_Ulysses",
        "29_1984",
        "30_Animal_Farm",
        "31_Pride_And_Prejudice",
        "32_Wuthering_Heights",
        "33_Jane_Eyre",
        "34_Great_Expectations",
        "35_David_Copperfield",
        "36_Frankenstein",
        "37_The_Picture_Of_Dorian_Gray",
        "38_Heart_Of_Darkness",
        "39_To_The_Lighthouse",
        "40_Mrs_Dalloway",
        "41_The_Lord_Of_The_Rings",
        "65_Middlemarch"
    ],
    "08_American_Literature": [
        "42_The_Great_Gatsby",
        "43_Moby_Dick",
        "44_The_Catcher_In_The_Rye",
        "45_To_Kill_A_Mockingbird",
        "46_Adventures_Of_Huckleberry_Finn",
        "47_The_Grapes_Of_Wrath",
        "48_The_Sound_And_The_Fury",
        "49_Lolita",
        "50_Beloved",
        "53_The_Old_Man_And_The_Sea"
    ],
    "09_World_Classics_And_SciFi": [
        "51_Brave_New_World",
        "52_Dune",
        "54_Don_Quixote",
        "55_One_Hundred_Years_Of_Solitude",
        "56_Love_In_The_Time_Of_Cholera",
        "57_The_Trial",
        "58_The_Metamorphosis",
        "59_The_Castle",
        "60_The_Odyssey",
        "61_The_Iliad",
        "62_The_Divine_Comedy",
        "63_The_Magic_Mountain",
        "64_One_Thousand_And_One_Nights"
    ]
}

def organize():
    for lang, suffix in [("english", ""), ("arabic", "_Arabic")]:
        lang_dir = os.path.join(BASE_DIR, lang)
        for cat, book_ids in CATEGORY_MAPPING.items():
            cat_dir = os.path.join(lang_dir, cat)
            os.makedirs(cat_dir, exist_ok=True)
            for b_id in book_ids:
                filename = f"{b_id}{suffix}.md"
                src_path = os.path.join(lang_dir, filename)
                dst_path = os.path.join(cat_dir, filename)
                if os.path.exists(src_path):
                    shutil.move(src_path, dst_path)
                    print(f"Moved [{lang}] {filename} -> {cat}")

if __name__ == "__main__":
    organize()
