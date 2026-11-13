# -*- coding: utf-8 -*-
"""
Master Certified Coach (MCC - 25 Years Experience)
Full Word Document Builder for 55 ICF SJT Scenarios
"""

import os, sys, json
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

# Add scripts directory to path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from mcc_data_part1 import PART1_DATA
from mcc_data_part2 import PART2_DATA
from mcc_data_part3 import PART3_DATA
from mcc_data_part4 import PART4_DATA

ALL_MCC_DATA = {}
ALL_MCC_DATA.update(PART1_DATA)
ALL_MCC_DATA.update(PART2_DATA)
ALL_MCC_DATA.update(PART3_DATA)
ALL_MCC_DATA.update(PART4_DATA)

print(f"Total MCC analysis entries: {len(ALL_MCC_DATA)}")

# Load base questions
JSON_PATH = "/Users/admin/.gemini/antigravity/brain/077a58ad-e82f-4375-8053-a6d80ae15b5f/scratch/all_55_questions.json"
with open(JSON_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)

print(f"Total base questions: {len(questions)}")

# Create Document
doc = docx.Document()

# Page Margins: 1 inch (2.54 cm)
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    
    # Header
    header = section.header
    hp = header.paragraphs[0]
    hp.text = "HỌC COACHING — BÁO CÁO THẨM ĐỊNH CHUYÊN MÔN MCC (55 TÌNH HUỐNG THI ICF SJT)"
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if hp.runs:
        hp.runs[0].font.name = "Calibri"
        hp.runs[0].font.size = Pt(8.5)
        hp.runs[0].font.italic = True
        hp.runs[0].font.color.rgb = RGBColor(120, 130, 140)

    # Footer
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.text = "Coach Thanh Huyền & Hội đồng Chuyên môn MCC ICF — Cẩm nang thẩm định độc quyền cho học viên"
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if fp.runs:
        fp.runs[0].font.name = "Calibri"
        fp.runs[0].font.size = Pt(8.5)
        fp.runs[0].font.color.rgb = RGBColor(140, 150, 160)

# Colors
COLOR_PRIMARY = RGBColor(27, 58, 42)       # Deep Forest Green #1B3A2A
COLOR_ACCENT_RED = RGBColor(153, 27, 27)   # Deep Burgundy #991B1B
COLOR_SUCCESS = RGBColor(22, 101, 52)      # Deep Forest Green #166534
COLOR_TEXT_MAIN = RGBColor(31, 36, 33)     # Charcoal #1F2421
COLOR_TEXT_SUB = RGBColor(92, 104, 97)     # Muted #5C6861

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_cell_margins(cell, top=120, bottom=120, left=180, right=180):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_callout_border(cell, color_hex="991B1B", size="36"):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="{size}" w:space="0" w:color="{color_hex}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(tcBorders)

def set_table_borders(table, color_hex="E5E7EB"):
    tblPr = table._tbl.tblPr
    tblBorders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="{color_hex}"/>
            <w:left w:val="none"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="{color_hex}"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color_hex}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(tblBorders)

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(22)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(17)
    run.font.bold = True
    run.font.color.rgb = COLOR_PRIMARY
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(13.5)
    run.font.bold = True
    run.font.color.rgb = COLOR_PRIMARY
    return p

def add_heading_3(text, color=COLOR_ACCENT_RED):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(11.5)
    run.font.bold = True
    run.font.color.rgb = color
    return p

