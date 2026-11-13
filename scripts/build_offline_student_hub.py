# -*- coding: utf-8 -*-
"""
Master Builder: Hoc Coaching Offline Standalone Learning Hub HTML
Combines 7 Modules, 29 Lessons, 55 SJT Scenarios, 53 Competency Sets (400 Qs),
Glossary, Flashcards, Mindful Tea, and LocalStorage Journal into 1 single file.
"""

import sys, re, os, glob, json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))
import icf_curriculum_data as icf

print("Loading curriculum data...")
modules = icf.get_icf_7_modules()
glossary = icf.get_glossary_terms()
tea = icf.get_tea_micro_lessons()

print("Loading SJT practice questions...")
with open(os.path.join(BASE_DIR, 'src/lib/seedData.ts'), 'r', encoding='utf-8') as f:
    c = f.read()
m = re.search(r'export const PRACTICE_QUESTIONS = (\[.*?\]);', c, re.DOTALL)
sjt_questions = json.loads(m.group(1)) if m else []

print("Loading competency exam sets from Downloads...")
files = [
    ('Ethics 2: Bảo Mật & Tuân Thủ', '/Users/admin/Downloads/gemini-code-1790350393341.html'),
    ('Competency 1: Thực Hành Đạo Đức', '/Users/admin/Downloads/gemini-code-1790350067121.html'),
    ('Competency 4: Xây Dựng Tin Tưởng & An Toàn', '/Users/admin/Downloads/ICF Credentialing-Competency 4 Mock exam.html'),
    ('Competency 5: Duy Trì Sự Hiện Diện', '/Users/admin/Downloads/ICF ACC Mock Exam - Competency 5 .html'),
    ('Competency 7: Khơi Gợi Nhận Thức', '/Users/admin/Downloads/ICF ACC Mock Exam - Competency 7.html'),
    ('Competency 8: Thúc Đẩy Khách Hàng Phát Triển', '/Users/admin/Downloads/ICF ACC Mock Exam - Competency 8.html'),
    ('Glossary Exam: Thuật Ngữ Chuyên Sâu', '/Users/admin/Downloads/CF ACC Credentialing - Glossary Exam.html'),
]

competency_groups = []
for name, path in files:
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        fc = f.read()
    start = fc.find('const formsData = [')
    end = fc.find('let currentFormIndex', start)
    if start == -1 or end == -1:
        continue
    raw = fc[start + len('const formsData = '):end].strip().rstrip(';')
    cleaned = re.sub(r'(\b(?:id|title|questions|q|options|correct|explain)\b)\s*:', r'"\1":', raw)
    cleaned = re.sub(r',\s*([\]}])', r'\1', cleaned)
    try:
        data = json.loads(cleaned)
        competency_groups.append({
            'groupName': name,
            'sets': data
        })
    except Exception as e:
        print(f"Error parsing {name}: {e}")

# Sanitize terminology: 100% khách hàng, 0 thân chủ, Học Coaching instead of Mentor Thi
def sanitize_text(text):
    if not isinstance(text, str):
        return text
    text = re.sub(r'Thân\s+chủ', 'Khách hàng', text)
    text = re.sub(r'thân\s+chủ', 'khách hàng', text)
    text = re.sub(r'THÂN\s+CHỦ', 'KHÁCH HÀNG', text)
    text = re.sub(r'Mentor\s+Thi', 'Học Coaching', text)
    return text

