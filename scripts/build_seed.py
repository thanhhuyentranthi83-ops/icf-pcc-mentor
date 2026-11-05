import json
import os

RAW_PATH = 'raw_data.json'
OUT_PATH = 'src/lib/parsedData.json'

with open(RAW_PATH, 'r', encoding='utf-8') as f:
    raw = json.load(f)

def split_bi(text):
    if not text:
        return '', ''
    text = text.strip()
    if '\nVI: ' in text:
        p = text.split('\nVI: ', 1)
        return p[0].strip(), p[1].strip()
    if '\nVI:' in text:
        p = text.split('\nVI:', 1)
        return p[0].strip(), p[1].strip()
    if ' // VI: ' in text:
        p = text.split(' // VI: ', 1)
        return p[0].strip(), p[1].strip()
    return text, text

# 1. Parse Glossary
glossary_rows = raw.get('07_Glossary', [])
glossary = []
for r in glossary_rows[3:]:
    term_en, term_vi = split_bi(r.get('A', ''))
    def_en, def_vi = split_bi(r.get('B', ''))
    cue_en, cue_vi = split_bi(r.get('C', ''))
    if term_en and def_en:
        glossary.append({
            'termEn': term_en,
            'termVi': term_vi,
            'definitionEn': def_en,
            'definitionVi': def_vi,
            'cueEn': cue_en,
            'cueVi': cue_vi
        })

# 2. Parse Exam Map & Competencies
comp_rows = raw.get('01_Exam_Map', [])
competencies = []
for r in comp_rows[3:]:
    domain_en, domain_vi = split_bi(r.get('B', ''))
    no = r.get('C', '')
    comp_en, comp_vi = split_bi(r.get('D', ''))
    lens_en, lens_vi = split_bi(r.get('E', ''))
    cue_en, cue_vi = split_bi(r.get('F', ''))
    trap_en, trap_vi = split_bi(r.get('G', ''))
    if no:
        competencies.append({
            'domainEn': domain_en,
            'domainVi': domain_vi,
            'number': no,
            'compEn': comp_en,
            'compVi': comp_vi,
            'lensEn': lens_en,
            'lensVi': lens_vi,
            'cueEn': cue_en,
            'cueVi': cue_vi,
            'trapEn': trap_en,
            'trapVi': trap_vi
        })

# 3. Parse Practice Questions & Answer Key
ak_rows = raw.get('06_Answer_Key', [])
answers = {}
for r in ak_rows[3:]:
    qid = r.get('A', '')
    if qid.startswith('Q'):
        best = r.get('B', '')
        worst = r.get('C', '')
        rat_en, rat_vi = split_bi(r.get('D', ''))
        comp_en, comp_vi = split_bi(r.get('E', ''))
        clue_en, clue_vi = split_bi(r.get('F', ''))
        answers[qid] = {
            'best': best,
            'worst': worst,
            'rationaleEn': rat_en,
            'rationaleVi': rat_vi,
            'competencyEn': comp_en,
            'competencyVi': comp_vi,
            'keyClueEn': clue_en,
            'keyClueVi': clue_vi
        }

p_rows = raw.get('05_Practice', [])
practice_questions = []
for idx, r in enumerate(p_rows[4:]):
    qid = r.get('A', '')
    if qid.startswith('Q'):
        sc_en, sc_vi = split_bi(r.get('B', ''))
        a_en, a_vi = split_bi(r.get('C', ''))
        b_en, b_vi = split_bi(r.get('D', ''))
        c_en, c_vi = split_bi(r.get('E', ''))
        d_en, d_vi = split_bi(r.get('F', ''))
        ans = answers.get(qid, {})
        practice_questions.append({
            'id': qid,
            'sectionId': None,
            'type': 'icf_sjt',
            'questionVi': sc_vi,
            'questionEn': sc_en,
            'options': [
                {'key': 'A', 'textVi': a_vi, 'textEn': a_en},
                {'key': 'B', 'textVi': b_vi, 'textEn': b_en},
                {'key': 'C', 'textVi': c_vi, 'textEn': c_en},
                {'key': 'D', 'textVi': d_vi, 'textEn': d_en}
            ],
            'bestAnswer': ans.get('best', 'A'),
            'worstAnswer': ans.get('worst', 'D'),
            'explanationVi': ans.get('rationaleVi', ''),
            'explanationEn': ans.get('rationaleEn', ''),
            'primaryCompetency': ans.get('competencyEn', ''),
            'keyClueVi': ans.get('keyClueVi', ''),
            'keyClueEn': ans.get('keyClueEn', ''),
            'difficulty': 'medium',
            'orderIndex': idx + 1
        })