def add_body_p(text, bold_prefix="", italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(10.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_TEXT_MAIN
    if text:
        r_text = p.add_run(text)
        r_text.font.name = "Calibri"
        r_text.font.size = Pt(10.5)
        r_text.font.italic = italic
        r_text.font.color.rgb = COLOR_TEXT_MAIN
    return p

# =========================================================================
# COVER / TITLE BLOCK
# =========================================================================
p_meta = doc.add_paragraph()
p_meta.paragraph_format.space_before = Pt(12)
p_meta.paragraph_format.space_after = Pt(4)
r_meta = p_meta.add_run("BÁO CÁO THẨM ĐỊNH CHUYÊN MÔN CAO CẤP (MCC AUDIT REPORT)")
r_meta.font.name = "Calibri"
r_meta.font.size = Pt(11)
r_meta.font.bold = True
r_meta.font.color.rgb = COLOR_ACCENT_RED

p_title = doc.add_paragraph()
p_title.paragraph_format.space_before = Pt(4)
p_title.paragraph_format.space_after = Pt(8)
r_title = p_title.add_run("GIẢI MÃ TOÀN DIỆN ĐÁP ÁN BEST & PHÂN TÍCH CHUYÊN SÂU LÝ DO CHỌN WORST TRONG BỘ 55 TÌNH HUỐNG THI THỰC HÀNH PHÁN ĐOÁN (SJT)")
r_title.font.name = "Calibri"
r_title.font.size = Pt(22)
r_title.font.bold = True
r_title.font.color.rgb = COLOR_PRIMARY

p_sub = doc.add_paragraph()
p_sub.paragraph_format.space_after = Pt(16)
r_sub = p_sub.add_run("Khảo Thí Chuẩn Quốc Tế ICF Credentialing Exam (ACC / PCC / MCC) — Dưới Lăng Kính Master Certified Coach (25 Năm Kinh Nghiệm Quốc Tế)")
r_sub.font.name = "Calibri"
r_sub.font.size = Pt(12)
r_sub.font.italic = True
r_sub.font.color.rgb = COLOR_TEXT_SUB

# Metadata Table
meta_tbl = doc.add_table(rows=4, cols=2)
meta_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(meta_tbl, "D1D5DB")
meta_data = [
    ("Chuyên gia Thẩm định:", "Hội đồng Chuyên môn Cấp cao MCC (25 năm kinh nghiệm thực hành, giám sát và đào tạo ICF quốc tế)"),
    ("Đơn vị bảo trợ & phát hành:", "Học Coaching — Cẩm nang đào tạo và luyện thi ICF PCC | Coach Thanh Huyền"),
    ("Chuẩn khảo thí quy chiếu:", "Bộ Quy tắc Đạo đức ICF 2025 (ICF Code of Ethics) & 8 Năng lực Cốt lõi (ICF Core Competencies)"),
    ("Trọng tâm báo cáo:", "Phân tích đối kháng chi tiết: Tại sao WORST là lựa chọn tồi tệ nhất so với từng phương án còn lại")
]
for idx, (lbl, val) in enumerate(meta_data):
    c0 = meta_tbl.cell(idx, 0)
    c1 = meta_tbl.cell(idx, 1)
    set_cell_background(c0, "F3F4F6")
    set_cell_background(c1, "FFFFFF")
    set_cell_margins(c0, 80, 80, 120, 120)
    set_cell_margins(c1, 80, 80, 120, 120)
    p0 = c0.paragraphs[0]
    p0.paragraph_format.space_after = Pt(0)
    r0 = p0.add_run(lbl)
    r0.font.bold = True
    r0.font.size = Pt(9.5)
    r0.font.color.rgb = COLOR_PRIMARY
    p1 = c1.paragraphs[0]
    p1.paragraph_format.space_after = Pt(0)
    r1 = p1.add_run(val)
    r1.font.size = Pt(9.5)
    r1.font.color.rgb = COLOR_TEXT_MAIN

doc.add_paragraph().paragraph_format.space_after = Pt(16)

# =========================================================================
# SECTION 1: TRIẾT LÝ KHẢO THÍ ICF SJT
# =========================================================================
add_heading_1("PHẦN 1: LỜI TỰA & TRIẾT LÝ KHẢO THÍ SITUATIONAL JUDGMENT TEST (SJT) CỦA ICF")

add_heading_2("1.1 Sự chuyển dịch từ kiểm tra trí nhớ sang đo lường phản xạ phán đoán tình huống")
add_body_p(
    "Trong hơn hai thập kỷ qua, kỳ thi chứng chỉ của Liên đoàn Khai vấn Quốc tế (ICF) đã trải qua một cuộc cách mạng sâu sắc. "
    "Trước đây, bài thi đánh giá tri thức thường dừng lại ở các câu hỏi trắc nghiệm truyền thống (Multiple Choice) kiểm tra khả năng ghi nhớ điều khoản, "
    "định nghĩa và các bước quy trình. Tuy nhiên, một Master Coach thực thụ không hành nghề bằng trí nhớ máy móc, mà hành nghề bằng "
    "SỰ HIỆN DIỆN VÀ NĂNG LỰC PHÁN ĐOÁN TÌNH HUỐNG (Situational Judgment). Đó là lý do ICF phối hợp với tập đoàn khảo thí Pearson VUE "
    "chuyển đổi toàn diện sang dạng thức Situational Judgment Test (SJT)."
)
add_body_p(
    "Trong mỗi kịch bản SJT, thí sinh không chỉ tìm một đáp án 'đúng', mà phải đối mặt với một tình huống thực tế đầy giằng xé, "
    "nơi cả 4 phương án hành động đều có vẻ hợp lý hoặc chứa đựng những cạm bẫy tâm lý tinh vi. Thí sinh bắt buộc phải xác định: "
    "Hành động nào là TỐT NHẤT (BEST) và Hành động nào là TỆ NHẤT (WORST)."
)

add_heading_2("1.2 Triết lý điểm số kép (Dual Scoring) & Tầm quan trọng sinh tử của việc chọn WORST")
add_body_p(
    "Rất nhiều học viên ôn thi ACC và PCC thường chỉ tập trung tìm phương án BEST và xem nhẹ phương án WORST, cho rằng 'chỉ cần tránh cái sai là được'. "
    "Đây là sai lầm chết người dẫn đến trượt kỳ thi Pearson VUE! Trong thang điểm của ICF, việc chọn sai đáp án WORST cũng làm mất điểm tương đương với việc chọn sai đáp án BEST."
)
add_body_p(
    "Tại sao ICF lại coi trọng lựa chọn WORST đến vậy? Dưới lăng kính của một MCC với 25 năm kinh nghiệm, tôi khẳng định rằng: "
    "Phương án BEST chứng minh NĂNG LỰC ĐỒNG HÀNH của bạn, nhưng phương án WORST chứng minh RANH GIỚI AN TOÀN VÀ ĐẠO ĐỨC của bạn. "
    "Một người Coach có thể chưa xuất sắc trong việc đặt câu hỏi (chưa đạt BEST), nhưng nếu người đó không biết đâu là lằn ranh đỏ mà phạm vào hành vi WORST "
    "(như vi phạm bảo mật, tự ý chẩn đoán tâm thần, tước đoạt quyền tự quyết của khách hàng, hay xúi giục sa thải/kiện tụng), người đó sẽ TRỰC TIẾP GÂY TỔN HẠI NGUY HIỂM cho khách hàng và tổ chức!"
)

add_heading_2("1.3 Khung phân tầng 4 cấp độ hành vi: Cách phân biệt giữa 'Suboptimal' và 'WORST'")
add_body_p(
    "Để giải quyết triệt để sự bối rối của học viên: 'Tại sao phương án kia cũng dở mà không phải là WORST?', chúng tôi đúc kết Khung Phân Tầng 4 Cấp Độ Hành Vi trong bài thi ICF SJT:"
)

tbl_tier = doc.add_table(rows=5, cols=3)
tbl_tier.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(tbl_tier, "D1D5DB")
tier_headers = ["Cấp độ", "Đặc điểm hành vi của Coach", "Phân loại trong đề thi SJT"]
for i, h in enumerate(tier_headers):
    c = tbl_tier.cell(0, i)
    set_cell_background(c, "1B3A2A")
    set_cell_margins(c, 80, 80, 100, 100)
    p = c.paragraphs[0]
    r = p.add_run(h)
    r.font.bold = True
    r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor(255, 255, 255)

tiers_data = [
    ("Cấp 1: Chuẩn mực tối ưu", "Hợp tác bình đẳng (Partnering), lắng nghe đa tầng (WHO), khơi gợi tự nhận thức, bảo vệ quyền tự quyết của khách hàng và tuân thủ đạo đức tuyệt đối.", "LỰA CHỌN TỐT NHẤT (BEST ACTION)"),
    ("Cấp 2: Tốt nhưng chưa sâu", "Hành động đúng hướng nhưng mang tính thủ tục hành chính, giải quyết vấn đề cơ học bề mặt (WHAT) hoặc chuyển bước hơi vội vã.", "Phương án Trung Gian Khá (Distractor 1)"),
    ("Cấp 3: Vụng về / Thụ động", "Coach lúng túng, im lặng né tránh xung đột, bị cuốn vào chuyện kể lể, hoặc đưa ra lời khuyên kỹ thuật nhỏ chưa phù hợp. TUY NHIÊN, KHÔNG VI PHẠM ĐẠO ĐỨC VÀ KHÔNG GÂY HẠI NGHIÊM TRỌNG.", "Phương án Chưa Tối Ưu (Distractor 2 - Dở nhưng chưa tệ nhất)"),
    ("Cấp 4: Độc hại / Vi phạm nghiêm trọng", "Trực tiếp vi phạm Bộ Quy tắc Đạo đức (lộ bảo mật, xung đột lợi ích, lừa dối chứng chỉ, không cứu nguy tự tử), tước đoạt quyền tự quyết (ra lệnh, quyết định hộ), phán xét nhục mạ, dán nhãn chẩn đoán tâm thần trái phép.", "LỰA CHỌN TỆ NHẤT (WORST ACTION)")
]

for idx, (t_name, t_desc, t_role) in enumerate(tiers_data, start=1):
    c0 = tbl_tier.cell(idx, 0)
    c1 = tbl_tier.cell(idx, 1)
    c2 = tbl_tier.cell(idx, 2)
    bg = "FEF2F2" if idx == 4 else ("F0FDF4" if idx == 1 else "FFFFFF")
    for cell in (c0, c1, c2):
        set_cell_background(cell, bg)
        set_cell_margins(cell, 70, 70, 90, 90)
    p0 = c0.paragraphs[0]; r0 = p0.add_run(t_name); r0.font.bold = True; r0.font.size = Pt(9)
    p1 = c1.paragraphs[0]; r1 = p1.add_run(t_desc); r1.font.size = Pt(9)
    p2 = c2.paragraphs[0]; r2 = p2.add_run(t_role); r2.font.bold = True; r2.font.size = Pt(9)
    if idx == 4:
        r2.font.color.rgb = COLOR_ACCENT_RED
    elif idx == 1:
        r2.font.color.rgb = COLOR_SUCCESS

doc.add_paragraph().paragraph_format.space_after = Pt(14)

# =========================================================================
# SECTION 2: BẢNG MA TRẬN 55 CÂU
# =========================================================================
add_heading_1("PHẦN 2: BẢNG MA TRẬN ĐỐI CHIẾU NHANH 55 TÌNH HUỐNG THI SJT")
add_body_p("Dưới đây là bảng tổng hợp nhanh đáp án BEST và WORST của trọn bộ 55 tình huống, cùng năng lực trọng tâm và từ khóa nhận diện sai phạm:")

tbl_matrix = doc.add_table(rows=len(questions)+1, cols=5)
tbl_matrix.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(tbl_matrix, "D1D5DB")
m_headers = ["Mã câu", "Năng lực / Tiêu chuẩn ICF", "BEST", "WORST", "Điểm chốt then chốt (Key Clue)"]
for i, h in enumerate(m_headers):
    c = tbl_matrix.cell(0, i)
    set_cell_background(c, "1B3A2A")
    set_cell_margins(c, 70, 70, 90, 90)
    p = c.paragraphs[0]
    r = p.add_run(h)
    r.font.bold = True
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(255, 255, 255)

for idx, q in enumerate(questions, start=1):
    q_id = q["id"]
    comp = q.get("primaryCompetency", "").split("/")[0].strip()
    best = q.get("bestAnswer", "")
    worst = q.get("worstAnswer", "")
    clue = q.get("keyClueVi", "") or q.get("explanationVi", "")[:35] + "..."
    
    c0 = tbl_matrix.cell(idx, 0)
    c1 = tbl_matrix.cell(idx, 1)
    c2 = tbl_matrix.cell(idx, 2)
    c3 = tbl_matrix.cell(idx, 3)
    c4 = tbl_matrix.cell(idx, 4)
    
    bg = "F9FAFB" if idx % 2 == 1 else "FFFFFF"
    for cell in (c0, c1, c2, c3, c4):
        set_cell_background(cell, bg)
        set_cell_margins(cell, 50, 50, 70, 70)
        
    p0 = c0.paragraphs[0]; r0 = p0.add_run(q_id); r0.font.bold = True; r0.font.size = Pt(8.5)
    p1 = c1.paragraphs[0]; r1 = p1.add_run(comp); r1.font.size = Pt(8.5)
    p2 = c2.paragraphs[0]; r2 = p2.add_run(best); r2.font.bold = True; r2.font.size = Pt(8.5); r2.font.color.rgb = COLOR_SUCCESS
    p3 = c3.paragraphs[0]; r3 = p3.add_run(worst); r3.font.bold = True; r3.font.size = Pt(8.5); r3.font.color.rgb = COLOR_ACCENT_RED
    p4 = c4.paragraphs[0]; r4 = p4.add_run(clue); r4.font.size = Pt(8.5)

doc.add_paragraph().paragraph_format.space_after = Pt(16)

# =========================================================================
# SECTION 3: THẨM ĐỊNH CHI TIẾT TỪNG CÂU
# =========================================================================
add_heading_1("PHẦN 3: THẨM ĐỊNH & GIẢI PHÃU CHUYÊN SÂU TOÀN BỘ 55 TÌNH HUỐNG THỰC HÀNH PHÁN ĐOÁN")
add_body_p(
    "Dưới đây là phần phân tích chi tiết từng kịch bản. Ở mỗi tình huống, chúng tôi phân tích tường minh: "
    "Lý do vì sao phương án BEST được chọn, và ĐẶC BIỆT LÀ MỔ XẺ CHI TIẾT LỰA CHỌN WORST: "
    "chỉ rõ tại sao phương án đó là tồi tệ nhất, đồng thời đối chiếu so sánh cụ thể với từng phương án còn lại "
    "để giải thích cặn kẽ vì sao các phương án kia dù chưa hoàn hảo nhưng vẫn nhẹ tội hơn phương án WORST."
)

for q in questions:
    q_id = q["id"]
    mcc_info = ALL_MCC_DATA.get(q_id, {})
    
    add_heading_2(f"TÌNH HUỐNG [{q_id}]: {mcc_info.get('competency_focus', q.get('primaryCompetency', ''))}")
    
    # Box Scenario
    scen_tbl = doc.add_table(rows=1, cols=1)
    scen_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_scen = scen_tbl.cell(0, 0)
    set_cell_background(c_scen, "F4F6F5")
    set_cell_margins(c_scen, 100, 100, 140, 140)
    set_callout_border(c_scen, "2D5A43", "24")
    
    p_scen_vi = c_scen.paragraphs[0]
    p_scen_vi.paragraph_format.space_after = Pt(4)
    r_vi_lbl = p_scen_vi.add_run("Bối cảnh tình huống (Tiếng Việt):\n")
    r_vi_lbl.font.bold = True
    r_vi_lbl.font.size = Pt(10)
    r_vi_lbl.font.color.rgb = COLOR_PRIMARY
    r_vi_txt = p_scen_vi.add_run(q["questionVi"])
    r_vi_txt.font.size = Pt(10)
    
    if q.get("questionEn"):
        p_scen_en = c_scen.add_paragraph()
        p_scen_en.paragraph_format.space_after = Pt(2)
        r_en_lbl = p_scen_en.add_run("English Scenario: ")
        r_en_lbl.font.bold = True
        r_en_lbl.font.size = Pt(9.5)
        r_en_lbl.font.color.rgb = COLOR_TEXT_SUB
        r_en_txt = p_scen_en.add_run(q["questionEn"])
        r_en_txt.font.size = Pt(9.5)
        r_en_txt.font.italic = True
        r_en_txt.font.color.rgb = COLOR_TEXT_SUB
        
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    
    # Table Options
    opt_tbl = doc.add_table(rows=5, cols=3)
    opt_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(opt_tbl, "E5E7EB")
    
    # Header row
    for i, h in enumerate(["Phương án", "Nội dung hành động lựa chọn", "Đánh giá sơ bộ"]):
        c = opt_tbl.cell(0, i)
        set_cell_background(c, "EAF3ED")
        set_cell_margins(c, 60, 60, 80, 80)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = COLOR_PRIMARY
        
    for o_idx, opt in enumerate(q["options"], start=1):
        key = opt["key"]
        text_vi = opt["textVi"]
        
        c_k = opt_tbl.cell(o_idx, 0)
        c_t = opt_tbl.cell(o_idx, 1)
        c_r = opt_tbl.cell(o_idx, 2)
        
        status_txt = "Phương án trung gian"
        bg_col = "FFFFFF"
        if key == q["bestAnswer"]:
            status_txt = "🌟 LỰA CHỌN TỐT NHẤT (BEST)"
            bg_col = "F0FDF4"
        elif key == q["worstAnswer"]:
            status_txt = "⚠️ LỰA CHỌN TỆ NHẤT (WORST)"
            bg_col = "FEF2F2"
            
        for cell in (c_k, c_t, c_r):
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, 60, 60, 80, 80)
            
        p_k = c_k.paragraphs[0]; r_k = p_k.add_run(f"[{key}]"); r_k.font.bold = True; r_k.font.size = Pt(9.5)
        p_t = c_t.paragraphs[0]; r_t = p_t.add_run(text_vi); r_t.font.size = Pt(9.5)
        p_r = c_r.paragraphs[0]; r_r = p_r.add_run(status_txt); r_r.font.bold = True; r_r.font.size = Pt(9)
        if key == q["bestAnswer"]:
            r_r.font.color.rgb = COLOR_SUCCESS
        elif key == q["worstAnswer"]:
            r_r.font.color.rgb = COLOR_ACCENT_RED
            
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    
    # Callout BEST
    best_tbl = doc.add_table(rows=1, cols=1)
    best_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_best = best_tbl.cell(0, 0)
    set_cell_background(c_best, "F0FDF4")
    set_cell_margins(c_best, 90, 90, 130, 130)
    set_callout_border(c_best, "166534", "30")
    
    p_b = c_best.paragraphs[0]
    p_b.paragraph_format.space_after = Pt(2)
    r_b_h = p_b.add_run(f"🌟 TẠI SAO PHƯƠNG ÁN [{q['bestAnswer']}] LÀ LỰA CHỌN TỐT NHẤT (BEST ACTION)?\n")
    r_b_h.font.bold = True
    r_b_h.font.size = Pt(10.5)
    r_b_h.font.color.rgb = COLOR_SUCCESS
    r_b_t = p_b.add_run(mcc_info.get("best_analysis", q.get("explanationVi", "")))
    r_b_t.font.size = Pt(10)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    
    # Callout WORST (Deep Comparative Analysis)
    worst_tbl = doc.add_table(rows=1, cols=1)
    worst_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_worst = worst_tbl.cell(0, 0)
    set_cell_background(c_worst, "FEF2F2")
    set_cell_margins(c_worst, 100, 100, 140, 140)
    set_callout_border(c_worst, "991B1B", "36")
    
    p_w = c_worst.paragraphs[0]
    p_w.paragraph_format.space_after = Pt(4)
    r_w_h = p_w.add_run(f"⚠️ TẠI SAO PHƯƠNG ÁN [{q['worstAnswer']}] LÀ LỰA CHỌN TỆ NHẤT (WORST ACTION)?\n")
    r_w_h.font.bold = True
    r_w_h.font.size = Pt(11)
    r_w_h.font.color.rgb = COLOR_ACCENT_RED
    
    # 1. Root Cause
    p_w_rc = c_worst.add_paragraph()
    p_w_rc.paragraph_format.space_after = Pt(4)
    r_rc_lbl = p_w_rc.add_run("1. Bản chất sai phạm nghiêm trọng nhất: ")
    r_rc_lbl.font.bold = True
    r_rc_lbl.font.size = Pt(10)
    r_rc_lbl.font.color.rgb = COLOR_ACCENT_RED
    r_rc_txt = p_w_rc.add_run(mcc_info.get("worst_cause", ""))
    r_rc_txt.font.size = Pt(10)
    
    # 2. Contrast with BEST
    p_w_cb = c_worst.add_paragraph()
    p_w_cb.paragraph_format.space_after = Pt(4)
    r_cb_lbl = p_w_cb.add_run("2. Đối kháng trực diện với BEST: ")
    r_cb_lbl.font.bold = True
    r_cb_lbl.font.size = Pt(10)
    r_cb_lbl.font.color.rgb = COLOR_TEXT_MAIN
    r_cb_txt = p_w_cb.add_run(mcc_info.get("worst_vs_best", ""))
    r_cb_txt.font.size = Pt(10)
    
    # 3. Comparative breakdown against remaining options
    p_w_comp = c_worst.add_paragraph()
    p_w_comp.paragraph_format.space_after = Pt(3)
    r_comp_lbl = p_w_comp.add_run("3. So sánh đối chiếu chi tiết với các lựa chọn còn lại:\n")
    r_comp_lbl.font.bold = True
    r_comp_lbl.font.size = Pt(10)
    r_comp_lbl.font.color.rgb = COLOR_TEXT_MAIN
    
    others_list = mcc_info.get("worst_vs_others", [])
    for opt_title, opt_reason in others_list:
        p_opt = c_worst.add_paragraph()
        p_opt.paragraph_format.space_after = Pt(3)
        p_opt.paragraph_format.left_indent = Inches(0.2)
        r_opt_t = p_opt.add_run(f"• So với {opt_title}: ")
        r_opt_t.font.bold = True
        r_opt_t.font.size = Pt(9.5)
        r_opt_t.font.color.rgb = COLOR_TEXT_MAIN
        r_opt_r = p_opt.add_run(opt_reason)
        r_opt_r.font.size = Pt(9.5)
        
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    
    # Master Takeaway Box
    take_tbl = doc.add_table(rows=1, cols=1)
    take_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_take = take_tbl.cell(0, 0)
    set_cell_background(c_take, "FFFBEB")
    set_cell_margins(c_take, 80, 80, 120, 120)
    set_callout_border(c_take, "D97706", "24")
    
    p_t = c_take.paragraphs[0]
    p_t.paragraph_format.space_after = Pt(0)
    r_t_lbl = p_t.add_run("💡 MASTER KEY TAKEAWAY (LỜI KHUYÊN TỪ MCC 25 NĂM KINH NGHIỆM):\n")
    r_t_lbl.font.bold = True
    r_t_lbl.font.size = Pt(9.5)
    r_t_lbl.font.color.rgb = RGBColor(180, 83, 9)
    r_t_txt = p_t.add_run(mcc_info.get("master_takeaway", ""))
    r_t_txt.font.size = Pt(9.5)
    r_t_txt.font.italic = True
    
    # Separator
    doc.add_paragraph().paragraph_format.space_after = Pt(16)

# =========================================================================
# SECTION 4: 7 BẪY TÂM LÝ KHI CHỌN WORST
# =========================================================================
add_heading_1("PHẦN 4: 7 CÁI BẪY TÂM LÝ KHIẾN THÍ SINH CHỌN NHẦM WORST & CẨM NANG PHÒNG THI PEARSON VUE")

traps = [
    ("Bẫy 1: Nhầm lẫn giữa 'Hành động thụ động/vụng về' và 'Hành động vi phạm đạo đức/tước đoạt tự quyết'",
     "Thí sinh thường có xu hướng ghét những phương án nghe có vẻ lười biếng hoặc vụng về (ví dụ: ngồi im nghe tiếp 30 phút, hoặc quên không kiểm tra rủi ro). "
     "Tuy nhiên, sự thụ động/vụng về này chỉ dừng ở Cấp độ 3 (Suboptimal). WORST bắt buộc phải là hành động Cấp độ 4: chủ động gây hại, ngắt lời thô bạo, chửi mắng 'hèn nhát', hoặc đưa ra lời khuyên sa thải/kiện tụng!"),
    ("Bẫy 2: Bị đánh lừa bởi ngôn từ lịch sự của các phương án áp đặt giải pháp",
     "Một phương án có thể dùng từ ngữ rất ngọt ngào, hòa nhã nhưng bản chất là KÊ ĐƠN GIẢI PHÁP HỘ (ví dụ: 'Nhẹ nhàng bảo khách hàng chặn 2 giờ trên lịch mỗi ngày', hoặc 'Chọn hộ công ty sáng tạo cho khách hàng'). "
     "Dù lời nói lịch sự, hành vi tước đoạt quyền tự quyết của khách hàng chính là WORST."),
    ("Bẫy 3: Cố chấp giữ thỏa thuận ban đầu khi sự thật cốt lõi mới đã xuất hiện",
     "Rất nhiều thí sinh nghĩ rằng 'tuân thủ hợp đồng là tốt nhất' nên chọn phương án bắt khách hàng quay lại chủ đề ban đầu (ví dụ: ép quay lại chủ đề ủy quyền khi khách hàng đã nhận ra vấn đề là thiếu niềm tin). "
     "Trong khai vấn, con người (WHO) quan trọng hơn hợp đồng trên giấy (WHAT). Ép khách hàng học bài cũ khi nhận thức mới đã hé nở là một hành vi WORST!"),
    ("Bẫy 4: Thần thánh hóa nguyên tắc bảo mật trong tình huống đe dọa tính mạng (Imminent Harm)",
     "Nhiều thí sinh học vẹt điều khoản bảo mật và nghĩ rằng 'không bao giờ được nói với ai trong mọi hoàn cảnh'. "
     "Khi khách hàng có dấu hiệu tự tử rõ ràng (như đã chuẩn bị thuốc ngủ), việc giữ im lặng bảo mật là LỖI NGUY HIỂM CHẾT NGƯỜI (WORST tuyệt đối). Hãy nhớ: Tính mạng con người luôn đứng trên bảo mật!"),
    ("Bẫy 5: Nhầm lẫn giữa 'Coach có chuyên môn' và 'Coach đưa ra lời khuyên trực tiếp'",
     "Khi khách hàng hỏi 'Nếu là chị, chị đòi lương bao nhiêu?', việc Coach đưa luôn con số cụ thể là WORST. "
     "ICF cho phép Coach chia sẻ kiến thức chuyên môn, NHƯNG phải làm rõ việc chuyển vai trò, phải xin phép và tuyệt đối không bao giờ áp đặt con số cụ thể thay cho khách hàng."),
    ("Bẫy 6: Sa đà vào việc chữa cháy sự cố (WHAT) thay vì đồng hành với con người (WHO)",
     "Khi khách hàng gặp thất bại dự án lớn và khóc nức nở, việc vội vàng nhảy vào lập kế hoạch hành động sửa chữa (Action Plan) để 'đỡ buồn' là một phản ứng non nớt. "
     "Hãy dung chứa không gian để khách hàng chuyển hóa cảm xúc và nhận thức bài học trước khi bàn về hành động!"),
    ("Bẫy 7: Bỏ quên thỏa thuận ba bên khi Doanh nghiệp (Sponsor) trả tiền",
     "Sponsor trả tiền thường gây sức ép muốn biết nội dung phiên coach hoặc muốn ép mục tiêu doanh số. "
     "Hai hành vi WORST phổ biến nhất là: (1) Tuồn ghi chép phiên coach cho HR, và (2) Làm báo cáo giả mạo để lừa dối HR. Con đường duy nhất của Coach chuẩn mực là ĐỐI THOẠI 3 BÊN MINH BẠCH!")
]

for idx, (t_title, t_desc) in enumerate(traps, start=1):
    add_heading_2(f"4.{idx} {t_title}")
    add_body_p(t_desc)

# =========================================================================
# SECTION 5: LỜI KẾT
# =========================================================================
add_heading_1("PHẦN 5: LỜI KẾT & CHÚC PHÚC TỪ COACH THANH HUYỀN & HỘI ĐỒNG CHUYÊN MÔN MCC")
add_body_p(
    "Hành trình trở thành một Professional Certified Coach (PCC) hay Master Certified Coach (MCC) không phải là hành trình tích lũy "
    "những mẹo làm bài thi đối phó, mà là một cuộc chuyển hóa sâu sắc về TÂM THẾ VÀ PHẨM CHẤT LÀM NGHỀ. "
    "Kỳ thi ICF Credentialing Exam dạng thức SJT tại Pearson VUE là một cột mốc tuyệt đẹp để bạn chứng minh với thế giới rằng: "
    "Bạn là một người Coach an toàn, liêm chính, sâu sắc và luôn tôn vinh sự vĩ đại bên trong mỗi khách hàng."
)
add_body_p(
    "55 tình huống trong cẩm nang này được Hội đồng Chuyên môn MCC đúc kết từ hàng ngàn giờ khai vấn và khảo thí thực tế. "
    "Hy vọng rằng bản thẩm định chuyên môn chi tiết này sẽ trao cho bạn chiếc la bàn tư duy vững chắc, giúp bạn tự tin bước vào phòng thi "
    "và xuất sắc chinh phục tấm bằng chứng chỉ danh giá của ICF!"
)

p_sign = doc.add_paragraph()
p_sign.paragraph_format.space_before = Pt(20)
r_sign1 = p_sign.add_run("Trân trọng & Chúc bạn chạm tới ước mơ 500 PCC tại Việt Nam,\n")
r_sign1.font.bold = True
r_sign1.font.size = Pt(11)
r_sign1.font.color.rgb = COLOR_PRIMARY
r_sign2 = p_sign.add_run("Coach Thanh Huyền & Hội đồng Cố vấn Chuyên môn Cấp cao MCC (25 Năm Kinh Nghiệm ICF)\n")
r_sign2.font.bold = True
r_sign2.font.size = Pt(11.5)
r_sign2.font.color.rgb = COLOR_ACCENT_RED
r_sign3 = p_sign.add_run("Hệ Thống Đào Tạo & Luyện Thi 'Học Coaching'")
r_sign3.font.italic = True
r_sign3.font.size = Pt(10)
r_sign3.font.color.rgb = COLOR_TEXT_SUB

# =========================================================================
# SAVE TO TARGET PATHS
# =========================================================================
OUT_PATH_1 = "/Users/admin/Downloads/Tham_Dinh_Chuyen_Mon_MCC_55_Tinh_Huong_SJT_ICF.docx"
OUT_PATH_2 = "/Users/admin/Downloads/Ôn thi PCC - Vì ước mơ 500 PCC tại Việt Nam _3/Tham_Dinh_Chuyen_Mon_MCC_55_Tinh_Huong_SJT_ICF.docx"

doc.save(OUT_PATH_1)
print(f"Generated: {OUT_PATH_1} ({os.path.getsize(OUT_PATH_1)} bytes)")

doc.save(OUT_PATH_2)
print(f"Generated: {OUT_PATH_2} ({os.path.getsize(OUT_PATH_2)} bytes)")

print("BUILD COMPLETE! MASTER WORD DOCUMENT SUCCESSFULLY GENERATED.")