def sanitize_obj(obj):
    if isinstance(obj, str):
        return sanitize_text(obj)
    elif isinstance(obj, list):
        return [sanitize_obj(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: sanitize_obj(v) for k, v in obj.items()}
    return obj

modules = sanitize_obj(modules)
glossary = sanitize_obj(glossary)
tea = sanitize_obj(tea)
sjt_questions = sanitize_obj(sjt_questions)
competency_groups = sanitize_obj(competency_groups)

print(f"Summary: {len(modules)} modules, {len(sjt_questions)} SJT items, {len(competency_groups)} competency groups")

# Dump datasets to JSON strings
json_modules = json.dumps(modules, ensure_ascii=False)
json_glossary = json.dumps(glossary, ensure_ascii=False)
json_tea = json.dumps(tea, ensure_ascii=False)
json_sjt = json.dumps(sjt_questions, ensure_ascii=False)
json_competency_groups = json.dumps(competency_groups, ensure_ascii=False)

html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Học Coaching - Cẩm Nang & Ứng Dụng Học Tập Toàn Diện | Coach Thanh Huyền</title>
    <meta name="description" content="Ứng dụng học tập và luyện thi ICF Credentialing offline độc lập. Trọn bộ 7 học phần ICF 2025, 55 tình huống SJT, 53 bộ đề trắc nghiệm năng lực, thuật ngữ và sổ học tập chánh niệm.">
    <style>
        :root {{
            --primary: #2d5a43;
            --primary-light: #eaf3ed;
            --primary-dark: #1b3a2a;
            --accent: #d47a8c;
            --accent-light: #fbeef1;
            --bg: #faf8f5;
            --card-bg: #ffffff;
            --sidebar-bg: #f4f0ea;
            --text-main: #1f2421;
            --text-sub: #5c6861;
            --border: #e3ded6;
            --border-light: #eee9e0;
            --success: #16a34a;
            --success-bg: #f0fdf4;
            --danger: #dc2626;
            --danger-bg: #fef2f2;
            --warning: #d97706;
            --warning-bg: #fffbeb;
            --shadow: 0 4px 12px rgba(45, 90, 67, 0.05);
            --shadow-lg: 0 8px 24px rgba(45, 90, 67, 0.08);
            --radius: 14px;
            --radius-sm: 8px;
        }}

        body.dark-mode {{
            --primary: #52a378;
            --primary-light: #1e3327;
            --primary-dark: #14241c;
            --accent: #e598a6;
            --accent-light: #3a1e24;
            --bg: #151816;
            --card-bg: #1c211e;
            --sidebar-bg: #181d1a;
            --text-main: #edf2ee;
            --text-sub: #a4b3aa;
            --border: #2c3630;
            --border-light: #242c27;
            --success-bg: #11281a;
            --danger-bg: #2d1417;
            --warning-bg: #2d2210;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            -webkit-tap-highlight-color: transparent;
        }}

        body {{
            background: var(--bg);
            color: var(--text-main);
            line-height: 1.6;
            font-size: 15px;
            padding-bottom: 60px;
            transition: background 0.3s ease, color 0.3s ease;
        }}

        /* Header Bar */
        header.top-header {{
            background: var(--card-bg);
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        }}
        .header-content {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 12px 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            flex-wrap: wrap;
        }}
        .brand-box {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .lotus-logo {{
            width: 40px;
            height: 40px;
            background: var(--accent-light);
            color: var(--accent);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            box-shadow: 0 2px 6px rgba(212,122,140,0.15);
        }}
        .brand-title {{
            font-size: 18px;
            font-weight: 700;
            color: var(--primary);
            letter-spacing: -0.01em;
            line-height: 1.2;
        }}
        .brand-slogan {{
            font-size: 12px;
            color: var(--text-sub);
            font-weight: 400;
        }}
        .coach-badge {{
            font-size: 11px;
            background: var(--primary-light);
            color: var(--primary);
            padding: 2px 8px;
            border-radius: 20px;
            font-weight: 600;
            margin-left: 6px;
        }}

        .header-stats {{
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .stat-chip {{
            display: flex;
            align-items: center;
            gap: 6px;
            background: var(--sidebar-bg);
            border: 1px solid var(--border);
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            color: var(--text-main);
        }}
        .stat-chip.lotus-chip {{
            background: var(--accent-light);
            border-color: var(--accent);
            color: var(--accent);
        }}
        .action-icon-btn {{
            background: var(--sidebar-bg);
            border: 1px solid var(--border);
            color: var(--text-main);
            width: 36px;
            height: 36px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 16px;
            transition: all 0.2s;
        }}
        .action-icon-btn:hover {{
            background: var(--primary-light);
            color: var(--primary);
            border-color: var(--primary);
        }}

        /* Main Nav Tabs */
        nav.nav-tabs-bar {{
            background: var(--card-bg);
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 65px;
            z-index: 90;
            overflow-x: auto;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }}
        .nav-tabs-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 16px;
            display: flex;
            gap: 6px;
        }}
        .main-tab-btn {{
            padding: 12px 16px;
            background: none;
            border: none;
            border-bottom: 3px solid transparent;
            font-size: 14px;
            font-weight: 600;
            color: var(--text-sub);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
        }}
        .main-tab-btn:hover {{
            color: var(--primary);
        }}
        .main-tab-btn.active {{
            color: var(--primary);
            border-bottom-color: var(--primary);
            background: var(--primary-light);
            border-radius: 8px 8px 0 0;
        }}

        /* Container */
        .container {{
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 16px;
        }}

        .tab-panel {{
            display: none;
        }}
        .tab-panel.active {{
            display: block;
            animation: fadeIn 0.25s ease-in-out;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(4px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* Cards & Grids */
        .card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 20px;
            box-shadow: var(--shadow);
            margin-bottom: 20px;
        }}

        /* Buttons */
        .btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 10px 18px;
            border-radius: var(--radius-sm);
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            border: none;
            transition: all 0.2s;
            text-decoration: none;
        }}
        .btn-primary {{
            background: var(--primary);
            color: #ffffff;
        }}
        .btn-primary:hover {{
            background: var(--primary-dark);
        }}
        .btn-accent {{
            background: var(--accent);
            color: #ffffff;
        }}
        .btn-accent:hover {{
            opacity: 0.9;
        }}
        .btn-outline {{
            background: transparent;
            border: 1px solid var(--border);
            color: var(--text-main);
        }}
        .btn-outline:hover {{
            border-color: var(--primary);
            color: var(--primary);
            background: var(--primary-light);
        }}
        .btn-sm {{
            padding: 6px 12px;
            font-size: 12px;
        }}

        /* TAB 1: CURRICULUM LAYOUT */
        .curriculum-layout {{
            display: grid;
            grid-template-columns: 340px 1fr;
            gap: 20px;
            align-items: start;
        }}
        @media (max-width: 860px) {{
            .curriculum-layout {{
                grid-template-columns: 1fr;
            }}
        }}
        .curriculum-sidebar {{
            background: var(--sidebar-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 16px;
            position: sticky;
            top: 130px;
            max-height: calc(100vh - 160px);
            overflow-y: auto;
        }}
        .module-group {{
            margin-bottom: 16px;
        }}
        .module-header {{
            font-size: 13px;
            font-weight: 700;
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 0.04em;
            margin-bottom: 8px;
            padding-bottom: 4px;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .lesson-nav-item {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
            padding: 8px 10px;
            margin-bottom: 4px;
            border-radius: var(--radius-sm);
            font-size: 13px;
            color: var(--text-main);
            cursor: pointer;
            background: transparent;
            border: 1px solid transparent;
            transition: all 0.15s;
        }}
        .lesson-nav-item:hover {{
            background: var(--card-bg);
            border-color: var(--border);
        }}
        .lesson-nav-item.active {{
            background: var(--card-bg);
            border-color: var(--primary);
            color: var(--primary);
            font-weight: 600;
            box-shadow: 0 2px 4px rgba(0,0,0,0.03);
        }}
        .lesson-nav-item .nav-status {{
            font-size: 12px;
        }}

        .lesson-detail-panel {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 24px;
            box-shadow: var(--shadow);
        }}
        .lesson-meta-bar {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 16px;
            flex-wrap: wrap;
        }}
        .tag-pill {{
            font-size: 12px;
            padding: 3px 10px;
            border-radius: 12px;
            font-weight: 600;
        }}
        .tag-pill.module-tag {{
            background: var(--primary-light);
            color: var(--primary);
        }}
        .tag-pill.time-tag {{
            background: var(--sidebar-bg);
            color: var(--text-sub);
        }}
        .tag-pill.status-done {{
            background: var(--success-bg);
            color: var(--success);
        }}

        .lesson-section-box {{
            background: var(--sidebar-bg);
            border: 1px solid var(--border-light);
            border-radius: var(--radius-sm);
            padding: 16px;
            margin-bottom: 18px;
        }}
        .lesson-section-box h4 {{
            font-size: 14px;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .source-excerpt {{
            font-family: inherit;
            font-size: 13px;
            color: var(--text-sub);
            white-space: pre-wrap;
            background: var(--card-bg);
            padding: 12px;
            border-radius: 6px;
            border-left: 3px solid var(--primary);
            margin-bottom: 12px;
        }}

        /* TAB 2: SJT SCENARIOS */
        .sjt-controls {{
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
        }}
        .filter-group {{
            display: flex;
            gap: 6px;
            overflow-x: auto;
            padding-bottom: 4px;
        }}
        .filter-btn {{
            padding: 6px 12px;
            border-radius: 20px;
            border: 1px solid var(--border);
            background: var(--card-bg);
            color: var(--text-sub);
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            white-space: nowrap;
        }}
        .filter-btn.active {{
            background: var(--primary);
            color: #fff;
            border-color: var(--primary);
        }}

        .scenario-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: var(--shadow);
            position: relative;
        }}
        .scenario-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 14px;
            border-bottom: 1px solid var(--border-light);
            padding-bottom: 10px;
        }}
        .scenario-competency {{
            font-size: 12px;
            font-weight: 700;
            color: var(--primary);
            background: var(--primary-light);
            padding: 3px 10px;
            border-radius: 12px;
        }}
        .scenario-text-en {{
            font-size: 15px;
            font-weight: 600;
            color: var(--text-main);
            margin-bottom: 8px;
            line-height: 1.5;
        }}
        .scenario-text-vi {{
            font-size: 14px;
            color: var(--text-sub);
            margin-bottom: 16px;
            font-style: italic;
        }}
        .scenario-options-grid {{
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 20px;
        }}
        .sjt-option-row {{
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 14px 16px;
            background: var(--card-bg);
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 16px;
            align-items: center;
            transition: all 0.15s;
        }}
        .sjt-option-row:hover {{
            background: var(--sidebar-bg);
        }}
        .option-text-box {{
            font-size: 14px;
        }}
        .option-key {{
            font-weight: 700;
            color: var(--primary);
            margin-right: 6px;
        }}
        .option-pickers {{
            display: flex;
            gap: 8px;
        }}
        .pick-btn {{
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            border: 1px solid var(--border);
            background: var(--card-bg);
            color: var(--text-sub);
            transition: all 0.15s;
        }}
        .pick-btn.pick-best.selected {{
            background: var(--success);
            color: #fff;
            border-color: var(--success);
            box-shadow: 0 2px 6px rgba(22,163,74,0.3);
        }}
        .pick-btn.pick-worst.selected {{
            background: var(--danger);
            color: #fff;
            border-color: var(--danger);
            box-shadow: 0 2px 6px rgba(220,38,38,0.3);
        }}

        .sjt-feedback-box {{
            background: var(--sidebar-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 16px;
            margin-top: 16px;
            display: none;
            animation: fadeIn 0.3s;
        }}
        .sjt-feedback-box.show {{
            display: block;
        }}
        .feedback-item {{
            margin-bottom: 10px;
            font-size: 13px;
        }}
        .feedback-item:last-child {{
            margin-bottom: 0;
        }}
        .badge-best {{
            color: var(--success);
            font-weight: 700;
        }}
        .badge-worst {{
            color: var(--danger);
            font-weight: 700;
        }}

        /* TAB 3: COMPETENCY MOCK EXAM SETS */
        .comp-selector-bar {{
            display: flex;
            gap: 8px;
            margin-bottom: 16px;
            overflow-x: auto;
            padding-bottom: 6px;
        }}
        .comp-group-btn {{
            padding: 8px 14px;
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            font-size: 13px;
            font-weight: 600;
            color: var(--text-sub);
            cursor: pointer;
            white-space: nowrap;
        }}
        .comp-group-btn.active {{
            background: var(--primary);
            color: #fff;
            border-color: var(--primary);
        }}

        .set-pills-bar {{
            display: flex;
            gap: 6px;
            margin-bottom: 20px;
            overflow-x: auto;
            padding-bottom: 6px;
        }}
        .set-pill-btn {{
            padding: 6px 12px;
            background: var(--sidebar-bg);
            border: 1px solid var(--border);
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            color: var(--text-main);
            cursor: pointer;
        }}
        .set-pill-btn.active {{
            background: var(--accent);
            color: #fff;
            border-color: var(--accent);
        }}

        .quiz-question-block {{
            margin-bottom: 20px;
            padding-bottom: 16px;
            border-bottom: 1px solid var(--border-light);
        }}
        .quiz-q-title {{
            font-weight: 700;
            font-size: 14px;
            margin-bottom: 10px;
        }}
        .quiz-options-list {{
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}
        .quiz-option-label {{
            display: flex;
            align-items: flex-start;
            gap: 10px;
            padding: 10px 14px;
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            background: var(--card-bg);
            font-size: 13px;
            cursor: pointer;
            transition: all 0.15s;
        }}
        .quiz-option-label:hover {{
            background: var(--sidebar-bg);
        }}
        .quiz-option-label.selected {{
            background: var(--primary-light);
            border-color: var(--primary);
        }}
        .quiz-option-label.is-correct {{
            background: var(--success-bg) !important;
            border-color: var(--success) !important;
            color: var(--success);
            font-weight: 600;
        }}
        .quiz-option-label.is-wrong {{
            background: var(--danger-bg) !important;
            border-color: var(--danger) !important;
            color: var(--danger);
        }}
        .quiz-feedback {{
            margin-top: 10px;
            padding: 10px 12px;
            border-radius: 6px;
            font-size: 13px;
            display: none;
        }}
        .quiz-feedback.show {{
            display: block;
        }}
        .quiz-feedback.success {{
            background: var(--success-bg);
            color: var(--success);
            border: 1px solid #bbf7d0;
        }}
        .quiz-feedback.error {{
            background: var(--danger-bg);
            color: var(--danger);
            border: 1px solid #fecaca;
        }}

        /* TAB 4: GLOSSARY & FLASHCARDS */
        .search-box-wrap {{
            margin-bottom: 20px;
            position: relative;
        }}
        .search-input {{
            width: 100%;
            padding: 12px 16px 12px 40px;
            border-radius: 30px;
            border: 1px solid var(--border);
            background: var(--card-bg);
            color: var(--text-main);
            font-size: 14px;
            outline: none;
            transition: all 0.2s;
        }}
        .search-input:focus {{
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(45,90,67,0.1);
        }}
        .search-icon {{
            position: absolute;
            left: 14px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-sub);
            font-size: 16px;
        }}

        .glossary-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 16px;
        }}
        .glossary-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 18px;
            box-shadow: var(--shadow);
            transition: transform 0.2s;
        }}
        .glossary-card:hover {{
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }}
        .term-en {{
            font-size: 16px;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 4px;
        }}
        .term-vi {{
            font-size: 14px;
            font-weight: 600;
            color: var(--text-main);
            margin-bottom: 8px;
        }}
        .term-desc {{
            font-size: 13px;
            color: var(--text-sub);
            line-height: 1.5;
        }}

        /* Flashcard 3D */
        .flashcard-stage {{
            max-width: 560px;
            margin: 30px auto;
            perspective: 1000px;
        }}
        .flashcard-inner {{
            width: 100%;
            min-height: 260px;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
        }}
        .flashcard-inner.flipped {{
            transform: rotateY(180deg);
        }}
        .flashcard-face {{
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            border-radius: var(--radius);
            border: 1px solid var(--border);
            padding: 30px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            box-shadow: var(--shadow-lg);
        }}
        .flashcard-front {{
            background: var(--card-bg);
            color: var(--primary);
        }}
        .flashcard-back {{
            background: var(--sidebar-bg);
            color: var(--text-main);
            transform: rotateY(180deg);
        }}

        /* TAB 5: MINDFUL TEA & BREATHING */
        .breathing-card {{
            text-align: center;
            padding: 40px 20px;
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            margin-bottom: 30px;
        }}
        .breathing-circle-wrap {{
            width: 160px;
            height: 160px;
            margin: 0 auto 20px;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .breathing-circle {{
            width: 80px;
            height: 80px;
            background: var(--accent-light);
            border: 3px solid var(--accent);
            border-radius: 50%;
            transition: all 4s ease-in-out;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
        }}
        .breathing-circle.inhale {{
            transform: scale(1.6);
            background: var(--primary-light);
            border-color: var(--primary);
        }}
        .breathing-circle.exhale {{
            transform: scale(1);
            background: var(--accent-light);
            border-color: var(--accent);
        }}
        .breathing-prompt {{
            font-size: 18px;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 8px;
        }}

        /* TAB 6: JOURNAL & LOTUS GARDEN */
        .lotus-garden-box {{
            background: linear-gradient(135deg, var(--card-bg) 0%, var(--sidebar-bg) 100%);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 30px;
            text-align: center;
            margin-bottom: 30px;
        }}
        .garden-blooms {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            justify-content: center;
            margin: 20px 0;
            min-height: 50px;
        }}
        .lotus-flower-icon {{
            font-size: 24px;
            animation: popIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }}
        @keyframes popIn {{
            from {{ transform: scale(0); }}
            to {{ transform: scale(1); }}
        }}

        .notes-list {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        .note-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 16px;
        }}
        .note-title {{
            font-weight: 700;
            font-size: 14px;
            color: var(--primary);
            margin-bottom: 6px;
        }}
        .note-content {{
            font-size: 13px;
            color: var(--text-main);
            white-space: pre-wrap;
        }}

        /* Print Media */
        @media print {{
            header.top-header, nav.nav-tabs-bar, .action-bar, .pick-btn, .btn, .search-box-wrap {{
                display: none !important;
            }}
            .container {{
                max-width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
            }}
            .tab-panel {{
                display: block !important;
                page-break-after: always;
            }}
            .card, .scenario-card, .lesson-detail-panel {{
                box-shadow: none !important;
                border: 1px solid #ccc !important;
            }}
        }}
    </style>
    <!-- Supabase JS Client v2 CDN -->
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
</head>
<body>