# 4. Sections Tree
sections = [
    {
        'id': 'sec-a',
        'parentId': None,
        'code': 'A',
        'titleVi': 'Phần A: Nền Tảng (Foundation)',
        'titleEn': 'Part A: Foundation',
        'descriptionVi': 'Thiết lập chuẩn mực đạo đức nghề nghiệp và nuôi dưỡng tư duy khai vấn rộng mở.',
        'descriptionEn': 'Demonstrating ethical practice and embodying an open, curious coaching mindset.',
        'natureIcon': 'seed',
        'orderIndex': 1,
        'isFree': True,
        'isPublished': True
    },
    {
        'id': 'sec-a1',
        'parentId': 'sec-a',
        'code': 'A.1',
        'titleVi': 'Năng lực 1: Thể hiện Thực hành Đạo đức',
        'titleEn': 'Competency 1: Demonstrates Ethical Practice',
        'descriptionVi': 'Hiểu và nhất quán áp dụng chuẩn mực đạo đức, bảo mật thông tin và tính chính trực.',
        'descriptionEn': 'Understands and consistently applies coaching ethics and standards of coaching.',
        'natureIcon': 'seed',
        'orderIndex': 1,
        'isFree': True,
        'isPublished': True
    },
    {
        'id': 'sec-a1-1',
        'parentId': 'sec-a1',
        'code': 'A1.1',
        'titleVi': 'A1.1: Chính trực & Bảo mật thông tin (Integrity & Confidentiality)',
        'titleEn': 'A1.1: Personal Integrity & Confidentiality',
        'descriptionVi': 'Giữ gìn ranh giới bảo mật với khách hàng và nhà tài trợ (sponsor), minh bạch xung đột lợi ích.',
        'descriptionEn': 'Demonstrating integrity, confidentiality, and managing conflict of interest.',
        'natureIcon': 'seed',
        'orderIndex': 1,
        'isFree': True,
        'isPublished': True
    },
    {
        'id': 'sec-a1-2',
        'parentId': 'sec-a1',
        'code': 'A1.2',
        'titleVi': 'A1.2: Tôn trọng Bản sắc & Giới thiệu Chuyên gia (Identity & Referral)',
        'titleEn': 'A1.2: Identity Sensitivity & Professional Referral',
        'descriptionVi': 'Tôn trọng bản sắc văn hóa đa dạng và nhận diện kịp thời lúc cần chuyển giới thiệu chuyên gia.',
        'descriptionEn': 'Respecting identity, cultural diversity, and recognizing when to refer to specialists.',
        'natureIcon': 'seed',
        'orderIndex': 2,
        'isFree': False,
        'isPublished': True
    },
    {
        'id': 'sec-a2',
        'parentId': 'sec-a',
        'code': 'A.2',
        'titleVi': 'Năng lực 2: Thể hiện Tư duy Khai vấn (Coaching Mindset)',
        'titleEn': 'Competency 2: Embodies a Coaching Mindset',
        'descriptionVi': 'Duy trì tư duy cởi mở, tò mò, linh hoạt và lấy khách hàng làm trung tâm; tự quản trị định kiến.',
        'descriptionEn': 'Develops and maintains an open, curious, flexible, and client-centered mindset.',
        'natureIcon': 'sprout',
        'orderIndex': 2,
        'isFree': False,
        'isPublished': True
    },
    {
        'id': 'sec-b',
        'parentId': None,
        'code': 'B',
        'titleVi': 'Phần B: Cùng Tạo dựng Mối quan hệ (Co-creating Relationship)',
        'titleEn': 'Part B: Co-creating the Relationship',
        'descriptionVi': 'Đồng hành cùng khách hàng thiết lập mục tiêu phiên và nuôi dưỡng không gian an toàn tâm lý.',
        'descriptionEn': 'Partnering with the client to establish clear agreements and deep psychological safety.',
        'natureIcon': 'sprout',
        'orderIndex': 2,
        'isFree': False,
        'isPublished': True
    },
    {
        'id': 'sec-b1',
        'parentId': 'sec-b',
        'code': 'B.1',
        'titleVi': 'Năng lực 3: Thiết lập & Duy trì Thỏa thuận (Agreements)',
        'titleEn': 'Competency 3: Establishes & Maintains Agreements',
        'descriptionVi': 'Xác định mục tiêu tổng thể, tiêu chí đo lường thành công và giữ quyền sở hữu phiên cho khách hàng.',
        'descriptionEn': 'Partners with client to establish overall and session agreements, measures of success.',
        'natureIcon': 'sprout',
        'orderIndex': 1,
        'isFree': False,
        'isPublished': True
    },
    {
        'id': 'sec-b2',
        'parentId': 'sec-b',
        'code': 'B.2',
        'titleVi': 'Năng lực 4: Nuôi dưỡng Niềm tin & Sự An toàn (Trust & Safety)',
        'titleEn': 'Competency 4: Cultivates Trust and Safety',
        'descriptionVi': 'Tạo môi trường an toàn, tôn trọng và hỗ trợ để khách hàng tự do chia sẻ điều sâu kín nhất.',
        'descriptionEn': 'Creates a safe, supportive environment where the client shares freely without judgment.',
        'natureIcon': 'sprout',
        'orderIndex': 2,
        'isFree': False,
        'isPublished': True
    },
    {
        'id': 'sec-c',
        'parentId': None,
        'code': 'C',
        'titleVi': 'Phần C: Giao tiếp Hiệu quả (Communicating Effectively)',
        'titleEn': 'Part C: Communicating Effectively',
        'descriptionVi': 'Duy trì sự hiện diện tĩnh lặng và lắng nghe toàn vẹn những điều chưa nói.',
        'descriptionEn': 'Remaining fully present and listening actively to both what is said and not said.',
        'natureIcon': 'bamboo',
        'orderIndex': 3,
        'isFree': False,
        'isPublished': True
    },
    {
        'id': 'sec-c1',
        'parentId': 'sec-c',
        'code': 'C.1',
        'titleVi': 'Năng lực 5: Duy trì Sự Hiện diện (Maintains Presence)',
        'titleEn': 'Competency 5: Maintains Presence',
        'descriptionVi': 'Hoàn toàn ý thức và hiện diện với khách hàng, đón nhận sự im lặng và những điều bất định.',
        'descriptionEn': 'Remains fully conscious and present with client, comfortable with silence and uncertainty.',
        'natureIcon': 'bamboo',
        'orderIndex': 1,
        'isFree': False,
        'isPublished': True
    },
    {
        'id': 'sec-c2',
        'parentId': 'sec-c',
        'code': 'C.2',
        'titleVi': 'Năng lực 6: Lắng nghe Chủ động (Listens Actively)',
        'titleEn': 'Competency 6: Listens Actively',
        'descriptionVi': 'Tập trung vào ngôn từ, giọng điệu, ngôn ngữ cơ thể, cảm xúc và bối cảnh toàn diện của khách hàng.',
        'descriptionEn': 'Focuses on verbal and non-verbal cues, tone, energy, and emotional resonance.',
        'natureIcon': 'bamboo',
        'orderIndex': 2,
        'isFree': False,
        'isPublished': True
    },
    {
        'id': 'sec-d',
        'parentId': None,
        'code': 'D',
        'titleVi': 'Phần D: Thúc đẩy Học tập & Phát triển (Cultivating Growth)',
        'titleEn': 'Part D: Cultivating Learning and Growth',
        'descriptionVi': 'Khơi gợi góc nhìn mới và đồng hành để khách hàng chuyển hóa nhận thức thành hành động bền vững.',
        'descriptionEn': 'Evoking deep insight and partnering to transform awareness into meaningful action.',
        'natureIcon': 'lotus',
        'orderIndex': 4,
        'isFree': False,
        'isPublished': True
    },
    {
        'id': 'sec-d1',
        'parentId': 'sec-d',
        'code': 'D.1',
        'titleVi': 'Năng lực 7: Khơi gợi Nhận thức (Evokes Awareness)',
        'titleEn': 'Competency 7: Evokes Awareness',
        'descriptionVi': 'Tạo điều kiện để khách hàng tự khám phá thông qua câu hỏi gợi mở, ẩn dụ và phản chiếu tinh tế.',
        'descriptionEn': 'Facilitates client insight and discovery using powerful questions, metaphors and silence.',
        'natureIcon': 'lotus',
        'orderIndex': 1,
        'isFree': False,
        'isPublished': True
    },
    {
        'id': 'sec-d2',
        'parentId': 'sec-d',
        'code': 'D.2',
        'titleVi': 'Năng lực 8: Thúc đẩy Sự Phát triển của Khách hàng (Growth)',
        'titleEn': 'Competency 8: Facilitates Client Growth',
        'descriptionVi': 'Đồng hành chuyển hóa học hỏi thành mục tiêu hành động rõ ràng và trao quyền tự chịu trách nhiệm.',
        'descriptionEn': 'Partners with the client to transform learning into action, autonomy and accountability.',
        'natureIcon': 'lotus',
        'orderIndex': 2,
        'isFree': False,
        'isPublished': True
    }
]

# Write JSON seed structure
output_data = {
    'sections': sections,
    'glossary': glossary,
    'competencies': competencies,
    'practiceQuestions': practice_questions
}

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print('Generated parsedData.json successfully!')
