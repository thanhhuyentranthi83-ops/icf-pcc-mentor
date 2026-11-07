# -*- coding: utf-8 -*-
"""
Rebuild Module 1 Lessons with all 68 sub-competencies from raw_data.json / official PDF 2025:
- Formatted with definition in its own block
- Each sub-competency on its own distinct line with bold official code
- Preserves quizzes, objectives, commentaries, and examples
- Updates Module 1 header sourceDoc & sourceUrl to 2025 PDF
"""
import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = os.path.join(BASE_DIR, 'raw_data.json')
CURRICULUM_PATH = os.path.join(BASE_DIR, 'scripts', 'icf_curriculum_data.py')

with open(RAW_DATA_PATH, 'r', encoding='utf-8') as f:
    raw = json.load(f)

sheet = raw.get('02_Core_Competencies', [])

comps_data = {}
cur_comp = None
for r in sheet[2:]:
    no = r.get('B', '').strip()
    if no:
        cur_comp = no
        def_text = r.get('D', '').strip()
        def_en = def_text.split('\nVI:')[0].strip() if '\nVI:' in def_text else def_text
        def_vi = def_text.split('\nVI:')[1].strip() if '\nVI:' in def_text else def_text
        title_text = r.get('C', '').strip()
        title_en = title_text.split('\nVI:')[0].strip() if '\nVI:' in title_text else title_text
        title_vi = title_text.split('\nVI:')[1].strip() if '\nVI:' in title_text else title_text
        comps_data[cur_comp] = {
            'number': no,
            'titleEn': title_en,
            'titleVi': title_vi,
            'defEn': def_en,
            'defVi': def_vi,
            'subs': []
        }
    sub = r.get('E', '').strip()
    if cur_comp and sub:
        content = r.get('F', '').strip()
        sub_en = content.split('\nVI:')[0].strip() if '\nVI:' in content else content
        sub_vi = content.split('\nVI:')[1].strip() if '\nVI:' in content else content
        # Ensure sub_vi does not contain 'thân chủ'
        sub_vi = re.sub(r'thân chủ', 'khách hàng', sub_vi, flags=re.IGNORECASE)
        comps_data[cur_comp]['subs'].append({
            'code': sub,
            'textEn': sub_en,
            'textVi': sub_vi
        })

print(f"Loaded {len(comps_data)} competencies with total {sum(len(c['subs']) for c in comps_data.values())} sub-competencies.")

# Import existing MODULE_1_LESSONS to preserve quizzes, objectives, commentaries
import sys
sys.path.insert(0, os.path.join(BASE_DIR, 'scripts'))
from icf_curriculum_data import MODULE_1_LESSONS

PAGE_MAP = {
    '1.0': 3,
    '2.0': 4,
    '3.0': 5,
    '4.0': 6,
    '5.0': 7,
    '6.0': 8,
    '7.0': 9,
    '8.0': 10
}

updated_lessons = []
for les in MODULE_1_LESSONS:
    les_num = les.get('lessonNumber')
    if les_num and 1 <= les_num <= 8:
        comp_key = f"{les_num}.0"
        cdata = comps_data.get(comp_key)
        if cdata:
            # Rebuild originalExcerptEn: Definition block + each sub-item on its own line
            en_lines = [f"Definition: {cdata['defEn']}\n"]
            for s in cdata['subs']:
                en_lines.append(f"{s['code']}. {s['textEn']}")
            excerpt_en = "\n\n".join(en_lines)

            # Rebuild translationVi: Định nghĩa block + each sub-item on its own line
            vi_lines = [f"Định nghĩa: {cdata['defVi']}\n"]
            for s in cdata['subs']:
                vi_lines.append(f"{s['code']}. {s['textVi']}")
            trans_vi = "\n\n".join(vi_lines)

            les['definitionEn'] = cdata['defEn']
            les['definitionVi'] = cdata['defVi']
            les['subCompetencies'] = cdata['subs']
            les['originalExcerptEn'] = excerpt_en
            les['translationVi'] = trans_vi
            les['sourceDocument'] = f"Khung Năng Lực Cốt Lõi ICF (Bản 2025), Trang {PAGE_MAP.get(comp_key, '')}"
            les['sourceVersion'] = "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)"
            les['sourceLink'] = "https://coachingfederation.org/coaching-competencies/core-competencies"
            les['pdfLink'] = "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf"

    updated_lessons.append(les)

print("Updated 8 lessons with full definitions and sub-competencies.")

# Now update scripts/icf_curriculum_data.py
with open(CURRICULUM_PATH, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update sourceDoc in ALL_ICF_MODULES for mod-1
code = code.replace(
    '"sourceDoc": "ICF Updated Core Competencies (2019)",',
    '"sourceDoc": "Khung Năng Lực Cốt Lõi ICF (Bản 2025)",'
)
code = code.replace(
    '"sourceUrl": "https://coachingfederation.org/credentialing/core-competencies",',
    '"sourceUrl": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",'
)

# 2. Serialize updated MODULE_1_LESSONS
new_m1_lessons_str = "MODULE_1_LESSONS = " + json.dumps(updated_lessons, ensure_ascii=False, indent=4)

idx_m1_start = code.find('MODULE_1_LESSONS = [')
idx_m1_end = code.find('MODULE_1_WRAPUP =')
assert idx_m1_start != -1 and idx_m1_end != -1, "Cannot find MODULE_1_LESSONS or MODULE_1_WRAPUP"

code = code[:idx_m1_start] + new_m1_lessons_str + '\n\n# Wrap-up Quiz for Module 1\n' + code[idx_m1_end:]

# Verify no "thân chủ"
assert 'thân chủ' not in code.lower(), "Found thân chủ in generated code!"

with open(CURRICULUM_PATH, 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully written updated MODULE_1_LESSONS to scripts/icf_curriculum_data.py!")
