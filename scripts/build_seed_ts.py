import json

with open('src/lib/parsedData.json', 'r', encoding='utf-8') as f:
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
        "svgContent": '<svg viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="54" fill="#F0EAE1" stroke="#8BA888" stroke-width="2"/><circle cx="60" cy="46" r="22" fill="#FDEBD0"/><path d="M52 44C52 44 56 47 60 47C64 47 68 44 68 44" stroke="#2F3A32" stroke-width="2.5" stroke-linecap="round"/><circle cx="50" cy="48" r="3" fill="#E8A0B4" opacity="0.6"/><circle cx="70" cy="48" r="3" fill="#E8A0B4" opacity="0.6"/><path d="M56 53C56 53 58 56 60 56C62 56 64 53 64 53" stroke="#2F3A32" stroke-width="2" stroke-linecap="round"/><path d="M38 72C38 68 46 64 60 64C74 64 82 68 82 72L86 98C86 100 78 102 60 102C42 102 34 100 34 98L38 72Z" fill="#D9A441"/><path d="M54 74C54 74 60 70 66 74" stroke="#4F6F52" stroke-width="2" stroke-linecap="round"/></svg>',
        "isActive": True
    },
    {
        "id": "stk-02",
        "code": "lotus_blooming",
        "nameVi": "Đóa sen nở rộ",
        "nameEn": "Blooming Lotus",
        "category": "lotus",
        "triggerEvent": "lesson_complete",
        "svgContent": '<svg viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="54" fill="#F6D6DF" fill-opacity="0.5" stroke="#E8A0B4" stroke-width="2"/><ellipse cx="60" cy="85" rx="35" ry="8" fill="#8BA888" opacity="0.4"/><path d="M60 30C52 46 44 64 60 78C76 64 68 46 60 30Z" fill="#E8A0B4"/><path d="M46 45C34 56 36 70 54 78C46 66 42 54 46 45Z" fill="#F6D6DF"/><path d="M74 45C86 56 84 70 66 78C74 66 78 54 74 45Z" fill="#F6D6DF"/><circle cx="60" cy="65" r="4" fill="#D9A441"/></svg>',
        "isActive": True
    },
    {
        "id": "stk-03",
        "code": "cat_zen",
        "nameVi": "Mèo thiền an nhiên",
        "nameEn": "Mindful Zen Cat",
        "category": "cat",
        "triggerEvent": "quiz_streak",
        "svgContent": '<svg viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="54" fill="#FAF7F2" stroke="#8BA888" stroke-width="2"/><path d="M42 42L48 56L36 56Z" fill="#D9A441"/><path d="M78 42L72 56L84 56Z" fill="#D9A441"/><circle cx="60" cy="62" r="26" fill="#FDEBD0"/><path d="M48 60C48 60 52 58 56 60" stroke="#2F3A32" stroke-width="2" stroke-linecap="round"/><path d="M64 60C64 60 68 58 72 60" stroke="#2F3A32" stroke-width="2" stroke-linecap="round"/><path d="M57 67C57 67 60 69 63 67" stroke="#E8A0B4" stroke-width="2" stroke-linecap="round"/><path d="M36 64L24 62M36 68L22 70" stroke="#8BA888" stroke-width="1.5"/><path d="M84 64L96 62M84 68L98 70" stroke="#8BA888" stroke-width="1.5"/></svg>',
        "isActive": True
    },
    {
        "id": "stk-04",
        "code": "lotus_comfort",
        "nameVi": "Mầm sen vỗ về",
        "nameEn": "Comforting Sprout",
        "category": "nature",
        "triggerEvent": "comfort_mistake",
        "svgContent": '<svg viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="54" fill="#F7F3EA" stroke="#4F6F52" stroke-width="2"/><path d="M60 88V50" stroke="#4F6F52" stroke-width="4" stroke-linecap="round"/><path d="M60 60C50 48 34 50 34 60C34 70 50 70 60 60Z" fill="#8BA888"/><path d="M60 50C70 38 86 40 86 50C86 60 70 60 60 50Z" fill="#8BA888"/><circle cx="60" cy="38" r="6" fill="#E8A0B4"/></svg>',
        "isActive": True
    },
    {
        "id": "stk-05",
        "code": "streak_3days",
        "nameVi": "3 Ngày Tinh Tấn",
        "nameEn": "3-Day Diligence",
        "category": "badge",
        "triggerEvent": "streak_milestone",
        "svgContent": '<svg viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="54" fill="#FAF7F2" stroke="#D9A441" stroke-width="3"/><circle cx="60" cy="60" r="42" fill="#F0EAE1"/><text x="60" y="58" font-family="serif" font-size="28" font-weight="bold" fill="#D9A441" text-anchor="middle">3</text><text x="60" y="78" font-family="sans-serif" font-size="12" fill="#4F6F52" text-anchor="middle">NGÀY THIỀN</text></svg>',
        "isActive": True
    },
    {
        "id": "stk-06",
        "code": "streak_7days",
        "nameVi": "7 Ngày Chánh Niệm",
        "nameEn": "7-Day Mindfulness",
        "category": "badge",
        "triggerEvent": "streak_milestone",
        "svgContent": '<svg viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="54" fill="#FAF7F2" stroke="#4F6F52" stroke-width="3"/><circle cx="60" cy="60" r="42" fill="#F6D6DF" fill-opacity="0.4"/><text x="60" y="58" font-family="serif" font-size="28" font-weight="bold" fill="#4F6F52" text-anchor="middle">7</text><text x="60" y="78" font-family="sans-serif" font-size="12" fill="#E8A0B4" text-anchor="middle">CHÁNH NIỆM</text></svg>',
        "isActive": True
    },
    {
        "id": "stk-07",
        "code": "streak_30days",
        "nameVi": "30 Ngày Vững Chãi",
        "nameEn": "30-Day Steadfast",
        "category": "badge",
        "triggerEvent": "streak_milestone",
        "svgContent": '<svg viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="54" fill="#FAF7F2" stroke="#D9A441" stroke-width="4"/><polygon points="60,20 72,45 100,45 78,62 86,88 60,72 34,88 42,62 20,45 48,45" fill="#D9A441" opacity="0.2"/><text x="60" y="58" font-family="serif" font-size="26" font-weight="bold" fill="#6B4F3A" text-anchor="middle">30</text><text x="60" y="78" font-family="sans-serif" font-size="11" font-weight="bold" fill="#4F6F52" text-anchor="middle">VỮNG CHÃI</text></svg>',
        "isActive": True
    },
    {
        "id": "stk-08",
        "code": "mountain_master",
        "nameVi": "Đỉnh Núi Tự Tin",
        "nameEn": "Mountain Mastery",
        "category": "badge",
        "triggerEvent": "exam_high_score",
        "svgContent": '<svg viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="54" fill="#F0EAE1" stroke="#4F6F52" stroke-width="2"/><circle cx="60" cy="38" r="14" fill="#D9A441" opacity="0.4"/><polygon points="60,35 25,95 95,95" fill="#4F6F52"/><polygon points="60,35 50,52 65,56" fill="#FAF7F2"/><polygon points="75,55 52,95 98,95" fill="#3A533D"/></svg>',
        "isActive": True
    },
    {
        "id": "stk-09",
        "code": "tea_cup",
        "nameVi": "Tách trà thảnh thơi",
        "nameEn": "Mindful Teacup",
        "category": "nature",
        "triggerEvent": "renewal_gentle",
        "svgContent": '<svg viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="54" fill="#FAF7F2" stroke="#8BA888" stroke-width="2"/><path d="M35 60C35 76 46 88 60 88C74 88 85 76 85 60L35 60Z" fill="#6B4F3A"/><path d="M85 66C92 66 96 70 96 74C96 78 90 82 85 82" stroke="#6B4F3A" stroke-width="3" stroke-linecap="round"/><ellipse cx="60" cy="60" rx="25" ry="6" fill="#8BA888"/><path d="M54 50C54 44 58 40 58 34" stroke="#8BA888" stroke-width="2" stroke-linecap="round" opacity="0.6"/><path d="M66 50C66 44 62 40 62 34" stroke="#8BA888" stroke-width="2" stroke-linecap="round" opacity="0.6"/></svg>',
        "isActive": True
    },
    {
        "id": "stk-10",
        "code": "bamboo_listening",
        "nameVi": "Lá trúc lắng nghe",
        "nameEn": "Bamboo Listening",
        "category": "nature",
        "triggerEvent": "lesson_complete",
        "svgContent": '<svg viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="54" fill="#F0EAE1" stroke="#8BA888" stroke-width="2"/><line x1="60" y1="20" x2="60" y2="100" stroke="#4F6F52" stroke-width="4"/><line x1="56" y1="50" x2="64" y2="50" stroke="#3A533D" stroke-width="3"/><path d="M60 50C75 45 88 52 92 60C85 65 70 60 60 50Z" fill="#8BA888"/><path d="M60 70C45 65 32 72 28 80C35 85 50 80 60 70Z" fill="#8BA888"/></svg>',
        "isActive": True
    },
    {
        "id": "stk-11",
        "code": "enso_circle",
        "nameVi": "Vòng tròn Enso",
        "nameEn": "Enso Circle",
        "category": "badge",
        "triggerEvent": "welcome",
        "svgContent": '<svg viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="54" fill="#F7F3EA" stroke="#E2D9CC" stroke-width="2"/><path d="M60 22C38 22 24 38 24 60C24 82 40 98 62 98C82 98 96 82 96 62C96 46 86 32 72 26" stroke="#2F3A32" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" opacity="0.85"/></svg>',
        "isActive": True
    },
    {
        "id": "stk-12",
        "code": "sparrow_zen",
        "nameVi": "Chim sẻ tự tại",
        "nameEn": "Free Sparrow",
        "category": "nature",
        "triggerEvent": "welcome",
        "svgContent": '<svg viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="54" fill="#FAF7F2" stroke="#8BA888" stroke-width="2"/><path d="M40 70C40 60 50 50 65 50C80 50 90 60 85 75C80 85 65 85 50 82L35 88L40 70Z" fill="#6B4F3A"/><circle cx="74" cy="58" r="3" fill="#2F3A32"/><polygon points="85,60 96,62 85,66" fill="#D9A441"/></svg>',
        "isActive": True
    }
]