<!-- Top Header -->
<header class="top-header">
    <div class="header-content">
        <div class="brand-box">
            <div class="lotus-logo">🪷</div>
            <div>
                <div class="brand-title">Học Coaching <span class="coach-badge">Coach Thanh Huyền</span></div>
                <div class="brand-slogan">Đưa coaching trở thành lối sống • Cẩm nang học tập & Luyện thi ICF PCC</div>
            </div>
        </div>

        <div class="header-stats">
            <div class="stat-chip" id="supabaseStatusChip" title="Đã kết nối cơ sở dữ liệu Supabase">
                <span>☁️</span>
                <span id="supabaseStatusText">Supabase Connected</span>
            </div>
            <div class="stat-chip lotus-chip">
                <span>🪷</span>
                <span id="lotusCount">0</span> Đóa sen
            </div>
            <div class="stat-chip">
                <span>📚</span>
                <span id="completedLessonsCount">0</span>/29 Bài học
            </div>
            <div class="stat-chip">
                <span>🎯</span>
                <span id="sjtAccuracy">0%</span> SJT Đạt
            </div>
            <button class="action-icon-btn" onclick="openBreathingModal()" title="Thực hành hít thở chánh niệm 30s">🫖</button>
            <button class="action-icon-btn" onclick="toggleDarkMode()" title="Chuyển chế độ sáng/tối">🌓</button>
            <button class="action-icon-btn" onclick="window.print()" title="In cẩm nang / Xuất PDF">🖨️</button>
        </div>
    </div>
</header>

<!-- Main Navigation Tabs -->
<nav class="nav-tabs-bar">
    <div class="nav-tabs-container">
        <button class="main-tab-btn active" onclick="switchMainTab('curriculum')">🌿 Lộ Trình Học Tập (7 Học Phần)</button>
        <button class="main-tab-btn" onclick="switchMainTab('sjt')">🎯 Thi Thử SJT (55 Tình Huống)</button>
        <button class="main-tab-btn" onclick="switchMainTab('competency')">📝 Đề Thi Theo Năng Lực (53 Sets)</button>
        <button class="main-tab-btn" onclick="switchMainTab('glossary')">📖 Thuật Ngữ & Flashcards</button>
        <button class="main-tab-btn" onclick="switchMainTab('tea')">🍵 Thưởng Trà & Chánh Niệm</button>
        <button class="main-tab-btn" onclick="switchMainTab('journal')">🪷 Sổ Học Tập & Vườn Sen</button>
    </div>
</nav>

