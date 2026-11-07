# -*- coding: utf-8 -*-
"""
Update Module 1 and Module 2 in scripts/icf_curriculum_data.py to 2025 standards:
- Module 1: 8 Core Competencies (2025 Edition, published Sept 2025), with 2019 comparison notes & exam clarity
- Module 2: Code of Ethics 2025 (Effective 01/04/2025), with 5 parts / 24 standards, 4 Core Values, and 2020 exam archive
"""
import re

with open('scripts/icf_curriculum_data.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Verify no "thân chủ" exists
assert 'thân chủ' not in code.lower(), "Found 'thân chủ' in existing file!"

# Replace Module 1 Lessons
NEW_M1 = r'''MODULE_1_LESSONS = [
    {
        "id": "mod1-les1",
        "moduleId": "mod-1",
        "lessonNumber": 1,
        "titleVi": "Năng Lực 1: Thể Hiện Thực Hành Đạo Đức (Bản 2025)",
        "titleEn": "Competency 1: Demonstrates Ethical Practice (2025 Edition)",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu định nghĩa chuẩn của Năng lực 1 theo Khung năng lực ICF 2025 mới nhất.",
            "Nắm vững 7 chỉ dấu hành vi chính thức (1.01–1.07): chính trực, nhạy cảm bản sắc, ngôn ngữ tôn trọng, bảo mật và giới hạn chuyển gửi.",
            "Phân biệt chuẩn thực hành hiện hành (2025) và chuẩn đề thi viết trên Pearson VUE (hiện đang dùng chuẩn 2019)."
        ],
        "objectivesEn": [
            "Master the official definition of Competency 1 under the updated ICF 2025 framework.",
            "Identify 7 core behaviors (1.01–1.07): integrity, identity sensitivity, respectful language, confidentiality, and referral boundaries.",
            "Distinguish current practice standard (2025) from the written exam baseline (2019)."
        ],
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025) & Bộ Quy Tắc Đạo Đức",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Understands and consistently applies coaching ethics and standards of coaching. 1.01 Demonstrates personal integrity and honesty in interactions with clients, sponsors and relevant stakeholders. 1.02 Is sensitive to clients' identity, environment, experiences, values and beliefs. 1.03 Uses language appropriate and respectful to clients, sponsors and relevant stakeholders. 1.04 Abides by the ICF Code of Ethics and upholds the Core Values. 1.05 Maintains confidentiality with client information per stakeholder agreements and pertinent laws. 1.06 Maintains the distinctions between coaching, consulting, psychotherapy and other support professions. 1.07 Refers clients to other support professionals, as appropriate.",
        "translationVi": "Định nghĩa: Hiểu và nhất quán áp dụng các chuẩn mực đạo đức và tiêu chuẩn khai vấn của ICF. 1.01 Thể hiện sự chính trực và trung thực cá nhân khi tương tác với khách hàng, nhà tài trợ và các bên liên quan. 1.02 Nhạy bén với bản sắc, môi trường, trải nghiệm, giá trị và niềm tin của khách hàng. 1.03 Sử dụng ngôn ngữ phù hợp và tôn trọng khách hàng, nhà tài trợ và các bên liên quan. 1.04 Tuân thủ Bộ Quy tắc Đạo đức ICF và phát huy các Giá trị Cốt lõi. 1.05 Duy trì tính bảo mật thông tin khách hàng theo thỏa thuận các bên và luật pháp hiện hành. 1.06 Giữ vững sự phân biệt giữa khai vấn, tư vấn chuyên gia, trị liệu tâm lý và các nghề trợ giúp khác. 1.07 Chuyển gửi khách hàng sang các chuyên gia trợ giúp khác khi phù hợp.",
        "comparison2019Vi": "So sánh 2019–2025: Bản 2025 tăng cường các quy định về bảo vệ quyền riêng tư kỹ thuật số, an toàn dữ liệu số khi sử dụng công cụ AI, và nhấn mạnh sâu sắc hơn về tính nhạy cảm liên văn hóa cũng như ranh giới quyền lực trong thỏa thuận ba bên.",
        "comparison2019En": "2019 vs 2025 Comparison: The 2025 update reinforces digital privacy safeguards, responsible use of AI tools, and deepens cross-cultural sensitivity and systemic power boundaries.",
        "commentaryVi": "Năng lực 1 là nền móng của toàn bộ ngôi nhà năng lực ICF. Điểm mấu chốt trong các tình huống thi viết SJT: Coach phải luôn bảo vệ tính bảo mật, minh bạch với nhà tài trợ về giới hạn báo cáo, không bao giờ tự ý chẩn đoán tâm lý và luôn tôn trọng sự tự quyết của khách hàng khi đề xuất chuyển gửi.",
        "commentaryEn": "Competency 1 is the bedrock of the ICF framework. Crucial exam insight: The coach must always safeguard confidentiality, clarify reporting boundaries with sponsors, never diagnose mental disorders, and honor client autonomy during referrals.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Tình huống: Khách hàng tâm sự trong phiên rằng họ đang chịu áp lực kinh khủng và nhiều lần nghĩ đến việc bỏ việc, nhưng yêu cầu coach không được kể với Giám đốc Nhân sự (người trả tiền hợp đồng). Coach ứng xử chuẩn mực: Khẳng định sự bảo mật tuyệt đối của nội dung thảo luận cá nhân theo thỏa thuận ba bên, giúp khách hàng yên tâm rằng coach chỉ báo cáo tiến độ mục tiêu chung mà khách hàng đã duyệt trước.",
        "exampleContentEn": "Scenario: Client shares intense burnout and thoughts of quitting, pleading with the coach not to inform HR (the sponsor). Exemplary response: Reassure absolute confidentiality per the tripartite agreement, affirming that only high-level progress approved by the client will be reported.",
        "quiz": {
            "questionVi": "Khi nhà tài trợ (Sponsor) yêu cầu coach chia sẻ chi tiết nguyên nhân khiến khách hàng mất động lực trong các phiên gần đây, hành động chuẩn mực nhất theo Năng lực 1 là gì?",
            "questionEn": "When a corporate sponsor asks the coach to disclose specific personal reasons behind the client's recent demotivation, what is the most ethical action under Competency 1?",
            "options": [
                {"key": "A", "textVi": "Báo cáo đầy đủ mọi điều khách hàng đã nói vì nhà tài trợ là bên chi trả toàn bộ phí coaching.", "textEn": "Report everything disclosed since the sponsor pays all coaching fees."},
                {"key": "B", "textVi": "Từ chối thẳng thừng và lập tức chấm dứt hợp đồng với doanh nghiệp mà không cần giải thích.", "textEn": "Abruptly refuse and terminate the corporate engagement without explanation."},
                {"key": "C", "textVi": "Nhắc lại thỏa thuận bảo mật đã ký, giải thích rằng nội dung phiên là bí mật và chỉ chia sẻ tiến độ mục tiêu đã có sự đồng thuận của khách hàng.", "textEn": "Reiterate the signed confidentiality agreement, explaining session details are confidential and only agreed progress goals are shared."},
                {"key": "D", "textVi": "Khuyên nhà tài trợ tự bí mật theo dõi máy tính của khách hàng để biết nguyên nhân.", "textEn": "Advise the sponsor to secretly monitor the client's laptop to uncover reasons."}
            ],
            "correctAnswer": "C",
            "explanationVi": "Phương án C là chuẩn mực đạo đức cao nhất: Coach bảo vệ thỏa thuận bảo mật, tôn trọng khách hàng và hành xử chuyên nghiệp với nhà tài trợ.",
            "explanationEn": "Option C is exemplary: The coach upholds confidentiality, respects client trust, and maintains professionalism with the sponsor."
        }
    },
    {
        "id": "mod1-les2",
        "moduleId": "mod-1",
        "lessonNumber": 2,
        "titleVi": "Năng Lực 2: Thể Hiện Tư Duy Khai Vấn (Bản 2025)",
        "titleEn": "Competency 2: Embodies a Coaching Mindset (2025 Edition)",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu định nghĩa cập nhật 2025 về tư duy cởi mở, tò mò, linh hoạt và lấy khách hàng làm trung tâm.",
            "Nắm vững 10 chỉ dấu hành vi (2.01–2.10), bao gồm 2 chỉ dấu mới về phản tư liên tục và chăm sóc sức khỏe toàn diện (well-being).",
            "Hiểu việc chủ động tìm kiếm sự hỗ trợ chuyên môn qua Giám sát Khai vấn (Supervision) và Mentor Coaching."
        ],
        "objectivesEn": [
            "Understand the updated 2025 definition of open, curious, flexible, and client-centered mindset.",
            "Master the 10 behavioral indicators (2.01–2.10), including 2 new indicators on reflective practice and coach well-being.",
            "Learn proactive engagement with coach supervision and mentor coaching."
        ],
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025)",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Develops and maintains a mindset that is open, curious, flexible and client-centered. 2.01 Acknowledges that clients are responsible for their own choices. 2.02 Engages in ongoing learning and development as a coach. 2.03 Develops an ongoing reflective practice to enhance one's coaching. 2.04 Remains aware of and open to the influence of context and culture on self and others. 2.05 Uses awareness of self and one's intuition to benefit clients. 2.06 Develops and maintains the ability to regulate one's emotions. 2.07 Mentally and emotionally prepares for sessions. 2.08 Actively manages one's well-being to sustain high coaching quality. 2.09 Uses support from coaching supervisors, mentor coaches, or peers as needed. 2.10 Acknowledges that clients are autonomous within their systemic context.",
        "translationVi": "Định nghĩa: Phát triển và duy trì tư duy cởi mở, tò mò, linh hoạt và lấy khách hàng làm trung tâm. 2.01 Công nhận rằng khách hàng chịu trách nhiệm về các lựa chọn của chính họ. 2.02 Tham gia vào quá trình học tập và phát triển liên tục với tư cách là coach. 2.03 Phát triển thói quen phản tư liên tục để nâng cao năng lực khai vấn. 2.04 Luôn nhận thức và cởi mở với ảnh hưởng của bối cảnh và văn hóa lên bản thân và người khác. 2.05 Sử dụng sự tự nhận thức và trực giác vì lợi ích của khách hàng. 2.06 Phát triển và duy trì khả năng điều tiết cảm xúc của bản thân. 2.07 Chuẩn bị tâm trí và cảm xúc trước các phiên khai vấn. 2.08 Chủ động quản lý sức khỏe toàn diện (well-being) để duy trì chất lượng khai vấn. 2.09 Tìm kiếm sự trợ giúp từ chuyên gia giám sát khai vấn (supervisor), mentor coach hoặc đồng nghiệp khi cần thiết. 2.10 Tôn trọng tính tự chủ của khách hàng trong bối cảnh hệ sinh thái của họ.",
        "comparison2019Vi": "So sánh 2019–2025: Bản 2019 có 8 chỉ dấu (2.1–2.8). Bản 2025 bổ sung cụ thể việc chăm sóc sức khỏe toàn diện của coach (well-being, 2.08) và chính thức hóa việc tìm kiếm hỗ trợ từ Coaching Supervision/Mentor (2.09), đồng thời nhấn mạnh tính tự chủ trong bối cảnh hệ thống (systemic context, 2.10).",
        "comparison2019En": "2019 vs 2025 Comparison: The 2019 framework had 8 sub-competencies. The 2025 update expands this to 10 by explicitly integrating coach well-being (2.08), formal coach supervision/mentoring (2.09), and systemic autonomy (2.10).",
        "commentaryVi": "Tư duy khai vấn thể hiện ở việc coach không áp đặt 'đáp án mẫu' của mình lên khách hàng, mà tin tưởng sâu sắc vào năng lực tự tìm giải pháp của khách hàng. Coach dành thời gian tĩnh tâm trước phiên (Centering) và thường xuyên thực hành phản tư sau phiên.",
        "commentaryEn": "Embodying a coaching mindset means resisting giving ready-made answers and believing in client capability. The coach prepares mindfully before sessions and engages in deliberate reflective practice afterwards.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Sau một phiên coach mà khách hàng im lặng rất nhiều và không đưa ra hành động cụ thể nào, coach cảm thấy bồn chồn lo lắng. Thay vì đổ lỗi cho khách hàng, coach ngồi lại phản tư: 'Cảm giác bồn chồn này đến từ đâu trong tôi? Phải chăng tôi đang muốn chứng tỏ bản thân có ích hơn là tin tưởng vào nhịp điệu của khách hàng?'",
        "exampleContentEn": "After a session marked by long silences and no concrete action plan, the coach feels anxious. Instead of judging the client, the coach reflects: 'Where does my anxiety stem from? Am I trying to prove my competence rather than trusting the client's pace?'",
        "quiz": {
            "questionVi": "Hành vi nào sau đây thể hiện rõ nét nhất điểm bổ sung mới của Năng lực 2 trong Khung năng lực ICF 2025?",
            "questionEn": "Which behavior best exemplifies the newly updated focus of Competency 2 under the 2025 ICF framework?",
            "options": [
                {"key": "A", "textVi": "Coach soạn sẵn giáo án 10 buổi và bắt khách hàng tuân thủ lịch trình.", "textEn": "Prepare 10 syllabi beforehand and force client compliance."},
                {"key": "B", "textVi": "Coach chủ động chăm sóc sức khỏe thể chất, tinh thần (well-being) và định kỳ phản tư cùng Coach Supervisor để giữ chất lượng phiên coach.", "textEn": "Actively manage personal well-being and regularly engage in reflective practice with a Coach Supervisor."},
                {"key": "C", "textVi": "Coach tự nhận mình đã hoàn hảo và không cần học thêm bất kỳ điều gì mới.", "textEn": "Claim personal perfection and cease all professional development."},
                {"key": "D", "textVi": "Coach đưa ra lời khuyên tài chính cá nhân cho khách hàng.", "textEn": "Offer unsolicited personal financial advice to clients."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B phản ánh chính xác điểm mới của Bản 2025 (Chỉ dấu 2.08 và 2.09): Quản lý well-being của bản thân và sử dụng hỗ trợ từ Coach Supervision.",
            "explanationEn": "Option B accurately mirrors 2025 updates (2.08 & 2.09): Coach well-being management and engaging coach supervision."
        }
    },
    {
        "id": "mod1-les3",
        "moduleId": "mod-1",
        "lessonNumber": 3,
        "titleVi": "Năng Lực 3: Thiết Lập Và Duy Trì Thỏa Thuận (Bản 2025)",
        "titleEn": "Competency 3: Establishes and Maintains Agreements (2025 Edition)",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu thỏa thuận ở cả 2 cấp độ: Thỏa thuận toàn bộ tiến trình (Engagement) và Thỏa thuận từng phiên (Session).",
            "Nắm vững các chỉ dấu mở rộng 2025: Thỏa thuận về công nghệ số, bảo mật dữ liệu AI và sự phối hợp minh bạch với bên tài trợ (Sponsors).",
            "Làm chủ 4 yếu tố cốt lõi của thỏa thuận phiên PCC: Chủ đề, Mục tiêu cụ thể, Thước đo thành công và Ý nghĩa quan trọng."
        ],
        "objectivesEn": [
            "Understand agreements at engagement-level and session-level.",
            "Master 2025 expanded indicators: digital agreements, AI privacy consent, and sponsor/stakeholder boundaries.",
            "Master the 4 core session contracting elements: Topic, Outcome, Measures of Success, and Meaning."
        ],
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025)",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Partners with the client and relevant stakeholders to create clear agreements about the coaching relationship, process, plans and goals. Establishes agreements for the overall coaching engagement as well as those for each coaching session. Highlights: Explicit agreements on technology, tools, confidentiality, session outcomes, measures of success, and recontracting as needs evolve.",
        "translationVi": "Định nghĩa: Hợp tác với khách hàng và các bên liên quan để thiết lập các thỏa thuận rõ ràng về mối quan hệ, quy trình, kế hoạch và mục tiêu khai vấn. Thiết lập thỏa thuận cho toàn bộ hành trình cũng như cho từng phiên khai vấn cụ thể. Điểm nhấn: Thỏa thuận rõ ràng về công nghệ, bảo mật dữ liệu, kết quả phiên, thước đo thành công và linh hoạt tái thỏa thuận.",
        "comparison2019Vi": "So sánh 2019–2025: Bản 2025 chuẩn hóa ngôn ngữ hợp tác bình đẳng (partnering), làm rõ thỏa thuận đa bên (multi-stakeholder contracting) và bổ sung thỏa thuận minh bạch về việc sử dụng công nghệ số/AI hỗ trợ phiên coach.",
        "comparison2019En": "2019 vs 2025 Comparison: Refines partnering language, clarifies multi-stakeholder contracting, and introduces transparent agreement protocols for AI tools.",
        "commentaryVi": "Ở cấp độ PCC, thỏa thuận phiên không chỉ là 'Hôm nay muốn nói chuyện gì?', mà phải làm rõ 4 tầng: (1) Bạn muốn đạt kết quả cụ thể nào khi kết thúc phiên này? (2) Làm sao bạn biết mình đã đạt được kết quả đó? (3) Điều này quan trọng thế nào với bạn lúc này? (4) Chúng ta cần khám phá điều gì trước tiên để đạt được mục tiêu đó?",
        "commentaryEn": "At PCC level, session contracting goes beyond a casual topic to establish clear outcome, measurable success criteria, personal meaning, and focus areas.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Khách hàng nói: 'Tôi muốn nói về chuyện quản lý thời gian.' Coach phản hồi chuẩn PCC: 'Quản lý thời gian là một chủ đề rộng. Cụ thể vào cuối phiên hôm nay, kết quả hữu hình nào bạn muốn cầm về để cảm thấy phiên làm việc này thực sự trọn vẹn và hữu ích?'",
        "exampleContentEn": "Client: 'I want to talk about time management.' PCC Coach: 'Time management is broad. Specifically by the end of today's session, what tangible outcome do you want to walk away with so this conversation is truly worthwhile?'",
        "quiz": {
            "questionVi": "Khách hàng bước vào phiên với sự bức xúc và kể rất nhiều câu chuyện vụn vặt. Sau 15 phút, khách hàng vẫn chưa xác định được mục tiêu phiên. Hành động nào của Coach thể hiện đúng Năng lực 3 nhất?",
            "questionEn": "Client speaks rapidly about fragmented frustrations. After 15 minutes, no clear outcome is established. Which coach action best reflects Competency 3?",
            "options": [
                {"key": "A", "textVi": "Để khách hàng kể tiếp cho hết giờ vì ngắt lời là mất lịch sự.", "textEn": "Let the client talk uninterrupted until time runs out."},
                {"key": "B", "textVi": "Tự ý chọn một chủ đề mà coach thấy quan trọng và bắt khách hàng tập trung vào đó.", "textEn": "Unilaterally pick an important topic and force client focus."},
                {"key": "C", "textVi": "Nhẹ nhàng xin phép tạm dừng, phản chiếu những điều khách hàng vừa chia sẻ và hỏi: 'Trong tất cả những khía cạnh này, điều gì là quan trọng nhất bạn muốn chúng ta cùng giải quyết hôm nay?'", "textEn": "Gently pause, reflect what was shared, and ask: 'Among all these aspects, what is most essential for us to resolve today?'"},
                {"key": "D", "textVi": "Dừng phiên và trừ tiền vì khách hàng không có sự chuẩn bị mục tiêu trước.", "textEn": "Terminate the session and fine the client for lack of preparation."}
            ],
            "correctAnswer": "C",
            "explanationVi": "Phương án C thể hiện sự đồng hành bình đẳng (Partnering), giúp khách hàng cô đọng trọng tâm mà không áp đặt.",
            "explanationEn": "Option C demonstrates equal partnering, helping the client distill focus without coach imposition."
        }
    },
    {
        "id": "mod1-les4",
        "moduleId": "mod-1",
        "lessonNumber": 4,
        "titleVi": "Năng Lực 4: Nuôi Dưỡng Niềm Tin Và Sự An Toàn (Bản 2025)",
        "titleEn": "Competency 4: Cultivates Trust and Safety (2025 Edition)",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu việc kiến tạo không gian an toàn tâm lý toàn diện để khách hàng tự do chia sẻ tổn thương.",
            "Nắm vững các chỉ dấu 2025: Tôn trọng thế giới quan (Worldview), bản sắc văn hóa, trải nghiệm cá nhân và ranh giới tự tôn.",
            "Thực hành ứng xử phi phán xét khi khách hàng bộc lộ những quan điểm hoặc cảm xúc khác biệt."
        ],
        "objectivesEn": [
            "Understand creating comprehensive psychological safety for vulnerability.",
            "Master 2025 focus: honoring client worldview, cultural identity, lived experience, and personal boundaries.",
            "Practice non-judgmental presence when clients express divergent viewpoints or raw emotions."
        ],
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025)",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Partners with the client to create a safe, supportive environment that allows the client to share freely. Maintains a relationship of mutual respect and trust. Seeks to understand the client within their context which may include their identity, environment, experiences, values and beliefs.",
        "translationVi": "Định nghĩa: Hợp tác với khách hàng để tạo ra môi trường an toàn, hỗ trợ, cho phép khách hàng tự do chia sẻ. Duy trì mối quan hệ tôn trọng và tin cậy lẫn nhau. Tìm kiếm sự thấu hiểu khách hàng trong toàn bộ bối cảnh của họ, bao gồm bản sắc, môi trường sống, trải nghiệm, giá trị và niềm tin.",
        "comparison2019Vi": "So sánh 2019–2025: Bản 2025 nhấn mạnh sâu sắc thuật ngữ 'Thế giới quan' (Worldview) trong Phụ lục thuật ngữ và đưa sự nhạy bén văn hóa, an toàn chấn thương (trauma-sensitive) vào trọng tâm của việc xây dựng niềm tin.",
        "comparison2019En": "2019 vs 2025 Comparison: Integrates 'Worldview' terminology from the new glossary and deepens trauma-sensitive, inclusive cross-cultural safety.",
        "commentaryVi": "Niềm tin không đến từ những lời khen sáo rỗng hay trấn an vội vã. Niềm tin được xây dựng khi coach chứng thực (validate) cảm xúc của khách hàng, tôn trọng thế giới quan riêng biệt và giữ trọn vẹn bảo mật.",
        "commentaryEn": "Trust does not stem from superficial praise or hasty reassurance. It is cultivated when the coach validates emotions, honors the client's worldview, and safeguards confidentiality.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Khách hàng bật khóc và nói: 'Tôi cảm thấy mình là một người mẹ tồi tệ vì dành quá nhiều thời gian cho sự nghiệp.' Coach không vội nói 'Đừng khóc, bạn là người mẹ tuyệt vời mà!' (trấn an làm mất an toàn). Thay vào đó, coach tĩnh lặng, ánh mắt ấm áp: 'Tôi cảm nhận được tình yêu thương và sự giằng xé rất lớn trong bạn lúc này. Cứ từ từ, tôi ở đây cùng bạn.'",
        "exampleContentEn": "Client weeps: 'I feel like a terrible mother.' Rather than rushing to reassure 'Don't cry, you are great!', the coach holds safe space: 'I sense immense love and struggle in you right now. Take your time, I am right here with you.'",
        "quiz": {
            "questionVi": "Khách hàng chia sẻ một quan điểm tôn giáo hoặc chính trị hoàn toàn đối lập với niềm tin cá nhân của Coach. Hành động nào của Coach thể hiện đúng Năng lực 4?",
            "questionEn": "Client shares a religious or political belief contradicting the coach's personal values. Which action best reflects Competency 4?",
            "options": [
                {"key": "A", "textVi": "Tranh luận để chứng minh khách hàng đang có cái nhìn sai lệch.", "textEn": "Debate to prove the client's perspective is flawed."},
                {"key": "B", "textVi": "Tôn trọng thế giới quan của khách hàng, gác lại niềm tin cá nhân và tìm hiểu xem niềm tin đó đang hỗ trợ hoặc thách thức mục tiêu của khách hàng như thế nào.", "textEn": "Honor the client's worldview, suspend personal biases, and explore how that belief serves or challenges the client's goal."},
                {"key": "C", "textVi": "Giả vờ đồng ý nhiệt tình để lấy lòng khách hàng.", "textEn": "Pretend passionate agreement to please the client."},
                {"key": "D", "textVi": "Lập tức hủy phiên và từ chối làm việc với những người có quan điểm khác mình.", "textEn": "Immediately cancel the engagement due to differing views."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Tôn trọng bản sắc và thế giới quan của khách hàng (Worldview) là cốt lõi của Năng lực 4.",
            "explanationEn": "Honoring the client's identity and worldview without bias is the core of Competency 4."
        }
    },
    {
        "id": "mod1-les5",
        "moduleId": "mod-1",
        "lessonNumber": 5,
        "titleVi": "Năng Lực 5: Duy Trì Sự Hiện Diện (Bản 2025)",
        "titleEn": "Competency 5: Maintains Presence (2025 Edition)",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu trạng thái hiện diện trọn vẹn (fully conscious, present, observant, empathetic).",
            "Nắm vững khả năng làm việc với khoảng lặng, phản ứng cảm xúc mạnh và những điều chưa biết (holding space for the unknown).",
            "Thực hành điều tiết cảm xúc của chính coach trong phiên để không can thiệp hay vội vàng sửa chữa."
        ],
        "objectivesEn": [
            "Understand full presence: fully conscious, observant, and empathetic.",
            "Master working with silence, intense emotions, and holding space for ambiguity.",
            "Practice self-regulation to avoid interrupting or rushing to fix."
        ],
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025)",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Is fully conscious and present with the client, employing a style that is open, flexible, grounded and confident. Remains focused, observant, empathetic and responsive to the client. Demonstrates curiosity and manages one's emotions to stay present.",
        "translationVi": "Định nghĩa: Hoàn toàn tỉnh thức và hiện diện cùng khách hàng, sử dụng phong cách cởi mở, linh hoạt, vững vàng và tự tin. Luôn tập trung, quan sát, thấu cảm và phản hồi khách hàng. Thể hiện sự tò mò và kiểm soát cảm xúc bản thân để duy trì sự hiện diện.",
        "comparison2019Vi": "So sánh 2019–2025: Bản 2025 làm sâu sắc hơn năng lực hiện diện tĩnh tại (grounded presence) và khả năng thích ứng linh hoạt trước sự bất định cũng như các thay đổi cảm xúc phức tạp của khách hàng.",
        "comparison2019En": "2019 vs 2025 Comparison: Deepens grounded presence and relational agility when navigating ambiguity and complex emotional shifts.",
        "commentaryVi": "Hiện diện ở cấp độ PCC là không vội vã lấp đầy khoảng lặng. Khi khách hàng im lặng sau một câu hỏi sâu sắc, đó là lúc não bộ họ đang tái tổ chức các khớp thần kinh để sinh ra nhận thức mới. Coach chen ngang lúc này là phá hủy khoảnh khắc chuyển hóa.",
        "commentaryEn": "PCC presence means never rushing into silence. Client silence after deep inquiry indicates neural rewiring and emerging insight. Interrupting ruins the transformative breakthrough.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Sau câu hỏi của Coach: 'Nếu nỗi sợ này không còn tồn tại, bạn sẽ là ai?', khách hàng im lặng nhìn ra cửa sổ suốt 45 giây. Coach không nói thêm gì, chỉ duy trì ánh mắt bình an và nhịp thở đều đặn, kiên nhẫn chờ khách hàng xử lý xong suy nghĩ bên trong.",
        "exampleContentEn": "After coach asks 'Who would you be without this fear?', client gazes out the window in 45-second silence. Coach maintains calm, steady presence, giving the client space to process.",
        "quiz": {
            "questionVi": "Khi khách hàng chìm vào khoảng lặng sâu sắc kéo dài hơn 30 giây sau một câu hỏi mạnh, hành động nào của Coach thể hiện sự Hiện diện (Năng lực 5) cao nhất?",
            "questionEn": "When client enters a 30-second reflective silence after a powerful question, which coach action demonstrates highest Presence (Competency 5)?",
            "options": [
                {"key": "A", "textVi": "Hỏi ngay câu hỏi khác vì sợ khách hàng cảm thấy ngượng ngùng.", "textEn": "Quickly ask another question to ease perceived awkwardness."},
                {"key": "B", "textVi": "Gợi ý luôn câu trả lời mẫu để giúp khách hàng đỡ phải suy nghĩ nhiều.", "textEn": "Suggest ready-made answers to save client mental energy."},
                {"key": "C", "textVi": "Giữ vững sự tĩnh lặng bình an, duy trì sự chú tâm hoàn toàn vào khách hàng và tôn trọng tiến trình tư duy của họ.", "textEn": "Hold peaceful silence, maintain full attentiveness, and honor the client's internal thinking process."},
                {"key": "D", "textVi": "Tranh thủ mở điện thoại kiểm tra tin nhắn vì khách hàng đang không nói chuyện.", "textEn": "Check phone messages while the client is quiet."}
            ],
            "correctAnswer": "C",
            "explanationVi": "Tôn trọng và đồng hành cùng khoảng lặng là biểu hiện bậc thầy của Năng lực 5.",
            "explanationEn": "Holding and honoring silence is a masterful demonstration of Competency 5."
        }
    },
    {
        "id": "mod1-les6",
        "moduleId": "mod-1",
        "lessonNumber": 6,
        "titleVi": "Năng Lực 6: Lắng Nghe Chủ Động (Bản 2025)",
        "titleEn": "Competency 6: Listens Actively (2025 Edition)",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu lắng nghe đa tầng: Lắng nghe ngôn từ, cảm xúc, phi ngôn từ và những điều KHÔNG được nói ra.",
            "Nắm vững các chỉ dấu 2025: Lắng nghe trong bối cảnh hệ thống, thế giới quan và bản sắc văn hóa của khách hàng.",
            "Thực hành phản chiếu cô đọng và tích hợp các mô thức hành vi lặp đi lặp lại."
        ],
        "objectivesEn": [
            "Understand multi-level listening: words, emotions, somatic cues, and what remains UNSAID.",
            "Master 2025 focus: listening within systemic context, client worldview, and cultural nuance.",
            "Practice succinct reflections and integrating recurring behavioral patterns."
        ],
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025)",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Focuses on what the client is and is not saying to fully understand what is being communicated in the context of the client systems and to support client self-expression. Considers the client's context, identity, environment, experiences, values and beliefs to enhance understanding.",
        "translationVi": "Định nghĩa: Tập trung vào những gì khách hàng đang nói và không nói để hiểu đầy đủ thông điệp trong bối cảnh hệ sinh thái của khách hàng và hỗ trợ khách hàng tự thể hiện. Xem xét bối cảnh, bản sắc, môi trường, trải nghiệm, giá trị và niềm tin để nâng cao sự thấu hiểu.",
        "comparison2019Vi": "So sánh 2019–2025: Bản 2025 tích hợp rõ nét hơn việc lắng nghe trong 'bối cảnh hệ thống' (client systems) và bối cảnh văn hóa, vượt ra ngoài việc chỉ nghe nội dung câu từ của cá nhân.",
        "comparison2019En": "2019 vs 2025 Comparison: Elevates listening to encompass 'client systems' and cultural frameworks, transcending isolated verbal content.",
        "commentaryVi": "Lắng nghe chủ động ở cấp độ PCC là nghe để hiểu Con Người (WHO), chứ không chỉ nghe Sự Việc (WHAT). Coach lắng nghe năng lượng thay đổi, tông giọng hạ thấp, sự ngập ngừng, và dùng chính ngôn từ của khách hàng (Client's custom language) để phản chiếu thay vì diễn giải lại bằng lời của coach.",
        "commentaryEn": "PCC Active Listening tunes into the WHO rather than merely the WHAT. Notice energy shifts, pitch drops, and mirror back the client's exact words rather than paraphrasing into coach jargon.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Khách hàng nói với nụ cười gượng gạo: 'Dạo này dự án vẫn ổn thôi, tôi quen với việc thức đến 2 giờ sáng rồi.' Coach phản hồi lắng nghe đa tầng: 'Bạn nói rằng mọi việc vẫn ổn kèm theo một nụ cười, nhưng tôi nhận thấy giọng bạn chùng xuống khi nhắc đến mốc 2 giờ sáng. Đằng sau sự 'ổn' đó, điều gì đang thực sự diễn ra?'",
        "exampleContentEn": "Client smiles tensely: 'Project is fine, I'm used to 2 AM nights.' PCC response: 'You said it's fine with a smile, yet your tone dropped at 2 AM. What is truly beneath that fine?'",
        "quiz": {
            "questionVi": "Hành vi nào sau đây là lỗi vi phạm nghiêm trọng Năng lực Lắng nghe Chủ động (Competency 6)?",
            "questionEn": "Which behavior represents a critical violation of Active Listening (Competency 6)?",
            "options": [
                {"key": "A", "textVi": "Ghi nhận từ ngữ ẩn dụ độc đáo mà khách hàng vừa sử dụng.", "textEn": "Acknowledging the unique metaphor used by the client."},
                {"key": "B", "textVi": "Nghe được 2 phút thì ngắt lời khách hàng để kể về một kinh nghiệm tương tự của chính bản thân Coach.", "textEn": "Interrupting after 2 minutes to share the coach's personal experience."},
                {"key": "C", "textVi": "Chú ý đến sự thay đổi tông giọng và tốc độ nói của khách hàng.", "textEn": "Noticing vocal pitch and tempo changes."},
                {"key": "D", "textVi": "Tóm tắt ngắn gọn các ý chính bằng chính ngôn từ của khách hàng.", "textEn": "Succinctly summarizing using the client's exact words."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Ngắt lời để kể chuyện bản thân là lỗi mất tập trung vào khách hàng và áp đặt cái tôi của Coach.",
            "explanationEn": "Interrupting to share coach stories violates client focus and imposes coach ego."
        }
    },
    {
        "id": "mod1-les7",
        "moduleId": "mod-1",
        "lessonNumber": 7,
        "titleVi": "Năng Lực 7: Khơi Gợi Nhận Thức (Bản 2025)",
        "titleEn": "Competency 7: Evokes Awareness (2025 Edition)",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu bản chất của Khơi gợi nhận thức: Giúp khách hàng vượt ra ngoài suy nghĩ thông thường để chạm tới góc nhìn chuyển hóa (Transformational Insight).",
            "Nắm vững 11 chỉ dấu hành vi 2025: Đặt câu hỏi mở, khám phá niềm tin cốt lõi, mời gọi góc nhìn mới và khám phá ẩn dụ.",
            "Tuyệt đối tránh các câu hỏi dẫn dụ (Leading questions) hoặc câu hỏi gài lời khuyên ngầm."
        ],
        "objectivesEn": [
            "Understand evoking awareness: shifting beyond problem-solving into transformational insight.",
            "Master 11 indicators: open-ended inquiry, examining core beliefs, inviting new perspectives, exploring metaphors.",
            "Strictly avoid leading questions or veiled advice."
        ],
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025)",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Facilitates client insight and learning by using tools and techniques such as powerful questioning, silence, metaphor or analogy. Asks questions to help the client explore beyond current thinking and see new possibilities.",
        "translationVi": "Định nghĩa: Thúc đẩy nhận thức và sự học hỏi của khách hàng bằng cách sử dụng các công cụ như câu hỏi gợi mở, khoảng lặng, ẩn dụ hoặc tương đồng. Đặt câu hỏi giúp khách hàng khám phá vượt ra ngoài lối mòn tư duy hiện tại và nhìn thấy các khả năng mới.",
        "comparison2019Vi": "So sánh 2019–2025: Bản 2025 nhấn mạnh nhận thức mang tính hệ thống (systemic awareness) và việc khám phá các giả định văn hóa/xã hội ẩn ngầm tạo nên góc nhìn hiện tại của khách hàng.",
        "comparison2019En": "2019 vs 2025 Comparison: Highlights systemic awareness and surfacing invisible cultural/societal assumptions shaping the client's current lens.",
        "commentaryVi": "Câu hỏi khơi gợi nhận thức thuần khiết là câu hỏi ngắn, mở, không có đáp án định sẵn trong đầu coach. Câu hỏi xuất sắc ở cấp độ PCC thường nhắm vào Căn Tính (Identity): 'Điều này nói lên điều gì về con người mà bạn muốn trở thành?' thay vì 'Bạn sẽ làm gì tiếp theo?'",
        "commentaryEn": "Pure evocative questions are concise, open, and free of predetermined coach answers. Masterful PCC inquiries target Identity ('Who do you choose to be?') rather than tactical mechanics ('What do you do next?').",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Khách hàng nói: 'Tôi cảm thấy như mình đang phải gánh một tảng đá khổng lồ trên lưng.'\n- Câu hỏi gợi mở cấp độ 1: 'Tảng đá đó nặng bao nhiêu kg?' (Hỏi chi tiết sự vụ).\n- Câu hỏi khơi gợi cấp độ PCC: 'Nếu tảng đá đó có thể lên tiếng lúc này, nó muốn nhắc nhở bạn điều gì quan trọng?'",
        "exampleContentEn": "Client: 'I feel like carrying a boulder on my back.'\n- Weak question: 'How heavy is it?' (Focus on mechanics).\n- PCC Evocative question: 'If that boulder could speak right now, what is it trying to remind you of?'",
        "quiz": {
            "questionVi": "Câu hỏi nào sau đây là câu hỏi DẪN DỤ (Leading Question) vi phạm nguyên tắc Khơi gợi Nhận thức (Năng lực 7)?",
            "questionEn": "Which question is a LEADING QUESTION violating Evoking Awareness (Competency 7)?",
            "options": [
                {"key": "A", "textVi": "'Điều gì quan trọng nhất với bạn trong tình huống này?'", "textEn": "'What is most meaningful to you in this situation?'"},
                {"key": "B", "textVi": "'Có phải việc nói chuyện thẳng thắn với sếp sẽ giải quyết được vấn đề này không?'", "textEn": "'Wouldn't having a direct talk with your boss solve this issue?'"},
                {"key": "C", "textVi": "'Bạn nhìn thấy cơ hội phát triển nào cho bản thân từ thách thức này?'", "textEn": "'What growth opportunity do you see for yourself in this challenge?'"},
                {"key": "D", "textVi": "'Góc nhìn nào khác mà bạn chưa từng nghĩ tới trước đây?'", "textEn": "'What other perspective haven't you considered yet?'"}
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B là câu hỏi Yes/No cài cắm sẵn giải pháp của Coach ('nói chuyện với sếp'), tước đoạt quyền tự suy ngẫm của khách hàng.",
            "explanationEn": "Option B is a leading Yes/No question embedding the coach's preconceived solution."
        }
    },
    {
        "id": "mod1-les8",
        "moduleId": "mod-1",
        "lessonNumber": 8,
        "titleVi": "Năng Lực 8: Thúc Đẩy Sự Phát Triển Của Khách Hàng (Bản 2025)",
        "titleEn": "Competency 8: Facilitates Client Growth (2025 Edition)",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu việc chuyển hóa nhận thức mới thành các hành động tự chủ và bền vững.",
            "Nắm vững các chỉ dấu 2025: Khách hàng toàn quyền làm chủ việc thiết kế hành động, thiết lập trách nhiệm giải trình tự thân (Self-Accountability) và ăn mừng tiến bộ.",
            "Tuyệt đối không 'giao bài tập về nhà' hay đóng vai trò người giám sát/kiểm soát thi hành án."
        ],
        "objectivesEn": [
            "Understand transforming insights into autonomous, sustainable actions.",
            "Master 2025 focus: client ownership of action design, self-accountability structures, and celebrating progress.",
            "Never assign homework or act as a policing accountability warden."
        ],
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025)",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Partners with the client to transform learning and insight into action. Promotes client autonomy in the coaching process. Highlights: Client-led action design, autonomous accountability, acknowledging progress, and integrating insights into daily life.",
        "translationVi": "Định nghĩa: Hợp tác với khách hàng để chuyển hóa sự học hỏi và nhận thức thành hành động. Thúc đẩy tính tự chủ của khách hàng trong tiến trình khai vấn. Điểm nhấn: Thiết kế hành động do khách hàng làm chủ, trách nhiệm giải trình tự thân, ghi nhận sự tiến bộ và tích hợp hiểu biết vào cuộc sống.",
        "comparison2019Vi": "So sánh 2019–2025: Bản 2025 tinh chỉnh mạnh mẽ ngôn ngữ về 'Trách nhiệm giải trình tự thân' (Autonomous Self-Accountability) trong Phụ lục thuật ngữ, khẳng định coach đồng hành chứ không kiểm soát hay bắt bí khách hàng.",
        "comparison2019En": "2019 vs 2025 Comparison: Refines 'Autonomous Self-Accountability' terminology, reinforcing partnering support rather than supervisory policing.",
        "commentaryVi": "Bẫy lớn nhất trong đề thi SJT của Năng lực 8 là Coach tự thiết kế kế hoạch hành động rồi 'yêu cầu khách hàng báo cáo hàng tuần'. Hành động chuẩn PCC luôn luôn là: 'Làm thế nào bạn muốn giữ cam kết này với chính mình?' — khách hàng là người quyết định phương thức theo dõi.",
        "commentaryEn": "The fatal SJT trap in Competency 8 is the coach designing actions and requiring weekly check-in reports. PCC standard: 'How do you choose to hold yourself accountable?' — the client dictates the accountability mechanism.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Sau khi nhận ra nguyên nhân trì hoãn, khách hàng rất hào hứng. Coach không giao bài tập mà hỏi: 'Từ nhận thức quý giá hôm nay, hành động cụ thể đầu tiên nào bạn muốn bắt tay thực hiện ngay trong 48 giờ tới? Và bạn muốn tự mình theo dõi tiến độ này bằng cách nào?'",
        "exampleContentEn": "After uncovering the root of procrastination, client is eager. Rather than assigning homework, coach asks: 'From today's breakthrough, what tangible first step do you wish to take within 48 hours? How will you track your own progress?'",
        "quiz": {
            "questionVi": "Khi kết thúc phiên khai vấn, hành động nào của Coach thể hiện chuẩn mực cao nhất của Năng lực 8 (Thúc đẩy Phát triển)?",
            "questionEn": "At session close, which coach action reflects the highest standard of Competency 8 (Facilitating Growth)?",
            "options": [
                {"key": "A", "textVi": "Giao cho khách hàng bản danh sách 5 bài tập về nhà và dọa phạt nếu không hoàn thành.", "textEn": "Assign a 5-item homework list and threaten penalties for non-completion."},
                {"key": "B", "textVi": "Mời khách hàng tổng kết điều họ đã học được về bản thân và cùng khách hàng thiết kế hành động do chính họ làm chủ.", "textEn": "Invite the client to summarize what they learned about themselves and partner to design client-owned actions."},
                {"key": "C", "textVi": "Yêu cầu khách hàng nhắn tin báo cáo coach mỗi sáng vào lúc 6h00.", "textEn": "Order the client to text the coach daily at 6:00 AM."},
                {"key": "D", "textVi": "Kết thúc phiên mà không cần quan tâm khách hàng có áp dụng được gì vào thực tế hay không.", "textEn": "End the session without exploring any real-world application."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B tôn trọng quyền tự chủ của khách hàng, giúp khách hàng tự đúc kết nhận thức và tự chịu trách nhiệm với hành động của mình.",
            "explanationEn": "Option B honors client autonomy, enabling client-led reflection and self-accountability."
        }
    },
    {
        "id": "mod1-les9",
        "moduleId": "mod-1",
        "lessonNumber": 9,
        "titleVi": "Bài 9: Phối Hợp 8 Năng Lực 2025 & Đối Chiếu Khung 2019 Cho Kỳ Thi Viết",
        "titleEn": "Lesson 9: Orchestrating 8 Competencies & 2019-2025 Exam Comparison",
        "estimatedMinutes": 20,
        "objectivesVi": [
            "Hiểu 8 Năng lực ICF là một dòng chảy hữu cơ thống nhất (Tapestry), không phải checklist cơ học.",
            "Làm chủ bảng phân biệt các cặp năng lực dễ nhầm lẫn nhất trong đề thi trắc nghiệm tình huống SJT.",
            "Nắm vững nguyên tắc làm bài thi trên Pearson VUE: Hiện tại kỳ thi viết vẫn sử dụng chuẩn 2019 cho đến khi có thông báo chuyển giao chính thức từ ICF."
        ],
        "objectivesEn": [
            "Understand the 8 ICF competencies as an integrated organic tapestry, not a mechanical checklist.",
            "Master the exam disambiguation table for frequently confusable pairs.",
            "Clarify exam administration on Pearson VUE: written exams currently evaluate against 2019 standards until official ICF transition."
        ],
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025) & Bảng Đối Chiếu 2019–2025",
        "sourceVersion": "Bản 2025 (Chuẩn thực hành) & Bản 2019 (Chuẩn đề thi viết hiện hành)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "The ICF Core Competencies are not isolated checklists; they represent an integrated tapestry. Demonstrates Ethical Practice and Embodies a Coaching Mindset provide the foundational soil. Establishes Agreements and Cultivates Trust co-create the relationship vessel. Maintains Presence and Listens Actively channel the communication. Evokes Awareness and Facilitates Growth harvest the transformation.",
        "translationVi": "8 Năng Lực Cốt Lõi ICF không phải là những chiếc hộp tách rời cơ học, mà là một tấm thảm dệt thống nhất. Năng lực 1 (Đạo đức) và Năng lực 2 (Tư duy) là mảnh đất nền móng. Năng lực 3 (Thỏa thuận) và Năng lực 4 (Niềm tin) tạo nên chiếc bình chứa mối quan hệ. Năng lực 5 (Hiện diện) và Năng lực 6 (Lắng nghe) dẫn truyền dòng chảy giao tiếp. Năng lực 7 (Khơi gợi) và Năng lực 8 (Phát triển) thu hoạch quả ngọt của sự chuyển hóa.",
        "comparison2019Vi": "ĐỐI CHIẾU CHUẨN ĐỀ THI & CHUẨN THỰC HÀNH: Khung 2025 là chuẩn thực hành mới nhất gồm 5 năng lực thành phần mới và 11 sửa đổi. Đối với đề thi viết trên Pearson VUE hiện hành, ngân hàng câu hỏi vẫn được chấm theo bộ tiêu chí năng lực 2019. Cả 2 bản đều nhất quán 100% về triết lý tôn trọng quyền tự quyết của khách hàng, không áp đặt và giữ đạo đức nghiêm ngặt.",
        "comparison2019En": "EXAM VS PRACTICE ALIGNMENT: 2025 represents the latest practice framework. For the current Pearson VUE exam, questions score against the 2019 benchmark. Both are 100% harmonized on client autonomy, zero coach projection, and strict ethical standards.",
        "commentaryVi": "BẢNG PHÂN BIỆT NHANH CÁC CẶP DỄ NHẦM TRONG ĐỀ THI:\n- Cặp 1: Comp 6 vs Comp 7: Lắng nghe (Comp 6) là phản chiếu nguyên vẹn từ ngữ, cảm xúc và bối cảnh của khách hàng; Khơi gợi (Comp 7) là đặt câu hỏi mời gọi khách hàng nhìn ra góc nhìn mới vượt lên trên câu chuyện cũ.\n- Cặp 2: Comp 3 vs Comp 8: Comp 3 xác định đích đến của phiên (Outcome for the session); Comp 8 chuyển hóa hiểu biết thành hành động sau phiên (Action beyond the session).",
        "commentaryEn": "EXAM DISAMBIGUATION TABLE:\n- Pair 1: Comp 6 vs 7: Listening reflects words/emotions; Evoking asks questions inviting new worldview beyond current story.\n- Pair 2: Comp 3 vs 8: Comp 3 contracts for session outcome; Comp 8 designs post-session actions.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Khi khách hàng nói: 'Tôi cảm thấy như đang bị giam cầm trong văn phòng này.'\n- Hành vi Comp 6: Phản chiếu: 'Bạn cảm nhận như có một sự giam cầm ở đây.'\n- Hành vi Comp 7: Đặt câu hỏi khơi gợi: 'Nếu cánh cửa phòng đó mở ra ngay bây giờ, điều đầu tiên bạn nhìn thấy là gì?'",
        "exampleContentEn": "When client says 'I feel imprisoned in this office':\n- Comp 6: Reflects 'You sense an imprisonment here.'\n- Comp 7: Evokes 'If that door unlocked right now, what is the first thing you would see?'",
        "quiz": {
            "questionVi": "Trong một phiên coach, khách hàng bất ngờ khám phá ra niềm tin giới hạn của bản thân và muốn chuyển sang thảo luận một mục tiêu hoàn toàn mới chưa từng thỏa thuận ở đầu phiên. Coach nên phối hợp Năng lực 3 và Năng lực 7 như thế nào?",
            "questionEn": "Client has a breakthrough and wishes to pivot to a completely new topic not agreed upon at session start. How should the coach orchestrate Competencies 3 and 7?",
            "options": [
                {"key": "A", "textVi": "Bắt buộc khách hàng quay lại mục tiêu ban đầu để không làm hỏng thỏa thuận Năng lực 3.", "textEn": "Force the client back to original goals to avoid breaching Competency 3."},
                {"key": "B", "textVi": "Ghi nhận nhận thức mới quý giá của khách hàng (Comp 7), đồng thời linh hoạt tái thỏa thuận (Recontracting - Comp 3): 'Nhận thức mới này có vẻ rất ý nghĩa với bạn. Với thời gian còn lại, bạn muốn chúng ta tiếp tục khám phá điều này hay quay lại mục tiêu ban đầu?'", "textEn": "Honor the breakthrough (Comp 7) while flexibly recontracting (Comp 3): 'This new awareness seems profound. With our remaining time, how do you wish to spend our focus?'"},
                {"key": "C", "textVi": "Lập tức đóng phiên và tính phí gấp đôi vì có hai mục tiêu.", "textEn": "Immediately close the session and double the invoice."},
                {"key": "D", "textVi": "Tự ý xóa bỏ hoàn toàn thỏa thuận mà không cần hỏi ý kiến khách hàng.", "textEn": "Disregard the contract entirely without consulting the client."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B là minh chứng sống động của sự kết hợp tinh tế giữa Khơi gợi nhận thức (Comp 7) và Tái thỏa thuận nhịp nhàng theo quyền tự quyết của khách hàng (Comp 3).",
            "explanationEn": "Option B exemplifies masterful harmony between evoking awareness (Comp 7) and partnering on flexible recontracting (Comp 3)."
        }
    }
]'''

# Replace Module 2 Lessons
NEW_M2 = r'''MODULE_2_LESSONS = [
    {
        "id": "mod2-les1",
        "moduleId": "mod-2",
        "lessonNumber": 1,
        "titleVi": "Bài 1: Cấu Trúc, Mục Đích & 4 Giá Trị Cốt Lõi Đạo Đức ICF (Bản 2025)",
        "titleEn": "Lesson 1: Structure, Purpose & 4 ICF Core Ethical Values (2025 Edition)",
        "estimatedMinutes": 18,
        "objectivesVi": [
            "Hiểu toàn diện cấu trúc Bộ Quy tắc Đạo đức ICF 2025 (Hiệu lực: 01/04/2025) gồm 5 Phần chính, 24 Tiêu chuẩn đạo đức, Lời cam kết (Pledge) và Phụ lục.",
            "Nắm vững 4 Giá trị Cốt lõi chính thức: Tính Chuyên nghiệp (Professionalism), Sự Hợp tác (Collaboration), Tính Nhân văn (Humanity), và Tính Công bằng & Hòa nhập (Equity).",
            "Phân biệt rõ ràng: Bản 2025 là chuẩn thực hành có hiệu lực từ 01/04/2025; trong khi bài thi viết trắc nghiệm trên Pearson VUE hiện hành vẫn dùng chuẩn Bộ Đạo đức 2020."
        ],
        "objectivesEn": [
            "Understand the complete architecture of the 2025 ICF Code of Ethics (Effective April 1, 2025) comprising 5 Sections, 24 Standards, the Pledge, and Appendix.",
            "Master the 4 official Core Values: Professionalism, Collaboration, Humanity, and Equity.",
            "Clearly distinguish the 2025 practice standard from the current written exam baseline (2020 Code)."
        ],
        "sourceDocument": "Bộ Quy Tắc Đạo Đức ICF (Bản 2025)",
        "sourceVersion": "Bản 2025 (Hiệu lực thực hành: 01/04/2025; Bản 2020 dùng cho bài thi viết hiện hành)",
        "effectiveDate": "01/04/2025",
        "sourceLink": "https://coachingfederation.org/credentialing/coaching-ethics/icf-code-of-ethics/",
        "originalExcerptEn": "The ICF Code of Ethics (effective April 1, 2025) applies across the entire ICF ecosystem. The 4 Core Values are: Professionalism, Collaboration, Humanity, and Equity. Comprises 5 distinct sections of ethical standards (24 numbered standards), an Ecosystem commitment, and the Pledge of Ethics.",
        "translationVi": "Bộ Quy tắc Đạo đức ICF (có hiệu lực từ ngày 01/04/2025) áp dụng rộng rãi cho toàn bộ hệ sinh thái ICF. 4 Giá trị Cốt lõi bao gồm: Tính Chuyên nghiệp (Professionalism), Sự Hợp tác (Collaboration), Tính Nhân văn (Humanity) và Tính Công bằng & Hòa nhập (Equity). Bộ Quy tắc gồm 5 phần tiêu chuẩn đạo đức riêng biệt với 24 chuẩn mực chính thức, cam kết toàn hệ sinh thái và Lời cam kết Đạo đức.",
        "commentaryVi": "GIẢI THÍCH SƯ PHẠM VỀ BẢN 2025:\n- Ngày có hiệu lực: 01/04/2025. Bản 2025 mở rộng phạm vi áp dụng không chỉ cho các Coach có chứng chỉ mà cho TOÀN BỘ HỆ SINH THÁI ICF (bao gồm nhân viên, hội đồng, giảng viên đào tạo, mentor, supervisor và học viên).\n- Bản 2025 tích hợp trực tiếp 4 Giá trị Cốt lõi vào văn bản và tổ chức thành 5 Phần (24 tiêu chuẩn), không dùng cấu trúc 28 tiêu chuẩn của bản 2020.\n- Đối với kỳ thi Pearson VUE: Ngân hàng đề thi viết hiện hành vẫn được đối chiếu theo bản 2020 (Tiêu chuẩn 1–28). Vì vậy học viên cần học bản 2025 để thực hành chuẩn mực và đối chiếu bản 2020 để thi đỗ.",
        "commentaryEn": "PEDAGOGICAL INSIGHT ON 2025 CODE: Effective April 1, 2025. Applies to the entire ICF ecosystem. Features 4 Core Values and 5 Sections with 24 standards. Note that current written exams still evaluate the 2020 Code baseline.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Một Mentor Coach đang hướng dẫn cho một học viên chuẩn bị thi PCC. Người học viên đề nghị trả thêm tiền để Mentor Coach viết hộ bài báo cáo năng lực. Dựa trên Giá trị Tính Chuyên nghiệp và Tính Chính trực của Bản 2025 (áp dụng cho toàn bộ hệ sinh thái gồm cả Mentor), Mentor Coach từ chối kiên quyết và giải thích rằng hành vi này vi phạm nghiêm trọng chuẩn mực đạo đức của nghề.",
        "exampleContentEn": "A mentee offers extra compensation for a mentor coach to ghostwrite their performance report. Upholding Professionalism under the 2025 Code (which explicitly binds mentors), the mentor refuses firmly, explaining this violates systemic ethical integrity.",
        "quiz": {
            "questionVi": "Bộ Quy tắc Đạo đức ICF 2025 chính thức có hiệu lực thực hành từ ngày nào, và gồm bao nhiêu Giá trị Cốt lõi?",
            "questionEn": "On what date did the 2025 ICF Code of Ethics officially take effect for practice, and how many Core Values does it feature?",
            "options": [
                {"key": "A", "textVi": "Hiệu lực từ 01/01/2020, gồm 3 Giá trị Cốt lõi.", "textEn": "Effective January 1, 2020, with 3 Core Values."},
                {"key": "B", "textVi": "Hiệu lực từ 01/04/2025, gồm 4 Giá trị Cốt lõi: Tính Chuyên nghiệp, Hợp tác, Nhân văn và Công bằng.", "textEn": "Effective April 1, 2025, with 4 Core Values: Professionalism, Collaboration, Humanity, and Equity."},
                {"key": "C", "textVi": "Hiệu lực từ 01/04/2027, gồm 6 Giá trị Cốt lõi.", "textEn": "Effective April 1, 2027, with 6 Core Values."},
                {"key": "D", "textVi": "Hiệu lực từ 11/11/2024, không có Giá trị Cốt lõi nào.", "textEn": "Effective November 11, 2024, without Core Values."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Bộ Quy tắc Đạo đức ICF 2025 chính thức có hiệu lực từ ngày 01/04/2025, với 4 Giá trị Cốt lõi là Professionalism, Collaboration, Humanity, và Equity.",
            "explanationEn": "The 2025 Code took effect on April 1, 2025, anchored in 4 Core Values: Professionalism, Collaboration, Humanity, and Equity."
        }
    },
    {
        "id": "mod2-les2",
        "moduleId": "mod-2",
        "lessonNumber": 2,
        "titleVi": "Bài 2: Phần 1 & 2 — Thỏa Thuận Với Khách Hàng / Sponsor & Tính Bảo Mật, AI / Công Nghệ Số (Tiêu Chuẩn 1.1–1.2 & 2.1–2.8)",
        "titleEn": "Lesson 2: Sections 1 & 2 — Client/Sponsor Agreements & Confidentiality, AI / Digital Tech (Standards 1.1–1.2 & 2.1–2.8)",
        "estimatedMinutes": 18,
        "objectivesVi": [
            "Nắm vững Phần 1: Thỏa thuận với Khách hàng và Sponsor (Tiêu chuẩn 1.1: Làm rõ bản chất, tài chính, vai trò; Tiêu chuẩn 1.2: Quyền chấm dứt thỏa thuận của các bên).",
            "Nắm vững Phần 2: Bảo mật và Tuân thủ Pháp lý (Tiêu chuẩn 2.1–2.8): Bảo mật nghiêm ngặt, giới hạn chia sẻ với sponsor, lưu trữ và tiêu hủy an toàn hồ sơ điện tử.",
            "Làm chủ quy định mới về Công nghệ số và AI: Bắt buộc có sự đồng thuận minh bạch của khách hàng trước khi dùng công cụ ghi âm/phiên âm bằng trí tuệ nhân tạo."
        ],
        "objectivesEn": [
            "Master Section 1: Agreements for Client & Sponsor (Std 1.1: contracting nature, roles, finances; Std 1.2: right to terminate).",
            "Master Section 2: Confidentiality & Compliance (Std 2.1–2.8): strict confidentiality, electronic record storage, and disposal.",
            "Comply with digital safeguards: mandatory transparent client consent before deploying AI transcription tools."
        ],
        "sourceDocument": "Bộ Quy Tắc Đạo Đức ICF (Bản 2025, Phần 1 & 2)",
        "sourceVersion": "Bản 2025 (Hiệu lực: 01/04/2025)",
        "effectiveDate": "01/04/2025",
        "sourceLink": "https://coachingfederation.org/credentialing/coaching-ethics/icf-code-of-ethics/",
        "originalExcerptEn": "Section 1: Agreements for Client and/or Sponsor Engagement (Standards 1.1-1.2). Section 2: Confidentiality and Legal Compliance (Standards 2.1-2.8). Standard 2.4: Maintain, store and dispose of records, including electronic files and communications, promoting confidentiality and privacy. Requires explicit informed consent for digital and AI technology recording.",
        "translationVi": "Phần 1: Thỏa thuận Hợp tác với Khách hàng và/hoặc Nhà tài trợ (Tiêu chuẩn 1.1–1.2). Phần 2: Tính Bảo mật và Tuân thủ Pháp lý (Tiêu chuẩn 2.1–2.8). Tiêu chuẩn 2.4: Duy trì, lưu trữ và tiêu hủy hồ sơ, bao gồm các tệp điện tử và thông tin liên lạc, đảm bảo tính bảo mật và quyền riêng tư. Yêu cầu có sự đồng thuận rõ ràng trước khi dùng công nghệ AI ghi âm.",
        "comparison2019Vi": "So sánh 2020 vs 2025: Trong bản 2020, các điều khoản này nằm trong Phần 1 (Tiêu chuẩn 1–11). Bản 2025 tái cấu trúc thành 2 Phần riêng biệt: Phần 1 (Thỏa thuận, gồm 1.1 và 1.2) và Phần 2 (Bảo mật & Pháp lý, gồm 2.1 đến 2.8), nâng cấp mạnh mẽ quy định về dữ liệu số và công cụ AI.",
        "comparison2019En": "2020 vs 2025 Comparison: Reorganizes legacy Standards 1-11 into Section 1 (Agreements 1.1-1.2) and Section 2 (Confidentiality & Compliance 2.1-2.8) with enhanced AI safeguards.",
        "commentaryVi": "GIẢI THÍCH SƯ PHẠM TỪ ICE:\n- Khi có xung đột giữa mong muốn của Nhà tài trợ (Sponsor) và sự bảo mật của Khách hàng (Client), trách nhiệm đạo đức của Coach luôn luôn ưu tiên bảo vệ Khách hàng trực tiếp.\n- Ngoại lệ bảo mật DUY NHẤT: Khi có nguy cơ đe dọa trực tiếp đến tính mạng con người (tự sát, giết người) hoặc yêu cầu bắt buộc của tòa án.\n- Tuyệt đối không tự ý bật bot AI ghi âm nếu chưa giải thích rõ nơi lưu trữ dữ liệu và nhận được sự đồng thuận bằng văn bản của khách hàng.",
        "commentaryEn": "ICE INSIGHT: In conflicts between sponsor desires and client confidentiality, the coach always prioritizes the direct client. Imminent threat to life is the sole confidentiality exception. AI recording requires prior informed written consent.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Coach A đang dùng một ứng dụng AI để tạo biên bản phiên coach. Trước khi bắt đầu phiên, Coach A gửi bản phụ lục bảo mật giải thích rõ dữ liệu lưu trữ ở đâu và hỏi khách hàng: 'Bạn có thoải mái để ứng dụng này ghi âm tóm tắt không?' Nếu khách hàng từ chối, coach vui vẻ tắt ứng dụng và ghi chép tay.",
        "exampleContentEn": "Coach uses an AI note-taker. Before starting, the coach transparently seeks consent: 'Are you comfortable with this tool summarizing key points?' If client declines, the coach immediately switches to handwritten notes.",
        "quiz": {
            "questionVi": "Trước khi sử dụng một phần mềm AI để tự động ghi âm và tóm tắt phiên khai vấn, hành động nào là BẮT BUỘC theo Chuẩn mực Đạo đức ICF 2025 (Tiêu chuẩn 2.4)?",
            "questionEn": "Before using an AI tool to record and summarize a coaching session, what is MANDATORY under ICF 2025 Code (Standard 2.4)?",
            "options": [
                {"key": "A", "textVi": "Bật âm thầm không cần nói vì AI chỉ để phục vụ học tập cá nhân của coach.", "textEn": "Run it silently since it only aids the coach's private learning."},
                {"key": "B", "textVi": "Chỉ cần công ty sản xuất phần mềm AI đó cam kết bảo mật là đủ.", "textEn": "Rely solely on the software vendor's generic terms of service."},
                {"key": "C", "textVi": "Minh bạch giải thích cách thức hoạt động, nơi lưu trữ dữ liệu của AI và nhận được sự đồng thuận có hiểu biết rõ ràng của khách hàng trước khi kích hoạt.", "textEn": "Transparently explain data handling and obtain explicit informed client consent prior to activation."},
                {"key": "D", "textVi": "Đăng tải bản ghi âm lên trang web cá nhân để quảng cáo công nghệ mới.", "textEn": "Post the recording publicly to promote technological prowess."}
            ],
            "correctAnswer": "C",
            "explanationVi": "Tiêu chuẩn 2.4 và hướng dẫn ICE 2025 yêu cầu bảo mật dữ liệu số và sự đồng thuận minh bạch của khách hàng đối với mọi công nghệ ghi âm.",
            "explanationEn": "Standard 2.4 and ICE guidelines mandate digital data protection and informed client consent."
        }
    },
    {
        "id": "mod2-les3",
        "moduleId": "mod-2",
        "lessonNumber": 3,
        "titleVi": "Bài 3: Phần 3 & 4 — Hành Vi Chuyên Nghiệp, Xung Đột Lợi Ích & Cam Kết Giá Trị (Tiêu Chuẩn 3.1–3.8 & 4.1–4.3)",
        "titleEn": "Lesson 3: Sections 3 & 4 — Professional Conduct, Conflicts of Interest & Delivering Value (Standards 3.1–3.8 & 4.1–4.3)",
        "estimatedMinutes": 18,
        "objectivesVi": [
            "Nắm vững Phần 3: Hành vi chuyên nghiệp và Xung đột lợi ích (Std 3.1–3.8): Nhận diện và công khai xung đột, quản lý vai trò kép, nghiêm cấm quan hệ tình cảm/thân mật bất chính.",
            "Nắm vững Phần 4: Cam kết mang lại giá trị nhất quán (Std 4.1–4.3): Tích cực quản lý tiến trình, nhận diện giới hạn năng lực cá nhân và giới thiệu chuyên gia/chấm dứt khi không còn giá trị.",
            "Luyện tập xử lý các tình huống xung đột lợi ích tài chính và ranh giới chuyên môn theo chuẩn 2025."
        ],
        "objectivesEn": [
            "Master Section 3: Professional Conduct & Conflicts of Interest (Std 3.1–3.8): dual roles, biases, absolute ban on sexual intimacy, fee transparency.",
            "Master Section 4: Delivering Consistent Value (Std 4.1–4.3): recognizing competence limits, monitoring value, ethical referrals and termination.",
            "Resolve financial and role conflict scenarios under 2025 standards."
        ],
        "sourceDocument": "Bộ Quy Tắc Đạo Đức ICF (Bản 2025, Phần 3 & 4)",
        "sourceVersion": "Bản 2025 (Hiệu lực: 01/04/2025)",
        "effectiveDate": "01/04/2025",
        "sourceLink": "https://coachingfederation.org/credentialing/coaching-ethics/icf-code-of-ethics/",
        "originalExcerptEn": "Section 3: Professional Conduct and Conflicts of Interest (Standards 3.1-3.8). Standard 3.6: Be mindful of intimacy in the coaching relationship; do not participate in any sexual or romantic intimacy. Standard 3.7: Disclose to the client when acting in a capacity other than coach. Section 4: Commitment to Delivering Consistent Value (Standards 4.1-4.3). Standard 4.2: Recognize personal limitations. Standard 4.3: Remain alert to indications that value received has diminished and suggest referral or termination.",
        "translationVi": "Phần 3: Hành vi Chuyên nghiệp và Xung đột Lợi ích (Tiêu chuẩn 3.1–3.8). Tiêu chuẩn 3.6: Nhận thức về sự thân mật trong mối quan hệ khai vấn; tuyệt đối không tham gia vào quan hệ tình cảm hoặc tình dục. Tiêu chuẩn 3.7: Minh bạch với khách hàng khi hành động trong vai trò khác ngoài coach. Phần 4: Cam kết Mang lại Giá trị Nhất quán (Tiêu chuẩn 4.1–4.3). Tiêu chuẩn 4.2: Nhận biết giới hạn cá nhân. Tiêu chuẩn 4.3: Nhạy bén khi giá trị phiên giảm sút để đề xuất chuyển gửi hoặc dừng hợp đồng.",
        "comparison2019Vi": "So sánh 2020 vs 2025: Trong bản 2020, nội dung này nằm rải rác ở Phần 2 và Phần 3 (Tiêu chuẩn 12–24). Bản 2025 hợp nhất thành 2 Phần chuyên biệt: Phần 3 (Xung đột & Hành vi chuyên nghiệp, 3.1–3.8) và Phần 4 (Cam kết mang lại giá trị, 4.1–4.3).",
        "comparison2019En": "2020 vs 2025 Comparison: Consolidates legacy standards into Section 3 (Professional Conduct & Conflicts 3.1-3.8) and Section 4 (Delivering Consistent Value 4.1-4.3).",
        "commentaryVi": "GIẢI THÍCH SƯ PHẠM VỀ VAI TRÒ KÉP VÀ RANH GIỚI:\n- Mối quan hệ khai vấn luôn có sự chênh lệch vô hình về sự cởi mở tổn thương (vulnerability). Vì vậy, Tiêu chuẩn 3.6 nghiêm cấm tuyệt đối quan hệ tình cảm hoặc tình dục với khách hàng/nhà tài trợ hiện tại.\n- Tiêu chuẩn 4.3 là kim chỉ nam cho việc chấm dứt hợp đồng: Nếu khách hàng không còn nhận được giá trị từ coaching hoặc cần sự hỗ trợ y tế/tâm lý, coach phải dũng cảm đề xuất chuyển gửi hoặc dừng lại vì lợi ích tối thượng của khách hàng.",
        "commentaryEn": "PEDAGOGICAL INSIGHT: Vulnerability creates an ethical duty of care. Standard 3.6 strictly prohibits sexual or romantic relationships. Standard 4.3 dictates ethical termination or referral when coaching ceases to add value.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Coach B đang huấn luyện cho một giám đốc điều hành. Sau 5 phiên, giám đốc đề nghị Coach B làm cố vấn chiến lược kiêm việc đầu tư cổ phần vào công ty. Coach B xử lý chuẩn mực: Minh bạch giải thích rằng vai trò coach đòi hỏi tính khách quan độc lập, việc làm cố vấn và nhà đầu tư tạo ra xung đột lợi ích nghiêm trọng. Do đó Coach B từ chối hoặc yêu cầu hoàn tất hợp đồng coach trước khi thảo luận cơ hội khác.",
        "exampleContentEn": "Client offers an equity investment and consulting role. Coach ethically clarifies the severe dual-role conflict, declining the investment to maintain objective coaching boundaries.",
        "quiz": {
            "questionVi": "Sau 8 phiên coaching, khách hàng bắt đầu có biểu hiện trầm cảm nặng và nói rằng các câu hỏi coaching khiến họ cảm thấy kiệt sức hơn. Theo Tiêu chuẩn 4.2 và 4.3 của Bản Đạo Đức 2025, hành động nào là chuẩn mực nhất?",
            "questionEn": "After 8 sessions, client exhibits severe depression and reports coaching inquiries cause emotional strain. Under Standards 4.2 and 4.3 (2025 Code), what is the most ethical action?",
            "options": [
                {"key": "A", "textVi": "Tiếp tục coach quyết liệt hơn để ép khách hàng vượt qua vùng an toàn.", "textEn": "Push aggressively to force the client out of comfort zone."},
                {"key": "B", "textVi": "Nhận biết giới hạn chuyên môn của coaching, nhẹ nhàng thảo luận với khách hàng về sự suy giảm giá trị và đề xuất chuyển gửi sang chuyên gia tâm lý trị liệu.", "textEn": "Recognize professional limits, sensitively discuss diminished value, and suggest referring to a licensed therapist."},
                {"key": "C", "textVi": "Kê đơn thuốc an thần cho khách hàng để họ ngủ ngon hơn.", "textEn": "Prescribe sleeping sedatives to the client."},
                {"key": "D", "textVi": "Tự ý chấm dứt hợp đồng qua tin nhắn ngắn mà không có buổi trò chuyện chia tay.", "textEn": "Abruptly terminate via short text without any closing dialogue."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Tiêu chuẩn 4.2 và 4.3 yêu cầu coach nhận biết giới hạn năng lực và chủ động chuyển gửi khi nhu cầu của khách hàng vượt quá phạm vi coaching.",
            "explanationEn": "Standards 4.2 & 4.3 require coaches to recognize scope limits and proactively suggest referral when coaching is no longer beneficial."
        }
    },
    {
        "id": "mod2-les4",
        "moduleId": "mod-2",
        "lessonNumber": 4,
        "titleVi": "Bài 4: Phần 5, Lời Cam Kết Đạo Đức (Pledge) & Lưu Trữ Đối Chiếu Bộ Đạo Đức 2020 Cho Bài Thi Viết (Tiêu Chuẩn 5.1–5.3 & Bản 2020)",
        "titleEn": "Lesson 4: Section 5, Pledge of Ethics & 2020 Code of Ethics Exam Archive (Standards 5.1–5.3 & 2020 Edition)",
        "estimatedMinutes": 20,
        "objectivesVi": [
            "Nắm vững Phần 5: Tính Chính trực Chuyên môn và Trách nhiệm Giải trình (Std 5.1: Công bố chính xác bằng cấp/chứng chỉ; Std 5.2: Tuyên bố trung thực về dịch vụ; Std 5.3: Triết lý 'làm điều thiện' — doing good).",
            "Hiểu sâu sắc Lời Cam Kết Đạo Đức (ICF Pledge of Ethics) và cơ chế xử lý khiếu nại đạo đức nghề nghiệp (Ethical Conduct Review - ECR).",
            "Làm chủ kho lưu trữ đối chiếu 28 tiêu chuẩn của Bộ Đạo đức 2020 phục vụ làm bài thi trắc nghiệm tình huống trên Pearson VUE."
        ],
        "objectivesEn": [
            "Master Section 5: Professional Integrity & Accountability (Std 5.1-5.3: accurate credentials, honest representations, 'doing good' philosophy).",
            "Understand the ICF Pledge of Ethics and the Ethical Conduct Review (ECR) process.",
            "Master the 2020 Code of Ethics archive table (28 Standards) for Pearson VUE exam success."
        ],
        "sourceDocument": "Bộ Quy Tắc Đạo Đức ICF (Bản 2025 & Kho Lưu Trữ Bản 2020)",
        "sourceVersion": "Bản 2025 (Chuẩn thực hành) & Bản 2020 (Chuẩn đề thi viết hiện hành)",
        "effectiveDate": "01/04/2025",
        "sourceLink": "https://coachingfederation.org/credentialing/coaching-ethics/icf-code-of-ethics/",
        "originalExcerptEn": "Section 5: Professional Integrity and Accountability (Standards 5.1-5.3). Standard 5.3: Adhere to the philosophy of 'doing good' versus merely 'avoiding bad'. ICF Pledge of Ethics: I pledge to abide by the ICF Code of Ethics and uphold the Core Values. Archive Note: The 2020 Code features 28 standards across 4 sections used in current exam scoring.",
        "translationVi": "Phần 5: Tính Chính trực Chuyên môn và Trách nhiệm Giải trình (Tiêu chuẩn 5.1–5.3). Tiêu chuẩn 5.3: Tuân thủ triết lý 'làm điều thiện' (doing good) thay vì chỉ đơn thuần 'tránh điều xấu' (avoiding bad). Lời cam kết Đạo đức ICF: Tôi cam kết tuân thủ Bộ Quy tắc Đạo đức và phát huy các Giá trị Cốt lõi. Ghi chú Lưu trữ: Bản 2020 gồm 28 tiêu chuẩn thuộc 4 phần đang dùng làm căn cứ chấm thi viết.",
        "comparison2019Vi": "KHO LƯU TRỮ ĐỐI CHIẾU 28 TIÊU CHUẨN BỘ ĐẠO ĐỨC 2020 (PHỤC VỤ THI VIẾT):\n• Phần I — Trách nhiệm với khách hàng (Tiêu chuẩn 1–11): Thỏa thuận minh bạch, bảo mật thông tin, bình đẳng bản sắc, chuyển gửi chuyên gia.\n• Phần II — Trách nhiệm với thực hành và hiệu suất (Tiêu chuẩn 12–20): Giới hạn chuyên môn, xung đột lợi ích, lưu trữ hồ sơ, công bố trung thực chứng chỉ ICF.\n• Phần III — Trách nhiệm với tính chuyên nghiệp (Tiêu chuẩn 21–24): Nghiêm cấm quan hệ tình cảm/thân mật, giữ vững ranh giới coaching vs trị liệu.\n• Phần IV — Trách nhiệm với xã hội (Tiêu chuẩn 25–28): Đóng góp cộng đồng, bình đẳng xã hội, tuân thủ pháp luật và trung thực nghiên cứu.",
        "comparison2019En": "2020 CODE OF ETHICS ARCHIVE (EXAM STUDY AID):\n• Section I — Responsibility to Clients (Standards 1–11)\n• Section II — Responsibility to Practice & Performance (Standards 12–20)\n• Section III — Responsibility to Professionalism (Standards 21–24)\n• Section IV — Responsibility to Society (Standards 25–28)",
        "commentaryVi": "ĐIỂM SÁNG TRIẾT LÝ BẢN 2025:\n- Tiêu chuẩn 5.3 đưa ra một tuyên ngôn đạo đức tiến bộ: Coach không chỉ 'ngồi yên để không phạm luật' (avoiding bad), mà phải chủ động lan tỏa những tác động tích cực, nhân văn, bình đẳng và nâng tầm phẩm giá con người (doing good).\n- Khi làm bài thi Pearson VUE: Thí sinh nhớ rằng mọi câu hỏi tình huống đều chấm theo logic đạo đức cao nhất: bảo vệ sự tự chủ của khách hàng, minh bạch vai trò và tôn trọng thỏa thuận.",
        "commentaryEn": "PHILOSOPHICAL HIGHLIGHT OF 2025: Standard 5.3 introduces the proactive duty of 'doing good' rather than passive compliance. In Pearson VUE exams, the highest scoring choice always protects client autonomy, role clarity, and agreement fidelity.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Một coach mới hoàn thành khóa học 60 giờ nhưng chưa vượt qua kỳ thi chứng chỉ ICF ACC. Trên trang web cá nhân, người này ghi: 'Chuyên gia Khai vấn Quốc tế ICF-PCC'. Hành vi này vi phạm trực tiếp Tiêu chuẩn 5.1 của Bản 2025 (và Tiêu chuẩn 16 của Bản 2020) về việc công bố trung thực trình độ chuyên môn và chứng chỉ ICF.",
        "exampleContentEn": "A coach with 60 training hours advertises as 'ICF-PCC Credentialed Coach'. This directly violates Standard 5.1 of 2025 Code (and legacy Standard 16 of 2020 Code) regarding truthful credential representation.",
        "quiz": {
            "questionVi": "Triết lý đạo đức mới nào được nêu bật trong Tiêu chuẩn 5.3 của Bộ Quy tắc Đạo đức ICF 2025?",
            "questionEn": "Which new ethical philosophy is highlighted in Standard 5.3 of the 2025 ICF Code of Ethics?",
            "options": [
                {"key": "A", "textVi": "Triết lý 'tối đa hóa lợi nhuận bằng mọi giá'.", "textEn": "'Maximize profits at all costs.'"},
                {"key": "B", "textVi": "Triết lý chủ động 'làm điều thiện' (doing good) thay vì chỉ đơn thuần 'tránh điều xấu' (avoiding bad).", "textEn": "The philosophy of actively 'doing good' versus merely 'avoiding bad.'"},
                {"key": "C", "textVi": "Triết lý không cần tuân theo bất kỳ nguyên tắc nào nếu khách hàng đồng ý.", "textEn": "Disregard ethics if the client agrees."},
                {"key": "D", "textVi": "Triết lý chỉ bảo vệ quyền lợi của tổ chức tài trợ.", "textEn": "Solely protect corporate sponsor interests."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Tiêu chuẩn 5.3 nêu rõ cam kết đạo đức tiến bộ: Chủ động thực hành làm điều tốt đẹp (doing good) cho khách hàng và xã hội.",
            "explanationEn": "Standard 5.3 explicitly articulates the active commitment to 'doing good' rather than passive risk avoidance."
        }
    }
]'''

# Replace in code using exact substring locations
idx_m2_start = code.find('MODULE_2_LESSONS = [')
idx_m2_end = code.find('MODULE_2_WRAPUP =')
assert idx_m2_start != -1 and idx_m2_end != -1, "Could not find MODULE_2_LESSONS or MODULE_2_WRAPUP"
code = code[:idx_m2_start] + NEW_M2 + '\n\n# Wrap-up Quiz for Module 2\n' + code[idx_m2_end:]

idx_m1_start = code.find('MODULE_1_LESSONS = [')
idx_m1_end = code.find('MODULE_1_WRAPUP =')
assert idx_m1_start != -1 and idx_m1_end != -1, "Could not find MODULE_1_LESSONS or MODULE_1_WRAPUP"
code = code[:idx_m1_start] + NEW_M1 + '\n\n# Wrap-up Quiz for Module 1\n' + code[idx_m1_end:]

with open('scripts/icf_curriculum_data.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully replaced MODULE_1_LESSONS and MODULE_2_LESSONS in scripts/icf_curriculum_data.py")

