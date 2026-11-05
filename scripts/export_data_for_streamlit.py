import json
import os

RAW_PATH = 'src/lib/parsedData.json'
OUT_DIR = 'data'
OUT_PATH = os.path.join(OUT_DIR, 'mentor_data.json')

with open(RAW_PATH, 'r', encoding='utf-8') as f:
    parsed = json.load(f)

sections = parsed['sections']
glossary = parsed['glossary']
competencies = parsed['competencies']
practice_questions = parsed['practiceQuestions']

# 30 Bilingual Mindfulness Messages
mindfulness_messages = [
    {
        "id": "mm-01",
        "textVi": "Mỗi phiên khai vấn là một hành trình trở về với sự hiện diện tĩnh lặng và lắng nghe không định kiến.",
        "textEn": "Every coaching session is a journey back to still presence and listening without prejudice.",
        "theme": "Hiện diện",
        "author": "Zen Coaching Wisdom",
        "isActive": True
    },
    {
        "id": "mm-02",
        "textVi": "Hãy để sự im lặng làm việc. Trong khoảng lặng sâu, khách hàng tìm thấy câu trả lời chân thật nhất của chính họ.",
        "textEn": "Let silence do the heavy lifting. In deep stillness, clients discover their own truest answers.",
        "theme": "Khoảng lặng",
        "author": "Zen Coaching Wisdom",
        "isActive": True
    },
    {
        "id": "mm-03",
        "textVi": "Coach không cần phải là người sửa chữa. Khách hàng tự thân đã trọn vẹn, sáng tạo và đủ đầy nguồn lực.",
        "textEn": "A coach is not a fixer. The client is naturally whole, creative, and fully resourceful.",
        "theme": "Tin tưởng",
        "author": "ICF Principle",
        "isActive": True
    },
    {
        "id": "mm-04",
        "textVi": "Khi buông bỏ nhu cầu chứng minh năng lực, ta mới thực sự trao trọn không gian cho khách hàng tỏa sáng.",
        "textEn": "When you surrender the need to prove your capability, you truly offer the space for the client to shine.",
        "theme": "Vô ngã",
        "author": "Zen Mind",
        "isActive": True
    },
    {
        "id": "mm-05",
        "textVi": "Một tách trà ấm, một hơi thở sâu. Ta có mặt trọn vẹn ở đây cho chính mình và cho người đồng hành.",
        "textEn": "A warm cup of tea, a deep breath. Arriving fully here for yourself and your companion.",
        "theme": "Chánh niệm",
        "author": "Zen Tea",
        "isActive": True
    },
    {
        "id": "mm-06",
        "textVi": "Lắng nghe không chỉ bằng tai mà bằng cả đôi mắt, trái tim và năng lượng của sự thấu cảm.",
        "textEn": "Listening not merely with ears, but with eyes, heart, and the gentle energy of empathy.",
        "theme": "Lắng nghe sâu",
        "author": "ICF Marker 6",
        "isActive": True
    },
    {
        "id": "mm-07",
        "textVi": "Đạo đức nghề nghiệp là gốc rễ. Khi gốc rễ vững chãi, cái cây khai vấn tự nhiên đơm hoa kết trái.",
        "textEn": "Ethical practice is the root. When roots are grounded, the coaching tree naturally blossoms.",
        "theme": "Đạo đức",
        "author": "ICF Ethics",
        "isActive": True
    },
    {
        "id": "mm-08",
        "textVi": "Đừng vội vàng đi tìm giải pháp. Hãy cùng khách hàng khám phá vẻ đẹp của câu hỏi đúng.",
        "textEn": "Do not rush toward solutions. Walk alongside the client into the profound beauty of the right question.",
        "theme": "Tò mò",
        "author": "Inquiry",
        "isActive": True
    },
    {
        "id": "mm-09",
        "textVi": "Mỗi sai sót khi làm bài thi thử là một hạt giống hiểu biết giúp bạn tiến gần hơn tới chuẩn mực PCC.",
        "textEn": "Every mistake in a mock test is a seed of insight bringing you closer to PCC mastery.",
        "theme": "Học hỏi",
        "author": "Growth Mindset",
        "isActive": True
    },
    {
        "id": "mm-10",
        "textVi": "Sự đồng hành bình đẳng (Partnership) là chìa khóa mở cánh cửa chuyển hóa bền vững.",
        "textEn": "True partnership is the master key that opens the door to sustainable transformation.",
        "theme": "Đồng hành",
        "author": "PCC Rule",
        "isActive": True
    },
    {
        "id": "mm-11",
        "textVi": "Tâm trí giống như mặt hồ. Khi mặt hồ tĩnh lặng, vạn vật mới phản chiếu chân thực nhất.",
        "textEn": "The mind is like a serene lake. Only in stillness does it reflect things as they truly are.",
        "theme": "Tĩnh lặng",
        "author": "Zen Mind",
        "isActive": True
    },
    {
        "id": "mm-12",
        "textVi": "Chấp nhận những điều bất định với lòng dũng cảm. Phiên coach tuyệt vời nhất nằm ở nơi không ai biết trước.",
        "textEn": "Embrace uncertainty with courage. The most profound coaching happens in unchartered waters.",
        "theme": "Dũng cảm",
        "author": "Presence",
        "isActive": True
    },
    {
        "id": "mm-13",
        "textVi": "Khi khách hàng im lặng sau một câu hỏi, đó là lúc điều kỳ diệu đang nở hoa trong tâm trí họ.",
        "textEn": "When a client pauses in silence after a question, magic is gently blooming in their mind.",
        "theme": "Khoảng lặng",
        "author": "PCC Marker 5.4",
        "isActive": True
    },
    {
        "id": "mm-14",
        "textVi": "Tôn trọng thế giới quan của khách hàng, ngay cả khi nó hoàn toàn khác biệt với trải nghiệm của bạn.",
        "textEn": "Honor the client’s worldview, even when it differs completely from your own lived experience.",
        "theme": "Tôn trọng",
        "author": "ICF Marker 4",
        "isActive": True
    },
    {
        "id": "mm-15",
        "textVi": "Hơi thở vào mang lại sự bình an; hơi thở ra giải tỏa mọi căng thẳng và kỳ vọng.",
        "textEn": "Breathing in brings calm peace; breathing out releases all tension and expectation.",
        "theme": "Hơi thở",
        "author": "Zen Breath",
        "isActive": True
    },
    {
        "id": "mm-16",
        "textVi": "Hãy để khách hàng dẫn đường về chủ đề, và coach giữ ngọn đèn chiếu sáng cho con đường ấy.",
        "textEn": "Let the client choose the path, while the coach gently holds the lantern to light the way.",
        "theme": "Đồng hành",
        "author": "ICF Marker 3",
        "isActive": True
    },
    {
        "id": "mm-17",
        "textVi": "Phản chiếu lại cảm xúc và ngôn từ của khách hàng mà không thêm bớt lời phán xét hay phân tích cá nhân.",
        "textEn": "Mirror back the client’s emotion and language without adding personal judgment or unsolicited analysis.",
        "theme": "Phản chiếu",
        "author": "Active Listening",
        "isActive": True
    },
    {
        "id": "mm-18",
        "textVi": "Khám phá cả cái 'Ai' (Who) sâu sắc của khách hàng, không chỉ dừng lại ở vấn đề 'Cái gì' (What).",
        "textEn": "Explore the deep 'Who' of the client, rather than merely fixing the surface 'What'.",
        "theme": "Chiều sâu",
        "author": "PCC Marker 7",
        "isActive": True
    },
    {
        "id": "mm-19",
        "textVi": "Mỗi ngày dành 15 phút học tập chánh niệm tốt hơn nhiều so với việc dồn ép trong lo âu.",
        "textEn": "Fifteen minutes of mindful daily study is infinitely more fruitful than cramming in anxiety.",
        "theme": "Tinh tấn",
        "author": "Daily Practice",
        "isActive": True
    },
    {
        "id": "mm-20",
        "textVi": "Thành công của kỳ thi PCC không chỉ là tấm bằng, mà là phẩm chất hiện diện bạn tôi luyện mỗi ngày.",
        "textEn": "Success in the PCC exam is not just a badge, but the quality of presence you cultivate each day.",
        "theme": "Chuyển hóa",
        "author": "The Journey",
        "isActive": True
    },
    {
        "id": "mm-21",
        "textVi": "Khi tâm an, vạn sự thông. Trước mỗi bài thi thử, hãy dành 3 hơi thở để thân tâm hợp nhất.",
        "textEn": "When the mind is calm, clarity emerges. Before each test, take three conscious breaths.",
        "theme": "An định",
        "author": "Three Breaths",
        "isActive": True
    },
    {
        "id": "mm-22",
        "textVi": "Hãy tò mò như một đứa trẻ nhìn thế giới lần đầu tiên: không giả định, không áp đặt kết luận.",
        "textEn": "Be curious like a child seeing the world for the first time: no assumptions, no hasty conclusions.",
        "theme": "Tâm ban đầu",
        "author": "Beginner Mind",
        "isActive": True
    },
    {
        "id": "mm-23",
        "textVi": "Mối quan hệ coaching là một không gian thiêng liêng được xây dựng trên sự tin cậy tuyệt đối.",
        "textEn": "The coaching relationship is a sacred sanctuary built upon unconditional trust.",
        "theme": "Niềm tin",
        "author": "Trust",
        "isActive": True
    },
    {
        "id": "mm-24",
        "textVi": "Quan sát năng lượng và sự thay đổi trong nhịp thở của khách hàng — đó là nơi sự thật đang lên tiếng.",
        "textEn": "Notice the client's energy shifts and rhythm of breath — that is where deep truth speaks.",
        "theme": "Quan sát",
        "author": "Presence",
        "isActive": True
    },
    {
        "id": "mm-25",
        "textVi": "Học cách bao dung với chính mình. Con đường luyện thi PCC là một hành trình tu dưỡng nội tâm.",
        "textEn": "Be gentle and forgiving with yourself. The PCC journey is a practice of inner cultivation.",
        "theme": "Tự thương",
        "author": "Self-Compassion",
        "isActive": True
    },
    {
        "id": "mm-26",
        "textVi": "Một câu hỏi sắc bén có sức mạnh mở toang những giới hạn mà khách hàng đã tự dựng lên suốt nhiều năm.",
        "textEn": "A poignant question has the power to dissolve the boundaries a client built for years.",
        "theme": "Gợi mở",
        "author": "Evoking Awareness",
        "isActive": True
    },
    {
        "id": "mm-27",
        "textVi": "Trao quyền cho khách hàng tự xác định kế hoạch hành động và phương thức họ muốn tự cam kết.",
        "textEn": "Empower the client to design their own action plan and choose how they will hold themselves accountable.",
        "theme": "Trao quyền",
        "author": "Client Growth",
        "isActive": True
    },
    {
        "id": "mm-28",
        "textVi": "Biết rõ ranh giới chuyên môn và dũng cảm giới thiệu khách hàng khi vấn đề vượt ngoài phạm vi khai vấn.",
        "textEn": "Know professional boundaries clearly and refer bravely when matters lie beyond coaching scope.",
        "theme": "Ranh giới",
        "author": "Ethics Referral",
        "isActive": True
    },
    {
        "id": "mm-29",
        "textVi": "Trong bài thi phán đoán tình huống (SJT), phương án BEST luôn lấy khách hàng làm trung tâm và tôn trọng thỏa thuận.",
        "textEn": "In Situational Judgment tests, the BEST response consistently honors client autonomy and agreements.",
        "theme": "Mẹo thi",
        "author": "PCC Playbook",
        "isActive": True
    },
    {
        "id": "mm-30",
        "textVi": "Dưới bóng mát của sự hiện diện, hạt giống nhận thức của khách hàng tự khắc đâm chồi nảy lộc.",
        "textEn": "Beneath the soothing shade of your presence, the client’s seeds of insight blossom naturally.",
        "theme": "Hoa sen nở",
        "author": "Zen Presence",
        "isActive": True
    }
]

