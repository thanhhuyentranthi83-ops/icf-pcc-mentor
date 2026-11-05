# -*- coding: utf-8 -*-
"""
Builder to generate scripts/sjt_50_data.py with exactly 50 authentic ICF SJT practice questions.
"""
import json

existing_16 = json.load(open('data/mentor_data.json'))['practiceQuestions']

# Define Q17 through Q50
new_questions = [
    {
        "id": "Q17",
        "questionVi": "Khách hàng là một CEO vừa hoàn thành một quý kinh doanh vượt bậc nhờ những chuyển hóa từ phiên khai vấn. Vào dịp lễ, khách hàng gửi tặng bạn một chiếc đồng hồ sang trọng trị giá 2.000 USD kèm thiệp cảm ơn sâu sắc. Bạn chưa từng thảo luận về chính sách quà tặng trong thỏa thuận ban đầu.",
        "questionEn": "A client who is a CEO achieved an outstanding fiscal quarter through transformative coaching insights. During the holidays, the client gifts you a luxury watch valued at $2,000 with a deeply appreciative card. You had not discussed gift policies in the initial agreement.",
        "options": [
            {
                "key": "A",
                "textVi": "Nhận món quà một cách nồng nhiệt và ngầm hiểu đây là phần thưởng xứng đáng cho chất lượng khai vấn của bạn.",
                "textEn": "Accept the gift warmly and treat it as a well-deserved reward for the quality of your coaching."
            },
            {
                "key": "B",
                "textVi": "Lập tức gửi trả lại món quà thông qua lễ tân công ty mà không cần liên hệ nói chuyện vì sợ vi phạm đạo đức.",
                "textEn": "Immediately return the gift via corporate reception without contacting the client to avoid ethical breach."
            },
            {
                "key": "C",
                "textVi": "Mở cuộc đối thoại cởi mở, bày tỏ sự trân trọng lòng tri ân của khách hàng, minh bạch giải thích quy tắc đạo đức ICF về việc tránh nhận quà giá trị lớn có thể ảnh hưởng đến tính khách quan, và cùng xem xét cách xử lý phù hợp.",
                "textEn": "Initiate an open dialogue, appreciate their gratitude, transparently explain ICF ethical codes regarding high-value gifts impacting objectivity, and explore an appropriate way forward together."
            },
            {
                "key": "D",
                "textVi": "Giữ chiếc đồng hồ nhưng giảm trừ 2.000 USD vào hóa đơn phí khai vấn của tháng tiếp theo.",
                "textEn": "Keep the watch but deduct $2,000 from the client's next coaching invoice."
            }
        ],
        "bestAnswer": "C",
        "worstAnswer": "A",
        "explanationVi": "BEST là C: Chuẩn mực đạo đức ICF 2025 yêu cầu Coach minh bạch, quản lý rủi ro xung đột lợi ích hoặc tổn hại tính khách quan khi nhận quà giá trị cao thông qua đối thoại tôn trọng. WORST là A: Nhận quà đắt tiền mà không xem xét ranh giới chuyên nghiệp làm xói mòn tính trung lập và thiết lập tiền lệ độc hại.",
        "explanationEn": "BEST is C: ICF 2025 Ethics mandates managing potential objectivity compromises and conflicts of interest through transparent, respectful dialogue. WORST is A: Accepting high-value gifts without boundary examination impairs neutrality and establishes an unethical precedent.",
        "primaryCompetency": "1. Demonstrates Ethical Practice / Ethics 3.1–3.4",
        "keyClueVi": "Quà tặng giá trị cao & ranh giới tính khách quan",
        "keyClueEn": "High-value gift & objectivity boundaries",
        "difficulty": "medium",
        "orderIndex": 17
    },
    {
        "id": "Q18",
        "questionVi": "Bạn đang khai vấn cho Giám đốc Khối Vận hành của một tập đoàn. Ban Nhân sự tập đoàn tiếp tục mời bạn ký hợp đồng khai vấn cho Tổng Giám đốc (người quản lý trực tiếp của Giám đốc Vận hành).",
        "questionEn": "You are currently coaching the VP of Operations at an enterprise. Corporate HR now approaches you to coach the CEO (the direct manager of the VP of Operations).",
        "options": [
            {
                "key": "A",
                "textVi": "Nhận lời ngay vì bạn sẽ nắm rõ thông tin cả hai bên, giúp việc khai vấn cho Giám đốc Vận hành đạt kết quả nhanh hơn.",
                "textEn": "Accept immediately because knowing both sides will accelerate results for the VP of Operations."
            },
            {
                "key": "B",
                "textVi": "Minh bạch nêu rõ xung đột lợi ích tiềm ẩn và rủi ro rò rỉ ranh giới bảo mật với các bên; đánh giá xem có thể thiết lập ranh giới tách biệt tuyệt đối không, hoặc chủ động giới thiệu một Coach độc lập khác cho Tổng Giám đốc.",
                "textEn": "Transparently disclose the potential conflict of interest and confidentiality boundary risks to all parties; evaluate whether absolute separation can be upheld, or proactively refer another independent Coach for the CEO."
            },
            {
                "key": "C",
                "textVi": "Nhận hợp đồng với Tổng Giám đốc nhưng đơn phương chấm dứt hợp đồng với Giám đốc Vận hành mà không báo trước.",
                "textEn": "Accept the contract with the CEO but unilaterally terminate the contract with the VP without prior notice."
            },
            {
                "key": "D",
                "textVi": "Yêu cầu Giám đốc Vận hành cho phép bạn chia sẻ những khó khăn của họ với Tổng Giám đốc trong phiên tới.",
                "textEn": "Ask the VP for permission to share their operational struggles with the CEO in the upcoming session."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: Quản lý chủ động xung đột vai trò trong cùng hệ sinh thái tổ chức để bảo vệ bảo mật và tâm lý khách hàng. WORST là A: Dùng thông tin từ khách hàng này để can thiệp vào khách hàng kia là vi phạm nghiêm trọng tính bảo mật và sự chính trực.",
        "explanationEn": "BEST is B: Proactively addresses multi-party systemic role conflict to protect client confidentiality and psychological safety. WORST is A: Cross-pollinating confidential information violates core integrity and confidentiality standards.",
        "primaryCompetency": "1. Demonstrates Ethical Practice / Ethics 3.1–3.3",
        "keyClueVi": "Khai vấn đồng thời sếp và cấp dưới / Xung đột vai trò",
        "keyClueEn": "Coaching manager and direct report / Role conflict",
        "difficulty": "hard",
        "orderIndex": 18
    },
    {
        "id": "Q19",
        "questionVi": "Trong phiên, khách hàng chia sẻ một quyết định nhân sự mà cá nhân Coach nhận thấy là thiếu công bằng và bất lợi cho cấp dưới của khách hàng. Coach cảm thấy sự khó chịu và phán xét mạnh mẽ đang dâng lên trong nội tâm.",
        "questionEn": "During a session, the client shares a personnel decision that the Coach personally feels is unfair and disadvantageous to the client's subordinate. The Coach notices rising internal discomfort and judgment.",
        "options": [
            {
                "key": "A",
                "textVi": "Nói rõ với khách hàng rằng quyết định đó là phi đạo đức và yêu cầu họ phải thay đổi cách hành xử.",
                "textEn": "Tell the client directly that their decision is unethical and demand that they change their conduct."
            },
            {
                "key": "B",
                "textVi": "Tự nhận thức cảm xúc và định kiến cá nhân đang nảy sinh, hít thở để đưa tâm trí về trạng thái hiện diện trung lập, không phán xét, và đặt câu hỏi để khách hàng tự khám phá các tác động đa chiều từ quyết định của họ.",
                "textEn": "Self-manage personal emotional triggers and biases, breathe to return to neutral, non-judgmental presence, and pose open questions for the client to explore multifaceted impacts of their decision."
            },
            {
                "key": "C",
                "textVi": "Kể câu chuyện về một người lãnh đạo từng thất bại thảm hại vì hành động bất công để răn đe khách hàng.",
                "textEn": "Share a cautionary tale of a leader who failed terribly due to unfair actions to deter the client."
            },
            {
                "key": "D",
                "textVi": "Lờ đi cảm xúc đó và chuyển hướng buổi khai vấn sang một chủ đề hoàn toàn khác không liên quan.",
                "textEn": "Ignore the emotions and abruptly divert the session to an unrelated topic."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: Năng lực 2 (Coaching Mindset) và Năng lực 5 (Presence) yêu cầu Coach tự quản lý cảm xúc (self-management), duy trì tính khách quan không phán xét và để khách hàng tự soi chiếu. WORST là A: Phán xét đạo đức và áp đặt quan điểm cá nhân phá hủy hoàn toàn mối quan hệ hợp tác.",
        "explanationEn": "BEST is B: Competencies 2 & 5 require reflective emotional self-management, maintaining non-judgmental neutrality while inviting client self-examination. WORST is A: Imposing moral condemnation completely destroys the partnering container.",
        "primaryCompetency": "2. Embodies a Coaching Mindset / 5. Maintains Presence",
        "keyClueVi": "Quản lý cảm xúc tự thân của Coach & không phán xét",
        "keyClueEn": "Coach emotional self-management & non-judgment",
        "difficulty": "medium",
        "orderIndex": 19
    },
    {
        "id": "Q20",
        "questionVi": "Khách hàng xuất thân từ một nền văn hóa đề cao thứ bậc gia tộc và tính tập thể, chia sẻ rằng họ cảm thấy bế tắc vì không thể từ chối đề bạt một người họ hàng thiếu năng lực vào công ty theo kỳ vọng của cha mẹ. Coach xuất thân từ văn hóa phương Tây đề cao chủ nghĩa cá nhân và chế độ trọng dụng nhân tài.",
        "questionEn": "The client comes from a culture prioritizing familial hierarchy and collectivism, expressing paralysis because they cannot refuse promoting an unqualified relative expected by elders. The Coach comes from an individualistic, merit-based Western culture.",
        "options": [
            {
                "key": "A",
                "textVi": "Khuyên khách hàng phải học cách tách bạch dứt khoát giữa gia đình và công việc theo thông lệ quản trị hiện đại.",
                "textEn": "Advise the client to strictly separate family from business according to modern governance best practices."
            },
            {
                "key": "B",
                "textVi": "Nhận biết sự khác biệt về văn hóa, giữ sự tò mò thuần khiết, mời khách hàng chia sẻ sâu hơn về những giá trị gia đình và ý nghĩa của kỳ vọng đó đối với căn tính cá nhân của họ.",
                "textEn": "Acknowledge cultural differences, remain genuinely curious, and invite the client to share what familial values and expectations signify for their personal identity."
            },
            {
                "key": "C",
                "textVi": "Nói với khách hàng rằng tư duy gia đình trị là nguyên nhân khiến doanh nghiệp không thể phát triển.",
                "textEn": "Tell the client that nepotism is the fundamental reason enterprises fail to scale."
            },
            {
                "key": "D",
                "textVi": "Đề xuất khách hàng gửi người họ hàng đi đào tạo ngắn hạn để hợp thức hóa việc đề bạt.",
                "textEn": "Suggest sending the relative to a short training course to rationalize the promotion."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "C",
        "explanationVi": "BEST là B: Năng lực 2 (Coaching Mindset) đòi hỏi nhận thức và tôn trọng bối cảnh văn hóa của khách hàng (cultural awareness), không áp đặt tiêu chuẩn riêng của Coach. WORST là C: Công kích hệ giá trị văn hóa và bối cảnh sống của khách hàng bằng sự áp đặt thành kiến.",
        "explanationEn": "BEST is B: Competency 2 requires cultural awareness, humility, and honoring the client's cultural framework without imposing personal values. WORST is C: Derogating the client's cultural heritage with bias and prejudice.",
        "primaryCompetency": "2. Embodies a Coaching Mindset / Cultural Awareness",
        "keyClueVi": "Bối cảnh văn hóa & tôn trọng thế giới quan khách hàng",
        "keyClueEn": "Cultural context & honoring client worldview",
        "difficulty": "medium",
        "orderIndex": 20
    },
    {
        "id": "Q21",
        "questionVi": "Mở đầu phiên, khách hàng nói: 'Hôm nay tôi muốn mình cảm thấy bớt căng thẳng và hạnh phúc hơn trong công việc'. Khi được hỏi thêm, khách hàng tiếp tục lặp lại các mong muốn chung chung.",
        "questionEn": "At the start of the session, the client states: 'Today I just want to feel less stressed and happier at work.' When probed further, the client repeats general aspirations.",
        "options": [
            {
                "key": "A",
                "textVi": "Đưa cho khách hàng bảng câu hỏi đánh giá mức độ căng thẳng tiêu chuẩn và hướng dẫn họ cách hít thở thư giãn.",
                "textEn": "Provide the client a standardized stress assessment quiz and instruct them on relaxation breathing."
            },
            {
                "key": "B",
                "textVi": "Đồng hành cùng khách hàng để làm rõ: 'Hạnh phúc hơn' cụ thể sẽ trông như thế nào, cảm thấy ra sao đối với họ; và điều gì cụ thể có thể đạt được trong phiên hôm nay để đo lường sự chuyển biến đó.",
                "textEn": "Partner with the client to explore what 'happier' looks, feels, and sounds like specifically for them, and define measurable indicators achievable within today's session."
            },
            {
                "key": "C",
                "textVi": "Chấp nhận mục tiêu mơ hồ đó và bắt đầu đặt các câu hỏi ngẫu nhiên về công việc hàng ngày.",
                "textEn": "Accept the vague goal and start asking random questions about their daily work routine."
            },
            {
                "key": "D",
                "textVi": "Yêu cầu khách hàng rời phiên và chỉ quay lại khi đã xác định được một KPI định lượng rõ ràng.",
                "textEn": "Instruct the client to leave the session and return only when they have defined a quantitative KPI."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "D",
        "explanationVi": "BEST là B: Năng lực 3 (Establishes and Maintains Agreements - PCC Marker 3.2, 3.3) yêu cầu Coach đồng hành để cụ thể hóa kết quả mong đợi và thước đo thành công cho phiên. WORST là D: Đẩy khách hàng ra khỏi không gian khai vấn thiếu sự đồng hành và thấu cảm.",
        "explanationEn": "BEST is B: Competency 3 (PCC Markers 3.2 & 3.3) mandates partnering with the client to define measurable outcomes and clear criteria for session success. WORST is D: Rejecting the client abruptly undermines rapport and partnering.",
        "primaryCompetency": "3. Establishes and Maintains Agreements / PCC Marker 3.2–3.3",
        "keyClueVi": "Cụ thể hóa mục tiêu mơ hồ & thiết lập thước đo phiên",
        "keyClueEn": "Clarifying vague goals & establishing session measures",
        "difficulty": "medium",
        "orderIndex": 21
    },
    {
        "id": "Q22",
        "questionVi": "Trong một chương trình khai vấn doanh nghiệp, Trưởng phòng Nhân sự (Sponsor) muốn mục tiêu của khách hàng là 'nâng cao năng lực thuyết phục để thúc đẩy doanh số', nhưng khách hàng lại muốn tập trung vào 'tìm lại sự cân bằng để tránh kiệt sức'.",
        "questionEn": "In an organizational coaching program, HR Director (Sponsor) sets the objective as 'enhancing persuasive leadership to boost sales', but the client wants to focus on 'reclaiming balance to avoid burnout.'",
        "options": [
            {
                "key": "A",
                "textVi": "Bỏ qua mong muốn của khách hàng và ép họ theo mục tiêu doanh số của HR vì HR là bên chi trả kinh phí.",
                "textEn": "Disregard the client's desire and force HR's sales target because HR pays the fees."
            },
            {
                "key": "B",
                "textVi": "Tạo điều kiện cho một phiên đối thoại 3 bên minh bạch giữa Coach, Khách hàng và Sponsor để dung hòa kỳ vọng, thống nhất thỏa thuận chung tôn trọng cả mục tiêu phát triển tổ chức và sức khỏe của khách hàng.",
                "textEn": "Facilitate a transparent three-way alignment meeting between Coach, Client, and Sponsor to harmonize expectations and agree on shared objectives honoring both organizational goals and client well-being."
            },
            {
                "key": "C",
                "textVi": "Bí mật làm việc theo mục tiêu cân bằng của khách hàng nhưng làm báo cáo giả mạo gửi cho HR là đang làm về doanh số.",
                "textEn": "Secretly focus on balance with the client while fabricating reports to HR claiming sales topics were addressed."
            },
            {
                "key": "D",
                "textVi": "Khuyên khách hàng nộp đơn xin nghỉ việc nếu tổ chức quá áp đặt.",
                "textEn": "Advise the client to resign if the organization is excessively demanding."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "C",
        "explanationVi": "BEST là B: Năng lực 3 & Đạo đức ICF yêu cầu minh bạch thỏa thuận đa bên (Sponsor agreement) để dung hòa mục tiêu mà không phá vỡ bảo mật. WORST là C: Báo cáo sai sự thật là vi phạm nghiêm trọng tính chính trực (Ethics Standard 5.1).",
        "explanationEn": "BEST is B: Competency 3 and ICF Ethics require transparent multi-stakeholder contracting reconciling organizational and individual growth. WORST is C: Falsifying progress reports directly violates core integrity (Ethics 5.1).",
        "primaryCompetency": "3. Establishes and Maintains Agreements / Sponsor Alignment",
        "keyClueVi": "Dung hòa thỏa thuận đa bên / Khách hàng vs Nhà tài trợ",
        "keyClueEn": "Harmonizing multi-party agreements / Client vs Sponsor",
        "difficulty": "hard",
        "orderIndex": 22
    },
    {
        "id": "Q23",
        "questionVi": "Phiên khai vấn 60 phút chỉ còn 12 phút. Khách hàng đột nhiên thốt lên một phát hiện chấn động về nguyên nhân gốc rễ khiến họ luôn e ngại phát biểu trước đám đông, hoàn toàn mở ra một hướng đi mới sâu sắc.",
        "questionEn": "With only 12 minutes remaining in a 60-minute session, the client suddenly experiences a profound realization regarding the root cause of their public speaking anxiety, opening up an entirely new dimension.",
        "options": [
            {
                "key": "A",
                "textVi": "Ngắt lời khách hàng và yêu cầu họ dừng lại để tập trung hoàn thành các cam kết hành động đã định từ đầu buổi.",
                "textEn": "Interrupt the client and stop them in order to finalize action commitments planned at the start."
            },
            {
                "key": "B",
                "textVi": "Nhận diện mốc thời gian còn lại cùng khách hàng: 'Tôi nhận thấy đây là một khám phá rất quan trọng, và chúng ta còn 12 phút. Bạn muốn dành thời gian còn lại để khám phá sâu hơn điểm này, hay muốn ghi nhận nó để chuẩn bị cho phiên tiếp theo?'.",
                "textEn": "Acknowledge the remaining time boundary together: 'I notice this is a significant realization, and we have 12 minutes left. How would you like to best use our remaining time—exploring this deeper now, or holding it as our launchpad for next session?'."
            },
            {
                "key": "C",
                "textVi": "Tự ý kéo dài phiên thêm 60 phút mà không cần hỏi xem khách hàng có bận lịch trình tiếp theo hay không.",
                "textEn": "Unilaterally extend the session by 60 minutes without checking the client's availability."
            },
            {
                "key": "D",
                "textVi": "Bỏ qua mốc thời gian, cứ tiếp tục trò chuyện cho đến khi cạn kiệt năng lượng.",
                "textEn": "Ignore the clock entirely and converse aimlessly until mental fatigue sets in."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: PCC Marker 3.4 & 8.1 yêu cầu Coach đồng hành quản lý thời gian linh hoạt (partnering with time), trao quyền cho khách hàng quyết định ưu tiên. WORST là A: Bóp nghẹt sự chuyển hóa sâu sắc của khách hàng vì sự cứng nhắc theo kịch bản hành động bề mặt.",
        "explanationEn": "BEST is B: PCC Marker 3.4 mandates partnering with the client to manage session pacing and honor emerging breakthroughs. WORST is A: Stifling transformative awareness to adhere mechanically to superficial task completion.",
        "primaryCompetency": "3. Establishes and Maintains Agreements / PCC Marker 3.4",
        "keyClueVi": "Quản lý tiến độ thời gian & tôn trọng phát hiện mới",
        "keyClueEn": "Managing session pacing & honoring emerging insights",
        "difficulty": "medium",
        "orderIndex": 23
    },
    {
        "id": "Q24",
        "questionVi": "Khách hàng xúc động rơi nước mắt và thú nhận: 'Tôi luôn mang cảm giác mình là kẻ lừa đảo (Imposter Syndrome). Dù bên ngoài thành công, tôi luôn sợ một ngày nào đó mọi người sẽ phát hiện ra tôi bất tài'.",
        "questionEn": "The client becomes emotional and tearfully confesses: 'I have always carried severe imposter syndrome. Despite external success, I live in constant dread that people will realize I am incompetent.'",
        "options": [
            {
                "key": "A",
                "textVi": "Gạt đi cảm xúc đó: 'Anh lo lắng vô cớ quá, thành tích của anh ai cũng thấy mà, hãy tự tin lên!'.",
                "textEn": "Dismiss the emotion: 'You worry unnecessarily; everyone sees your accomplishments, just be confident!'."
            },
            {
                "key": "B",
                "textVi": "Giữ không gian tĩnh lặng, đón nhận sự yếu lòng của khách hàng với sự trân trọng và đồng cảm sâu sắc: ghi nhận lòng dũng cảm khi chia sẻ, và cùng khách hàng hiện diện với cảm xúc đó mà không phán xét.",
                "textEn": "Hold silent space, embrace the vulnerability with deep empathy and respect: acknowledge their courage in sharing, and remain present with the feeling without judgment."
            },
            {
                "key": "C",
                "textVi": "Yêu cầu khách hàng ghi chép nhật ký 10 thành tựu mỗi ngày như một bài tập bắt buộc để chữa trị hội chứng này.",
                "textEn": "Instruct the client to record 10 daily achievements as a mandatory homework assignment to cure the syndrome."
            },
            {
                "key": "D",
                "textVi": "Khuyên khách hàng lập tức uống thuốc an thần để giảm bớt sự sợ hãi.",
                "textEn": "Advise the client to immediately take anti-anxiety medication to reduce fear."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: Năng lực 4 (Cultivates Trust and Safety - PCC Marker 4.1, 4.3) tạo không gian an toàn tâm lý tuyệt đối, trân trọng sự tổn thương và biểu đạt cảm xúc. WORST là A: Gạt bỏ cảm xúc (toxic positivity) làm khách hàng cảm thấy xấu hổ và bị từ chối.",
        "explanationEn": "BEST is B: Competency 4 (PCC Markers 4.1 & 4.3) cultivates psychological safety, honoring vulnerability and acknowledging deep emotions without judgment. WORST is A: Dismissive positivity invalidates client vulnerability and destroys safety.",
        "primaryCompetency": "4. Cultivates Trust and Safety / Psychological Safety",
        "keyClueVi": "Tôn trọng sự tổn thương & kiến tạo an toàn tâm lý",
        "keyClueEn": "Honoring vulnerability & cultivating psychological safety",
        "difficulty": "medium",
        "orderIndex": 24
    },
    {
        "id": "Q25",
        "questionVi": "Khách hàng vừa phạm phải một sai lầm nghiêm trọng trong dự án và kể với vẻ phòng thủ, lo sợ rằng Coach sẽ khiển trách hoặc đánh giá thấp năng lực của mình.",
        "questionEn": "The client recently made a severe project error and recounts it defensively, fearing the Coach will reprimand them or judge their competence.",
        "options": [
            {
                "key": "A",
                "textVi": "Nhắc lại các cam kết hiệu suất trước đây và cảnh báo rằng sai lầm như vậy là không thể chấp nhận ở cấp quản lý.",
                "textEn": "Reiterate previous performance agreements and warn that such an error is unacceptable at management level."
            },
            {
                "key": "B",
                "textVi": "Tái khẳng định mối quan hệ hợp tác bình đẳng, thấu cảm với áp lực khách hàng đang trải qua, và mời khách hàng nhìn vào bài học nhận thức rút ra từ sự cố thay vì chìm trong tự trách.",
                "textEn": "Reaffirm the equal partnering relationship, empathize with their pressure, and invite the client to explore learnings emerging from the incident rather than dwelling on self-blame."
            },
            {
                "key": "C",
                "textVi": "Trấn an qua loa rồi vội vã đưa ra giải pháp sửa chữa sự cố giúp khách hàng.",
                "textEn": "Offer superficial reassurance and immediately provide a solution to fix the issue for the client."
            },
            {
                "key": "D",
                "textVi": "Yêu cầu khách hàng giải trình bằng văn bản nguyên nhân sai phạm trước khi phiên tiếp tục.",
                "textEn": "Demand a written explanation of the error before the session can proceed."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: Năng lực 4 tôn trọng tính trọn vẹn của khách hàng, nhìn nhận sai lầm như cơ hội học tập phát triển. WORST là A: Đóng vai giám sát viên khiển trách làm tổn hại nghiêm trọng tư duy khai vấn.",
        "explanationEn": "BEST is B: Competency 4 respects client resourcefulness, treating setbacks as rich reflective learning opportunities. WORST is A: Adopting a punitive managerial stance violates partnering fundamentals.",
        "primaryCompetency": "4. Cultivates Trust and Safety / Non-judgmental Support",
        "keyClueVi": "Bình đẳng hợp tác & chuyển hóa sai lầm thành bài học",
        "keyClueEn": "Partnering equality & transforming errors into learning",
        "difficulty": "medium",
        "orderIndex": 25
    },
    {
        "id": "Q26",
        "questionVi": "Khách hàng chia sẻ rằng họ cảm thấy bị cô lập tại nơi làm việc vì thuộc một nhóm thiểu số (về giới/sắc tộc/xuất thân), và ngập ngừng hỏi liệu Coach có hiểu được những trải nghiệm đặc thù này không.",
        "questionEn": "The client shares feeling isolated in the workplace due to belonging to a minority identity group, hesitatingly asking if the Coach can comprehend these lived experiences.",
        "options": [
            {
                "key": "A",
                "textVi": "Tuyên bố rằng: 'Trong khai vấn, tôi xem mọi người hoàn toàn giống nhau, màu da hay xuất thân không có ý nghĩa gì cả'.",
                "textEn": "Assert: 'In coaching, I treat everyone identically; background or identity makes zero difference to me.'."
            },
            {
                "key": "B",
                "textVi": "Khiêm nhường thừa nhận ranh giới trải nghiệm cá nhân, khẳng định sự trân trọng tuyệt đối căn tính độc bản của khách hàng, và tạo không gian an toàn để khách hàng thoải mái bày tỏ những tác động của bối cảnh đó đến họ.",
                "textEn": "Humbly acknowledge experiential boundaries, affirm unequivocal respect for the client's unique identity, and hold safe space for them to express systemic impacts on their journey."
            },
            {
                "key": "C",
                "textVi": "Khuyên khách hàng không nên nhạy cảm quá mức về xuất thân của mình trong công việc.",
                "textEn": "Advise the client against being overly sensitive regarding their identity at work."
            },
            {
                "key": "D",
                "textVi": "Chia sẻ ngay trải nghiệm của bản thân khi từng bị phân biệt đối xử để chứng minh mình cũng từng khổ như họ.",
                "textEn": "Immediately share personal grievances of discrimination to prove the Coach suffered similarly."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: Chuẩn mực DEIB của ICF 2025 tôn trọng sự đa dạng, bình đẳng và hòa nhập, lắng nghe với sự khiêm nhường học hỏi. WORST là A: 'Mù màu văn hóa' (color-blindness) phủ nhận căn tính và nỗi đau thực tế của khách hàng.",
        "explanationEn": "BEST is B: ICF 2025 DEIB standards champion cultural humility and authentic validation of intersectional identities. WORST is A: Dismissive 'color-blindness' invalidates systemic realities and lived experiences.",
        "primaryCompetency": "4. Cultivates Trust and Safety / DEIB & Inclusivity",
        "keyClueVi": "Tôn trọng căn tính đa dạng (DEIB) & khiêm nhường học hỏi",
        "keyClueEn": "Honoring identity diversity (DEIB) & cultural humility",
        "difficulty": "hard",
        "orderIndex": 26
    },
    {
        "id": "Q27",
        "questionVi": "Giữa phiên khai vấn, Coach nhận thấy tâm trí mình bị xao nhãng bởi một vấn đề cá nhân khẩn cấp và đã bỏ lỡ vài câu nói vừa rồi của khách hàng.",
        "questionEn": "Midway through a session, the Coach notices their mind wandering to an urgent personal concern, missing the client's last few sentences.",
        "options": [
            {
                "key": "A",
                "textVi": "Giả vờ như vẫn đang lắng nghe chăm chú, gật đầu liên tục và đặt một câu hỏi chung chung để lấp liếm.",
                "textEn": "Pretend to listen intently, nod continually, and ask a generic question to mask the lapse."
            },
            {
                "key": "B",
                "textVi": "Dừng lại một nhịp, hít thở sâu, chân thành và minh bạch xin lỗi khách hàng vì một thoáng xao nhãng, rồi nhờ khách hàng vui lòng chia sẻ lại ý vừa rồi.",
                "textEn": "Pause, take a centering breath, sincerely and transparently apologize for the brief lapse in attention, and invite the client to re-share their last thought."
            },
            {
                "key": "C",
                "textVi": "Đổ lỗi cho đường truyền mạng bị giật để che giấu sự mất tập trung của mình.",
                "textEn": "Blame a poor internet connection to conceal the loss of attention."
            },
            {
                "key": "D",
                "textVi": "Lập tức đề nghị kết thúc phiên sớm vì không đủ năng lượng làm việc tiếp.",
                "textEn": "Immediately propose terminating the session early due to inadequate energy."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: Năng lực 5 (Maintains Presence - PCC Marker 5.1) thể hiện sự chân thật, minh bạch (vulnerability) và đưa sự chú ý trở lại trọn vẹn với khách hàng. WORST là A: Giả tạo lắng nghe phá vỡ niềm tin cốt lõi và kết nối năng lượng.",
        "explanationEn": "BEST is B: Competency 5 (PCC Marker 5.1) embodies presence, integrity, and authenticity by transparently resetting attention. WORST is A: Feigning presence erodes authentic rapport and energetic connection.",
        "primaryCompetency": "5. Maintains Presence / PCC Marker 5.1",
        "keyClueVi": "Tự nhận thức sự hiện diện & minh bạch chân thật",
        "keyClueEn": "Self-awareness of presence & authentic transparency",
        "difficulty": "medium",
        "orderIndex": 27
    },
    {
        "id": "Q28",
        "questionVi": "Sau khi đối diện với một nghịch lý khó khăn, khách hàng bỗng bật cười sảng khoái và nói: 'Nghĩ lại thấy chuyện này vừa bi hài vừa thú vị thật đấy!'.",
        "questionEn": "After confronting a challenging paradox, the client suddenly bursts into genuine laughter and says: 'Looking back, this whole ordeal is absurdly hilarious!'",
        "options": [
            {
                "key": "A",
                "textVi": "Nghiêm nghị nhắc nhở khách hàng rằng đây là phiên làm việc chuyên nghiệp, không nên cười cợt thiếu nghiêm túc.",
                "textEn": "Sternly remind the client that this is a professional coaching session and levity is inappropriate."
            },
            {
                "key": "B",
                "textVi": "Hiện diện trọn vẹn, cộng hưởng tự nhiên với năng lượng và sự hóm hỉnh của khách hàng, tạo không gian để năng lượng tích cực này mở ra góc nhìn mới nhẹ nhõm hơn.",
                "textEn": "Remain fully present, naturally resonance with the client's levity and humor, holding space for this energy shift to open up a lighter perspective."
            },
            {
                "key": "C",
                "textVi": "Bỏ qua tiếng cười của khách hàng và đọc lại danh sách rủi ro đã thảo luận trước đó.",
                "textEn": "Ignore the laughter and re-read the risk analysis matrix discussed earlier."
            },
            {
                "key": "D",
                "textVi": "Phân tích tâm lý học rằng nụ cười là cơ chế phòng vệ che đậy nỗi sợ hãi tiềm thức.",
                "textEn": "Analyze psychologically that laughter is merely a defense mechanism masking subconscious terror."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: PCC Marker 5.4 khuyến khích Coach linh hoạt cộng hưởng với năng lượng, sự hóm hỉnh và tính tự nhiên của khách hàng. WORST là A: Phán xét sự hài hước bóp nghẹt trạng thái thả lỏng tự nhiên.",
        "explanationEn": "BEST is B: PCC Marker 5.4 honors partnering with humor, playfulness, and energy shifts that emerge organically. WORST is A: Rigidity and admonishing humor kills psychological safety and flow.",
        "primaryCompetency": "5. Maintains Presence / PCC Marker 5.4 (Humor & Agility)",
        "keyClueVi": "Cộng hưởng năng lượng & sự hóm hỉnh tự nhiên",
        "keyClueEn": "Resonating with energy & authentic humor",
        "difficulty": "easy",
        "orderIndex": 28
    },
    {
        "id": "Q29",
        "questionVi": "Khách hàng bối rối hỏi: 'Tôi không biết phải làm gì nữa. Coach là chuyên gia, xin hãy cho tôi biết tôi nên chọn phương án 1 hay phương án 2?'.",
        "questionEn": "The client feels stuck and pleads: 'I honestly don't know what to do. You are the seasoned expert; please just tell me whether I should pick Option 1 or Option 2?'",
        "options": [
            {
                "key": "A",
                "textVi": "Chọn giúp khách hàng Phương án 1 vì bạn có nhiều năm kinh nghiệm quản lý hơn khách hàng.",
                "textEn": "Choose Option 1 for the client based on your extensive managerial experience."
            },
            {
                "key": "B",
                "textVi": "Thấu hiểu mong muốn tìm kiếm sự chỉ dẫn, nhưng giữ vững niềm tin vào quyền tự quyết và trí tuệ nội tại của khách hàng: 'Tôi cảm nhận được sự giằng xé của bạn lúc này. Nếu có một khoảng lặng để lắng nghe tiếng nói sâu thẳm nhất bên trong, điều gì đang thôi thúc bạn hướng về mỗi lựa chọn?'.",
                "textEn": "Empathize with their desire for external answers while holding steadfast belief in their self-determination: 'I feel your tension right now. In stillness, what does your inner wisdom whisper about each choice?'."
            },
            {
                "key": "C",
                "textVi": "Chỉ trích khách hàng vì thiếu tính độc lập và lười suy nghĩ.",
                "textEn": "Criticize the client for lacking independence and being mentally lazy."
            },
            {
                "key": "D",
                "textVi": "Bỏ phiếu bốc thăm ngẫu nhiên để chọn phương án cho khách hàng.",
                "textEn": "Flip a coin to choose the option randomly for the client."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: Triết lý ICF khẳng định khách hàng là chuyên gia về cuộc đời họ; Coach giữ vai trò đối tác gợi mở năng lực tự quyết. WORST là A: Cho lời khuyên biến phiên khai vấn thành tư vấn chỉ đạo (consulting/mentoring) làm xói mòn trách nhiệm tự thân.",
        "explanationEn": "BEST is B: Core ICF philosophy sees the client as the ultimate creative authority of their life; Coach evokes self-reliance. WORST is A: Directing answers degenerates coaching into consulting and disempowers autonomy.",
        "primaryCompetency": "5. Maintains Presence / Partnering & Non-direction",
        "keyClueVi": "Khách hàng đòi lời khuyên & trao quyền tự quyết",
        "keyClueEn": "Client asks for advice & preserving client autonomy",
        "difficulty": "medium",
        "orderIndex": 29
    },
    {
        "id": "Q30",
        "questionVi": "Khách hàng kể liên tu bất tận suốt 15 phút về các chi tiết vụn vặt trong cuộc họp tuần trước, lặp đi lặp lại những lời phàn nàn về thái độ của đồng nghiệp mà không đi vào trọng tâm.",
        "questionEn": "The client speaks ceaselessly for 15 minutes about minute details from last week's meeting, repetitively complaining about colleagues without getting to the core issue.",
        "options": [
            {
                "key": "A",
                "textVi": "Ngắt lời thô bạo và bảo khách hàng im lặng vì đang làm lãng phí thời gian của phiên khai vấn.",
                "textEn": "Rudely interrupt and tell the client to shut up because they are wasting billable time."
            },
            {
                "key": "B",
                "textVi": "Khéo léo xin phép can thiệp để làm gương soi: 'Cho phép tôi tạm dừng một nhịp; tôi nghe thấy bạn chia sẻ rất nhiều chi tiết về cuộc họp, nhưng điều gì thực sự đang là mấu chốt quan trọng nhất đối với bạn ở bên dưới những câu chuyện này?'.",
                "textEn": "Skillfully request permission to intervene as a mirror: 'May I pause us for a moment; I hear extensive tactical details, but beneath all of these stories, what is truly the essential crux for you?'."
            },
            {
                "key": "C",
                "textVi": "Ngồi im nghe tiếp thêm 30 phút nữa cho đến hết phiên mà không can thiệp.",
                "textEn": "Sit silently and let them talk for another 30 minutes until the session expires."
            },
            {
                "key": "D",
                "textVi": "Bắt đầu ghi chép tên của tất cả các đồng nghiệp bị phàn nàn và hỏi chi tiết từng người.",
                "textEn": "Start documenting names of all complained colleagues and interrogate each one."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: PCC Marker 5.3 & 6.1 cho phép Coach can thiệp khéo léo (intervene with partnering) để giúp khách hàng thoát khỏi câu chuyện bề mặt và quay về trọng tâm chuyển hóa. WORST là A: Ngắt lời thô lỗ phá hủy tính chuyên nghiệp và sự tôn trọng.",
        "explanationEn": "BEST is B: PCC Markers 5.3 & 6.1 permit respectful interruptions that partner with the client to cut through circular storytelling down to core meaning. WORST is A: Aggressive interruption violates professional respect.",
        "primaryCompetency": "6. Listens Actively / PCC Marker 5.3 & 6.1",
        "keyClueVi": "Can thiệp khéo léo vào câu chuyện chi tiết bề mặt",
        "keyClueEn": "Skillful interruption of circular narrative",
        "difficulty": "medium",
        "orderIndex": 30
    },
    {
        "id": "Q31",
        "questionVi": "Khi được hỏi về cảm xúc sau khi bàn giao dự án tâm huyết cho người khác, khách hàng mỉm cười nói: 'Tôi thấy hoàn toàn bình thường, không có vấn đề gì cả', nhưng giọng nói nghẹn lại, ánh mắt nhìn xuống và đôi bàn tay siết chặt.",
        "questionEn": "When asked about handing over their flagship project to a successor, the client smiles and says: 'I feel completely fine, no issues at all', but their voice catches, eyes cast downward, and hands clench tightly.",
        "options": [
            {
                "key": "A",
                "textVi": "Tin tưởng tuyệt đối vào lời nói 'bình thường' và nhanh chóng chuyển sang chủ đề khác.",
                "textEn": "Accept 'fine' at face value and quickly move to another agenda item."
            },
            {
                "key": "B",
                "textVi": "Phản chiếu trung lập sự không tương thích giữa lời nói và ngôn ngữ cơ thể: 'Bạn nói là bình thường, nhưng tôi nhận thấy giọng bạn nghẹn lại và bàn tay siết chặt. Có điều gì đang diễn ra bên dưới bề mặt đó không?'.",
                "textEn": "Neutrally reflect the incongruence between verbal statement and body language: 'You say fine, yet I noticed your voice trembling and your hands clenching. What might be stirring beneath that surface?'."
            },
            {
                "key": "C",
                "textVi": "Khẳng định chắc nịch rằng khách hàng đang nói dối và yêu cầu họ phải trung thực.",
                "textEn": "Assert aggressively that the client is lying and demand complete honesty."
            },
            {
                "key": "D",
                "textVi": "Tự động phân tích rằng khách hàng đang có dấu hiệu trầm cảm nghiêm trọng.",
                "textEn": "Diagnose that the client is exhibiting clinical depression."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "C",
        "explanationVi": "BEST là B: PCC Marker 6.2 yêu cầu Coach lắng nghe đa tầng (lời nói, ngữ điệu, cơ thể) và phản chiếu sự bất tương thích một cách khách quan không kết tội. WORST là C: Buộc tội khách hàng nói dối làm tan vỡ hoàn toàn lòng tin.",
        "explanationEn": "BEST is B: PCC Marker 6.2 listens for holistic incongruence (tone, physiology, non-verbals) and mirrors observations neutrally. WORST is C: Accusing the client of dishonesty shatters psychological safety.",
        "primaryCompetency": "6. Listens Actively / PCC Marker 6.2 (Holistic Listening)",
        "keyClueVi": "Lắng nghe phi ngôn ngữ & phản chiếu sự bất tương thích",
        "keyClueEn": "Non-verbal listening & reflecting incongruence",
        "difficulty": "medium",
        "orderIndex": 31
    },
    {
        "id": "Q32",
        "questionVi": "Khách hàng là kỹ sư trưởng sử dụng liên tục các thuật ngữ kỹ thuật chuyên ngành hẹp và nói: 'Chúng tôi đang gặp vấn đề nghẽn cổ chai kiến trúc monolith phân mảnh'. Coach hoàn toàn không hiểu khái niệm công nghệ này.",
        "questionEn": "The client is a chief architect using dense technical jargon, stating: 'We are bottlenecked by fragmented monolithic architecture.' The Coach has zero technical background.",
        "options": [
            {
                "key": "A",
                "textVi": "Gật gù giả vờ hiểu để giữ hình ảnh chuyên nghiệp trong mắt khách hàng.",
                "textEn": "Nod along pretending to understand to maintain a sophisticated facade."
            },
            {
                "key": "B",
                "textVi": "Thành thật bày tỏ rằng mình không có chuyên môn kỹ thuật, và mời khách hàng giải thích bằng ngôn từ đời thường: 'Khi bạn nói về sự nghẽn cổ chai phân mảnh đó, nó tác động thế nào đến vai trò lãnh đạo và cảm xúc của bạn?'.",
                "textEn": "Transparently state lacking technical knowledge and invite everyday metaphor: 'When you speak of this fragmented bottleneck, how does that manifest in your leadership and energy?'."
            },
            {
                "key": "C",
                "textVi": "Lập tức tra cứu Google trên điện thoại ngay giữa phiên để tìm hiểu thuật ngữ.",
                "textEn": "Immediately Google the terms on a phone during the session."
            },
            {
                "key": "D",
                "textVi": "Bảo khách hàng dừng nói về kỹ thuật vì Coach không quan tâm đến chuyện kỹ thuật.",
                "textEn": "Tell the client to stop talking tech because the Coach doesn't care about technical details."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: Khai vấn cấp độ PCC lắng nghe con người (WHO) đằng sau vấn đề kỹ thuật (WHAT) và minh bạch dùng ngôn từ của khách hàng để gợi mở nhận thức. WORST là A: Giả tạo hiểu biết khiến phiên khai vấn trở nên sáo rỗng.",
        "explanationEn": "BEST is B: PCC coaching focuses on the WHO behind the technical WHAT, using authentic inquiry to explore human impacts. WORST is A: Pretending domain fluency undermines authenticity and presence.",
        "primaryCompetency": "6. Listens Actively / Focus on the WHO behind the WHAT",
        "keyClueVi": "Lắng nghe con người (WHO) thay vì mắc kẹt thuật ngữ (WHAT)",
        "keyClueEn": "Listening to the WHO rather than trapped in technical WHAT",
        "difficulty": "medium",
        "orderIndex": 32
    },
    {
        "id": "Q33",
        "questionVi": "Khách hàng khẳng định với niềm tin sắt đá: 'Ở độ tuổi 50 như tôi, không ai có thể học thêm kỹ năng mới để chuyển đổi nghề nghiệp được nữa'.",
        "questionEn": "The client asserts with absolute conviction: 'At age 50, it is simply impossible for anyone to acquire new skills and pivot careers.'",
        "options": [
            {
                "key": "A",
                "textVi": "Nói thẳng rằng suy nghĩ đó là sai lầm và kể tên những danh nhân khởi nghiệp thành công ở tuổi 60.",
                "textEn": "Tell them bluntly that their belief is false and cite famous entrepreneurs who succeeded at 60."
            },
            {
                "key": "B",
                "textVi": "Mời khách hàng thám hiểm nguồn gốc của niềm tin giới hạn này: 'Điều gì từ quá khứ hay trải nghiệm đã hình thành nên kết luận chắc nịch đó trong bạn? Và nếu niềm tin này không hoàn toàn đúng, điều gì sẽ trở nên khả thi?'.",
                "textEn": "Invite the client to examine the origin of this limiting belief: 'What past experiences shaped that absolute conclusion? And if that belief were not entirely true, what might become possible?'."
            },
            {
                "key": "C",
                "textVi": "Đồng tình với khách hàng rằng 50 tuổi quả thực là quá muộn để thay đổi.",
                "textEn": "Agree that 50 is indeed too late to attempt any substantial change."
            },
            {
                "key": "D",
                "textVi": "Yêu cầu khách hàng đọc to 20 câu khẳng định tích cực (affirmations) trước gương mỗi sáng.",
                "textEn": "Instruct the client to recite 20 positive affirmations in the mirror daily."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: PCC Marker 7.2 & 7.3 khơi gợi nhận thức bằng cách mời khách hàng khám phá niềm tin, giá trị và góc nhìn giới hạn. WORST là A: Tranh luận đúng sai và áp đặt ví dụ bên ngoài làm tăng sự kháng cự của khách hàng.",
        "explanationEn": "BEST is B: PCC Markers 7.2 & 7.3 evoke awareness by exploring foundational assumptions and expanding perspectives. WORST is A: Debating beliefs directly triggers defensiveness and shuts down inquiry.",
        "primaryCompetency": "7. Evokes Awareness / PCC Marker 7.2–7.3",
        "keyClueVi": "Khám phá niềm tin giới hạn & gợi mở góc nhìn mới",
        "keyClueEn": "Exploring limiting beliefs & expanding perspectives",
        "difficulty": "medium",
        "orderIndex": 33
    },
    {
        "id": "Q34",
        "questionVi": "Khách hàng đang phân vân giữa hai lời mời làm việc: một bên lương rất cao nhưng áp lực văn hóa độc hại, một bên lương trung bình nhưng môi trường tôn trọng sự sáng tạo. Khách hàng bắt đầu lập bảng so sánh chi tiết về tiền bạc.",
        "questionEn": "The client is torn between two job offers: one with lucrative compensation but toxic culture, another with average pay but high creative autonomy. The client starts making a spreadsheet comparing salaries.",
        "options": [
            {
                "key": "A",
                "textVi": "Giúp khách hàng tính toán chi tiết bài toán tài chính và chi phí sinh hoạt.",
                "textEn": "Help calculate detailed financial models and cost-of-living differences."
            },
            {
                "key": "B",
                "textVi": "Mời khách hàng lùi lại một bước khỏi các con số để kết nối với hệ giá trị cốt lõi: 'Khi nghĩ về con người bạn muốn trở thành trong 5 năm tới, môi trường nào nuôi dưỡng đúng căn tính và giá trị sống của bạn nhất?'.",
                "textEn": "Invite the client to step back from numbers to connect with core values: 'Looking at who you want to become over the next 5 years, which environment genuinely nourishes your identity and life values?'."
            },
            {
                "key": "C",
                "textVi": "Khuyên khách hàng nên chọn nơi lương cao vì tiền bạc là quan trọng nhất trong thời kỳ kinh tế khó khăn.",
                "textEn": "Advise taking the lucrative job because money is paramount during economic instability."
            },
            {
                "key": "D",
                "textVi": "Quyết định thay cho khách hàng chọn công ty thứ hai.",
                "textEn": "Decide on behalf of the client to choose the second company."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "C",
        "explanationVi": "BEST là B: PCC Marker 7.1 & 7.4 chuyển dịch sự chú ý từ bình diện sự việc (WHAT - tiền bạc, con số) sang bình diện con người (WHO - căn tính, hệ giá trị sống). WORST là C: Áp đặt quan điểm thực dụng của Coach vào quyết định cuộc đời khách hàng.",
        "explanationEn": "BEST is B: PCC Markers 7.1 & 7.4 elevate exploration from tactical facts (WHAT) to core identity and values (WHO). WORST is C: Imposing the Coach's materialistic bias onto the client's life choices.",
        "primaryCompetency": "7. Evokes Awareness / WHO vs WHAT Exploration",
        "keyClueVi": "Tập trung vào căn tính (WHO) thay vì chỉ sự việc (WHAT)",
        "keyClueEn": "Focusing on WHO rather than tactical WHAT",
        "difficulty": "medium",
        "orderIndex": 34
    },
    {
        "id": "Q35",
        "questionVi": "Khách hàng đột nhiên dừng lại, mắt mở to và thốt lên: 'Trời ơi, hóa ra bấy lâu nay tôi làm việc kiệt sức không phải vì công việc quá nhiều, mà là vì tôi luôn muốn làm hài lòng người khác để được công nhận!'.",
        "questionEn": "The client pauses abruptly, eyes widening, and gasps: 'Oh wow, all along my burnout wasn't because of workload, but because of my desperate need to please others for validation!'",
        "options": [
            {
                "key": "A",
                "textVi": "Lập tức đưa ra 3 bài tập quản lý thời gian để khách hàng làm quen với việc từ chối người khác.",
                "textEn": "Immediately assign 3 time-management drills for the client to practice saying no."
            },
            {
                "key": "B",
                "textVi": "Giữ sự tĩnh lặng để insight lắng đọng trọn vẹn, rồi khẽ hỏi: 'Nhận thức mới này vừa làm sáng tỏ điều gì về bạn? Và nó thay đổi cách bạn nhìn nhận chính mình ra sao?'.",
                "textEn": "Hold stillness for the breakthrough to settle deeply, then softly ask: 'What does this awareness illuminate about you? And how does it reshape how you see yourself?'."
            },
            {
                "key": "C",
                "textVi": "Khen ngợi ầm ĩ và nói rằng khách hàng cuối cùng cũng đã thông minh ra.",
                "textEn": "Applaud boisterously and say the client is finally getting smarter."
            },
            {
                "key": "D",
                "textVi": "Chuyển sang kiểm tra mục tiêu ban đầu của phiên xem có khớp với phát hiện này không.",
                "textEn": "Revert to checking the initial agenda to ensure it matches this finding."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: PCC Marker 7.5 & 7.7 cho phép khách hàng trải nghiệm trọn vẹn khoảnh khắc thức tỉnh (Aha moment) và mở rộng nhận thức trước khi vội vã chuyển sang hành động. WORST là A: Nhảy cóc vào giao bài tập làm triệt tiêu sự chuyển hóa sâu sắc nội tâm.",
        "explanationEn": "BEST is B: PCC Markers 7.5 & 7.7 allow the client to integrate transformative breakthrough before moving into action. WORST is A: Rushing to superficial task homework prematurely curtails profound transformation.",
        "primaryCompetency": "7. Evokes Awareness / PCC Marker 7.5 & 7.7 (Integrating Insight)",
        "keyClueVi": "Tôn trọng khoảnh khắc thức tỉnh & tích hợp insight",
        "keyClueEn": "Honoring breakthrough insight & deep integration",
        "difficulty": "medium",
        "orderIndex": 35
    },
    {
        "id": "Q36",
        "questionVi": "Khách hàng miêu tả cảm giác lãnh đạo tổ chức qua cơn khủng hoảng: 'Tôi cảm thấy mình như một thuyền trưởng đang chèo lái con tàu qua tâm bão giữa đại dương gầm thét'.",
        "questionEn": "The client describes steering through organizational crisis: 'I feel like a ship captain navigating through the vortex of a raging hurricane at sea.'",
        "options": [
            {
                "key": "A",
                "textVi": "Phản hồi: 'Con tàu đó có trang bị radar không?' để cố gắng hiểu theo nghĩa đen.",
                "textEn": "Ask: 'Does the ship have radar installed?' trying to interpret literally."
            },
            {
                "key": "B",
                "textVi": "Mời khách hàng khám phá chiều sâu từ chính ẩn dụ của họ: 'Trong tâm bão dữ dội đó, người thuyền trưởng bên trong bạn đang neo giữ vào điều gì để giữ cho con tàu vững vàng?'.",
                "textEn": "Invite exploration within their own metaphor: 'In that raging storm, what is the captain within you anchored to in order to keep the ship steady?'."
            },
            {
                "key": "C",
                "textVi": "Kể chuyện Coach từng đi du thuyền bị say sóng để tạo sự đồng cảm.",
                "textEn": "Tell a personal story of getting seasick on a cruise to build rapport."
            },
            {
                "key": "D",
                "textVi": "Khuyên khách hàng nên đổi ẩn dụ khác vì ẩn dụ bão biển nghe quá tiêu cực.",
                "textEn": "Advise changing metaphors because ocean storms sound excessively negative."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "C",
        "explanationVi": "BEST là B: PCC Marker 7.8 sử dụng ẩn dụ của chính khách hàng để khai phóng nhận thức nội tại và năng lực tiềm ẩn. WORST là C: Đưa trải nghiệm cá nhân của Coach làm loãng không gian khai vấn.",
        "explanationEn": "BEST is B: PCC Marker 7.8 leverages client-generated metaphors to evoke profound self-awareness and inner fortitude. WORST is C: Injecting the Coach's trivial anecdote derails the client's metaphorical exploration.",
        "primaryCompetency": "7. Evokes Awareness / PCC Marker 7.8 (Client Metaphor)",
        "keyClueVi": "Khai thác ẩn dụ của chính khách hàng",
        "keyClueEn": "Leveraging client's own organic metaphor",
        "difficulty": "easy",
        "orderIndex": 36
    },
    {
        "id": "Q37",
        "questionVi": "Sau khi có nhận thức mới, khách hàng hưng phấn lập danh sách 10 hành động khổng lồ dự định hoàn thành ngay trong 3 ngày tới, dù lịch làm việc thực tế đã kín mít.",
        "questionEn": "Energized by new awareness, the client excitedly lists 10 colossal action items to complete over the next 3 days, despite having an already packed calendar.",
        "options": [
            {
                "key": "A",
                "textVi": "Cổ vũ nhiệt liệt và yêu cầu khách hàng phải cam kết thực hiện đủ 10 điều bằng mọi giá.",
                "textEn": "Applaud fervently and demand commitment to execute all 10 items at all costs."
            },
            {
                "key": "B",
                "textVi": "Đồng hành kiểm tra tính khả thi: 'Nhìn vào lịch trình bận rộn của bạn tuần này, 10 hành động này thực tế đến mức nào? Bước đi nhỏ đầu tiên nào sẽ tạo lực đẩy bền vững nhất mà không làm bạn quá tải?'.",
                "textEn": "Partner to explore feasibility: 'Looking realistically at your schedule, how feasible are these 10 actions? What small first step would build sustainable momentum without burnout?'."
            },
            {
                "key": "C",
                "textVi": "Gạch bỏ hết 9 điều và tự tay chọn giúp khách hàng điều duy nhất được làm.",
                "textEn": "Cross out 9 items unilaterally and dictate the only permissible action."
            },
            {
                "key": "D",
                "textVi": "Nói rằng khách hàng đang hão huyền và thiếu thực tế.",
                "textEn": "Tell the client they are completely delusional and impractical."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: PCC Marker 8.1 & 8.3 thiết kế hành động có tính khả thi, bền vững và do khách hàng làm chủ tốc độ. WORST là A: Ép cam kết phi thực tế dẫn đến thất bại và chán nản.",
        "explanationEn": "BEST is B: PCC Markers 8.1 & 8.3 partner on realistic, self-paced action design that builds sustainable momentum. WORST is A: Demanding adherence to unrealistic over-commitments guarantees failure and disillusionment.",
        "primaryCompetency": "8. Facilitates Client Growth / PCC Marker 8.1 & 8.3",
        "keyClueVi": "Thiết kế hành động khả thi & bước đi đầu tiên bền vững",
        "keyClueEn": "Designing feasible actions & sustainable first steps",
        "difficulty": "medium",
        "orderIndex": 37
    },
    {
        "id": "Q38",
        "questionVi": "Khách hàng nói với Coach: 'Tôi hay quên lắm, Coach hãy nhắn tin nhắc nhở tôi mỗi sáng lúc 7h để tôi hoàn thành mục tiêu tập thể dục nhé!'.",
        "questionEn": "The client tells the Coach: 'I am so forgetful; please text me every morning at 7 AM to ensure I do my workout routine!'",
        "options": [
            {
                "key": "A",
                "textVi": "Đồng ý ngay và cài đặt báo thức để nhắn tin kiểm tra khách hàng mỗi sáng.",
                "textEn": "Agree readily and set personal alarms to micromanage the client daily."
            },
            {
                "key": "B",
                "textVi": "Gợi mở trách nhiệm giải trình tự thân: 'Tôi luôn ở đây đồng hành cùng bạn; tuy nhiên, điều gì trong chính cuộc sống hay môi trường của bạn sẽ là hệ thống nhắc nhở hiệu quả nhất mà không cần phụ thuộc vào Coach?'.",
                "textEn": "Foster internal accountability: 'I am here partnering with you; however, what internal cues or environmental systems can you establish to sustain this without relying on me?'."
            },
            {
                "key": "C",
                "textVi": "Từ chối thẳng thừng và nói rằng Coach không phải là người giúp việc.",
                "textEn": "Refuse bluntly and declare that a Coach is not a personal babysitter."
            },
            {
                "key": "D",
                "textVi": "Đề xuất tính thêm phí dịch vụ tin nhắn nhắc nhở mỗi sáng.",
                "textEn": "Propose an extra recurring fee for daily reminder text services."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: PCC Marker 8.4 trao quyền tự chịu trách nhiệm giải trình (self-accountability) cho khách hàng thay vì tạo sự phụ thuộc vào Coach. WORST là A: Biến Coach thành người giám sát vi mô triệt tiêu tính tự chủ của khách hàng.",
        "explanationEn": "BEST is B: PCC Marker 8.4 anchors accountability firmly within the client's internal ecosystem rather than fostering dependency. WORST is A: Assuming micromanagement policing destroys adult-to-adult partnership.",
        "primaryCompetency": "8. Facilitates Client Growth / PCC Marker 8.4 (Accountability)",
        "keyClueVi": "Trách nhiệm giải trình tự thân (Self-Accountability)",
        "keyClueEn": "Self-accountability vs coach dependency",
        "difficulty": "medium",
        "orderIndex": 38
    },
    {
        "id": "Q39",
        "questionVi": "Khách hàng vừa hoàn thành xuất sắc một thương vụ đàm phán quan trọng nhưng khi chia sẻ lại xua tay: 'Ôi chẳng qua là ăn may thôi, người ta nhường tôi đấy chứ tôi có giỏi giang gì đâu'.",
        "questionEn": "The client successfully closed a crucial negotiation but dismisses it: 'Oh it was pure luck; they took pity on me, not because of any talent.'",
        "options": [
            {
                "key": "A",
                "textVi": "Gật đầu đồng ý rằng may mắn là yếu tố quyết định trong kinh doanh và hỏi về thương vụ tiếp theo.",
                "textEn": "Nod in agreement that luck decides business and ask about the next deal."
            },
            {
                "key": "B",
                "textVi": "Mời khách hàng dừng lại để ghi nhận: 'Dù may mắn có thể góp phần, nhưng những năng lực, sự chuẩn bị và phẩm chất nào của chính bạn đã tạo điều kiện cho kết quả này xảy ra?'.",
                "textEn": "Invite the client to acknowledge their agency: 'While circumstance played a role, what specific preparation, resilience, and strengths of your own made this outcome possible?'."
            },
            {
                "key": "C",
                "textVi": "Bắt khách hàng phải viết một bức thư cảm ơn đối tác vì đã nhường nhịn mình.",
                "textEn": "Instruct the client to write a thank-you letter to the partner for being lenient."
            },
            {
                "key": "D",
                "textVi": "Phê bình khách hàng vì thái độ khiêm tốn giả tạo.",
                "textEn": "Criticize the client for displaying false modesty."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: PCC Marker 8.7 đồng hành cùng khách hàng để ghi nhận tiến bộ và tôn vinh năng lực nội tại. WORST là A: Đồng tình gạt bỏ nỗ lực của khách hàng làm củng cố hội chứng tự ti.",
        "explanationEn": "BEST is B: PCC Marker 8.7 partners with client to acknowledge progress, validate self-worth, and celebrate intrinsic competence. WORST is A: Validating self-diminishment deepens feelings of inadequacy.",
        "primaryCompetency": "8. Facilitates Client Growth / PCC Marker 8.7 (Celebrating Growth)",
        "keyClueVi": "Ghi nhận tiến bộ & tôn vinh năng lực nội tại",
        "keyClueEn": "Acknowledging progress & celebrating intrinsic competence",
        "difficulty": "easy",
        "orderIndex": 39
    },
    {
        "id": "Q40",
        "questionVi": "Ở những phút cuối cùng của phiên khai vấn, sau khi khách hàng đã có nhiều phát hiện và dự định hành động, Coach muốn khép lại phiên một cách trọn vẹn.",
        "questionEn": "In the closing minutes of a fruitful coaching session, after multiple breakthroughs and actions are identified, the Coach intends to close gracefully.",
        "options": [
            {
                "key": "A",
                "textVi": "Coach tự tổng kết lại toàn bộ bài học và chỉ ra cho khách hàng biết họ cần nhớ những gì.",
                "textEn": "Coach summarizes all takeaways and dictates what the client must remember."
            },
            {
                "key": "B",
                "textVi": "Mời khách hàng tự đúc kết: 'Nhìn lại hành trình phiên hôm nay, bạn đang mang theo nhận thức quan trọng nào về chính mình, và bài học đó sẽ đồng hành cùng bạn thế nào trong tuần tới?'.",
                "textEn": "Invite client self-distillation: 'Looking back at our journey today, what meaningful takeaway about yourself are you carrying forward, and how will it accompany you this week?'."
            },
            {
                "key": "C",
                "textVi": "Vội vàng ngắt kết nối cuộc gọi để kịp giờ nghỉ ngơi cá nhân.",
                "textEn": "Abruptly disconnect the call to make time for a personal break."
            },
            {
                "key": "D",
                "textVi": "Yêu cầu khách hàng hứa sẽ không bao giờ mắc lại sai lầm cũ nữa.",
                "textEn": "Demand the client promise never to repeat past mistakes again."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: PCC Marker 8.8 trao quyền cho khách hàng tự tổng hợp và tích hợp bài học học được về bản thân. WORST là A: Coach làm thay khách hàng biến phiên khai vấn thành bài giảng lý thuyết.",
        "explanationEn": "BEST is B: PCC Marker 8.8 invites the client to integrate and articulate their own learning and growth. WORST is A: The Coach hijacking closing takeaways reduces partnering to a top-down lecture.",
        "primaryCompetency": "8. Facilitates Client Growth / PCC Marker 8.8 (Closing Integration)",
        "keyClueVi": "Khách hàng tự đúc kết & tích hợp nhận thức về bản thân",
        "keyClueEn": "Client integrates & articulates learning about self",
        "difficulty": "easy",
        "orderIndex": 40
    },
    {
        "id": "Q41",
        "questionVi": "Trong phiên, khách hàng bộc lộ ý định tự tử rõ ràng, nói rằng họ đã chuẩn bị sẵn thuốc và không còn muốn sống qua đêm nay.",
        "questionEn": "During a session, the client reveals explicit suicidal intent, disclosing they have lethal medication prepared and do not wish to survive tonight.",
        "options": [
            {
                "key": "A",
                "textVi": "Giữ bí mật tuyệt đối theo nguyên tắc bảo mật khai vấn và hứa sẽ không nói với bất kỳ ai.",
                "textEn": "Maintain absolute confidentiality and promise never to disclose this to anyone."
            },
            {
                "key": "B",
                "textVi": "Ưu tiên an toàn tính mạng hàng đầu: giữ sự bình tĩnh, duy trì kết nối nhân văn, thông báo ngay cho người liên hệ khẩn cấp/cơ quan y tế cứu hộ theo quy trình an toàn và điều khoản miễn trừ bảo mật của ICF.",
                "textEn": "Prioritize life safety above all: remain composed, maintain compassionate connection, contact designated emergency services/contacts immediately under ICF emergency confidentiality exception."
            },
            {
                "key": "C",
                "textVi": "Tiếp tục đặt các câu hỏi khai vấn sâu về mục tiêu cuộc đời khách hàng để giúp họ tìm lại ý nghĩa sống.",
                "textEn": "Continue standard deep coaching questions on life purpose to inspire meaning."
            },
            {
                "key": "D",
                "textVi": "Trách mắng khách hàng vì suy nghĩ tiêu cực và làm ảnh hưởng tâm lý của Coach.",
                "textEn": "Admonish the client for negative thoughts that affect the Coach's mental state."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: Chuẩn mực đạo đức ICF 2025 quy định ngoại lệ bảo mật tuyệt đối khi có nguy cơ đe dọa tính mạng sắp xảy ra. An toàn tính mạng là tối thượng. WORST là A: Giữ bí mật khi tính mạng bị đe dọa là sự vô cảm và vi phạm đạo đức nghiêm trọng.",
        "explanationEn": "BEST is B: ICF 2025 Ethics unequivocally mandates breaching confidentiality when imminent danger to life exists; safety is supreme. WORST is A: Concealing imminent suicide under false confidentiality is fatal negligence.",
        "primaryCompetency": "1. Demonstrates Ethical Practice / Ethics 2.2 (Imminent Harm Exception)",
        "keyClueVi": "Nguy cơ tính mạng & ngoại lệ phá vỡ bảo mật khẩn cấp",
        "keyClueEn": "Imminent harm & emergency confidentiality exception",
        "difficulty": "hard",
        "orderIndex": 41
    },
    {
        "id": "Q42",
        "questionVi": "Coach vừa hoàn thành khóa đào tạo PCC và đang chuẩn bị nộp hồ sơ thi, chưa nhận chứng chỉ chính thức. Trong hồ sơ năng lực gửi cho một tập đoàn lớn, Coach muốn tạo ấn tượng mạnh.",
        "questionEn": "A Coach has finished PCC-level training and is preparing the exam portfolio but has not received the official credential. To impress a large corporate client, the Coach prepares marketing collateral.",
        "options": [
            {
                "key": "A",
                "textVi": "Ghi danh xưng là 'ICF PCC Certified Coach' vì đằng nào mình cũng sắp đỗ.",
                "textEn": "Claim the title 'ICF PCC Certified Coach' assuming passing is inevitable."
            },
            {
                "key": "B",
                "textVi": "Mô tả trung thực và chính xác trình độ hiện tại (ví dụ: 'ACC, PCC Candidate' hoặc 'Hoàn thành chương trình Level 2') tuân thủ nghiêm ngặt quy định thương hiệu ICF.",
                "textEn": "Accurately state current credentials (e.g., 'ACC, PCC Candidate' or 'Completed Level 2 training') in strict adherence to ICF branding and ethical guidelines."
            },
            {
                "key": "C",
                "textVi": "Tự nhận là MCC (Master Certified Coach) để có thể tính mức phí cao gấp đôi.",
                "textEn": "Falsely claim MCC (Master Certified Coach) status to double the billing rate."
            },
            {
                "key": "D",
                "textVi": "Không cần ghi chứng chỉ nào và bảo rằng ICF không có giá trị gì.",
                "textEn": "Omit credentials entirely and claim ICF credentials carry zero value."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "C",
        "explanationVi": "BEST là B: Chuẩn mực đạo đức ICF (Section 3.5) yêu cầu trung thực tuyệt đối về chứng chỉ và năng lực chuyên môn. WORST là C: Mạo danh cấp độ chứng chỉ cao cấp là hành vi lừa dối nghiêm trọng nhất.",
        "explanationEn": "BEST is B: ICF Ethics 3.5 mandates absolute veracity regarding coaching qualifications and credentials. WORST is C: Falsely claiming highest-tier credentials constitutes egregious fraud.",
        "primaryCompetency": "1. Demonstrates Ethical Practice / Ethics 3.5 (Accurate Credentials)",
        "keyClueVi": "Tính trung thực về chứng chỉ chuyên môn ICF",
        "keyClueEn": "Veracity in ICF credentials & marketing claims",
        "difficulty": "easy",
        "orderIndex": 42
    },
    {
        "id": "Q43",
        "questionVi": "Coach muốn ghi âm phiên khai vấn để làm tư liệu nộp hồ sơ đánh giá chứng chỉ PCC lên ICF.",
        "questionEn": "The Coach wishes to record a coaching session to submit as an audio performance evaluation for ICF PCC credentialing.",
        "options": [
            {
                "key": "A",
                "textVi": "Bí mật bấm nút ghi âm từ đầu phiên, nếu phiên diễn ra xuất sắc thì mới hỏi xin phép khách hàng sau.",
                "textEn": "Secretly record from the start; only ask permission afterwards if the session turns out stellar."
            },
            {
                "key": "B",
                "textVi": "Giải thích rõ ràng mục đích ghi âm trước phiên, cung cấp văn bản thỏa thuận đồng thuận có thông tin (Informed Consent), tôn trọng quyền từ chối của khách hàng và chỉ ghi âm khi được đồng ý bằng văn bản.",
                "textEn": "Explain the recording purpose prior to the session, provide an informed consent document detailing storage and ICF review, respect refusal, and record only with explicit written consent."
            },
            {
                "key": "C",
                "textVi": "Tuyên bố rằng việc ghi âm là bắt buộc theo quy định của ICF và khách hàng không có quyền từ chối.",
                "textEn": "Claim recording is mandatory under ICF law and the client has no right to decline."
            },
            {
                "key": "D",
                "textVi": "Đăng đoạn ghi âm lên mạng xã hội để xin ý kiến đánh giá từ cộng đồng mạng.",
                "textEn": "Post the recording publicly on social media to solicit crowd-sourced feedback."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "D",
        "explanationVi": "BEST là B: Chuẩn mực đạo đức ICF (Ethics 2.1 & 2.4) yêu cầu có sự đồng thuận có hiểu biết (Informed Consent) bằng văn bản trước khi ghi âm. WORST là D: Đăng tải bản ghi âm của khách hàng lên không gian công cộng phá hủy tính bảo mật.",
        "explanationEn": "BEST is B: ICF Ethics 2.1 & 2.4 requires advance written informed consent explaining storage and purpose. WORST is D: Publicly posting confidential recordings is a catastrophic ethics violation.",
        "primaryCompetency": "1. Demonstrates Ethical Practice / Ethics 2.1–2.4 (Informed Consent)",
        "keyClueVi": "Đồng thuận có hiểu biết (Informed Consent) & ghi âm phiên",
        "keyClueEn": "Informed consent & recording confidentiality",
        "difficulty": "medium",
        "orderIndex": 43
    },
    {
        "id": "Q44",
        "questionVi": "Khách hàng chia sẻ quan điểm tôn giáo và triết lý sống trái ngược hoàn toàn với niềm tin thiêng liêng nhất của Coach. Coach cảm thấy sự bất đồng quan điểm sâu sắc làm giảm đi sự tôn trọng đối với khách hàng.",
        "questionEn": "The client shares spiritual and philosophical beliefs that directly conflict with the Coach's sacred convictions. The Coach feels profound ideological dissonance eroding respect.",
        "options": [
            {
                "key": "A",
                "textVi": "Tận dụng phiên khai vấn để tranh luận và khai sáng cho khách hàng thấy chân lý tôn giáo đúng đắn.",
                "textEn": "Use the session to debate and enlighten the client on correct spiritual truths."
            },
            {
                "key": "B",
                "textVi": "Nhận diện định kiến cá nhân, tìm kiếm sự tham vấn từ Coach Giám sát (Coaching Supervision); nếu nhận thấy không thể giữ được sự trung lập tôn trọng vô điều kiện, chủ động chuyển giao khách hàng một cách nhân văn.",
                "textEn": "Recognize personal bias, seek coaching supervision; if unable to maintain unconditional positive regard and neutrality, ethically initiate a compassionate referral."
            },
            {
                "key": "C",
                "textVi": "Gỉa vờ đồng ý với khách hàng nhưng ngầm mỉa mai qua các câu hỏi gài bẫy.",
                "textEn": "Feign agreement while subtly mocking the client through loaded trap questions."
            },
            {
                "key": "D",
                "textVi": "Đơn phương cắt đứt liên lạc với khách hàng mà không đưa ra lý do.",
                "textEn": "Ghost the client unilaterally without providing any professional explanation."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: Năng lực 2 & Đạo đức ICF đòi hỏi Coach quản lý định kiến thông qua Coaching Supervision hoặc chuyển giao có đạo đức khi không thể phục vụ khách hàng tốt nhất. WORST là A: Truyền bá tôn giáo/đức tin cá nhân trong không gian khai vấn.",
        "explanationEn": "BEST is B: Competency 2 and Ethics require processing personal triggers via supervision and referring ethically if unconditional positive regard is impossible. WORST is A: Proselytizing personal religious dogma during coaching.",
        "primaryCompetency": "2. Embodies a Coaching Mindset / Supervision & Neutrality",
        "keyClueVi": "Xung đột niềm tin thiêng liêng & tìm kiếm Coach Giám sát",
        "keyClueEn": "Value conflict & seeking coaching supervision",
        "difficulty": "hard",
        "orderIndex": 44
    },
    {
        "id": "Q45",
        "questionVi": "Trong chương trình khai vấn lãnh đạo do doanh nghiệp chi trả, khách hàng bắt đầu phiên bằng việc khóc nức nở về sự đổ vỡ hôn nhân gia đình và muốn dành các phiên tiếp theo để tháo gỡ chuyện tình cảm cá nhân.",
        "questionEn": "In a corporate-sponsored executive coaching program, the client starts the session sobbing about marriage breakdown, wishing to dedicate future sessions to marital therapy.",
        "options": [
            {
                "key": "A",
                "textVi": "Lập tức báo cáo với bộ phận Nhân sự của công ty về việc khách hàng gặp trục trặc gia đình.",
                "textEn": "Immediately inform corporate HR that the client is having domestic problems."
            },
            {
                "key": "B",
                "textVi": "Dành sự đồng cảm nhân văn, cùng khách hàng nhìn lại phạm vi thỏa thuận 3 bên với doanh nghiệp; thảo luận ranh giới giữa khai vấn lãnh đạo và tư vấn hôn nhân gia đình, đồng thời gợi ý khách hàng tiếp cận chuyên gia tư vấn hôn nhân chuyên nghiệp.",
                "textEn": "Offer compassionate presence, review the tri-partite agreement scope together; discern boundaries between executive coaching and marriage counseling, and recommend certified marriage therapy."
            },
            {
                "key": "C",
                "textVi": "Nhận làm luôn tư vấn hôn nhân dù Coach chưa từng được đào tạo về liệu pháp gia đình.",
                "textEn": "Act as a marriage therapist despite having zero training in family counseling."
            },
            {
                "key": "D",
                "textVi": "Nói rằng chuyện gia đình vớ vẩn không thuộc hợp đồng và từ chối lắng nghe.",
                "textEn": "Call marital problems trivial and refuse to hear another word."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: Năng lực 3 & Đạo đức ICF xác định rõ ranh giới phạm vi thực hành (Scope of Practice) và tôn trọng hợp đồng 3 bên, hỗ trợ chuyển gửi chuyên môn thích hợp. WORST là A: Tiết lộ đời tư cá nhân cho doanh nghiệp vi phạm nghiêm trọng tính bảo mật.",
        "explanationEn": "BEST is B: Competency 3 & Ethics maintain scope of practice boundaries while honoring tri-partite confidentiality and facilitating proper therapy referrals. WORST is A: Disclosing private marital breakdown to HR breaches confidentiality.",
        "primaryCompetency": "3. Establishes and Maintains Agreements / Scope of Practice",
        "keyClueVi": "Ranh giới phạm vi thực hành & chuyển gửi tư vấn gia đình",
        "keyClueEn": "Scope of practice & referral to family therapy",
        "difficulty": "medium",
        "orderIndex": 45
    },
    {
        "id": "Q46",
        "questionVi": "Khách hàng là một nhân viên trẻ mới được tuyển dụng, bước vào phiên khai vấn đầu tiên với sự lo sợ, nói rằng: 'Em sợ nói sai sẽ bị đuổi việc, vì em thấy Coach rất thân thiết với Giám đốc điều hành'.",
        "questionEn": "The client is a junior recruit entering their first session intimidated, stating: 'I fear speaking candidly might get me fired, seeing that the Coach is so close with our CEO.'",
        "options": [
            {
                "key": "A",
                "textVi": "Khoe khoang về mối quan hệ thân thiết với CEO để chứng minh quyền lực của mình.",
                "textEn": "Boast about the intimate connection with the CEO to demonstrate personal influence."
            },
            {
                "key": "B",
                "textVi": "Thấu cảm với nỗi lo về quyền lực bất cân xứng, giải thích cặn kẽ cam kết bảo mật độc lập tuyệt đối giữa Coach và Khách hàng; làm rõ rằng Coach là đối tác bình đẳng chỉ phục vụ sự phát triển của họ.",
                "textEn": "Empathize with power asymmetry anxiety, articulate ironclad confidentiality separating the Coach from corporate hierarchy; establish that coaching is a safe, equal partnership solely serving their growth."
            },
            {
                "key": "C",
                "textVi": "Bảo khách hàng rằng họ quá nhút nhát và không xứng đáng làm việc tại tập đoàn.",
                "textEn": "Tell the client they are too timid and unworthy of working at the enterprise."
            },
            {
                "key": "D",
                "textVi": "Hứa sẽ nói đỡ cho khách hàng trước mặt CEO để họ được tăng lương.",
                "textEn": "Promise to lobby the CEO to secure a salary raise for the client."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: Năng lực 4 (Cultivates Trust and Safety) nhận diện sự bất cân xứng quyền lực (power dynamics), thiết lập sự bình đẳng và cam kết bảo mật vững chắc. WORST là A: Dùng quyền lực uy hiếp khách hàng phá hủy hoàn toàn an toàn tâm lý.",
        "explanationEn": "BEST is B: Competency 4 addresses power dynamics, dismantles intimidation, and anchors robust confidentiality and unconditional equality. WORST is A: Leveraging relationship power over the client destroys psychological safety.",
        "primaryCompetency": "4. Cultivates Trust and Safety / Power Dynamics",
        "keyClueVi": "Bất cân xứng quyền lực & thiết lập an toàn tâm lý",
        "keyClueEn": "Power asymmetry & establishing psychological safety",
        "difficulty": "medium",
        "orderIndex": 46
    },
    {
        "id": "Q47",
        "questionVi": "Khách hàng đang hào hứng kể về kế hoạch khởi nghiệp, nhưng khi nhắc đến tên người cộng sự sáng lập thì giọng nói bỗng hạ thấp, ngập ngừng và thở dài thườn thượt.",
        "questionEn": "The client is enthusiastically narrating a startup plan, but when mentioning their co-founder's name, their tone suddenly drops, hesitating with a heavy sigh.",
        "options": [
            {
                "key": "A",
                "textVi": "Bỏ qua sự thay đổi này và giục khách hàng tiếp tục nói về kế hoạch kinh doanh.",
                "textEn": "Ignore the shift and urge the client to continue discussing business metrics."
            },
            {
                "key": "B",
                "textVi": "Nhẹ nhàng phản chiếu quan sát khách quan: 'Tôi nhận thấy khi nhắc đến tên người cộng sự, giọng bạn trầm xuống và có một tiếng thở dài. Điều gì đang hiện diện ở đó?'.",
                "textEn": "Gently reflect the objective observation: 'I noticed when naming your co-founder, your tone lowered and you took a deep sigh. What is present for you there?'."
            },
            {
                "key": "C",
                "textVi": "Khuyên khách hàng nên sa thải ngay người cộng sự đó trước khi quá muộn.",
                "textEn": "Advise immediately firing the co-founder before it is too late."
            },
            {
                "key": "D",
                "textVi": "Phỏng đoán rằng người cộng sự đã biển thủ tiền của công ty.",
                "textEn": "Speculate that the co-founder must have embezzled company funds."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "C",
        "explanationVi": "BEST là B: PCC Marker 6.2 ghi nhận sự thay đổi năng lượng và âm điệu cảm xúc, phản chiếu khách quan để mời khách hàng khám phá. WORST là C: Vội vã đưa ra lời khuyên chỉ đạo cực đoan.",
        "explanationEn": "BEST is B: PCC Marker 6.2 notices shifts in tone and energy, neutrally inviting the client to explore underlying dynamics. WORST is C: Jumping to rash, directive advice sabotages the coaching process.",
        "primaryCompetency": "6. Listens Actively / PCC Marker 6.2 (Energy & Tone Shift)",
        "keyClueVi": "Ghi nhận sự thay đổi âm điệu và tiếng thở dài",
        "keyClueEn": "Noticing vocal tone shifts & sigh reflections",
        "difficulty": "easy",
        "orderIndex": 47
    },
    {
        "id": "Q48",
        "questionVi": "Khách hàng đau khổ kể lại việc dự án trước đó của họ bị thất bại nặng nề: 'Tôi cảm thấy mình là một sự thất bại hoàn toàn và sẽ không bao giờ có thể dẫn dắt dự án nào thành công nữa'.",
        "questionEn": "The client laments a disastrous past project failure: 'I feel I am an utter failure and can never lead any successful project again.'",
        "options": [
            {
                "key": "A",
                "textVi": "Nói với khách hàng rằng họ nên quên đi quá khứ vì có khóc lóc cũng chẳng giải quyết được gì.",
                "textEn": "Tell the client to forget the past since crying changes nothing."
            },
            {
                "key": "B",
                "textVi": "Mời khách hàng tái định khung (Reframing): 'Sự việc đó quả thực rất nặng nề; nhưng nếu tách rời con người bạn ra khỏi sự cố đó, trải nghiệm này đã trao cho bạn sự kiên cường và bài học quý giá nào về nghệ thuật lãnh đạo?'.",
                "textEn": "Invite generative reframing: 'That event was deeply painful; yet separating your worth from that outcome, what resilience and wisdom did that ordeal forge in your leadership?'."
            },
            {
                "key": "C",
                "textVi": "Đồng tình rằng thất bại lớn như thế thì quả thực khó ai dám tin tưởng giao việc tiếp.",
                "textEn": "Agree that such a gigantic failure makes future trust nearly impossible."
            },
            {
                "key": "D",
                "textVi": "Chỉ trích các thành viên cũ trong nhóm của khách hàng là những kẻ vô trách nhiệm.",
                "textEn": "Criticize former team members as irresponsible culprits."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "C",
        "explanationVi": "BEST là B: PCC Marker 7.6 tái định khung (Reframing) giúp khách hàng tách biệt bản thể (WHO) khỏi sự kiện thất bại (WHAT) để tìm thấy bài học trưởng thành. WORST là C: Đồng tình hạ thấp giá trị nhân phẩm của khách hàng.",
        "explanationEn": "BEST is B: PCC Marker 7.6 helps the client reframe, decoupling intrinsic self-worth (WHO) from situational setbacks (WHAT) to discover growth. WORST is C: Reinforcing self-condemnation damages mental well-being.",
        "primaryCompetency": "7. Evokes Awareness / PCC Marker 7.6 (Reframing)",
        "keyClueVi": "Tái định khung (Reframing) & tách rời bản thể khỏi thất bại",
        "keyClueEn": "Generative reframing & separating WHO from failure",
        "difficulty": "medium",
        "orderIndex": 48
    },
    {
        "id": "Q49",
        "questionVi": "Khách hàng đã thiết lập một kế hoạch hành động rõ ràng để nói chuyện thẳng thắn với sếp về việc phân chia công việc. Tuy nhiên, khách hàng có tiền sử né tránh xung đột trong quá khứ.",
        "questionEn": "The client has formulated an action plan to have a candid conversation with their boss regarding workload. However, the client has a chronic pattern of conflict avoidance.",
        "options": [
            {
                "key": "A",
                "textVi": "Bỏ qua tiền sử né tránh và kết thúc phiên ngay lập tức để tiết kiệm thời gian.",
                "textEn": "Ignore conflict avoidance history and adjourn the session to save time."
            },
            {
                "key": "B",
                "textVi": "Đồng hành dự báo rào cản: 'Khi bước vào cuộc trò chuyện đó, rào cản hay phản xạ né tránh cũ nào có thể xuất hiện? Và nguồn lực hay neo cảm xúc nào sẽ giúp bạn giữ vững sự can đảm và chính trực?'.",
                "textEn": "Partner in anticipating obstacles: 'Entering that dialogue, what old avoidance reflexes might emerge? What inner anchor or resource will support you in standing firm in courage?'."
            },
            {
                "key": "C",
                "textVi": "Cảnh báo khách hàng rằng nếu lần này tiếp tục hèn nhát né tránh thì phiên khai vấn hoàn toàn vô nghĩa.",
                "textEn": "Warn the client that cowardice will render the entire coaching engagement worthless."
            },
            {
                "key": "D",
                "textVi": "Đề nghị đi cùng khách hàng đến gặp sếp để làm trọng tài phân xử.",
                "textEn": "Offer to accompany the client to the meeting to referee the confrontation."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "C",
        "explanationVi": "BEST là B: PCC Marker 8.5 & 8.6 hỗ trợ khách hàng dự báo rào cản tiềm ẩn và kích hoạt nguồn lực bên trong để thành công. WORST là C: Nhục mạ khách hàng phá hủy hoàn toàn mối quan hệ khai vấn.",
        "explanationEn": "BEST is B: PCC Markers 8.5 & 8.6 partner with the client to anticipate internal obstacles and anchor supporting resources. WORST is C: Shaming the client destroys trust and emotional safety.",
        "primaryCompetency": "8. Facilitates Client Growth / PCC Marker 8.5–8.6 (Anticipating Obstacles)",
        "keyClueVi": "Dự báo rào cản tiềm ẩn & kích hoạt nguồn lực bên trong",
        "keyClueEn": "Anticipating internal obstacles & anchoring inner resources",
        "difficulty": "medium",
        "orderIndex": 49
    },
    {
        "id": "Q50",
        "questionVi": "Đây là phiên khai vấn cuối cùng trong chuỗi 6 tháng đồng hành. Khách hàng đã đạt được toàn bộ mục tiêu đề ra ban đầu và cảm thấy rất tự hào.",
        "questionEn": "This is the concluding session of a 6-month coaching journey. The client has successfully achieved all initial goals and feels proud.",
        "options": [
            {
                "key": "A",
                "textVi": "Dành phần lớn thời gian phiên để chào mời khách hàng ký tiếp gói hợp đồng 12 tháng tiếp theo với giá ưu đãi.",
                "textEn": "Spend most of the session aggressively pitching a discounted 12-month renewal package."
            },
            {
                "key": "B",
                "textVi": "Đồng hành cùng khách hàng điểm lại bức tranh chuyển hóa toàn diện trong 6 tháng qua, tôn vinh sự trưởng thành nội tại, và xác định cách thức khách hàng duy trì tư duy tự khai vấn bền vững trong tương lai.",
                "textEn": "Partner with the client to review the overall 6-month transformational journey, celebrate internal expansion, and design sustainable self-coaching practices for the future."
            },
            {
                "key": "C",
                "textVi": "Tự nhận phần lớn công lao thành công của khách hàng là nhờ vào phương pháp khai vấn siêu việt của Coach.",
                "textEn": "Claim the majority of the credit for the client's success due to superior coaching techniques."
            },
            {
                "key": "D",
                "textVi": "Kết thúc phiên chỉ sau 5 phút vì mọi việc đã xong xuôi.",
                "textEn": "Terminate the final session after 5 minutes since all goals are met."
            }
        ],
        "bestAnswer": "B",
        "worstAnswer": "A",
        "explanationVi": "BEST là B: PCC Marker 8.7 & 8.8 tôn vinh thành quả trọn vẹn, khép lại hành trình có ý nghĩa và thúc đẩy tính tự chủ độc lập bền vững của khách hàng. WORST là A: Biến phiên bế mạc thành cơ hội chào hàng thương mại phá vỡ trải nghiệm chuyển hóa thiêng liêng.",
        "explanationEn": "BEST is B: PCC Markers 8.7 & 8.8 celebrate holistic transformation, anchor independent self-coaching habits, and honor closure. WORST is A: Turning a sacred closing session into commercial hard-selling degrades professionalism.",
        "primaryCompetency": "8. Facilitates Client Growth / Engagement Completion & Sustainable Growth",
        "keyClueVi": "Tổng kết hành trình dài hạn & duy trì tự khai vấn bền vững",
        "keyClueEn": "Comprehensive journey review & sustainable self-coaching",
        "difficulty": "medium",
        "orderIndex": 50
    }
]

# Ensure sectionId and type are populated
for q in new_questions:
    q["sectionId"] = None
    q["type"] = "icf_sjt"

# Combine Q01-Q16 and Q17-Q50
all_50_questions = existing_16 + new_questions

print(f"Total questions compiled: {len(all_50_questions)}")
assert len(all_50_questions) == 50, f"Expected 50 questions, got {len(all_50_questions)}"

# Write to scripts/sjt_50_data.py
with open("scripts/sjt_50_data.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nPre-compiled 50 authentic ICF SJT practice questions with dual BEST/WORST scoring.\n"""\n\n')
    f.write("def generate_sjt_50():\n")
    f.write("    return " + json.dumps(all_50_questions, indent=4, ensure_ascii=False) + "\n")

print("Successfully written scripts/sjt_50_data.py!")