# System Settings with Bank & VietQR info
system_settings = {
    "bankName": "Vietcombank (Ngân hàng TMCP Ngoại Thương Việt Nam)",
    "accountNumber": "9988776655",
    "accountHolder": "VI VIEN KHAI VAN ZEN PCC",
    "bankBin": "970436", # Vietcombank BIN
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

# Demo users
demo_users = [
    {
        "id": "usr-admin",
        "email": "admin@pcc.vn",
        "fullName": "Super Admin Tâm An",
        "role": "super_admin",
        "tier": "12_months",
        "tierExpiresAt": "2027-12-31T23:59:59Z",
        "streakCount": 28,
        "lastActiveDate": "2026-11-03",
        "selectedStickerPack": "monk_welcome",
        "minimalMode": False,
        "soundEnabled": True
    },
    {
        "id": "usr-editor",
        "email": "editor@pcc.vn",
        "fullName": "Biên Tập Viên Tuệ Minh",
        "role": "editor",
        "tier": "12_months",
        "tierExpiresAt": "2027-12-31T23:59:59Z",
        "streakCount": 14,
        "lastActiveDate": "2026-11-03",
        "selectedStickerPack": "lotus_blooming",
        "minimalMode": False,
        "soundEnabled": True
    },
    {
        "id": "usr-billing",
        "email": "billing@pcc.vn",
        "fullName": "Thu Ngân Diệu Thiện",
        "role": "billing",
        "tier": "12_months",
        "tierExpiresAt": "2027-12-31T23:59:59Z",
        "streakCount": 7,
        "lastActiveDate": "2026-11-03",
        "selectedStickerPack": "cat_zen",
        "minimalMode": False,
        "soundEnabled": True
    },
    {
        "id": "usr-free",
        "email": "student.free@pcc.vn",
        "fullName": "Học Viên Minh Đức (Gói Free)",
        "role": "student",
        "tier": "free",
        "tierExpiresAt": None,
        "streakCount": 3,
        "lastActiveDate": "2026-11-03",
        "selectedStickerPack": "sprout_seed",
        "minimalMode": False,
        "soundEnabled": True
    },
    {
        "id": "usr-1m",
        "email": "student.1m@pcc.vn",
        "fullName": "Học Viên Thu Hương (Gói 1 Tháng)",
        "role": "student",
        "tier": "1_month",
        "tierExpiresAt": "2026-11-30T23:59:59Z",
        "streakCount": 9,
        "lastActiveDate": "2026-11-03",
        "selectedStickerPack": "streak_7days",
        "minimalMode": False,
        "soundEnabled": True
    },
    {
        "id": "usr-6m",
        "email": "student.6m@pcc.vn",
        "fullName": "Học Viên Bảo Nam (Gói 6 Tháng)",
        "role": "student",
        "tier": "6_months",
        "tierExpiresAt": "2027-04-30T23:59:59Z",
        "streakCount": 18,
        "lastActiveDate": "2026-11-03",
        "selectedStickerPack": "lotus_blooming",
        "minimalMode": False,
        "soundEnabled": True
    },
    {
        "id": "usr-12m",
        "email": "student.12m@pcc.vn",
        "fullName": "Học Viên Trọng Nghĩa (Gói 12 Tháng)",
        "role": "student",
        "tier": "12_months",
        "tierExpiresAt": "2027-10-31T23:59:59Z",
        "streakCount": 45,
        "lastActiveDate": "2026-11-03",
        "selectedStickerPack": "streak_30days",
        "minimalMode": False,
        "soundEnabled": True
    }
]

# Generate detailed 6-tab content for leaf sections
theories = []
keywords = []
flashcards = []
case_studies = []
quizzes = []

# Map leaf sections
leaf_sections = ['sec-a1-1', 'sec-a1-2', 'sec-a2', 'sec-b1', 'sec-b2', 'sec-c1', 'sec-c2', 'sec-d1', 'sec-d2']

for idx, sec_id in enumerate(leaf_sections):
    # Find matching competency
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

#### Đối Chiếu Sơ Đồ Tư Duy (Mindmap):
Học viên có thể tham khảo trực tiếp sơ đồ tư duy năng lực tại file đính kèm: `ICF Core Competencies - Mindmap VN.pdf` trong tài liệu học viên.
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

#### Mindmap Reference:
Students can cross-reference the visual hierarchy in `ICF Core Competencies - Mindmap EN.pdf`.
""",
        "videoUrl": "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
        "attachments": [
            {"nameVi": "Sơ đồ tư duy Năng lực ICF (Tiếng Việt)", "nameEn": "ICF Competencies Mindmap (VN)", "url": "/docs/mindmap-vn.pdf", "type": "pdf"},
            {"nameVi": "Bản đối chiếu chuẩn PCC Markers 2025", "nameEn": "PCC Markers 2025 Matrix", "url": "/docs/pcc-markers.pdf", "type": "pdf"}
        ],
        "isFree": (sec_id == 'sec-a1-1')
    })

    # 2. Keywords (Mẹo ghi nhớ + Tổng quát)
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
        "audioTermEnUrl": None,
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
        "audioTermEnUrl": None,
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
        "titleVi": f"Tình Huống Thực Tế: Xử Lý Ranh Giới & Thấu Cảm trong {comp['compVi']}",
        "titleEn": f"Practical Scenario: Navigating Boundaries & Empathy in {comp['compEn']}",
        "scenarioDialogueVi": f"""**Bối cảnh:** Trong phiên khai vấn thứ 3, khách hàng (Giám đốc dự án) chia sẻ với vẻ mệt mỏi cùng cực:
- **Khách hàng:** “Tôi cảm thấy bế tắc hoàn toàn. Cả team đều chống lại tôi, ban giám đốc thì ép tiến độ. Tôi không ngủ được suốt 2 tuần qua và không biết mình có thể trụ thêm được bao lâu nữa...”
- **Coach lắng nghe trong tĩnh lặng và nhận thấy nhịp thở dồn dập của khách hàng.**
""",
        "scenarioDialogueEn": f"""**Context:** During session 3, the client (a project director) shares with visible exhaustion:
- **Client:** "I feel utterly stuck. The team resists my decisions, and executive leadership demands aggressive deadlines. I haven't slept properly for 2 weeks and don't know how much longer I can hold on..."
- **The coach observes with stillness, noticing the client's shallow breathing.**
""",
        "analysisQuestionsVi": f"1. Coach nên phản hồi như thế nào để vừa duy trì sự an toàn tâm lý (Năng lực 4), vừa tôn trọng ranh giới đạo đức và thẩm định nguy cơ?\n2. Đâu là hành vi vi phạm chuẩn mực PCC Markers nếu coach vội vàng can thiệp?",
        "analysisQuestionsEn": f"1. How should the coach respond to maintain psychological safety while honoring ethical scope and evaluating potential referral needs?\n2. What action would violate PCC markers if the coach rushes to advise?",
        "suggestedAnswersVi": f"""**Đáp án phân tích gợi ý:**
- **Hành động phù hợp chuẩn PCC (BEST):** Coach thừa nhận cảm xúc và sự quá tải của khách hàng một cách chân thành, hiện diện trọn vẹn mà không vội vàng tìm giải pháp khắc phục. Sau đó kiểm tra mức độ an toàn sức khỏe và hỏi khách hàng muốn dành phiên này để chăm sóc bản thân hay cần tìm kiếm sự hỗ trợ chuyên môn y tế.
- **Hành động vi phạm (WORST):** Coach tự đưa ra lời khuyên về phương pháp quản lý căng thẳng hoặc cam đoan hứa hẹn mọi chuyện sẽ ổn, vượt quá phạm vi thẩm quyền của một Coach chuyên nghiệp.""",
        "suggestedAnswersEn": f"""**Suggested Analysis:**
- **PCC-Aligned Behavior (BEST):** Coach warmly acknowledges the client's felt distress and emotional weight without rushing to troubleshoot. Then gently explores what support the client needs right now, including checking whether professional medical/therapy support is needed.
- **PCC Violation (WORST):** Coach acts as an advice-giver offering remedies for insomnia or guarantees everything will be fine, breaching professional boundaries.""",
        "competencyMapping": f"ICF Core Competency: {comp['compEn']} & Ethics Standard 1",
        "pccMarkers": ["Marker 4.1: Acknowledges client expressions", "Marker 5.1: Remains fully present and grounded", "Marker 1.2: Adheres to ethical boundary referral"],
        "orderIndex": 1
    })

    # 5. Quiz
    quizzes.append({
        "id": f"qz-{sec_id}-1",
        "sectionId": sec_id,
        "type": "standard_mcq",
        "questionVi": f"Khi đánh giá câu hỏi thi về năng lực '{comp['compVi']}', dấu hiệu nào sau đây chỉ ra hành vi của coach đạt chuẩn cấp độ PCC?",
        "questionEn": f"When assessing questions on '{comp['compEn']}', which behavior indicates PCC-level mastery?",
        "options": [
            {"key": "A", "textVi": "Coach chủ động gợi ý sẵn các giải pháp để tiết kiệm thời gian cho khách hàng.", "textEn": "The coach proactively suggests solutions to save client time."},
            {"key": "B", "textVi": "Coach tôn trọng quyền tự quyết của khách hàng và cùng xác nhận lại hướng đi của phiên.", "textEn": "The coach honors client autonomy and partners to reconfirm session direction."},
            {"key": "C", "textVi": "Coach tập trung phân tích nguồn gốc sai lầm trong quá khứ của khách hàng.", "textEn": "The coach focuses on dissecting past mistakes of the client."},
            {"key": "D", "textVi": "Coach chia sẻ kinh nghiệm thành công của chính mình để khách hàng noi theo.", "textEn": "The coach shares personal success stories for the client to follow."}
        ],
        "correctAnswer": "B",
        "explanationVi": f"Theo chuẩn ICF PCC, coach luôn giữ vai trò đồng hành bình đẳng (Partnering), không chọn giải pháp hay áp đặt agenda lên khách hàng. Quy tắc nhanh: '{comp['cueVi']}'.",
        "explanationEn": f"Under ICF PCC standards, the coach maintains an equal partnership and never imposes an agenda or fixes solutions. Fast rule: '{comp['cueEn']}'.",
        "primaryCompetency": comp['compEn'],
        "keyClueVi": "Tôn trọng quyền tự quyết và đồng hành bình đẳng",
        "keyClueEn": "Honoring client autonomy and equal partnership",
        "difficulty": "medium",
        "orderIndex": 1
    })

# Now assemble full seedData.ts file
ts_content = f"""// AUTO-GENERATED AUTHENTIC ICF PCC SEED DATA
import {{
  Section,
  Theory,
  Keyword,
  Flashcard,
  CaseStudy,
  QuizQuestion,
  MindfulnessMessage,
  Sticker,
  SystemSettings,
  UserProfile,
  Order
}} from "@/types";

export const SEED_SECTIONS: Section[] = {json.dumps(sections, ensure_ascii=False, indent=2)};

export const SEED_THEORIES: Theory[] = {json.dumps(theories, ensure_ascii=False, indent=2)};

export const SEED_KEYWORDS: Keyword[] = {json.dumps(keywords, ensure_ascii=False, indent=2)};

export const SEED_FLASHCARDS: Flashcard[] = {json.dumps(flashcards, ensure_ascii=False, indent=2)};

export const SEED_CASE_STUDIES: CaseStudy[] = {json.dumps(case_studies, ensure_ascii=False, indent=2)};

export const SEED_QUIZZES: QuizQuestion[] = {json.dumps(quizzes, ensure_ascii=False, indent=2)};

export const SEED_FULL_MOCK_EXAM: QuizQuestion[] = {json.dumps(practice_questions, ensure_ascii=False, indent=2)};

export const SEED_MINDFULNESS_MESSAGES: MindfulnessMessage[] = {json.dumps(mindfulness_messages, ensure_ascii=False, indent=2)};

export const SEED_STICKERS: Sticker[] = {json.dumps(stickers, ensure_ascii=False, indent=2)};

export const SEED_SYSTEM_SETTINGS: SystemSettings = {json.dumps(system_settings, ensure_ascii=False, indent=2)};

export const SEED_USERS: UserProfile[] = {json.dumps(demo_users, ensure_ascii=False, indent=2)};

export const SEED_DISCOUNT_CODES = {json.dumps(discount_codes, ensure_ascii=False, indent=2)};

export const SEED_ORDERS: Order[] = [
  {{
    id: "ord-demo-01",
    userId: "usr-1m",
    orderCode: "PCC-1001-A89",
    tierId: "1_month",
    amount: 299000,
    status: "approved",
    receiptUrl: "/receipts/receipt-demo-1.png",
    approvedBy: "usr-billing",
    approvedAt: "2026-11-01T10:30:00Z",
    createdAt: "2026-11-01T10:15:00Z",
    updatedAt: "2026-11-01T10:30:00Z"
  }},
  {{
    id: "ord-demo-02",
    userId: "usr-6m",
    orderCode: "PCC-1002-B72",
    tierId: "6_months",
    amount: 1190000,
    status: "approved",
    receiptUrl: "/receipts/receipt-demo-2.png",
    approvedBy: "usr-billing",
    approvedAt: "2026-10-31T15:20:00Z",
    createdAt: "2026-10-31T15:00:00Z",
    updatedAt: "2026-10-31T15:20:00Z"
  }},
  {{
    id: "ord-demo-03",
    userId: "usr-free",
    orderCode: "PCC-1003-C34",
    tierId: "6_months",
    amount: 1190000,
    status: "pending_approval",
    receiptUrl: "/receipts/receipt-demo-3.png",
    createdAt: "2026-11-03T14:30:00Z",
    updatedAt: "2026-11-03T14:30:00Z"
  }}
];
"""

with open('src/lib/seedData.ts', 'w', encoding='utf-8') as f:
    f.write(ts_content)

print("Generated src/lib/seedData.ts successfully!")