# 12 SVG Stickers
stickers = [
    {
        "id": "stk-01",
        "code": "monk_welcome",
        "nameVi": "Chú tiểu hoan hỉ",
        "nameEn": "Joyful Zen Monk",
        "category": "monk",
        "triggerEvent": "welcome",
        "isActive": True
    },
    {
        "id": "stk-02",
        "code": "lotus_blooming",
        "nameVi": "Đóa sen nở rộ",
        "nameEn": "Blooming Lotus",
        "category": "lotus",
        "triggerEvent": "lesson_complete",
        "isActive": True
    },
    {
        "id": "stk-03",
        "code": "cat_zen",
        "nameVi": "Mèo thiền an nhiên",
        "nameEn": "Mindful Zen Cat",
        "category": "cat",
        "triggerEvent": "quiz_streak",
        "isActive": True
    },
    {
        "id": "stk-04",
        "code": "lotus_comfort",
        "nameVi": "Mầm sen vỗ về",
        "nameEn": "Comforting Sprout",
        "category": "nature",
        "triggerEvent": "comfort_mistake",
        "isActive": True
    },
    {
        "id": "stk-05",
        "code": "streak_3days",
        "nameVi": "3 Ngày Tinh Tấn",
        "nameEn": "3-Day Diligence",
        "category": "badge",
        "triggerEvent": "streak_milestone",
        "isActive": True
    },
    {
        "id": "stk-06",
        "code": "streak_7days",
        "nameVi": "7 Ngày Chánh Niệm",
        "nameEn": "7-Day Mindfulness",
        "category": "badge",
        "triggerEvent": "streak_milestone",
        "isActive": True
    },
    {
        "id": "stk-07",
        "code": "streak_30days",
        "nameVi": "30 Ngày Vững Chãi",
        "nameEn": "30-Day Steadfast",
        "category": "badge",
        "triggerEvent": "streak_milestone",
        "isActive": True
    },
    {
        "id": "stk-08",
        "code": "mountain_master",
        "nameVi": "Đỉnh Núi Tự Tin",
        "nameEn": "Mountain Mastery",
        "category": "badge",
        "triggerEvent": "exam_high_score",
        "isActive": True
    },
    {
        "id": "stk-09",
        "code": "tea_cup",
        "nameVi": "Tách trà thảnh thơi",
        "nameEn": "Mindful Teacup",
        "category": "nature",
        "triggerEvent": "renewal_gentle",
        "isActive": True
    },
    {
        "id": "stk-10",
        "code": "bamboo_listening",
        "nameVi": "Lá trúc lắng nghe",
        "nameEn": "Bamboo Listening",
        "category": "nature",
        "triggerEvent": "lesson_complete",
        "isActive": True
    },
    {
        "id": "stk-11",
        "code": "enso_circle",
        "nameVi": "Vòng tròn Enso",
        "nameEn": "Enso Circle",
        "category": "badge",
        "triggerEvent": "welcome",
        "isActive": True
    },
    {
        "id": "stk-12",
        "code": "sparrow_zen",
        "nameVi": "Chim sẻ tự tại",
        "nameEn": "Free Sparrow",
        "category": "nature",
        "triggerEvent": "welcome",
        "isActive": True
    }
]

