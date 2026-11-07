# -*- coding: utf-8 -*-
"""
Official ICF Core Competencies (2025 Edition) Data Provider
Includes all 8 Core Competencies across 4 Domains, 2025 definitions,
68+ verified sub-competencies, 2019 comparison elements, study cues,
exam triggers, and assessor perspectives.
"""
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = os.path.join(BASE_DIR, 'raw_data.json')

def split_bi(val):
    if not val:
        return '', ''
    if '\nVI: ' in val:
        parts = val.split('\nVI: ')
        return parts[0].strip(), parts[1].strip()
    if '\nVI:' in val:
        parts = val.split('\nVI:')
        return parts[0].strip(), parts[1].strip()
    return val.strip(), val.strip()

CHANGES_2025 = {
    '1.0': {
        'vi': 'Tích hợp quy định bảo vệ quyền riêng tư số và sử dụng công nghệ/AI có trách nhiệm; tăng cường sự nhạy bén liên văn hóa và ranh giới quyền lực.',
        'en': 'Integrates digital privacy protection and responsible AI technology use; reinforces cross-cultural sensitivity and systemic power boundaries.'
    },
    '2.0': {
        'vi': 'Mở rộng định nghĩa tư duy phản tư liên tục, sức khỏe toàn diện của coach (well-being), tìm kiếm sự hỗ trợ qua Coach Supervision / Mentor Coaching và tôn trọng quyền tự quyết của khách hàng trong bối cảnh hệ thống.',
        'en': 'Expands reflective practice, coach well-being, engaging in coach supervision/mentoring, and honoring client self-determination within systemic contexts.'
    },
    '3.0': {
        'vi': 'Bổ sung thỏa thuận về bảo mật dữ liệu số, sự đồng thuận khi sử dụng công cụ AI phiên âm/ghi chú, và ranh giới với các bên liên quan (sponsor/stakeholders) trong thỏa thuận nhiều bên.',
        'en': 'Adds explicit contracting on digital data security, consent for AI transcription/recording, and multi-stakeholder boundary clarity.'
    },
    '4.0': {
        'vi': 'Nhấn mạnh việc tạo môi trường an toàn tâm lý toàn diện, tôn trọng tính đa dạng, bình đẳng và hòa nhập (DEI), nhạy bén với tổn thương và thế giới quan (worldview) của khách hàng.',
        'en': 'Emphasizes comprehensive psychological safety, diversity, equity and inclusion (DEI), trauma sensitivity, and honoring client worldview.'
    },
    '5.0': {
        'vi': 'Làm sâu sắc năng lực hiện diện tĩnh tại, nhạy bén với các phản ứng cảm xúc phức tạp, linh hoạt chuyển hướng theo thân tâm trí của khách hàng mà không vội vàng giải quyết.',
        'en': 'Deepens grounded presence, agility with complex emotional shifts, following the somatic/cognitive flow without rushing to fix.'
    },
    '6.0': {
        'vi': 'Lắng nghe đa tầng: ngôn từ, phi ngôn từ, cảm xúc, năng lượng, các khoảng lặng và bối cảnh văn hóa/xã hội bao quanh câu chuyện của khách hàng.',
        'en': "Multi-layered listening: words, non-verbal cues, emotions, energy shifts, pauses, and the client's cultural and societal context."
    },
    '7.0': {
        'vi': 'Khơi gợi nhận thức mang tính biến chuyển (transformational insight): khám phá hệ thống niềm tin cốt lõi, giả định ẩn giấu, ẩn dụ cá nhân và mô thức hành vi xuyên suốt.',
        'en': 'Evokes transformational awareness: uncovering core belief systems, hidden assumptions, personal metaphors, and recurring behavioral patterns.'
    },
    '8.0': {
        'vi': 'Khách hàng toàn quyền làm chủ việc thiết kế hành động, thiết lập cơ chế trách nhiệm giải trình tự thân (self-accountability) và tích hợp bài học vào đời sống dài hạn.',
        'en': 'Client fully owns action design, autonomous accountability structures, and sustainable long-term integration of insights.'
    }
}

