# -*- coding: utf-8 -*-
"""
Helper module defining 9 Case Studies, 90 Flashcards, 90 Quizzes, and 50 SJT questions.
"""

# 1. 9 Tailored Case Studies (Zero coach projection, pure ICF PCC compliance)
CASE_STUDIES = [
    {
        "id": "cs-sec-a1-1",
        "sectionId": "sec-a1-1",
        "titleVi": "Tình huống: Ranh giới bảo mật với Nhà tài trợ (Sponsor) & Khách hàng",
        "titleEn": "Case Study: Confidentiality Boundaries with Sponsor & Client",
        "scenarioVi": "Khách hàng là Phó Tổng Giám đốc tham gia chương trình khai vấn do Tổng Giám đốc (Sponsor) chi trả. Khách hàng ngập ngừng chia sẻ vì lo ngại Coach sẽ báo cáo lại nội dung nhạy cảm cho Sponsor.",
        "scenarioEn": "The client is an Executive VP in a corporate coaching engagement paid by the CEO (Sponsor). The client hesitates to share due to concerns that sensitive disclosures might be reported back to the Sponsor.",
        "dialogue": [
            {
                "speaker": "Khách hàng",
                "textVi": "Tôi rất muốn cởi mở, nhưng trong hợp đồng tài trợ tôi thấy có điều khoản báo cáo định kỳ. Tôi lo rằng những bất đồng của tôi với ban điều hành sẽ bị tiết lộ.",
                "textEn": "I want to be transparent, but the sponsorship agreement mentions periodic progress updates. I worry my disagreements with executive leadership might be disclosed.",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Tôi ghi nhận sự băn khoăn rất thực tế của bạn về tính bảo mật. Theo chuẩn đạo đức ICF và thỏa thuận 3 bên, mọi nội dung thảo luận trong không gian này là bảo mật tuyệt đối, chỉ có tiến độ mục tiêu tổng quát do chính bạn đồng ý mới được báo cáo. Điều gì sẽ giúp bạn cảm thấy hoàn toàn an tâm trong phiên hôm nay?",
                "textEn": "I appreciate your candid concern regarding confidentiality. Under ICF ethics and our three-party agreement, everything discussed here is strictly confidential; only high-level progress approved by you is shared. What would support you in feeling completely safe in today's session?",
                "markerTag": "PCC Marker 1.1 & 3.1"
            },
            {
                "speaker": "Khách hàng",
                "textVi": "Nghe Coach khẳng định như vậy thì tôi yên tâm hơn nhiều. Vấn đề thực sự là tôi đang mất niềm tin vào chiến lược hiện tại của tổ chức.",
                "textEn": "Hearing you affirm that brings immense relief. The real issue is that I am losing conviction in our organization's current strategic direction.",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Cảm ơn bạn đã tin tưởng chia sẻ. Khi nhìn vào việc 'mất niềm tin vào chiến lược', điều gì là quan trọng nhất bạn muốn chúng ta cùng làm việc trong phiên này?",
                "textEn": "Thank you for trusting the space. Looking at 'losing conviction in the strategy', what is most essential for us to focus on in today's conversation?",
                "markerTag": "PCC Marker 3.2 & 3.3"
            }
        ],
        "reflectionQuestionsVi": [
            "Tại sao Coach cần tái khẳng định ranh giới bảo mật trước khi đi vào nội dung?",
            "Làm thế nào Coach giữ được tính trung lập giữa quyền lợi của Sponsor và quyền riêng tư của Khách hàng?",
            "Coach đã dùng chính ngôn từ nào của Khách hàng để mời họ thiết lập mục tiêu phiên?"
        ],
        "reflectionQuestionsEn": [
            "Why must the Coach re-affirm confidentiality boundaries before delving into the topic?",
            "How does the Coach maintain neutrality between Sponsor expectations and Client privacy?",
            "What exact words of the Client did the Coach mirror to establish the session agreement?"
        ],
        "pccMarkerRef": "ICF Competency 1 (Ethical Practice) / Ethics 3.1–3.4 & PCC Marker 3.1–3.3",
        "orderIndex": 1
    },
    {
        "id": "cs-sec-a1-2",
        "sectionId": "sec-a1-2",
        "titleVi": "Tình huống: Nhận diện ranh giới Khai vấn và Chuyển gửi Chuyên gia Trị liệu",
        "titleEn": "Case Study: Scope of Practice and Referral to Mental Health Specialists",
        "scenarioVi": "Khách hàng chia sẻ dấu hiệu kiệt sức kéo dài, mất ngủ trầm trọng và cảm giác tuyệt vọng vô cớ trong nhiều tuần qua, hỏi Coach về phương pháp trị liệu.",
        "scenarioEn": "The client shares symptoms of prolonged burnout, severe insomnia, and persistent despair over several weeks, asking the Coach for therapeutic remedies.",
        "dialogue": [
            {
                "speaker": "Khách hàng",
                "textVi": "Dạo gần đây tôi không thể ngủ nổi, người lúc nào cũng kiệt quệ và có những ngày tôi thấy cuộc sống vô nghĩa. Coach có liệu pháp nào giúp tôi chữa trị chứng này không?",
                "textEn": "Lately I cannot sleep at all, feeling perpetually drained and finding life meaningless. Does coaching offer therapy techniques to cure this?",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Tôi trân trọng sự dũng cảm và thành thật của bạn khi nói ra những trải nghiệm này. Khai vấn tập trung vào tiềm năng phát triển và mục tiêu tương lai, không phải là liệu pháp y khoa hay trị liệu tâm lý. Khi lắng nghe những điều bạn vừa chia sẻ, bạn nghĩ sao về việc tìm kiếm thêm sự đồng hành từ một bác sĩ hoặc chuyên gia tâm lý chuyên sâu?",
                "textEn": "I deeply honor your courage in voicing these experiences. Coaching focuses on development and future goals; it is not clinical psychotherapy or medical treatment. Hearing your own reflections, what are your thoughts on seeking professional support from a licensed therapist or physician?",
                "markerTag": "PCC Marker 1.2 & Scope of Practice"
            },
            {
                "speaker": "Khách hàng",
                "textVi": "Tôi cũng từng nghĩ đến bác sĩ nhưng sợ bị người khác đánh giá. Nhưng có lẽ tôi thực sự cần được trợ giúp chuyên môn trước.",
                "textEn": "I considered a therapist but worried about stigma. Yet, perhaps I genuinely need clinical support first.",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Sức khỏe và sự an lành của bạn là ưu tiên cao nhất. Bạn muốn chúng ta sắp xếp tiến trình khai vấn này như thế nào trong lúc bạn tìm kiếm sự hỗ trợ chuyên môn?",
                "textEn": "Your well-being is the ultimate priority. How would you like us to pace our coaching partnership while you explore specialized medical support?",
                "markerTag": "PCC Marker 1.2 & Partnership"
            }
        ],
        "reflectionQuestionsVi": [
            "Dấu hiệu nào trong lời nói của khách hàng báo hiệu cần chuyển gửi chuyên gia?",
            "Coach đã từ chối vai trò trị liệu như thế nào mà vẫn giữ được sự thấu cảm và tôn trọng khách hàng?",
            "Tại sao việc cố tiếp tục phiên coaching khi khách hàng đang trầm cảm nặng là vi phạm đạo đức?"
        ],
        "reflectionQuestionsEn": [
            "What indicators in the client's words signal an imperative need for specialist referral?",
            "How did the Coach decline therapy while maintaining deep empathy and psychological safety?",
            "Why is pushing forward with coaching during severe clinical depression an ethical breach?"
        ],
        "pccMarkerRef": "ICF Competency 1 / Ethics Standard 1.2 & Scope of Practice",
        "orderIndex": 2
    },
    {
        "id": "cs-sec-a2",
        "sectionId": "sec-a2",
        "titleVi": "Tình huống: Nuôi dưỡng Tư duy Khai vấn & Quản trị Định kiến Cá nhân",
        "titleEn": "Case Study: Embodying a Coaching Mindset & Suspending Assumptions",
        "scenarioVi": "Khách hàng là lãnh đạo cấp cao gặp bất đồng gay gắt với đối tác quốc tế có văn hóa giao tiếp gián tiếp, liên tục hỏi xin lời khuyên của Coach.",
        "scenarioEn": "The client is a senior executive in conflict with an overseas partner who uses an indirect communication style, repeatedly pressing the Coach for operational advice.",
        "dialogue": [
            {
                "speaker": "Khách hàng",
                "textVi": "Họ làm việc quá vòng vo và không bao giờ nói thẳng vào vấn đề! Coach từng làm việc ở tập đoàn đa quốc gia rồi, Coach hãy nói cho tôi biết tôi nên dùng chiến thuật gì để ép họ ra quyết định?",
                "textEn": "They are so ambiguous and never get straight to the point! You navigated multinational corporations before; tell me what tactic I should use to force a decision?",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Tôi nghe thấy sự sốt ruột và mong muốn sớm có kết quả rõ ràng trong dự án này. Với tư cách là Coach, tôi ở đây để đồng hành giúp bạn tìm ra chiến lược phù hợp nhất với phong cách của bạn thay vì đưa ra lời khuyên từ góc nhìn cá nhân của tôi. Khi bạn quan sát cách giao tiếp của đối tác, điều gì đang là rào cản lớn nhất đối với bạn?",
                "textEn": "I hear your urgency and intense desire for clarity. As your Coach, my role is to partner with you to discover the strategy authentic to your leadership, rather than imposing advice from my own experience. As you observe their communication, what stands out as the primary barrier for you?",
                "markerTag": "PCC Marker 2.1 & 3.2"
            },
            {
                "speaker": "Khách hàng",
                "textVi": "Rào cản là tôi luôn cho rằng sự im lặng hoặc chậm chạp của họ là thiếu tôn trọng. Nhưng có thể họ cần sự đồng thuận nội bộ trước.",
                "textEn": "The barrier is my assumption that their silence means disrespect. Yet perhaps they require collective internal consensus first.",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Một góc nhìn mới vừa mở ra. Nếu tiếp cận từ nhận định 'họ cần sự đồng thuận nội bộ', bạn thấy mình có thêm những lựa chọn hành động nào?",
                "textEn": "A fresh perspective just emerged. If you operate from the lens of 'they need internal consensus', what new options become visible to you?",
                "markerTag": "PCC Marker 7.2 & 8.1"
            }
        ],
        "reflectionQuestionsVi": [
            "Tại sao Coach từ chối đưa ra lời khuyên dù bản thân từng có kinh nghiệm trong lĩnh vực đó?",
            "Làm thế nào Coach giúp khách hàng tự nhận diện định kiến của chính họ về 'sự chậm chạp'?",
            "Hành vi nào thể hiện tư duy cởi mở, tò mò (Curious Mindset) của Coach?"
        ],
        "reflectionQuestionsEn": [
            "Why does the Coach withhold advice even when possessing direct corporate background in the matter?",
            "How does the Coach invite the client to inspect their own underlying assumption regarding 'slowness'?",
            "Which behavior demonstrates the Coach's open, flexible, and curious mindset?"
        ],
        "pccMarkerRef": "ICF Competency 2 (Embodies a Coaching Mindset) / PCC Marker 2.1–2.4",
        "orderIndex": 3
    },
    {
        "id": "cs-sec-b1",
        "sectionId": "sec-b1",
        "titleVi": "Tình huống: Thiết lập Thỏa thuận Phiên Rõ ràng & Tiêu chí Đo lường Thành công",
        "titleEn": "Case Study: Clarifying Session Agreement & Measures of Success",
        "scenarioVi": "Khách hàng bước vào phiên với tâm trạng choáng ngợp và liệt kê cùng lúc 3 chủ đề lớn, Coach đồng hành để khách hàng tự chọn tiêu điểm.",
        "scenarioEn": "The client arrives overwhelmed and presents three substantial, competing issues. The Coach partners to clarify a single focus and clear success criteria.",
        "dialogue": [
            {
                "speaker": "Khách hàng",
                "textVi": "Hôm nay tôi thấy quá tải. Tôi vừa muốn xử lý mâu thuẫn với Giám đốc Tài chính, vừa muốn tái cấu trúc phòng ban, lại vừa băn khoăn về việc có nên nhận thêm dự án mới hay không.",
                "textEn": "I feel utterly overloaded today. I want to address friction with the CFO, restructure my department, and debate whether to accept a demanding new project.",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Bạn đang mang nhiều trọng trách lớn cùng một lúc. Để thời gian phiên hôm nay đem lại giá trị thiết thực nhất cho bạn, trong 3 chủ đề đó, chủ đề nào là tâm điểm bạn muốn chúng ta cùng làm việc?",
                "textEn": "You are carrying multiple significant priorities right now. To ensure our time today generates the most tangible value for you, which among these three is the focal point you choose to work on?",
                "markerTag": "PCC Marker 3.1 & 3.2"
            },
            {
                "speaker": "Khách hàng",
                "textVi": "Tôi nghĩ việc xử lý khúc mắc với Giám đốc Tài chính là gốc rễ. Nếu không giải quyết được điều này thì mọi kế hoạch tái cấu trúc đều tắc nghẽn.",
                "textEn": "Resolving friction with the CFO is the root. Unless that is addressed, any restructuring will stall.",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Chúng ta đã thống nhất tiêu điểm là khúc mắc với Giám đốc Tài chính. Khi phiên hôm nay kết thúc, điều cụ thể nào đạt được sẽ cho bạn biết rằng cuộc trò chuyện này thực sự thành công?",
                "textEn": "We have aligned on the friction with the CFO as our focus. When we conclude today's session, what specific outcome will signal that our conversation was genuinely successful?",
                "markerTag": "PCC Marker 3.3"
            }
        ],
        "reflectionQuestionsVi": [
            "Tại sao Coach không tự chọn chủ đề mà để khách hàng tự quyết định?",
            "Câu hỏi về 'tiêu chí đo lường thành công' (Measure of Success) giúp ích gì cho khách hàng?",
            "Làm thế nào Coach giữ cho phiên không bị chệch hướng khỏi thỏa thuận ban đầu?"
        ],
        "reflectionQuestionsEn": [
            "Why does the Coach refrain from prioritizing the topic and empower the client to choose?",
            "How does exploring the 'measure of success' anchor the session outcomes?",
            "How can the Coach ensure the session remains aligned with the established agreement?"
        ],
        "pccMarkerRef": "ICF Competency 3 (Establishes Agreements) / PCC Marker 3.1–3.4",
        "orderIndex": 4
    },
    {
        "id": "cs-sec-b2",
        "sectionId": "sec-b2",
        "titleVi": "Tình huống: Nuôi dưỡng Niềm tin & Không gian Tâm lý An toàn Tuyệt đối",
        "titleEn": "Case Study: Cultivating Deep Trust & Unconditional Psychological Safety",
        "scenarioVi": "Khách hàng ngập ngừng thổ lộ một thất bại đau đớn trong quá khứ mà họ chưa từng dám chia sẻ với bất kỳ ai vì nỗi sợ bị chê trách.",
        "scenarioEn": "The client hesitantly discloses a painful past mistake they had never dared share with anyone, paralyzed by fear of harsh judgment.",
        "dialogue": [
            {
                "speaker": "Khách hàng",
                "textVi": "Thực sự... có một sai sót cách đây 6 tháng khiến công ty mất một khách hàng lớn. Tôi chưa từng dám nói với ai trong ban giám đốc vì sợ họ nghĩ tôi yếu kém.",
                "textEn": "Truthfully... a mistake of mine six months ago cost our firm a major client. I never dared voice this to the board fearing they would deem me incompetent.",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "(Lắng nghe ấm áp, hiện diện trọn vẹn) Cảm ơn bạn rất nhiều vì đã tin tưởng và mở lòng chia sẻ điều này với tôi. Trong không gian này, bạn hoàn toàn được đón nhận trọn vẹn mà không có bất kỳ sự phán xét nào. Khi bạn nói ra điều này thành lời, cảm giác bên trong bạn lúc này thế nào?",
                "textEn": "(Warm attentive presence) Thank you deeply for your trust and courage in sharing this with me. In this space, you are met with unconditional acceptance and zero judgment. As you give voice to this, what are you experiencing internally right now?",
                "markerTag": "PCC Marker 4.1, 4.2 & 4.3"
            },
            {
                "speaker": "Khách hàng",
                "textVi": "Tôi thấy một tảng đá trong lòng như được nhấc ra. Tôi nhận ra bấy lâu nay năng lượng của tôi bị cạn kiệt chỉ vì cố che giấu sai lầm này.",
                "textEn": "A heavy stone feels lifted from my chest. I realize my energy has been drained simply trying to conceal this failure.",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Tôi ghi nhận sự dũng cảm và nhận thức sâu sắc đó ở bạn. Khi tảng đá đó đã được đặt xuống, bạn muốn chúng ta cùng khám phá điều gì tiếp theo cho chặng đường phía trước?",
                "textEn": "I honor that courage and profound insight in you. Now that the weight is lifted, what would you like us to explore next for your path forward?",
                "markerTag": "PCC Marker 4.4 & 8.1"
            }
        ],
        "reflectionQuestionsVi": [
            "Cách Coach đón nhận sự tổn thương (Vulnerability) của khách hàng ảnh hưởng thế nào đến niềm tin?",
            "Tại sao Coach không lập tức đưa ra lời khuyên sửa sai mà lại hỏi về cảm xúc hiện tại?",
            "Hành vi nào thể hiện sự tôn trọng bản sắc và con người toàn vẹn của khách hàng?"
        ],
        "reflectionQuestionsEn": [
            "How does the Coach's reception of client vulnerability deepen mutual trust?",
            "Why does the Coach refrain from problem-solving and instead inquire into current internal experience?",
            "Which behavior demonstrates honoring the whole personhood of the client?"
        ],
        "pccMarkerRef": "ICF Competency 4 (Cultivates Trust & Safety) / PCC Marker 4.1–4.4",
        "orderIndex": 5
    },
    {
        "id": "cs-sec-c1",
        "sectionId": "sec-c1",
        "titleVi": "Tình huống: Duy trì Sự Hiện diện Tĩnh lặng & Đón nhận Khoảng lặng Sâu",
        "titleEn": "Case Study: Maintaining Still Presence & Embracing Profound Silence",
        "scenarioVi": "Sau một câu hỏi gợi mở, khách hàng rơi vào trạng thái im lặng kéo dài hơn 15 giây. Coach giữ vững sự hiện diện tĩnh lặng, không ngắt lời hay thêm câu hỏi.",
        "scenarioEn": "Following an evocative inquiry, the client falls into a deep 15-second silence. The Coach holds quiet, centered space without interrupting or rushing.",
        "dialogue": [
            {
                "speaker": "Coach",
                "textVi": "Khi bạn nhìn vào khao khát được công nhận của mình, điều gì là sự thật mà bạn bấy lâu nay chưa dám nhìn thẳng vào?",
                "textEn": "Looking closely at your hunger for external validation, what is the underlying truth you have resisted confronting?",
                "markerTag": "PCC Marker 7.1"
            },
            {
                "speaker": "Khách hàng",
                "textVi": "Thực sự là... (Dừng lại, ánh mắt nhìn xa xăm, im lặng hoàn toàn suốt 15 giây)...",
                "textEn": "It really is... (Pauses, gazes reflectively, complete silence for 15 seconds)...",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "(Duy trì sự hiện diện tĩnh lặng, nhịp thở êm đềm, không ngắt lời, kiên nhẫn đợi khách hàng hoàn tất tiến trình suy tư)",
                "textEn": "(Maintains grounded presence, calm breath, patient silence, allowing internal integration to unfold)",
                "markerTag": "PCC Marker 5.4 (Holds Silence)"
            },
            {
                "speaker": "Khách hàng",
                "textVi": "Tôi vừa nhận ra... tôi luôn phấn đấu để chứng minh cho bố tôi thấy tôi có giá trị. Nhưng bố tôi đã mất 3 năm rồi. Tôi đang tiếp tục sống cuộc đời vì một sự chứng minh không còn cần thiết nữa.",
                "textEn": "I just realized... I have been striving endlessly to prove my worth to my father. Yet he passed away three years ago. I am living my life fighting for validation that is no longer needed.",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "(Thở nhẹ cùng khách hàng) Một khoảnh khắc thức tỉnh rất thiêng liêng. Bạn muốn dành thêm bao nhiêu không gian tĩnh lặng lúc này để đón nhận điều này?",
                "textEn": "(Gentle breath with client) That is a profoundly sacred breakthrough. How much stillness would you like right now to let this settle?",
                "markerTag": "PCC Marker 5.2 & 5.4"
            }
        ],
        "reflectionQuestionsVi": [
            "Nếu Coach sốt ruột và nói chen vào sau 5 giây im lặng, điều gì sẽ bị phá vỡ?",
            "Khoảng lặng (Silence) trong khai vấn cấp độ PCC đóng vai trò như thế nào?",
            "Làm sao Coach rèn luyện được khả năng tĩnh lặng mà không cảm thấy ngượng ngùng?"
        ],
        "reflectionQuestionsEn": [
            "If the Coach grew anxious and interrupted after 5 seconds, what would have been lost?",
            "What critical transformational role does Silence play in PCC-level mastery?",
            "How does a Coach cultivate comfortable stillness without anxiety or awkwardness?"
        ],
        "pccMarkerRef": "ICF Competency 5 (Maintains Presence) / PCC Marker 5.1–5.4",
        "orderIndex": 6
    },
    {
        "id": "cs-sec-c2",
        "sectionId": "sec-c2",
        "titleVi": "Tình huống: Lắng nghe Chủ động Cấp độ 3 — Phản chiếu Sự Bất nhất trong Ngôn từ & Năng lượng",
        "titleEn": "Case Study: Level 3 Active Listening — Reflecting Incongruence in Energy & Words",
        "scenarioVi": "Khách hàng nói bằng lời rằng mình rất hào hứng với vị trí mới, nhưng giọng nói chùng xuống, vai co lại và thở dài nặng nề.",
        "scenarioEn": "The client verbally states excitement regarding a new promotion, yet their vocal pitch drops, shoulders slump, and a heavy sigh escapes.",
        "dialogue": [
            {
                "speaker": "Khách hàng",
                "textVi": "Tôi vừa được thăng chức lên Tổng Giám đốc vùng. Đây là cơ hội tuyệt vời và tôi cảm thấy rất hào hứng... (thở dài, mắt nhìn xuống, giọng chùng xuống)",
                "textEn": "I was just promoted to Regional Managing Director. It is a fantastic opportunity and I feel very thrilled... (heavy sigh, downcast gaze, flattened tone)",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Bạn vừa dùng từ 'rất hào hứng', nhưng tôi nhận thấy một tiếng thở dài và năng lượng trong giọng nói của bạn có phần chùng xuống. Giữa từ 'hào hứng' và tiếng thở dài đó, điều gì đang thực sự diễn ra bên trong bạn?",
                "textEn": "You used the word 'thrilled', yet I noticed a heavy sigh and a distinct dip in your vocal energy. Between the word 'thrilled' and that sigh, what is genuinely happening inside you?",
                "markerTag": "PCC Marker 6.1 & 6.2"
            },
            {
                "speaker": "Khách hàng",
                "textVi": "Thực sự là tôi rất sợ... Trách nhiệm quá lớn và tôi sợ mình sẽ không còn thời gian cho con gái mới sinh.",
                "textEn": "Truthfully, I am terrified... The responsibility is massive, and I dread losing time with my newborn daughter.",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Cảm ơn bạn đã lắng nghe tiếng nói chân thực nhất của mình. Giữa trọng trách của cương vị Tổng Giám đốc vùng và sự hiện diện bên cạnh con gái, điều gì là giá trị cốt lõi bạn muốn gìn giữ?",
                "textEn": "Thank you for tuning into your truest voice. Between the mantle of Regional Director and being present for your daughter, what core value do you wish to honor?",
                "markerTag": "PCC Marker 6.3 & 7.1"
            }
        ],
        "reflectionQuestionsVi": [
            "Coach đã phản chiếu điều gì ngoài ngôn từ (Verbal) của khách hàng?",
            "Tại sao Coach không kết luận rằng khách hàng 'đang nói dối' mà chỉ phản ánh sự bất nhất?",
            "Làm thế nào việc nghe năng lượng (Level 3 Listening) giúp mở ra chủ đề cốt lõi thực sự?"
        ],
        "reflectionQuestionsEn": [
            "What non-verbal signals did the Coach reflect back to the client?",
            "Why did the Coach refrain from labeling dishonesty and simply mirror the energetic discrepancy?",
            "How does Level 3 energetic listening unearth the genuine underlying agenda?"
        ],
        "pccMarkerRef": "ICF Competency 6 (Listens Actively) / PCC Marker 6.1–6.4",
        "orderIndex": 7
    },
    {
        "id": "cs-sec-d1",
        "sectionId": "sec-d1",
        "titleVi": "Tình huống: Khơi gợi Nhận thức Sâu sắc Qua Ẩn dụ & Câu hỏi Khám phá 'Who'",
        "titleEn": "Case Study: Evoking Awareness Through Client Metaphor & Inquiring into 'Who'",
        "scenarioVi": "Khách hàng dùng ẩn dụ 'con sư tử bị nhốt trong lồng kính', Coach đồng hành khám phá ẩn dụ mà không gán ghép ý nghĩa cá nhân của Coach.",
        "scenarioEn": "The client introduces the metaphor of 'a lion trapped behind a glass cage'. The Coach partners to explore the imagery without imposing outside interpretations.",
        "dialogue": [
            {
                "speaker": "Khách hàng",
                "textVi": "Ở công ty hiện tại, tôi thấy mình như một con sư tử bị nhốt trong lồng kính. Người ta vẫn thấy tôi oai vệ, nhưng tôi chẳng thể gầm hay chạy được.",
                "textEn": "In my current firm, I feel like a lion locked inside a glass cage. People still see me as majestic, but I can neither roar nor run.",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Hình ảnh 'con sư tử trong lồng kính' rất giàu sức gợi. Khi con sư tử đó nhìn qua tấm kính, nó đang nhìn thấy điều gì ở thế giới bên ngoài?",
                "textEn": "The imagery of 'a lion behind a glass cage' is deeply evocative. Looking through that glass, what does that lion see in the world outside?",
                "markerTag": "PCC Marker 7.1 & 7.3"
            },
            {
                "speaker": "Khách hàng",
                "textVi": "Nó thấy cánh đồng thảo nguyên bao la... nơi nó thuộc về. Và chiếc lồng kính đó thực chất là do chính nó tự dựng lên vì sợ rủi ro tài chính.",
                "textEn": "It sees the vast open savannah... where it truly belongs. And that glass cage was actually self-built out of fear of financial insecurity.",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Khi nhận ra chiếc lồng do chính mình dựng lên, người lãnh đạo dũng cảm bên trong bạn muốn làm gì với tấm kính đó lúc này?",
                "textEn": "Recognizing that the cage was self-constructed, what does the courageous leader within you choose to do with that glass right now?",
                "markerTag": "PCC Marker 7.2 & 7.4"
            }
        ],
        "reflectionQuestionsVi": [
            "Coach đã tận dụng ẩn dụ (Metaphor) của khách hàng như thế nào để khơi gợi nhận thức?",
            "Làm sao câu hỏi của Coach chạm vào con người (Who) chứ không chỉ dừng ở vấn đề công việc (What)?",
            "Điểm khác biệt giữa câu hỏi mở gợi thức và câu hỏi dẫn dắt có chủ đích là gì?"
        ],
        "reflectionQuestionsEn": [
            "How did the Coach utilize the client's own metaphor to evoke deeper awareness?",
            "How did the inquiry explore the personhood ('Who') rather than merely transactional tasks ('What')?",
            "What distinguishes an evocative inquiry from a leading, manipulative question?"
        ],
        "pccMarkerRef": "ICF Competency 7 (Evokes Awareness) / PCC Marker 7.1–7.4",
        "orderIndex": 8
    },
    {
        "id": "cs-sec-d2",
        "sectionId": "sec-d2",
        "titleVi": "Tình huống: Thúc đẩy Sự Phát triển — Thiết kế Hành động & Trách nhiệm Tự chủ",
        "titleEn": "Case Study: Facilitating Growth — Designing Autonomous Action & Accountability",
        "scenarioVi": "Khách hàng vừa có bước chuyển nhận thức lớn về việc cân bằng cuộc sống và cần chuyển hóa thành cam kết hành động cụ thể không bị trì hoãn.",
        "scenarioEn": "The client achieves a breakthrough realization regarding life integration and needs to translate insight into autonomous, sustainable commitments.",
        "dialogue": [
            {
                "speaker": "Khách hàng",
                "textVi": "Tôi nhận ra nếu không dành 1 tiếng mỗi tối hoàn toàn ngắt kết nối công việc cho gia đình, tôi sẽ đánh mất tuổi thơ của con gái mình.",
                "textEn": "I realize that unless I disconnect completely from work for one hour each evening for family, I will forfeit my daughter's childhood.",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Một nhận thức mang tính bước ngoặt sâu sắc. Từ nhận thức thiêng liêng này, hành động cụ thể đầu tiên bạn muốn thực hiện ngay tối nay là gì?",
                "textEn": "A profound, milestone realization. From this sacred awareness, what is the very first concrete step you choose to take starting tonight?",
                "markerTag": "PCC Marker 8.1"
            },
            {
                "speaker": "Khách hàng",
                "textVi": "Đúng 19h30, tôi sẽ tắt wifi trên điện thoại và để máy ở phòng làm việc, rồi cùng con gái đọc sách trong 45 phút.",
                "textEn": "At precisely 7:30 PM, I will turn off my phone's Wi-Fi, leave it in my study, and read stories with my daughter for 45 minutes.",
                "markerTag": None
            },
            {
                "speaker": "Coach",
                "textVi": "Hành động rất rõ ràng và ý nghĩa. Điều gì có thể là lực cản lớn nhất đối với kế hoạch này, và bạn sẽ làm thế nào để tự chịu trách nhiệm với cam kết của mình nếu chuông điện thoại reo?",
                "textEn": "Clear, meaningful, and grounded. What might be the greatest obstacle to this commitment, and how will you hold yourself accountable if work urgency tempts you?",
                "markerTag": "PCC Marker 8.2 & 8.3"
            }
        ],
        "reflectionQuestionsVi": [
            "Tại sao Coach yêu cầu hành động phải do chính khách hàng thiết kế?",
            "Câu hỏi về 'lực cản' và 'cơ chế tự chịu trách nhiệm' (Accountability) giúp kế hoạch bền vững ra sao?",
            "Làm thế nào Coach khép lại phiên khai vấn bằng việc tôn vinh sự học hỏi và quyền tự quyết của khách hàng?"
        ],
        "reflectionQuestionsEn": [
            "Why must the action plan be exclusively authored by the client rather than suggested by the Coach?",
            "How do questions on obstacles and self-accountability guarantee sustainability?",
            "How does the Coach close the session celebrating client learning and autonomy?"
        ],
        "pccMarkerRef": "ICF Competency 8 (Facilitates Client Growth) / PCC Marker 8.1–8.4",
        "orderIndex": 9
    }
]

print(f"Defined {len(CASE_STUDIES)} Case Studies without any coach projection.")