# System Settings with Bank & VietQR info
system_settings = {
    "bankName": "Vietcombank (Ngân hàng TMCP Ngoại Thương Việt Nam)",
    "accountNumber": "9988776655",
    "accountHolder": "VI VIEN KHAI VAN ZEN PCC",
    "bankBin": "970436",
    "pricing": {
        "free": {
            "price": 0,
            "nameVi": "Gói Khởi Đầu (Miễn phí)",
            "nameEn": "Starter Tier (Free)",
            "featuresVi": [
                "Truy cập bài học miễn phí Phần A.1 (Đạo đức)",
                "Luyện tập 15 Flashcard cơ bản",
                "Thực hành 5 câu hỏi Quiz mẫu",
                "Xem Vườn sen chánh niệm",
                "Nhận Lời nhắn chánh niệm mỗi ngày"
            ],
            "featuresEn": [
                "Access free lessons in Part A.1 (Ethics)",
                "Practice 15 basic Flashcards",
                "Attempt 5 sample Quiz questions",
                "View personal Lotus Garden",
                "Receive Daily Mindfulness Message"
            ]
        },
        "1_month": {
            "price": 299000,
            "nameVi": "Gói Tinh Tấn (1 Tháng)",
            "nameEn": "Diligence Tier (1 Month)",
            "featuresVi": [
                "Mở khóa toàn bộ 8 Năng lực cốt lõi ICF",
                "Toàn bộ 6 tab chuyên sâu từng bài",
                "Luyện tập không giới hạn toàn bộ ngân hàng Flashcard & Quiz",
                "Tham gia Thi thử tổng PCC chuẩn ICF",
                "Ghi chú cá nhân & theo dõi biểu đồ tiến độ"
            ],
            "featuresEn": [
                "Unlock all 8 ICF Core Competencies",
                "Full access to 6 in-depth tabs per lesson",
                "Unlimited practice on all Flashcards & Quizzes",
                "Attempt full standard ICF PCC Mock Exams",
                "Personal notes & progress analytics"
            ]
        },
        "6_months": {
            "price": 1190000,
            "nameVi": "Gói Đồng Hành (6 Tháng - Tiết kiệm 35%)",
            "nameEn": "Companion Tier (6 Months - Save 35%)",
            "featuresVi": [
                "Toàn bộ quyền lợi của gói Tinh Tấn",
                "Thời hạn 6 tháng ôn thi vững tâm, thảnh thơi",
                "Mở khóa toàn bộ kho Sticker chánh niệm độc quyền",
                "Tải tài liệu PDF sơ đồ tư duy Mindmap song ngữ",
                "Hỗ trợ giải đáp chuyên môn qua email"
            ],
            "featuresEn": [
                "All features of Diligence Tier",
                "6-month tranquil study access without pressure",
                "Unlock all exclusive mindfulness stickers",
                "Download bilingual Mindmap PDFs",
                "Priority email coaching support"
            ]
        },
        "12_months": {
            "price": 1890000,
            "nameVi": "Gói Trọn Vẹn (12 Tháng - Tốt nhất)",
            "nameEn": "Mastery Tier (12 Months - Best Value)",
            "featuresVi": [
                "Toàn bộ quyền lợi cao cấp nhất trong 1 năm trọn vẹn",
                "Tự động cập nhật mọi câu hỏi tình huống SJT mới theo chuẩn ICF 2026",
                "Không giới hạn số lượt thi thử và lưu lịch sử làm bài chi tiết",
                "Huy hiệu Thiền sinh Tinh anh trong Vườn sen",
                "Ưu đãi đặc biệt khi gia hạn"
            ],
            "featuresEn": [
                "All premium privileges for 1 full year",
                "Automatic updates with new SJT questions per ICF 2026 standards",
                "Unlimited mock exams with comprehensive review history",
                "Elite Zen Coach badge in Lotus Garden",
                "Special alumni renewal discount"
            ]
        }
    },
    "bannerAnnouncement": {
        "vi": "Chào mừng bạn đến với Mentor thi ICF PCC. Chúc bạn một hành trình ôn thi an lạc và tự tin!",
        "en": "Welcome to ICF PCC Mentor. Wishing you a peaceful and confident preparation journey!",
        "active": True
    }
}