LEGACY_2019_SUBS = {
    '1.0': [
        {'subId': '1.1', 'behaviorEn': 'Demonstrates personal integrity and honesty in interactions with clients, sponsors and relevant stakeholders', 'behaviorVi': 'Thể hiện sự chính trực và trung thực trong tương tác với khách hàng, nhà tài trợ và các bên liên quan.'},
        {'subId': '1.2', 'behaviorEn': 'Is sensitive to clients’ identity, environment, experiences, values and beliefs', 'behaviorVi': 'Nhạy cảm và tôn trọng bản sắc, môi trường, trải nghiệm, giá trị và niềm tin của khách hàng.'},
        {'subId': '1.3', 'behaviorEn': 'Uses language appropriate and respectful to clients, sponsors and relevant stakeholders', 'behaviorVi': 'Sử dụng ngôn ngữ phù hợp và tôn trọng khách hàng, nhà tài trợ và các bên liên quan.'},
        {'subId': '1.4', 'behaviorEn': 'Abides by the ICF Code of Ethics and upholds the Core Values', 'behaviorVi': 'Tuân thủ Bộ Quy tắc Đạo đức ICF và phát huy các Giá trị Cốt lõi.'},
        {'subId': '1.5', 'behaviorEn': 'Maintains confidentiality with client information per stakeholder agreements and pertinent laws', 'behaviorVi': 'Duy trì tính bảo mật thông tin khách hàng theo thỏa thuận các bên và luật pháp hiện hành.'},
        {'subId': '1.6', 'behaviorEn': 'Maintains the distinctions between coaching, consulting, psychotherapy and other support professions', 'behaviorVi': 'Giữ vững sự phân biệt giữa khai vấn, tư vấn chuyên môn, trị liệu tâm lý và các ngành nghề hỗ trợ khác.'},
        {'subId': '1.7', 'behaviorEn': 'Refers clients to other support professionals, as appropriate', 'behaviorVi': 'Chuyển gửi khách hàng sang các chuyên gia trợ giúp khác khi phù hợp.'}
    ],
    '2.0': [
        {'subId': '2.1', 'behaviorEn': 'Acknowledges that clients are responsible for their own choices', 'behaviorVi': 'Công nhận rằng khách hàng chịu trách nhiệm về các lựa chọn của chính họ.'},
        {'subId': '2.2', 'behaviorEn': 'Engages in ongoing learning and development as a coach', 'behaviorVi': 'Tham gia vào quá trình học tập và phát triển liên tục với tư cách là coach.'},
        {'subId': '2.3', 'behaviorEn': 'Develops an ongoing reflective practice to enhance one’s coaching', 'behaviorVi': 'Phát triển thói quen phản tư liên tục để nâng cao năng lực khai vấn.'},
        {'subId': '2.4', 'behaviorEn': 'Remains aware of and open to the influence of context and culture on self and others', 'behaviorVi': 'Nhận thức và cởi mở với ảnh hưởng của bối cảnh và văn hóa lên bản thân và người khác.'},
        {'subId': '2.5', 'behaviorEn': 'Uses awareness of self and one’s intuition to benefit clients', 'behaviorVi': 'Sử dụng sự tự nhận thức và trực giác vì lợi ích của khách hàng.'},
        {'subId': '2.6', 'behaviorEn': 'Develops and maintains the ability to regulate one’s emotions', 'behaviorVi': 'Phát triển và duy trì khả năng điều tiết cảm xúc của bản thân.'},
        {'subId': '2.7', 'behaviorEn': 'Mentally and emotionally prepares for sessions', 'behaviorVi': 'Chuẩn bị tâm trí và cảm xúc trước các phiên khai vấn.'},
        {'subId': '2.8', 'behaviorEn': 'Seeks help from outside sources when necessary', 'behaviorVi': 'Tìm kiếm sự trợ giúp từ bên ngoài khi cần thiết.'}
    ]
}

def get_competencies_2025():
    with open(RAW_DATA_PATH, 'r', encoding='utf-8') as f:
        raw = json.load(f)

    sheet = raw.get('02_Core_Competencies', [])
    comps = []
    cur_comp = None

    for r in sheet[2:]:
        no = r.get('B', '').strip()
        if no:
            domain_en, domain_vi = split_bi(r.get('A', ''))
            comp_en, comp_vi = split_bi(r.get('C', ''))
            def_en, def_vi = split_bi(r.get('D', ''))
            cue_en, cue_vi = split_bi(r.get('G', ''))
            trigger_en, trigger_vi = split_bi(r.get('H', ''))
            nature_en, nature_vi = split_bi(r.get('I', ''))
            natural_en, natural_vi = split_bi(r.get('J', ''))
            assessor_en, assessor_vi = split_bi(r.get('K', ''))
            traps_en, traps_vi = split_bi(r.get('L', ''))
            
            cur_comp = {
                'code': f'Năng lực {no}',
                'number': no,
                'domainEn': domain_en,
                'domainVi': domain_vi,
                'compEn': comp_en,
                'compVi': comp_vi,
                'nameEn': comp_en,
                'nameVi': comp_vi,
                'titleEn': comp_en,
                'titleVi': comp_vi,
                'descEn': def_en,
                'descVi': def_vi,
                'definitionEn': def_en,
                'definitionVi': def_vi,
                'studyCueEn': cue_en,
                'studyCueVi': cue_vi,
                'cueEn': cue_en,
                'cueVi': cue_vi,
                'examTriggerEn': trigger_en,
                'examTriggerVi': trigger_vi,
                'natureEn': nature_en,
                'natureVi': nature_vi,
                'naturalInCoachingEn': natural_en,
                'naturalInCoachingVi': natural_vi,
                'assessorPerspectiveEn': assessor_en,
                'assessorPerspectiveVi': assessor_vi,
                'commonTrapsEn': traps_en,
                'commonTrapsVi': traps_vi,
                'trapEn': traps_en,
                'trapVi': traps_vi,
                'lensEn': cue_en,
                'lensVi': cue_vi,
                'changes2025Vi': CHANGES_2025.get(no, {}).get('vi', ''),
                'changes2025En': CHANGES_2025.get(no, {}).get('en', ''),
                'subCompetencies2025': [],
                'subCompetencies2019': LEGACY_2019_SUBS.get(no, [])
            }
            comps.append(cur_comp)

        sub_id = r.get('E', '').strip()
        if cur_comp and sub_id:
            beh_en, beh_vi = split_bi(r.get('F', ''))
            cur_comp['subCompetencies2025'].append({
                'subId': sub_id,
                'behaviorEn': beh_en,
                'behaviorVi': beh_vi
            })

    return comps