<!-- Main Container -->
<main class="container">

    <!-- ========================================================================= -->
    <!-- TAB 1: CURRICULUM -->
    <!-- ========================================================================= -->
    <section id="panel-curriculum" class="tab-panel active">
        <div class="curriculum-layout">
            <!-- Sidebar -->
            <aside class="curriculum-sidebar" id="curriculumSidebar">
                <!-- Injected via JS -->
            </aside>

            <!-- Detail Area -->
            <div class="lesson-detail-panel" id="lessonDetailPanel">
                <!-- Injected via JS -->
            </div>
        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- TAB 2: SJT SCENARIOS -->
    <!-- ========================================================================= -->
    <section id="panel-sjt" class="tab-panel">
        <div class="sjt-controls">
            <div class="filter-group" id="sjtFilterGroup">
                <button class="filter-btn active" onclick="filterSjt('all')">Tất cả (55 câu)</button>
                <button class="filter-btn" onclick="filterSjt('daily10')">⚡ Luyện 10 câu ngẫu nhiên</button>
                <button class="filter-btn" onclick="filterSjt('Ethical')">Đạo Đức (Ethics)</button>
                <button class="filter-btn" onclick="filterSjt('Presence')">Hiện Diện (Presence)</button>
                <button class="filter-btn" onclick="filterSjt('Listening')">Lắng Nghe (Listening)</button>
                <button class="filter-btn" onclick="filterSjt('Awareness')">Khơi Gợi (Awareness)</button>
            </div>
            <div style="font-size: 13px; color: var(--text-sub);">
                Quy tắc: Chọn đúng <b>1 BEST (+1đ)</b> và <b>1 WORST (+1đ)</b>
            </div>
        </div>

        <div id="sjtScenariosList">
            <!-- Injected via JS -->
        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- TAB 3: COMPETENCY MOCK EXAM SETS -->
    <!-- ========================================================================= -->
    <section id="panel-competency" class="tab-panel">
        <div class="card" style="margin-bottom: 16px;">
            <div style="font-size: 14px; font-weight: 700; color: var(--primary); margin-bottom: 8px;">
                Chọn Nhóm Năng Lực & Bộ Đề Thực Hành:
            </div>
            <div class="comp-selector-bar" id="compGroupBar">
                <!-- Injected via JS -->
            </div>
            <div class="set-pills-bar" id="compSetPillsBar">
                <!-- Injected via JS -->
            </div>
        </div>

        <div id="compScoreContainer" style="display:none;" class="card"></div>

        <div class="card" id="compQuestionsContainer">
            <!-- Injected via JS -->
        </div>

        <div style="display: flex; gap: 12px; justify-content: center; margin-top: 20px;">
            <button class="btn btn-primary" onclick="gradeCurrentCompSet()">✔️ Chấm Điểm Set Này</button>
            <button class="btn btn-outline" onclick="resetCurrentCompSet()">🔄 Làm Lại Set Này</button>
        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- TAB 4: GLOSSARY & FLASHCARDS -->
    <!-- ========================================================================= -->
    <section id="panel-glossary" class="tab-panel">
        <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 10px;">
                <div style="display: flex; gap: 8px;">
                    <button class="btn btn-primary btn-sm" id="btnViewGlossaryList" onclick="toggleGlossaryView('list')">📋 Danh Sách Từ Điển</button>
                    <button class="btn btn-outline btn-sm" id="btnViewGlossaryCards" onclick="toggleGlossaryView('cards')">🃏 Thẻ Ghi Nhớ (Flashcards)</button>
                </div>
                <div style="font-size: 13px; color: var(--text-sub);">
                    15 Thuật ngữ song ngữ chuẩn hóa ICF 2025
                </div>
            </div>

            <div class="search-box-wrap">
                <span class="search-icon">🔍</span>
                <input type="text" class="search-input" id="glossarySearchInput" placeholder="Tìm kiếm thuật ngữ tiếng Anh hoặc tiếng Việt (VD: Partnering, Khách hàng, Bảo mật)..." oninput="handleGlossarySearch()">
            </div>

            <!-- List View -->
            <div class="glossary-grid" id="glossaryGrid">
                <!-- Injected via JS -->
            </div>

            <!-- Flashcard View -->
            <div id="flashcardView" style="display: none;">
                <div class="flashcard-stage">
                    <div class="flashcard-inner" id="flashcardInner" onclick="flipFlashcard()">
                        <div class="flashcard-face flashcard-front">
                            <span style="font-size: 12px; text-transform: uppercase; color: var(--text-sub); letter-spacing: 0.05em; margin-bottom: 10px;">Thẻ Ghi Nhớ ICF • Bấm để lật xem nghĩa</span>
                            <h2 id="fcTermEn" style="font-size: 24px; color: var(--primary); margin-bottom: 8px;"></h2>
                            <p id="fcCategory" style="font-size: 13px; color: var(--accent); font-weight: 600;"></p>
                        </div>
                        <div class="flashcard-face flashcard-back">
                            <span style="font-size: 12px; text-transform: uppercase; color: var(--text-sub); margin-bottom: 10px;">Định Nghĩa Chuẩn Mực</span>
                            <h3 id="fcTermVi" style="font-size: 18px; color: var(--primary); margin-bottom: 12px;"></h3>
                            <p id="fcDefVi" style="font-size: 14px; color: var(--text-main); line-height: 1.5;"></p>
                        </div>
                    </div>
                </div>

                <div style="display: flex; gap: 12px; justify-content: center; align-items: center; margin-top: 16px;">
                    <button class="btn btn-outline btn-sm" onclick="prevFlashcard()">⬅️ Thẻ Trước</button>
                    <span id="fcCounter" style="font-size: 13px; font-weight: 600; color: var(--text-sub);">1 / 15</span>
                    <button class="btn btn-outline btn-sm" onclick="nextFlashcard()">Thẻ Kế Tiếp ➡️</button>
                </div>
            </div>
        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- TAB 5: MINDFUL TEA & BREATHING -->
    <!-- ========================================================================= -->
    <section id="panel-tea" class="tab-panel">
        <div class="breathing-card">
            <h2 style="font-size: 20px; color: var(--primary); margin-bottom: 6px;">Khoảng Lặng Thưởng Trà & Hít Thở 30 Giây</h2>
            <p style="font-size: 13px; color: var(--text-sub); margin-bottom: 24px;">Trước khi học hoặc bước vào phòng thi, hãy dành 30 giây để trở về với hiện tại trọn vẹn.</p>
            
            <div class="breathing-circle-wrap">
                <div class="breathing-circle" id="breathingCircle">🪷</div>
            </div>
            <div class="breathing-prompt" id="breathingText">Sẵn sàng hít thở...</div>
            <button class="btn btn-accent btn-sm" id="btnStartBreathing" onclick="startBreathingCycle()">Bắt Đầu 30 Giây Hít Thở</button>
        </div>

        <h3 style="font-size: 18px; color: var(--primary); margin-bottom: 16px;">Các Bài Học Thưởng Trà Vi Mô (Tea Micro-Lessons)</h3>
        <div class="glossary-grid" id="teaLessonsGrid">
            <!-- Injected via JS -->
        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- TAB 6: JOURNAL & LOTUS GARDEN -->
    <!-- ========================================================================= -->
    <section id="panel-journal" class="tab-panel">
        <div class="lotus-garden-box">
            <h2 style="font-size: 22px; color: var(--primary); margin-bottom: 6px;">Vườn Sen Chánh Niệm Của Tôi</h2>
            <p style="font-size: 14px; color: var(--text-sub);">Mỗi bài học hoàn thành hoặc đề thi đạt điểm giúp 1 đóa sen chánh niệm bung nở.</p>
            
            <div class="garden-blooms" id="gardenBloomsContainer">
                <!-- Lotus icons injected via JS -->
            </div>

            <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
                <button class="btn btn-outline btn-sm" onclick="exportDataJson()">💾 Sao Lưu Tiến Độ (Tải File JSON)</button>
                <label class="btn btn-outline btn-sm" style="cursor: pointer;">
                    📥 Nhập Bản Sao Lưu
                    <input type="file" id="importFileInput" accept=".json" style="display: none;" onchange="importDataJson(event)">
                </label>
                <button class="btn btn-outline btn-sm" onclick="resetAllProgress()" style="color: var(--danger);">🗑️ Làm Lại Từ Đầu</button>
            </div>
        </div>

        <div class="card">
            <h3 style="font-size: 16px; font-weight: 700; color: var(--primary); margin-bottom: 12px;">Sổ Ghi Chép & Chiêm Nghiệm Của Tôi (Reflection Journal)</h3>
            <div id="journalNotesContainer" class="notes-list">
                <!-- Injected via JS -->
            </div>
        </div>
    </section>

</main>

<!-- Injected Embedded Data -->
<script>
const CURRICULUM_MODULES = {json_modules};
const GLOSSARY_TERMS = {json_glossary};
const TEA_LESSONS = {json_tea};
const SJT_QUESTIONS = {json_sjt};
const COMPETENCY_GROUPS = {json_competency_groups};

// =========================================================================
// KHỞI TẠO KẾT NỐI SUPABASE CLOUD (SUPABASE CLIENT INITIALIZATION)
// =========================================================================
const SUPABASE_PROJECT_URL = "https://ebfmbqgzttjcivcoyncb.supabase.co";
const SUPABASE_PUBLISHABLE_KEY = "sb_publishable_JEbnW3h1PCT58KWt5eT5yg_Z-RAuq74";

// Alias tương thích các chuẩn gọi cấu hình
const SUPABASE_URL = SUPABASE_PROJECT_URL;
const SUPABASE_ANON_KEY = SUPABASE_PUBLISHABLE_KEY;

// Khởi tạo Supabase Client (dùng var supabaseClient để tránh xung đột SyntaxError với identifier của thư viện CDN)
var supabaseClient = null;
try {{
    if (typeof window !== "undefined" && window.supabase && typeof window.supabase.createClient === "function") {{
        supabaseClient = window.supabase.createClient(SUPABASE_PROJECT_URL, SUPABASE_PUBLISHABLE_KEY);
        window.supabaseClient = supabaseClient;
        console.log("🌿 Supabase client đã sẵn sàng kết nối:", SUPABASE_PROJECT_URL);
    }}
}} catch (err) {{
    console.warn("⚠️ Không thể khởi tạo Supabase client:", err);
}}

// LocalStorage Persistence Keys
const STORE_KEY_PROGRESS = "hoc_coaching_offline_progress_v1";
const STORE_KEY_NOTES = "hoc_coaching_offline_notes_v1";
const STORE_KEY_DARK = "hoc_coaching_offline_dark_v1";

let appState = {{
    completedLessons: {{}}, // lessonId -> {{ status: 'done', score: 100 }}
    sjtAnswers: {{}},       // qId -> {{ best: 'A', worst: 'B', isCorrect: true }}
    compAnswers: {{}},      // `group_set_q` -> optIdx
    notes: {{}},            // lessonId -> "note text"
    lotusCount: 0
}};

function loadAppState() {{
    try {{
        const rawProg = localStorage.getItem(STORE_KEY_PROGRESS);
        if (rawProg) {{
            const parsed = JSON.parse(rawProg);
            appState.completedLessons = parsed.completedLessons || {{}};
            appState.sjtAnswers = parsed.sjtAnswers || {{}};
            appState.compAnswers = parsed.compAnswers || {{}};
            appState.lotusCount = parsed.lotusCount || 0;
        }}
        const rawNotes = localStorage.getItem(STORE_KEY_NOTES);
        if (rawNotes) {{
            appState.notes = JSON.parse(rawNotes);
        }}
    }} catch(e) {{
        console.warn("Storage load error:", e);
    }}
    updateGlobalStats();
}}

