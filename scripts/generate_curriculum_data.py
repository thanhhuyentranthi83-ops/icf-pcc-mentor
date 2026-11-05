"""
Builder script to expand ICF PCC Mentor curriculum:
- 9 tailored, pure-PCC Case Studies (Zero coach projection/interpretation)
- 90 Leitner Flashcards (10 per section x 9 sections)
- 90 Diagnostic Mini Quizzes (10 per section x 9 sections)
- Exactly 50 authentic ICF SJT practice questions with dual BEST/WORST scoring
- 100% standardized "khách hàng" terminology
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "mentor_data.json")
SEED_TS_PATH = os.path.join(BASE_DIR, "src", "lib", "seedData.ts")

# 1. Load existing base data
with open(DATA_PATH, "r", encoding="utf-8") as f:
    existing = json.load(f)

sections = existing["sections"]
competencies = existing["competencies"]
theories = existing["theories"]
keywords = existing["keywords"]
mindfulness_messages = existing["mindfulnessMessages"]
stickers = existing["stickers"]
system_settings = existing["systemSettings"]
discount_codes = existing["discountCodes"]

leaf_sec_ids = ['sec-a1-1', 'sec-a1-2', 'sec-a2', 'sec-b1', 'sec-b2', 'sec-c1', 'sec-c2', 'sec-d1', 'sec-d2']

print(f"Base data loaded. Sections: {len(sections)}, Theories: {len(theories)}")