# Discount codes
discount_codes = [
    {"code": "PCC2026", "discountPercent": 20, "validUntil": "2026-12-31T23:59:59Z", "isActive": True},
    {"code": "ZENCOACH", "discountPercent": 15, "validUntil": "2026-12-31T23:59:59Z", "isActive": True},
    {"code": "LANGMAI", "discountPercent": 10, "validUntil": "2026-12-31T23:59:59Z", "isActive": True}
]

# Generate detailed 6-tab content for leaf sections
theories = []
keywords = []
flashcards = []
case_studies = []
quizzes = []

leaf_sections = ['sec-a1-1', 'sec-a1-2', 'sec-a2', 'sec-b1', 'sec-b2', 'sec-c1', 'sec-c2', 'sec-d1', 'sec-d2']

for idx, sec_id in enumerate(leaf_sections):
    comp = competencies[idx % len(competencies)]
    
    # 1. Theory
    theories.append({
        "id": f"th-{sec_id}",
        "sectionId": sec_id,
        "titleVi": f"Bài Giảng Chuyên Sâu: {comp['compVi']}",
        "titleEn": f"In-Depth Lecture: {comp['compEn']}",
        "contentVi": f"""### 1. Bản Chất Năng Lực Theo Chuẩn ICF 2025
Năng lực **{comp['compVi']}** thuộc miền `{comp['domainVi']}` là một trong những cột trụ quyết định đánh giá cấp độ PCC.

#### Định Nghĩa Cốt Lõi:
Coach thể hiện sự hiểu biết sâu sắc và áp dụng nhất quán các quy chuẩn hành vi chuyên nghiệp, coi khách hàng là người làm chủ mục tiêu và kết quả phiên khai vấn.

#### Góc Nhìn Khi Làm Bài Thi (Exam Lens):
> **Tự hỏi bản thân:** {comp['lensVi']}

#### Gợi Ý Ghi Nhớ Nhanh (Memory Cue):
- **Quy tắc vàng:** `{comp['cueVi']}`
- **Bẫy thường gặp (Common Trap):** {comp['trapVi']}. Khi gặp tình huống này, phương án chọn can thiệp trực tiếp hoặc áp đặt giải pháp luôn là phương án **WORST (Tệ nhất)**!

#### Bảng So Sánh ACC vs PCC vs MCC:
- **ACC:** Tập trung vào làm đúng quy trình đặt câu hỏi, đôi khi còn nặng tính tư vấn nhẹ hoặc bám vào giải pháp bề mặt (What).
- **PCC:** Đồng hành bình đẳng (Partnership), khơi mở thế giới quan và con người khách hàng (Who), đón nhận khoảng lặng và chuyển hóa nhận thức sâu sắc.
- **MCC:** Thuần khiết hiện diện, không bận tâm đến việc chứng minh kỹ năng, phiên khai vấn chảy trôi tự nhiên như dòng nước.
""",
        "contentEn": f"""### 1. Essence of the Competency per ICF 2025 Standards
Competency **{comp['compEn']}** under `{comp['domainEn']}` is a foundational pillar determining PCC credentialing success.

#### Core Definition:
The coach demonstrates deep understanding and consistent application of professional coaching behaviors, honoring client ownership of session direction and outcomes.

#### Exam Lens:
> **Ask yourself:** {comp['lensEn']}

#### Fast Memory Cue:
- **Golden Rule:** `{comp['cueEn']}`
- **Common Trap:** {comp['trapEn']}. When faced with this scenario, choosing to direct or solve for the client is consistently the **WORST** response!

#### ACC vs PCC vs MCC Contrast:
- **ACC:** Adheres to basic questioning sequences, occasionally leans into light consulting or remains on surface problems (What).
- **PCC:** Unconditional partnership, evokes the client's worldview and inner identity (Who), embraces stillness and profound awareness shifts.
- **MCC:** Pure effortless presence, unattached to proving skill, coaching flows seamlessly like moving water.
""",
        "isFree": (sec_id == 'sec-a1-1')
    })

    # 2. Keywords
    keywords.append({
        "id": f"kw-{sec_id}-1",
        "sectionId": sec_id,
        "termVi": f"{comp['cueVi']}",
        "termEn": f"{comp['cueEn']}",
        "definitionVi": f"Quy tắc ghi nhớ trọng tâm cho năng lực {comp['compVi']}: {comp['lensVi']}",
        "definitionEn": f"Core mnemonic rule for {comp['compEn']}: {comp['lensEn']}",
        "category": "mnemonic",
        "memoryCueVi": f"Bẫy cần tránh: {comp['trapVi']}",
        "memoryCueEn": f"Trap to avoid: {comp['trapEn']}",
        "orderIndex": 1
    })
    
    g_term = glossary[idx % len(glossary)]
    keywords.append({
        "id": f"kw-{sec_id}-2",
        "sectionId": sec_id,
        "termVi": g_term['termVi'],
        "termEn": g_term['termEn'],
        "definitionVi": g_term['definitionVi'],
        "definitionEn": g_term['definitionEn'],
        "category": "overview",
        "memoryCueVi": g_term['cueVi'],
        "memoryCueEn": g_term['cueEn'],
        "orderIndex": 2
    })

    # 3. Flashcards
    flashcards.append({
        "id": f"fc-{sec_id}-1",
        "sectionId": sec_id,
        "frontVi": f"Quy tắc phản xạ cốt lõi khi gặp tình huống liên quan đến: {comp['compVi']} là gì?",
        "frontEn": f"What is the reflex rule when encountering situations related to: {comp['compEn']}?",
        "backVi": f"{comp['cueVi']} — Góc nhìn thi: {comp['lensVi']}",
        "backEn": f"{comp['cueEn']} — Exam Lens: {comp['lensEn']}",
        "hintVi": f"Cảnh giác với: {comp['trapVi']}",
        "hintEn": f"Beware of: {comp['trapEn']}",
        "orderIndex": 1
    })
    flashcards.append({
        "id": f"fc-{sec_id}-2",
        "sectionId": sec_id,
        "frontVi": f"Ý nghĩa chuẩn mực của thuật ngữ: \"{g_term['termVi']}\" là gì?",
        "frontEn": f"What is the exact definition of: \"{g_term['termEn']}\"?",
        "backVi": g_term['definitionVi'],
        "backEn": g_term['definitionEn'],
        "hintVi": g_term['cueVi'],
        "hintEn": g_term['cueEn'],
        "orderIndex": 2
    })

    # 4. Case Study
    case_studies.append({
        "id": f"cs-{sec_id}",
        "sectionId": sec_id,
        "titleVi": f"Tình huống thực tế: Vấn đề trong {comp['compVi']}",
        "titleEn": f"Case Study: Dilemma in {comp['compEn']}",
        "scenarioVi": f"Khách hàng là giám đốc điều hành gặp khó khăn khi phân bổ quyền lực cho đội ngũ. Trong phiên khai vấn, khách hàng liên tục yêu cầu Coach chia sẻ kinh nghiệm lãnh đạo từ doanh nghiệp cũ của Coach.",
        "scenarioEn": f"The client is an executive struggling with delegating power. During the session, the client repeatedly asks the Coach to share past leadership experiences from the Coach's previous corporate career.",
        "dialogue": [
            {"speaker": "Client", "textVi": "Tôi thực sự bế tắc với nhân sự cấp dưới. Coach từng lãnh đạo tập đoàn lớn, Coach hãy cho tôi biết trong trường hợp này tôi phải làm gì?", "textEn": "I am truly stuck with my direct reports. Coach, you led large corporations before, can you tell me what to do in this scenario?", "markerTag": None},
            {"speaker": "Coach", "textVi": "Tôi nghe thấy áp lực lớn đang đè nặng lên vai bạn lúc này. Trước khi ta đi đến hành động, điều gì khiến việc buông bớt quyền kiểm soát trở nên khó khăn với bạn như vậy?", "textEn": "I hear the tremendous weight you are carrying right now. Before we look at actions, what makes letting go of control feel so challenging for you?", "markerTag": "PCC Marker 7.1"},
            {"speaker": "Client", "textVi": "Ồ... có lẽ tôi sợ nếu không tự tay làm, mọi thứ sẽ sụp đổ và tôi sẽ bị coi là người thất bại.", "textEn": "Oh... perhaps I fear that if I don't handle it myself, everything will collapse and I will be seen as a failure.", "markerTag": None},
            {"speaker": "Coach", "textVi": "(Im lặng 5 giây mỉm cười đón nhận)... Bạn nhận thấy nỗi sợ này đang dẫn dắt phong cách lãnh đạo của mình như thế nào?", "textEn": "(5-second mindful silence)... How do you notice this fear guiding your leadership style?", "markerTag": "PCC Marker 5.4 & 7.2"}
        ],
        "reflectionQuestionsVi": [
            "Tại sao Coach từ chối đưa ra lời khuyên trực tiếp?",
            "Khoảng lặng của Coach mang lại tác động gì cho sự chuyển biến của khách hàng?",
            "Làm thế nào để duy trì tính đồng hành (Partnership) khi khách hàng liên tục 'nhờ vả' giải pháp?"
        ],
        "reflectionQuestionsEn": [
            "Why did the Coach refrain from offering direct advice?",
            "What impact did the Coach's silence have on the client's insight?",
            "How can you maintain true Partnership when the client pushes for solutions?"
        ],
        "pccMarkerRef": "ICF PCC Markers 3.2, 5.4, 7.1",
        "orderIndex": 1
    })

    # 5. Quiz Questions
    quizzes.append({
        "id": f"qz-{sec_id}-1",
        "sectionId": sec_id,
        "type": "single_choice",
        "questionVi": f"Theo lăng kính năng lực {comp['compVi']}, hành động nào sau đây thể hiện tốt nhất cấp độ PCC?",
        "questionEn": f"According to the lens of {comp['compEn']}, which behavior best demonstrates PCC mastery?",
        "options": [
            {"key": "A", "textVi": "Đưa ra lời khuyên dựa trên kinh nghiệm thành công của chính coach.", "textEn": "Giving direct advice based on the coach's own successful experience."},
            {"key": "B", "textVi": "Đồng hành khám phá góc nhìn của khách hàng và tôn trọng quyền tự quyết định của họ.", "textEn": "Partnering to explore the client's perspective and honoring their autonomy to choose."},
            {"key": "C", "textVi": "Chuyển buổi coaching thành buổi đào tạo kỹ năng ngắn hạn.", "textEn": "Switching the coaching session into a short skills training tutorial."},
            {"key": "D", "textVi": "Yêu cầu khách hàng thực hiện đúng bài tập do coach chỉ định.", "textEn": "Mandating the client to execute specific assignments determined by the coach."}
        ],
        "correctAnswer": "B",
        "explanationVi": f"Ở cấp độ PCC, coach duy trì tính đồng hành bình đẳng (Partnership) và khơi gợi nhận thức thay vì áp đặt giải pháp. {comp['cueVi']}",
        "explanationEn": f"At the PCC level, the coach maintains equal partnership and evokes awareness rather than prescribing solutions. {comp['cueEn']}",
        "orderIndex": 1
    })

# Master dataset assembly
mentor_data = {
    "sections": sections,
    "competencies": competencies,
    "theories": theories,
    "keywords": keywords,
    "flashcards": flashcards,
    "caseStudies": case_studies,
    "quizzes": quizzes,
    "practiceQuestions": practice_questions,
    "mindfulnessMessages": mindfulness_messages,
    "stickers": stickers,
    "systemSettings": system_settings,
    "discountCodes": discount_codes
}

os.makedirs(OUT_DIR, exist_ok=True)
with open(OUT_PATH, 'w', encoding='utf-8') as f:
    json.dump(mentor_data, f, ensure_ascii=False, indent=2)

print(f"Exported complete mentor_data.json successfully to {OUT_PATH}!")
print(f"Sections: {len(sections)}, Competencies: {len(competencies)}, SJT Questions: {len(practice_questions)}")
print(f"Theories: {len(theories)}, Flashcards: {len(flashcards)}, Case Studies: {len(case_studies)}, Quizzes: {len(quizzes)}")