function saveAppState() {{
    try {{
        localStorage.setItem(STORE_KEY_PROGRESS, JSON.stringify({{
            completedLessons: appState.completedLessons,
            sjtAnswers: appState.sjtAnswers,
            compAnswers: appState.compAnswers,
            lotusCount: appState.lotusCount
        }}));
        localStorage.setItem(STORE_KEY_NOTES, JSON.stringify(appState.notes));
    }} catch(e) {{
        console.warn("Storage save error:", e);
    }}
    updateGlobalStats();
}}

function updateGlobalStats() {{
    // Calculate completed lessons
    const doneCount = Object.keys(appState.completedLessons).length;
    document.getElementById("completedLessonsCount").innerText = doneCount;
    
    // Calculate SJT accuracy
    const sjtKeys = Object.keys(appState.sjtAnswers);
    let sjtCorrect = 0;
    sjtKeys.forEach(k => {{
        if (appState.sjtAnswers[k].isCorrect) sjtCorrect++;
    }});
    const pct = sjtKeys.length ? Math.round((sjtCorrect / sjtKeys.length) * 100) : 0;
    document.getElementById("sjtAccuracy").innerText = pct + "%";

    // Lotus Count
    document.getElementById("lotusCount").innerText = appState.lotusCount;

    // Update garden if in view
    renderGardenBlooms();
}}

function addLotus() {{
    appState.lotusCount++;
    saveAppState();
}}

/* Tab Switching */
function switchMainTab(tabName) {{
    document.querySelectorAll(".main-tab-btn").forEach(b => b.classList.remove("active"));
    document.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));
    
    const targetPanel = document.getElementById("panel-" + tabName);
    if (targetPanel) targetPanel.classList.add("active");
    
    const btn = Array.from(document.querySelectorAll(".main-tab-btn")).find(b => b.getAttribute("onclick").includes(tabName));
    if (btn) btn.classList.add("active");
    window.scrollTo({{ top: 0, behavior: 'smooth' }});

    if (tabName === 'journal') renderJournalNotes();
}}

/* Dark Mode */
function toggleDarkMode() {{
    document.body.classList.toggle("dark-mode");
    const isDark = document.body.classList.contains("dark-mode");
    localStorage.setItem(STORE_KEY_DARK, isDark ? "1" : "0");
}}
if (localStorage.getItem(STORE_KEY_DARK) === "1") {{
    document.body.classList.add("dark-mode");
}}

/* ========================================================================= */
/* TAB 1: CURRICULUM LOGIC */
/* ========================================================================= */
let currentLessonId = "mod1-les1";

function initCurriculum() {{
    const sidebar = document.getElementById("curriculumSidebar");
    let html = "";
    
    CURRICULUM_MODULES.forEach(mod => {{
        html += `<div class="module-group">
            <div class="module-header">${{mod.icon}} ${{mod.titleVi}}</div>`;
        if (mod.lessons && mod.lessons.length > 0) {{
            mod.lessons.forEach(les => {{
                const isDone = !!appState.completedLessons[les.id];
                const activeClass = les.id === currentLessonId ? "active" : "";
                html += `<div class="lesson-nav-item ${{activeClass}}" id="nav-les-${{les.id}}" onclick="selectLesson('${{les.id}}')">
                    <span>${{les.lessonNumber}}. ${{les.titleVi.substring(0, 32)}}...</span>
                    <span class="nav-status">${{isDone ? '🪷' : '⚪'}}</span>
                </div>`;
            }});
        }} else {{
            html += `<div style="font-size:12px; color:var(--text-sub); padding:4px 10px;">Chuyên đề thực hành & tra cứu</div>`;
        }}
        html += `</div>`;
    }});
    sidebar.innerHTML = html;
    renderLessonDetail(currentLessonId);
}}

function selectLesson(lessonId) {{
    currentLessonId = lessonId;
    document.querySelectorAll(".lesson-nav-item").forEach(item => item.classList.remove("active"));
    const navItem = document.getElementById("nav-les-" + lessonId);
    if (navItem) navItem.classList.add("active");
    renderLessonDetail(lessonId);
}}

function findLessonById(lessonId) {{
    for (const m of CURRICULUM_MODULES) {{
        for (const l of m.lessons) {{
            if (l.id === lessonId) return {{ lesson: l, module: m }};
        }}
    }}
    return null;
}}

function renderLessonDetail(lessonId) {{
    const panel = document.getElementById("lessonDetailPanel");
    const found = findLessonById(lessonId);
    if (!found) {{
        panel.innerHTML = `<p>Vui lòng chọn bài học từ danh mục bên trái.</p>`;
        return;
    }}
    const {{ lesson, module }} = found;
    const isDone = !!appState.completedLessons[lessonId];
    const savedNote = appState.notes[lessonId] || "";

    let html = `
        <div class="lesson-meta-bar">
            <span class="tag-pill module-tag">${{module.icon}} ${{module.titleVi}}</span>
            <span class="tag-pill time-tag">⏱️ ${{lesson.estimatedMinutes || 15}} phút</span>
            ${{isDone ? '<span class="tag-pill status-done">🪷 Đã Hoàn Thành</span>' : '<span class="tag-pill time-tag">⚪ Chưa Hoàn Thành</span>'}}
        </div>

        <h2 style="font-size: 22px; color: var(--primary); margin-bottom: 8px;">${{lesson.titleVi}}</h2>
        <p style="font-size: 14px; color: var(--text-sub); font-style: italic; margin-bottom: 20px;">${{lesson.titleEn}}</p>

        <!-- Objectives -->
        ${{lesson.objectivesVi && lesson.objectivesVi.length > 0 ? `
            <div class="lesson-section-box">
                <h4>🎯 Mục Tiêu Bài Học</h4>
                <ul style="padding-left: 20px; font-size: 13.5px; color: var(--text-main);">
                    ${{lesson.objectivesVi.map(obj => `<li style="margin-bottom: 4px;">${{obj}}</li>`).join('')}}
                </ul>
            </div>
        ` : ''}}

        <!-- Source & Translation -->
        <div class="lesson-section-box">
            <h4>📖 Trích Dẫn Chuẩn Mực ICF & Bản Dịch Tiếng Việt</h4>
            ${{lesson.sourceDocument ? `<div style="font-size:12px; color:var(--text-sub); margin-bottom:8px;"><b>Nguồn:</b> ${{lesson.sourceDocument}}</div>` : ''}}
            ${{lesson.originalExcerptEn ? `<div class="source-excerpt"><b>[English Original]:</b>\n${{lesson.originalExcerptEn}}</div>` : ''}}
            ${{lesson.translationVi ? `<div class="source-excerpt" style="border-left-color: var(--accent);"><b>[Bản Dịch Tiếng Việt Chuẩn Xác]:</b>\n${{lesson.translationVi}}</div>` : ''}}
        </div>

        <!-- 2019 vs 2025 comparison -->
        ${{lesson.comparison2019Vi ? `
            <div class="lesson-section-box">
                <h4>⚖️ Điểm Mới & So Sánh Chuẩn 2019 – 2025</h4>
                <p style="font-size: 13.5px; color: var(--text-main);">${{lesson.comparison2019Vi}}</p>
            </div>
        ` : ''}}

        <!-- Commentary -->
        ${{lesson.commentaryVi ? `
            <div class="lesson-section-box" style="background: var(--primary-light); border-color: var(--primary);">
                <h4 style="color: var(--primary-dark);">💬 Lời Bình Chuyên Môn Từ Coach Thanh Huyền</h4>
                <p style="font-size: 13.5px; color: var(--text-main); font-style: italic;">"${{lesson.commentaryVi}}"</p>
            </div>
        ` : ''}}

        <!-- Quiz Section -->
        ${{lesson.miniQuiz && lesson.miniQuiz.length > 0 ? `
            <div class="card" style="margin-top: 24px; border-color: var(--primary);">
                <h3 style="font-size: 16px; color: var(--primary); margin-bottom: 12px;">❓ Bài Kiểm Tra Nhanh Nhận Sen (Mini-Quiz)</h3>
                ${{renderLessonMiniQuiz(lesson)}}
            </div>
        ` : `
            <div style="margin-top: 24px; text-align: center;">
                ${{!isDone ? `
                    <button class="btn btn-primary" onclick="markLessonComplete('${{lessonId}}')">🌱 Đánh Dấu Đã Học Xong (+1 Đóa Sen)</button>
                ` : `
                    <div style="color: var(--success); font-weight: 600;">✨ Bạn đã hoàn thành bài học này và nhận được 1 đóa sen!</div>
                `}}
            </div>
        `}}

        <!-- Reflection Note -->
        <div class="card" style="margin-top: 20px;">
            <h4 style="font-size: 14px; color: var(--primary); margin-bottom: 8px;">✍️ Ghi Chú Chiêm Nghiệm Riêng (Tự động lưu vào máy)</h4>
            <textarea id="noteInput_${{lessonId}}" style="width:100%; min-height:80px; padding:10px; border-radius:8px; border:1px solid var(--border); background:var(--bg); color:var(--text-main); font-size:13px; font-family:inherit; outline:none;" placeholder="Ghi lại điều bạn tâm đắc nhất từ bài học này..." oninput="handleSaveNote('${{lessonId}}')">${{savedNote}}</textarea>
            <div style="font-size:11px; color:var(--text-sub); margin-top:4px;">Ghi chú được lưu an toàn 100% trong bộ nhớ trình duyệt của bạn.</div>
        </div>
    `;
    panel.innerHTML = html;
}}

function renderLessonMiniQuiz(lesson) {{
    let qHtml = "";
    lesson.miniQuiz.forEach((q, idx) => {{
        qHtml += `
            <div style="margin-bottom: 16px;">
                <div style="font-size: 13.5px; font-weight: 700; margin-bottom: 8px;">Câu ${{idx + 1}}: ${{q.questionVi}}</div>
                <div style="display:flex; flex-direction:column; gap:6px;">
                    ${{q.options.map(opt => `
                        <label class="quiz-option-label" id="lbl_lq_${{lesson.id}}_${{idx}}_${{opt.key}}">
                            <input type="radio" name="lq_${{lesson.id}}_${{idx}}" value="${{opt.key}}" onchange="handleLessonQuizSelect('${{lesson.id}}', ${{idx}}, '${{opt.key}}')">
                            <span><b>${{opt.key}}.</b> ${{opt.textVi}}</span>
                        </label>
                    `).join('')}}
                </div>
                <div class="quiz-feedback" id="lq_feedback_${{lesson.id}}_${{idx}}"></div>
            </div>
        `;
    }});
    qHtml += `
        <button class="btn btn-primary btn-sm" onclick="submitLessonQuiz('${{lesson.id}}')">Kiểm Tra Đáp Án</button>
    `;
    return qHtml;
}}

let lessonQuizAnswers = {{}};
function handleLessonQuizSelect(lessonId, qIdx, optKey) {{
    lessonQuizAnswers[`${{lessonId}}_${{qIdx}}`] = optKey;
}}

function submitLessonQuiz(lessonId) {{
    const found = findLessonById(lessonId);
    if (!found || !found.lesson.miniQuiz) return;
    const quizes = found.lesson.miniQuiz;
    let allCorrect = true;

    quizes.forEach((q, idx) => {{
        const userPick = lessonQuizAnswers[`${{lessonId}}_${{idx}}`];
        const fb = document.getElementById(`lq_feedback_${{lessonId}}_${{idx}}`);
        if (userPick === q.correctAnswer) {{
            fb.className = "quiz-feedback success show";
            fb.innerHTML = `<b>Chính xác!</b> ${{q.explanationVi || ''}}`;
        }} else {{
            allCorrect = false;
            fb.className = "quiz-feedback error show";
            fb.innerHTML = `<b>Chưa đúng!</b> Đáp án chuẩn: <b>${{q.correctAnswer}}</b>. ${{q.explanationVi || ''}}`;
        }}
    }});

    if (allCorrect && !appState.completedLessons[lessonId]) {{
        markLessonComplete(lessonId);
        alert("🎉 Chúc mừng bạn đã vượt qua bài trắc nghiệm và nhận 1 đóa sen chánh niệm 🪷!");
    }}
}}

function markLessonComplete(lessonId) {{
    if (!appState.completedLessons[lessonId]) {{
        appState.completedLessons[lessonId] = {{ status: "done", score: 100, at: new Date().toISOString() }};
        addLotus();
        renderLessonDetail(lessonId);
        // update nav icon
        const nav = document.getElementById("nav-les-" + lessonId);
        if (nav) nav.querySelector(".nav-status").innerText = "🪷";
    }}
}}

function handleSaveNote(lessonId) {{
    const val = document.getElementById("noteInput_" + lessonId).value;
    appState.notes[lessonId] = val;
    saveAppState();
}}

/* ========================================================================= */
/* TAB 2: SJT SCENARIOS LOGIC */
/* ========================================================================= */
let activeSjtFilter = "all";

function filterSjt(type) {{
    activeSjtFilter = type;
    document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
    const btn = Array.from(document.querySelectorAll(".filter-btn")).find(b => b.getAttribute("onclick").includes(type));
    if (btn) btn.classList.add("active");
    renderSjtScenarios();
}}

function renderSjtScenarios() {{
    const container = document.getElementById("sjtScenariosList");
    let list = [...SJT_QUESTIONS];

    if (activeSjtFilter === 'daily10') {{
        list = list.slice(0, 10);
    }} else if (activeSjtFilter !== 'all') {{
        list = list.filter(q => (q.primaryCompetency || "").toLowerCase().includes(activeSjtFilter.toLowerCase()));
    }}

    let html = "";
    list.forEach((q, idx) => {{
        const userAns = appState.sjtAnswers[q.id] || {{}};
        const isDone = userAns.best && userAns.worst;

        html += `
            <div class="scenario-card" id="sjt_card_${{q.id}}">
                <div class="scenario-header">
                    <span style="font-weight: 700; color: var(--primary); font-size: 14px;">Tình Huống #${{idx + 1}} (${{q.id}})</span>
                    <span class="scenario-competency">${{q.primaryCompetency || 'ICF Credentialing SJT'}}</span>
                </div>

                <div class="scenario-text-en">${{q.questionEn}}</div>
                <div class="scenario-text-vi"><b>Bản dịch:</b> ${{q.questionVi}}</div>

                ${{q.keyClueVi ? `<div style="font-size: 12px; color: var(--accent); margin-bottom: 14px; font-weight: 600;">🔑 Điểm then chốt: ${{q.keyClueVi}} (${{q.keyClueEn || ''}})</div>` : ''}}

                <div class="scenario-options-grid">
                    ${{q.options.map(opt => `
                        <div class="sjt-option-row" id="row_${{q.id}}_${{opt.key}}">
                            <div class="option-text-box">
                                <span class="option-key">${{opt.key}}.</span>
                                <span>${{opt.textEn}}</span>
                                <div style="font-size: 12.5px; color: var(--text-sub); margin-top: 2px;">${{opt.textVi}}</div>
                            </div>
                            <div class="option-pickers">
                                <button class="pick-btn pick-best ${{userAns.best === opt.key ? 'selected' : ''}}" onclick="handleSjtPick('${{q.id}}', '${{opt.key}}', 'best')">🌟 BEST</button>
                                <button class="pick-btn pick-worst ${{userAns.worst === opt.key ? 'selected' : ''}}" onclick="handleSjtPick('${{q.id}}', '${{opt.key}}', 'worst')">⚠️ WORST</button>
                            </div>
                        </div>
                    `).join('')}}
                </div>

                <div style="display: flex; gap: 10px; align-items: center;">
                    <button class="btn btn-primary btn-sm" onclick="checkSjtAnswer('${{q.id}}')">Kiểm Tra Đáp Án</button>
                    <button class="btn btn-outline btn-sm" onclick="resetSjtAnswer('${{q.id}}')">Làm Lại</button>
                </div>

                <div class="sjt-feedback-box ${{isDone ? 'show' : ''}}" id="sjt_fb_${{q.id}}">
                    <div class="feedback-item">
                        <span class="badge-best">🌟 BEST Action: ${{q.bestAnswer}}</span>
                    </div>
                    <div class="feedback-item">
                        <span class="badge-worst">⚠️ WORST Action: ${{q.worstAnswer}}</span>
                    </div>
                    <div class="feedback-item" style="color: var(--text-main); margin-top: 8px;">
                        <b>Giải thích chuyên môn:</b>\n${{q.explanationVi}}
                    </div>
                    ${{q.explanationEn ? `<div class="feedback-item" style="color: var(--text-sub); font-style: italic;"><b>ICF Rationale (EN):</b>\n${{q.explanationEn}}</div>` : ''}}
                </div>
            </div>
        `;
    }});
    container.innerHTML = html;
}}

function handleSjtPick(qId, key, type) {{
    if (!appState.sjtAnswers[qId]) appState.sjtAnswers[qId] = {{}};
    if (type === 'best') {{
        appState.sjtAnswers[qId].best = key;
        if (appState.sjtAnswers[qId].worst === key) delete appState.sjtAnswers[qId].worst;
    }} else {{
        appState.sjtAnswers[qId].worst = key;
        if (appState.sjtAnswers[qId].best === key) delete appState.sjtAnswers[qId].best;
    }}
    saveAppState();
    
    // Update button states
    const card = document.getElementById("sjt_card_" + qId);
    card.querySelectorAll(".pick-best").forEach(b => b.classList.remove("selected"));
    card.querySelectorAll(".pick-worst").forEach(b => b.classList.remove("selected"));
    
    if (appState.sjtAnswers[qId].best) {{
        const bBtn = card.querySelector(`#row_${{qId}}_${{appState.sjtAnswers[qId].best}} .pick-best`);
        if (bBtn) bBtn.classList.add("selected");
    }}
    if (appState.sjtAnswers[qId].worst) {{
        const wBtn = card.querySelector(`#row_${{qId}}_${{appState.sjtAnswers[qId].worst}} .pick-worst`);
        if (wBtn) wBtn.classList.add("selected");
    }}
}}

function checkSjtAnswer(qId) {{
    const q = SJT_QUESTIONS.find(x => x.id === qId);
    if (!q) return;
    const ans = appState.sjtAnswers[qId];
    if (!ans || !ans.best || !ans.worst) {{
        alert("Vui lòng chọn cả 1 phương án BEST và 1 phương án WORST trước khi kiểm tra!");
        return;
    }}
    const isCorrect = (ans.best === q.bestAnswer && ans.worst === q.worstAnswer);
    ans.isCorrect = isCorrect;
    if (isCorrect) {{
        addLotus();
    }}
    saveAppState();
    document.getElementById("sjt_fb_" + qId).classList.add("show");
}}

function resetSjtAnswer(qId) {{
    delete appState.sjtAnswers[qId];
    saveAppState();
    const card = document.getElementById("sjt_card_" + qId);
    card.querySelectorAll(".pick-best").forEach(b => b.classList.remove("selected"));
    card.querySelectorAll(".pick-worst").forEach(b => b.classList.remove("selected"));
    document.getElementById("sjt_fb_" + qId).classList.remove("show");
}}

/* ========================================================================= */
/* TAB 3: COMPETENCY MOCK EXAM SETS LOGIC */
/* ========================================================================= */
let currentCompGroupIdx = 0;
let currentCompSetIdx = 0;

function initCompetencyMock() {{
    const groupBar = document.getElementById("compGroupBar");
    groupBar.innerHTML = COMPETENCY_GROUPS.map((g, idx) => `
        <button class="comp-group-btn ${{idx === 0 ? 'active' : ''}}" onclick="selectCompGroup(${{idx}})">${{g.groupName}}</button>
    `).join('');
    selectCompGroup(0);
}}

function selectCompGroup(idx) {{
    currentCompGroupIdx = idx;
    document.querySelectorAll(".comp-group-btn").forEach((b, i) => {{
        if (i === idx) b.classList.add("active");
        else b.classList.remove("active");
    }});

    const group = COMPETENCY_GROUPS[idx];
    const pillsBar = document.getElementById("compSetPillsBar");
    pillsBar.innerHTML = group.sets.map((s, sIdx) => `
        <button class="set-pill-btn ${{sIdx === 0 ? 'active' : ''}}" onclick="selectCompSet(${{sIdx}})">SET ${{sIdx + 1}}</button>
    `).join('');
    selectCompSet(0);
}}

function selectCompSet(sIdx) {{
    currentCompSetIdx = sIdx;
    document.querySelectorAll(".set-pill-btn").forEach((b, i) => {{
        if (i === sIdx) b.classList.add("active");
        else b.classList.remove("active");
    }});
    renderCompQuestions();
}}

function renderCompQuestions() {{
    const container = document.getElementById("compQuestionsContainer");
    const scoreBox = document.getElementById("compScoreContainer");
    scoreBox.style.display = "none";

    const group = COMPETENCY_GROUPS[currentCompGroupIdx];
    const set = group.sets[currentCompSetIdx];
    if (!set) return;

    let html = `
        <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-light); padding-bottom: 12px;">
            <h2 style="font-size: 18px; color: var(--primary); margin-bottom: 4px;"># ${{set.title}}</h2>
            <div style="font-size: 13px; color: var(--text-sub);">Gồm ${{set.questions.length}} câu hỏi trắc nghiệm năng lực chuyên sâu.</div>
        </div>
    `;

    set.questions.forEach((q, qIdx) => {{
        const storedVal = appState.compAnswers[`${{currentCompGroupIdx}}_${{currentCompSetIdx}}_${{qIdx}}`];
        html += `
            <div class="quiz-question-block" id="comp_block_${{qIdx}}">
                <div class="quiz-q-title">Câu ${{qIdx + 1}}: ${{q.q}}</div>
                <div class="quiz-options-list">
                    ${{q.options.map((opt, optIdx) => `
                        <label class="quiz-option-label ${{storedVal === optIdx ? 'selected' : ''}}" id="comp_lbl_${{qIdx}}_${{optIdx}}">
                            <input type="radio" name="comp_q_${{qIdx}}" value="${{optIdx}}" ${{storedVal === optIdx ? 'checked' : ''}} onchange="handleCompSelect(${{qIdx}}, ${{optIdx}})">
                            <span>${{opt}}</span>
                        </label>
                    `).join('')}}
                </div>
                <div class="quiz-feedback" id="comp_fb_${{qIdx}}"></div>
            </div>
        `;
    }});

    container.innerHTML = html;
}}

function handleCompSelect(qIdx, optIdx) {{
    appState.compAnswers[`${{currentCompGroupIdx}}_${{currentCompSetIdx}}_${{qIdx}}`] = optIdx;
    saveAppState();
    for (let i = 0; i < 4; i++) {{
        const lbl = document.getElementById(`comp_lbl_${{qIdx}}_${{i}}`);
        if (lbl) lbl.classList.remove("selected");
    }}
    const curr = document.getElementById(`comp_lbl_${{qIdx}}_${{optIdx}}`);
    if (curr) curr.classList.add("selected");
}}

function gradeCurrentCompSet() {{
    const group = COMPETENCY_GROUPS[currentCompGroupIdx];
    const set = group.sets[currentCompSetIdx];
    let score = 0;
    const total = set.questions.length;
    const pts = 100 / total;

    set.questions.forEach((q, qIdx) => {{
        const sel = appState.compAnswers[`${{currentCompGroupIdx}}_${{currentCompSetIdx}}_${{qIdx}}`];
        const fb = document.getElementById(`comp_fb_${{qIdx}}`);
        for (let i = 0; i < 4; i++) {{
            const lbl = document.getElementById(`comp_lbl_${{qIdx}}_${{i}}`);
            if (lbl) lbl.classList.remove("is-correct", "is-wrong");
        }}

        const correctLbl = document.getElementById(`comp_lbl_${{qIdx}}_${{q.correct}}`);
        if (sel !== undefined) {{
            const selLbl = document.getElementById(`comp_lbl_${{qIdx}}_${{sel}}`);
            if (sel === q.correct) {{
                score += pts;
                if (selLbl) selLbl.classList.add("is-correct");
                fb.className = "quiz-feedback success show";
                fb.innerHTML = `<b>CHÍNH XÁC (+${{Math.round(pts)}}đ)!</b><br>${{q.explain || ''}}`;
            }} else {{
                if (selLbl) selLbl.classList.add("is-wrong");
                if (correctLbl) correctLbl.classList.add("is-correct");
                fb.className = "quiz-feedback error show";
                fb.innerHTML = `<b>CHƯA ĐÚNG!</b> Đáp án chuẩn: <b>${{q.options[q.correct].substring(0, 2)}}</b>.<br><i>Giải thích:</i> ${{q.explain || ''}}`;
            }}
        }} else {{
            if (correctLbl) correctLbl.classList.add("is-correct");
            fb.className = "quiz-feedback error show";
            fb.innerHTML = `<b>CHƯA TRẢ LỜI!</b> Đáp án chuẩn: <b>${{q.options[q.correct].substring(0, 2)}}</b>.<br><i>Giải thích:</i> ${{q.explain || ''}}`;
        }}
    }});

    const finalScore = Math.round(score);
    const scoreBox = document.getElementById("compScoreContainer");
    scoreBox.style.display = "block";
    scoreBox.innerHTML = `
        <h3 style="font-size: 20px; color: var(--primary); margin-bottom: 6px;">KẾT QUẢ: ${{finalScore}} / 100 ĐIỂM</h3>
        <p style="font-size: 14px; color: var(--text-sub);">${{finalScore >= 70 ? '🎉 Xuất sắc! Bạn đã thể hiện tư duy đạo đức và năng lực khai vấn vững vàng.' : '💡 Hãy đọc kỹ phần giải thích chi tiết dưới từng câu để hoàn thiện phản xạ.'}}</p>
    `;
    if (finalScore >= 70) {{
        addLotus();
    }}
    window.scrollTo({{ top: scoreBox.offsetTop - 80, behavior: 'smooth' }});
}}

function resetCurrentCompSet() {{
    const group = COMPETENCY_GROUPS[currentCompGroupIdx];
    const set = group.sets[currentCompSetIdx];
    set.questions.forEach((_, qIdx) => {{
        delete appState.compAnswers[`${{currentCompGroupIdx}}_${{currentCompSetIdx}}_${{qIdx}}`];
    }});
    saveAppState();
    renderCompQuestions();
}}

/* ========================================================================= */
/* TAB 4: GLOSSARY & FLASHCARDS LOGIC */
/* ========================================================================= */
let currentFlashcardIdx = 0;

function initGlossary() {{
    renderGlossaryGrid(GLOSSARY_TERMS);
    updateFlashcardUI();
}}

function renderGlossaryGrid(list) {{
    const grid = document.getElementById("glossaryGrid");
    grid.innerHTML = list.map(item => `
        <div class="glossary-card">
            <div class="term-en">${{item.termEn}}</div>
            <div class="term-vi">${{item.termVi}}</div>
            <div class="term-desc"><b>Định nghĩa:</b> ${{item.definitionVi}}</div>
            ${{item.relatedStandard ? `<div style="font-size: 11px; color: var(--accent); margin-top: 6px; font-weight: 600;">Liên quan: ${{item.relatedStandard}}</div>` : ''}}
        </div>
    `).join('');
}}

function handleGlossarySearch() {{
    const query = document.getElementById("glossarySearchInput").value.toLowerCase();
    const filtered = GLOSSARY_TERMS.filter(t => 
        (t.termEn || "").toLowerCase().includes(query) ||
        (t.termVi || "").toLowerCase().includes(query) ||
        (t.definitionVi || "").toLowerCase().includes(query)
    );
    renderGlossaryGrid(filtered);
}}

function toggleGlossaryView(mode) {{
    const grid = document.getElementById("glossaryGrid");
    const cards = document.getElementById("flashcardView");
    const btnList = document.getElementById("btnViewGlossaryList");
    const btnCards = document.getElementById("btnViewGlossaryCards");

    if (mode === 'list') {{
        grid.style.display = "grid";
        cards.style.display = "none";
        btnList.className = "btn btn-primary btn-sm";
        btnCards.className = "btn btn-outline btn-sm";
    }} else {{
        grid.style.display = "none";
        cards.style.display = "block";
        btnList.className = "btn btn-outline btn-sm";
        btnCards.className = "btn btn-primary btn-sm";
        updateFlashcardUI();
    }}
}}

function flipFlashcard() {{
    document.getElementById("flashcardInner").classList.toggle("flipped");
}}

function updateFlashcardUI() {{
    const item = GLOSSARY_TERMS[currentFlashcardIdx];
    if (!item) return;
    document.getElementById("flashcardInner").classList.remove("flipped");
    document.getElementById("fcTermEn").innerText = item.termEn;
    document.getElementById("fcCategory").innerText = item.category || "ICF Glossary";
    document.getElementById("fcTermVi").innerText = item.termVi;
    document.getElementById("fcDefVi").innerText = item.definitionVi;
    document.getElementById("fcCounter").innerText = `${{currentFlashcardIdx + 1}} / ${{GLOSSARY_TERMS.length}}`;
}}

function prevFlashcard() {{
    if (currentFlashcardIdx > 0) {{
        currentFlashcardIdx--;
        updateFlashcardUI();
    }}
}}

function nextFlashcard() {{
    if (currentFlashcardIdx < GLOSSARY_TERMS.length - 1) {{
        currentFlashcardIdx++;
        updateFlashcardUI();
    }}
}}

/* ========================================================================= */
/* TAB 5: MINDFUL TEA & BREATHING */
/* ========================================================================= */
let breathingTimer = null;
let breathingSeconds = 30;

function openBreathingModal() {{
    switchMainTab('tea');
    startBreathingCycle();
}}

function startBreathingCycle() {{
    if (breathingTimer) clearInterval(breathingTimer);
    breathingSeconds = 30;
    const circle = document.getElementById("breathingCircle");
    const text = document.getElementById("breathingText");
    const btn = document.getElementById("btnStartBreathing");
    btn.disabled = true;

    function runPhase(sec) {{
        const phase = sec % 16;
        if (phase < 4) {{
            circle.className = "breathing-circle inhale";
            text.innerText = `Hít vào chậm rãi (${{4 - phase}}s)...`;
        }} else if (phase < 8) {{
            text.innerText = `Giữ hơi tĩnh lặng (${{8 - phase}}s)...`;
        }} else if (phase < 12) {{
            circle.className = "breathing-circle exhale";
            text.innerText = `Thở ra nhẹ nhàng (${{12 - phase}}s)...`;
        }} else {{
            text.innerText = `Nghỉ ngơi trong chánh niệm (${{16 - phase}}s)...`;
        }}
    }}

    runPhase(0);
    breathingTimer = setInterval(() => {{
        breathingSeconds--;
        if (breathingSeconds <= 0) {{
            clearInterval(breathingTimer);
            circle.className = "breathing-circle";
            text.innerText = "Tâm trí đã an định. Chúc bạn một buổi học an vui! 🪷";
            btn.disabled = false;
            addLotus();
        }} else {{
            runPhase(30 - breathingSeconds);
        }}
    }}, 1000);
}}

function initTeaLessons() {{
    const grid = document.getElementById("teaLessonsGrid");
    grid.innerHTML = TEA_LESSONS.map(t => `
        <div class="glossary-card" style="border-left: 3px solid var(--accent);">
            <div style="font-size: 16px; font-weight: 700; color: var(--primary); margin-bottom: 4px;">🍵 ${{t.titleVi}}</div>
            <div style="font-size: 13px; color: var(--text-sub); font-style: italic; margin-bottom: 8px;">"${{t.quoteVi}}"</div>
            <div style="font-size: 13px; color: var(--text-main); margin-bottom: 8px;"><b>Chiêm nghiệm:</b> ${{t.promptVi}}</div>
            <button class="btn btn-outline btn-sm" onclick="selectLesson('${{t.lessonId}}'); switchMainTab('curriculum');">Đến Bài Học Tương Ứng ➡️</button>
        </div>
    `).join('');
}}

/* ========================================================================= */
/* TAB 6: JOURNAL & GARDEN */
/* ========================================================================= */
function renderGardenBlooms() {{
    const container = document.getElementById("gardenBloomsContainer");
    if (!container) return;
    const count = Math.min(appState.lotusCount, 50);
    let html = "";
    for (let i = 0; i < count; i++) {{
        html += `<span class="lotus-flower-icon" title="Đóa sen thứ ${{i + 1}}">🪷</span>`;
    }}
    if (count === 0) {{
        html = `<div style="font-size: 13px; color: var(--text-sub);">Chưa có đóa sen nào. Hãy hoàn thành bài học hoặc làm đề thi để gieo hạt mầm đầu tiên!</div>`;
    }}
    container.innerHTML = html;
}}

function renderJournalNotes() {{
    const container = document.getElementById("journalNotesContainer");
    const noteKeys = Object.keys(appState.notes).filter(k => (appState.notes[k] || "").trim() !== "");
    if (noteKeys.length === 0) {{
        container.innerHTML = `<div style="font-size: 13px; color: var(--text-sub); padding: 12px;">Bạn chưa ghi chú bài học nào. Khi học các bài ở Lộ Trình, hãy ghi lại suy ngẫm vào ô Ghi chú chiêm nghiệm!</div>`;
        return;
    }}
    container.innerHTML = noteKeys.map(k => {{
        const found = findLessonById(k);
        const title = found ? found.lesson.titleVi : k;
        return `
            <div class="note-card">
                <div class="note-title">📖 ${{title}}</div>
                <div class="note-content">${{appState.notes[k]}}</div>
            </div>
        `;
    }}).join('');
}}

function exportDataJson() {{
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(appState, null, 2));
    const a = document.createElement('a');
    a.setAttribute("href", dataStr);
    a.setAttribute("download", `Hoc_Coaching_Tien_Do_${{new Date().toISOString().substring(0,10)}}.json`);
    document.body.appendChild(a);
    a.click();
    a.remove();
}}

function importDataJson(event) {{
    const file = event.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = function(e) {{
        try {{
            const parsed = JSON.parse(e.target.result);
            appState = parsed;
            saveAppState();
            alert("Đã khôi phục tiến độ thành công!");
            location.reload();
        }} catch(err) {{
            alert("File không hợp lệ: " + err);
        }}
    }};
    reader.readAsText(file);
}}

function resetAllProgress() {{
    if (confirm("Bạn có chắc chắn muốn làm mới toàn bộ tiến độ học và hoa sen không? Thao tác này không thể hoàn tác.")) {{
        localStorage.removeItem(STORE_KEY_PROGRESS);
        localStorage.removeItem(STORE_KEY_NOTES);
        appState = {{ completedLessons: {{}}, sjtAnswers: {{}}, compAnswers: {{}}, notes: {{}}, lotusCount: 0 }};
        saveAppState();
        location.reload();
    }}
}}

// Initialize on Load
window.addEventListener("DOMContentLoaded", () => {{
    loadAppState();
    initCurriculum();
    renderSjtScenarios();
    initCompetencyMock();
    initGlossary();
    initTeaLessons();
    renderGardenBlooms();
}});
</script>

</body>
</html>
"""

out_paths = [
    os.path.join(BASE_DIR, 'public/Hoc_Coaching_Cam_Nang_Hoc_Tap_Toan_Dien.html'),
    os.path.join(BASE_DIR, 'public/index.html'),
    '/Users/admin/Downloads/Hoc_Coaching_Cam_Nang_Hoc_Tap_Toan_Dien.html',
    '/Users/admin/Downloads/index.html',
    '/Users/admin/Downloads/AI/Hoc_Coaching_Cam_Nang_Hoc_Tap_Toan_Dien.html',
    '/Users/admin/Downloads/Ôn thi PCC - Vì ước mơ 500 PCC tại Việt Nam _3/Hoc_Coaching_Cam_Nang_Hoc_Tap_Toan_Dien.html',
    '/Users/admin/Downloads/Ôn thi PCC - Vì ước mơ 500 PCC tại Việt Nam _3/index.html'
]

for p in out_paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html_template)
    print(f"Generated: {p} ({len(html_template)} bytes)")

print("BUILD COMPLETE! ALL TARGETS CREATED.")
