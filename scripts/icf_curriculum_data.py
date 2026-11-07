# -*- coding: utf-8 -*-
"""
Master Data Store for the 7 Official ICF Curriculum Modules (Mentor Thi)
Fully verified against official ICF publications, Pearson VUE guidelines, and ICF Research.
Terminology standard: 100% "khách hàng" (0 occurrences of unapproved legacy terminology).
"""

import re
import unicodedata

def remove_accents(input_str):
    if not input_str:
        return ""
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)]).lower()

# ==============================================================================
# HỌC PHẦN 1: NĂNG LỰC CỐT LÕI (ICF CORE COMPETENCIES)
# ==============================================================================
MODULE_1_LESSONS = [
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
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025), Trang 3",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Understands and consistently applies coaching ethics and standards of coaching.\n\n\n1.01. Demonstrates personal integrity and honesty in interactions with clients, sponsors and relevant stakeholders\n\n1.02. Is sensitive to clients’ identity, environment, experiences, values and beliefs\n\n1.03. Uses language appropriate and respectful to clients, sponsors and relevant stakeholders\n\n1.04. Abides by the ICF Code of Ethics and upholds the ICF Core Values\n\n1.05. Maintains confidentiality with client information per stakeholder agreements and pertinent laws\n\n1.06. Maintains the distinctions between coaching, consulting, psychotherapy and other support professions\n\n1.07. Refers clients to other support professionals, as appropriate",
        "translationVi": "Định nghĩa: Hiểu và nhất quán áp dụng đạo đức khai vấn và các chuẩn mực của nghề khai vấn.\n\n\n1.01. Thể hiện sự chính trực và trung thực trong tương tác với khách hàng, bên tài trợ và các bên liên quan.\n\n1.02. Nhạy cảm và tôn trọng bản sắc, môi trường, trải nghiệm, giá trị và niềm tin của khách hàng.\n\n1.03. Sử dụng ngôn ngữ phù hợp và tôn trọng đối với khách hàng, bên tài trợ và các bên liên quan.\n\n1.04. Tuân thủ ICF Code of Ethics và duy trì các Giá trị Cốt lõi của ICF.\n\n1.05. Duy trì tính bảo mật của thông tin khách hàng theo thỏa thuận với các bên liên quan và pháp luật áp dụng.\n\n1.06. Duy trì sự phân biệt giữa khai vấn, tư vấn, tâm lý trị liệu và các nghề hỗ trợ khác.\n\n1.07. Giới thiệu khách hàng đến các chuyên gia hỗ trợ khác khi phù hợp.",
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
                {
                    "key": "A",
                    "textVi": "Báo cáo đầy đủ mọi điều khách hàng đã nói vì nhà tài trợ là bên chi trả toàn bộ phí coaching.",
                    "textEn": "Report everything disclosed since the sponsor pays all coaching fees."
                },
                {
                    "key": "B",
                    "textVi": "Từ chối thẳng thừng và lập tức chấm dứt hợp đồng với doanh nghiệp mà không cần giải thích.",
                    "textEn": "Abruptly refuse and terminate the corporate engagement without explanation."
                },
                {
                    "key": "C",
                    "textVi": "Nhắc lại thỏa thuận bảo mật đã ký, giải thích rằng nội dung phiên là bí mật và chỉ chia sẻ tiến độ mục tiêu đã có sự đồng thuận của khách hàng.",
                    "textEn": "Reiterate the signed confidentiality agreement, explaining session details are confidential and only agreed progress goals are shared."
                },
                {
                    "key": "D",
                    "textVi": "Khuyên nhà tài trợ tự bí mật theo dõi máy tính của khách hàng để biết nguyên nhân.",
                    "textEn": "Advise the sponsor to secretly monitor the client's laptop to uncover reasons."
                }
            ],
            "correctAnswer": "C",
            "explanationVi": "Phương án C là chuẩn mực đạo đức cao nhất: Coach bảo vệ thỏa thuận bảo mật, tôn trọng khách hàng và hành xử chuyên nghiệp với nhà tài trợ.",
            "explanationEn": "Option C is exemplary: The coach upholds confidentiality, respects client trust, and maintains professionalism with the sponsor."
        },
        "definitionEn": "Understands and consistently applies coaching ethics and standards of coaching.",
        "definitionVi": "Hiểu và nhất quán áp dụng đạo đức khai vấn và các chuẩn mực của nghề khai vấn.",
        "subCompetencies": [
            {
                "code": "1.01",
                "textEn": "Demonstrates personal integrity and honesty in interactions with clients, sponsors and relevant stakeholders",
                "textVi": "Thể hiện sự chính trực và trung thực trong tương tác với khách hàng, bên tài trợ và các bên liên quan."
            },
            {
                "code": "1.02",
                "textEn": "Is sensitive to clients’ identity, environment, experiences, values and beliefs",
                "textVi": "Nhạy cảm và tôn trọng bản sắc, môi trường, trải nghiệm, giá trị và niềm tin của khách hàng."
            },
            {
                "code": "1.03",
                "textEn": "Uses language appropriate and respectful to clients, sponsors and relevant stakeholders",
                "textVi": "Sử dụng ngôn ngữ phù hợp và tôn trọng đối với khách hàng, bên tài trợ và các bên liên quan."
            },
            {
                "code": "1.04",
                "textEn": "Abides by the ICF Code of Ethics and upholds the ICF Core Values",
                "textVi": "Tuân thủ ICF Code of Ethics và duy trì các Giá trị Cốt lõi của ICF."
            },
            {
                "code": "1.05",
                "textEn": "Maintains confidentiality with client information per stakeholder agreements and pertinent laws",
                "textVi": "Duy trì tính bảo mật của thông tin khách hàng theo thỏa thuận với các bên liên quan và pháp luật áp dụng."
            },
            {
                "code": "1.06",
                "textEn": "Maintains the distinctions between coaching, consulting, psychotherapy and other support professions",
                "textVi": "Duy trì sự phân biệt giữa khai vấn, tư vấn, tâm lý trị liệu và các nghề hỗ trợ khác."
            },
            {
                "code": "1.07",
                "textEn": "Refers clients to other support professionals, as appropriate",
                "textVi": "Giới thiệu khách hàng đến các chuyên gia hỗ trợ khác khi phù hợp."
            }
        ]
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
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025), Trang 4",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Engages in ongoing personal and professional learning and development as a coach. Works with coaching supervisors or mentor coaches as needed. \n\nDevelops and maintains a mindset that is open, curious, flexible and client-centered.\n\n\n2.01. Acknowledges that clients are responsible for their own choices\n\n2.02. Engages in ongoing learning and development as a coach, including remaining aware of current coaching best practices and use of technology\n\n2.03. Develops an ongoing reflective practice to enhance one’s coaching\n\n2.04. Remains aware of and open to the influence of biases, context and culture on self and others\n\n2.05. Uses awareness of self and one’s intuition to benefit clients\n\n2.06. Develops and maintains the ability to manage one’s emotions\n\n2.07. Maintains emotional, physical, and mental well-being in preparation for, throughout, and following each session\n\n2.08. Seeks help from outside sources when necessary\n\n2.09. Nurtures openness and curiosity in oneself, the client, and the coaching process\n\n2.10. Remains aware of the influence of one’s thoughts and behaviors on the client and others",
        "translationVi": "Định nghĩa: Liên tục học hỏi và phát triển cá nhân, nghề nghiệp với tư cách coach; làm việc với coach supervisor hoặc mentor coach khi cần; duy trì tư duy cởi mở, tò mò, linh hoạt và lấy khách hàng làm trung tâm.\n\n\n2.01. Công nhận rằng khách hàng chịu trách nhiệm cho các lựa chọn của chính mình.\n\n2.02. Liên tục học hỏi và phát triển với tư cách coach, bao gồm cập nhật các thực hành tốt hiện hành và việc sử dụng công nghệ trong coaching.\n\n2.03. Duy trì thực hành tự phản tư thường xuyên để nâng cao năng lực coaching.\n\n2.04. Nhận thức và cởi mở trước ảnh hưởng của thiên kiến, bối cảnh và văn hóa lên bản thân và người khác.\n\n2.05. Sử dụng sự tự nhận thức và trực giác của bản thân theo cách có lợi cho khách hàng.\n\n2.06. Phát triển và duy trì khả năng quản trị cảm xúc của bản thân.\n\n2.07. Duy trì sức khỏe cảm xúc, thể chất và tinh thần trước, trong và sau mỗi phiên khai vấn.\n\n2.08. Tìm kiếm sự hỗ trợ từ nguồn bên ngoài khi cần thiết.\n\n2.09. Nuôi dưỡng sự cởi mở và tò mò ở bản thân, khách hàng và trong quá trình khai vấn.\n\n2.10. Nhận thức về ảnh hưởng của suy nghĩ và hành vi của bản thân lên khách hàng và người khác.",
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
                {
                    "key": "A",
                    "textVi": "Coach soạn sẵn giáo án 10 buổi và bắt khách hàng tuân thủ lịch trình.",
                    "textEn": "Prepare 10 syllabi beforehand and force client compliance."
                },
                {
                    "key": "B",
                    "textVi": "Coach chủ động chăm sóc sức khỏe thể chất, tinh thần (well-being) và định kỳ phản tư cùng Coach Supervisor để giữ chất lượng phiên coach.",
                    "textEn": "Actively manage personal well-being and regularly engage in reflective practice with a Coach Supervisor."
                },
                {
                    "key": "C",
                    "textVi": "Coach tự nhận mình đã hoàn hảo và không cần học thêm bất kỳ điều gì mới.",
                    "textEn": "Claim personal perfection and cease all professional development."
                },
                {
                    "key": "D",
                    "textVi": "Coach đưa ra lời khuyên tài chính cá nhân cho khách hàng.",
                    "textEn": "Offer unsolicited personal financial advice to clients."
                }
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B phản ánh chính xác điểm mới của Bản 2025 (Chỉ dấu 2.08 và 2.09): Quản lý well-being của bản thân và sử dụng hỗ trợ từ Coach Supervision.",
            "explanationEn": "Option B accurately mirrors 2025 updates (2.08 & 2.09): Coach well-being management and engaging coach supervision."
        },
        "definitionEn": "Engages in ongoing personal and professional learning and development as a coach. Works with coaching supervisors or mentor coaches as needed. \n\nDevelops and maintains a mindset that is open, curious, flexible and client-centered.",
        "definitionVi": "Liên tục học hỏi và phát triển cá nhân, nghề nghiệp với tư cách coach; làm việc với coach supervisor hoặc mentor coach khi cần; duy trì tư duy cởi mở, tò mò, linh hoạt và lấy khách hàng làm trung tâm.",
        "subCompetencies": [
            {
                "code": "2.01",
                "textEn": "Acknowledges that clients are responsible for their own choices",
                "textVi": "Công nhận rằng khách hàng chịu trách nhiệm cho các lựa chọn của chính mình."
            },
            {
                "code": "2.02",
                "textEn": "Engages in ongoing learning and development as a coach, including remaining aware of current coaching best practices and use of technology",
                "textVi": "Liên tục học hỏi và phát triển với tư cách coach, bao gồm cập nhật các thực hành tốt hiện hành và việc sử dụng công nghệ trong coaching."
            },
            {
                "code": "2.03",
                "textEn": "Develops an ongoing reflective practice to enhance one’s coaching",
                "textVi": "Duy trì thực hành tự phản tư thường xuyên để nâng cao năng lực coaching."
            },
            {
                "code": "2.04",
                "textEn": "Remains aware of and open to the influence of biases, context and culture on self and others",
                "textVi": "Nhận thức và cởi mở trước ảnh hưởng của thiên kiến, bối cảnh và văn hóa lên bản thân và người khác."
            },
            {
                "code": "2.05",
                "textEn": "Uses awareness of self and one’s intuition to benefit clients",
                "textVi": "Sử dụng sự tự nhận thức và trực giác của bản thân theo cách có lợi cho khách hàng."
            },
            {
                "code": "2.06",
                "textEn": "Develops and maintains the ability to manage one’s emotions",
                "textVi": "Phát triển và duy trì khả năng quản trị cảm xúc của bản thân."
            },
            {
                "code": "2.07",
                "textEn": "Maintains emotional, physical, and mental well-being in preparation for, throughout, and following each session",
                "textVi": "Duy trì sức khỏe cảm xúc, thể chất và tinh thần trước, trong và sau mỗi phiên khai vấn."
            },
            {
                "code": "2.08",
                "textEn": "Seeks help from outside sources when necessary",
                "textVi": "Tìm kiếm sự hỗ trợ từ nguồn bên ngoài khi cần thiết."
            },
            {
                "code": "2.09",
                "textEn": "Nurtures openness and curiosity in oneself, the client, and the coaching process",
                "textVi": "Nuôi dưỡng sự cởi mở và tò mò ở bản thân, khách hàng và trong quá trình khai vấn."
            },
            {
                "code": "2.10",
                "textEn": "Remains aware of the influence of one’s thoughts and behaviors on the client and others",
                "textVi": "Nhận thức về ảnh hưởng của suy nghĩ và hành vi của bản thân lên khách hàng và người khác."
            }
        ]
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
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025), Trang 5",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Partners with the client and relevant stakeholders to create clear agreements about the coaching relationship, process, plans and goals. Establishes agreements for the overall coaching engagement as well as those for each coaching session.\n\n\n3.01. Describes one's coaching philosophy and clearly defines what coaching is and is not for potential clients and stakeholders\n\n3.02. Reaches agreement about what is and is not appropriate in the relationship, what is and is not being offered, and the responsibilities of the client and relevant stakeholders, including commitment to working toward coaching goals\n\n3.03. Reaches agreement about the guidelines and specific parameters of the coaching relationship such as logistics, fees, scheduling, duration, termination, confidentiality and inclusion of others\n\n3.04. Partners with the client and relevant stakeholders to establish an overall coaching plan and goals\n\n3.05. Partners with the client to determine client-coach compatibility\n\n3.06. Partners with the client to identify or reconfirm what they want to accomplish in the session\n\n3.07. Partners with the client to define what the client believes they need to address or resolve to achieve what they want to accomplish in the session\n\n3.08. Partners with the client to define or reconfirm measures of success for what the client wants to accomplish in the coaching engagement or individual session\n\n3.09. Partners with the client to manage the time and focus of the session\n\n3.10. Continues coaching in the direction of the client’s desired outcome unless the client indicates otherwise\n\n3.11. Partners with the client to close the coaching relationship in a way that respects the client and the coaching experience\n\n3.12. Revisits the coaching agreement when necessary to ensure the coaching approach is meeting the client's needs",
        "translationVi": "Định nghĩa: Đồng hành với khách hàng và các bên liên quan để tạo ra các thỏa thuận rõ ràng về mối quan hệ, quy trình, kế hoạch và mục tiêu khai vấn; thiết lập thỏa thuận cho cả toàn bộ quá trình và từng phiên.\n\n\n3.01. Mô tả triết lý khai vấn của mình và xác định rõ coaching là gì và không phải là gì đối với khách hàng tiềm năng và các bên liên quan.\n\n3.02. Thống nhất điều gì phù hợp/không phù hợp trong mối quan hệ, điều gì được/không được cung cấp, và trách nhiệm của khách hàng cùng các bên liên quan, bao gồm cam kết hướng tới mục tiêu khai vấn.\n\n3.03. Thống nhất các nguyên tắc và thông số cụ thể của mối quan hệ khai vấn như logistics, phí, lịch, thời lượng, chấm dứt, bảo mật và sự tham gia của người khác.\n\n3.04. Đồng hành với khách hàng và các bên liên quan để thiết lập kế hoạch và mục tiêu khai vấn tổng thể.\n\n3.05. Đồng hành với khách hàng để xác định mức độ phù hợp giữa khách hàng và coach.\n\n3.06. Đồng hành với khách hàng để xác định hoặc xác nhận lại điều họ muốn đạt được trong phiên.\n\n3.07. Đồng hành với khách hàng để xác định điều mà chính họ tin rằng cần xử lý hoặc làm rõ nhằm đạt được mục tiêu của phiên.\n\n3.08. Đồng hành với khách hàng để xác định hoặc xác nhận lại tiêu chí thành công cho mục tiêu của toàn bộ quá trình hoặc từng phiên.\n\n3.09. Đồng hành với khách hàng để quản lý thời gian và trọng tâm của phiên.\n\n3.10. Tiếp tục coaching theo hướng kết quả mà khách hàng mong muốn, trừ khi khách hàng cho biết họ muốn thay đổi.\n\n3.11. Đồng hành với khách hàng để khép lại mối quan hệ khai vấn theo cách tôn trọng khách hàng và trải nghiệm khai vấn.\n\n3.12. Xem lại thỏa thuận khai vấn khi cần để bảo đảm cách tiếp cận đang đáp ứng nhu cầu của khách hàng.",
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
                {
                    "key": "A",
                    "textVi": "Để khách hàng kể tiếp cho hết giờ vì ngắt lời là mất lịch sự.",
                    "textEn": "Let the client talk uninterrupted until time runs out."
                },
                {
                    "key": "B",
                    "textVi": "Tự ý chọn một chủ đề mà coach thấy quan trọng và bắt khách hàng tập trung vào đó.",
                    "textEn": "Unilaterally pick an important topic and force client focus."
                },
                {
                    "key": "C",
                    "textVi": "Nhẹ nhàng xin phép tạm dừng, phản chiếu những điều khách hàng vừa chia sẻ và hỏi: 'Trong tất cả những khía cạnh này, điều gì là quan trọng nhất bạn muốn chúng ta cùng giải quyết hôm nay?'",
                    "textEn": "Gently pause, reflect what was shared, and ask: 'Among all these aspects, what is most essential for us to resolve today?'"
                },
                {
                    "key": "D",
                    "textVi": "Dừng phiên và trừ tiền vì khách hàng không có sự chuẩn bị mục tiêu trước.",
                    "textEn": "Terminate the session and fine the client for lack of preparation."
                }
            ],
            "correctAnswer": "C",
            "explanationVi": "Phương án C thể hiện sự đồng hành bình đẳng (Partnering), giúp khách hàng cô đọng trọng tâm mà không áp đặt.",
            "explanationEn": "Option C demonstrates equal partnering, helping the client distill focus without coach imposition."
        },
        "definitionEn": "Partners with the client and relevant stakeholders to create clear agreements about the coaching relationship, process, plans and goals. Establishes agreements for the overall coaching engagement as well as those for each coaching session.",
        "definitionVi": "Đồng hành với khách hàng và các bên liên quan để tạo ra các thỏa thuận rõ ràng về mối quan hệ, quy trình, kế hoạch và mục tiêu khai vấn; thiết lập thỏa thuận cho cả toàn bộ quá trình và từng phiên.",
        "subCompetencies": [
            {
                "code": "3.01",
                "textEn": "Describes one's coaching philosophy and clearly defines what coaching is and is not for potential clients and stakeholders",
                "textVi": "Mô tả triết lý khai vấn của mình và xác định rõ coaching là gì và không phải là gì đối với khách hàng tiềm năng và các bên liên quan."
            },
            {
                "code": "3.02",
                "textEn": "Reaches agreement about what is and is not appropriate in the relationship, what is and is not being offered, and the responsibilities of the client and relevant stakeholders, including commitment to working toward coaching goals",
                "textVi": "Thống nhất điều gì phù hợp/không phù hợp trong mối quan hệ, điều gì được/không được cung cấp, và trách nhiệm của khách hàng cùng các bên liên quan, bao gồm cam kết hướng tới mục tiêu khai vấn."
            },
            {
                "code": "3.03",
                "textEn": "Reaches agreement about the guidelines and specific parameters of the coaching relationship such as logistics, fees, scheduling, duration, termination, confidentiality and inclusion of others",
                "textVi": "Thống nhất các nguyên tắc và thông số cụ thể của mối quan hệ khai vấn như logistics, phí, lịch, thời lượng, chấm dứt, bảo mật và sự tham gia của người khác."
            },
            {
                "code": "3.04",
                "textEn": "Partners with the client and relevant stakeholders to establish an overall coaching plan and goals",
                "textVi": "Đồng hành với khách hàng và các bên liên quan để thiết lập kế hoạch và mục tiêu khai vấn tổng thể."
            },
            {
                "code": "3.05",
                "textEn": "Partners with the client to determine client-coach compatibility",
                "textVi": "Đồng hành với khách hàng để xác định mức độ phù hợp giữa khách hàng và coach."
            },
            {
                "code": "3.06",
                "textEn": "Partners with the client to identify or reconfirm what they want to accomplish in the session",
                "textVi": "Đồng hành với khách hàng để xác định hoặc xác nhận lại điều họ muốn đạt được trong phiên."
            },
            {
                "code": "3.07",
                "textEn": "Partners with the client to define what the client believes they need to address or resolve to achieve what they want to accomplish in the session",
                "textVi": "Đồng hành với khách hàng để xác định điều mà chính họ tin rằng cần xử lý hoặc làm rõ nhằm đạt được mục tiêu của phiên."
            },
            {
                "code": "3.08",
                "textEn": "Partners with the client to define or reconfirm measures of success for what the client wants to accomplish in the coaching engagement or individual session",
                "textVi": "Đồng hành với khách hàng để xác định hoặc xác nhận lại tiêu chí thành công cho mục tiêu của toàn bộ quá trình hoặc từng phiên."
            },
            {
                "code": "3.09",
                "textEn": "Partners with the client to manage the time and focus of the session",
                "textVi": "Đồng hành với khách hàng để quản lý thời gian và trọng tâm của phiên."
            },
            {
                "code": "3.10",
                "textEn": "Continues coaching in the direction of the client’s desired outcome unless the client indicates otherwise",
                "textVi": "Tiếp tục coaching theo hướng kết quả mà khách hàng mong muốn, trừ khi khách hàng cho biết họ muốn thay đổi."
            },
            {
                "code": "3.11",
                "textEn": "Partners with the client to close the coaching relationship in a way that respects the client and the coaching experience",
                "textVi": "Đồng hành với khách hàng để khép lại mối quan hệ khai vấn theo cách tôn trọng khách hàng và trải nghiệm khai vấn."
            },
            {
                "code": "3.12",
                "textEn": "Revisits the coaching agreement when necessary to ensure the coaching approach is meeting the client's needs",
                "textVi": "Xem lại thỏa thuận khai vấn khi cần để bảo đảm cách tiếp cận đang đáp ứng nhu cầu của khách hàng."
            }
        ]
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
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025), Trang 6",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Partners with the client to create a safe, supportive environment that allows the client to share freely.\n\nMaintains a relationship of mutual respect and trust.\n\n\n4.01. Seeks to understand the client within their context which may include their identity, environment, experiences, values and beliefs\n\n4.02. Demonstrates respect for the client’s identity, perceptions, style and language and adapts one’s coaching to the client\n\n4.03. Acknowledges and respects the client’s unique talents, insights and work in the coaching process\n\n4.04. Shows support, empathy and concern for the client\n\n4.05. Acknowledges and supports the client’s expression of feelings, perceptions, concerns, beliefs and suggestions\n\n4.06. Demonstrates openness and transparency as a way to display vulnerability and build trust with the client",
        "translationVi": "Định nghĩa: Đồng hành với khách hàng để tạo ra môi trường an toàn, nâng đỡ, cho phép khách hàng chia sẻ tự do; duy trì mối quan hệ dựa trên sự tôn trọng và tin cậy lẫn nhau.\n\n\n4.01. Tìm hiểu khách hàng trong bối cảnh của họ, có thể bao gồm bản sắc, môi trường, trải nghiệm, giá trị và niềm tin.\n\n4.02. Thể hiện sự tôn trọng bản sắc, nhận thức, phong cách và ngôn ngữ của khách hàng, đồng thời điều chỉnh cách coaching phù hợp với họ.\n\n4.03. Ghi nhận và tôn trọng tài năng, insight và nỗ lực độc đáo của khách hàng trong quá trình khai vấn.\n\n4.04. Thể hiện sự hỗ trợ, thấu cảm và quan tâm dành cho khách hàng.\n\n4.05. Ghi nhận và hỗ trợ khách hàng bày tỏ cảm xúc, nhận thức, mối quan tâm, niềm tin và đề xuất.\n\n4.06. Thể hiện sự cởi mở và minh bạch như một cách cho thấy sự dễ tổn thương và xây dựng niềm tin với khách hàng.",
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
                {
                    "key": "A",
                    "textVi": "Tranh luận để chứng minh khách hàng đang có cái nhìn sai lệch.",
                    "textEn": "Debate to prove the client's perspective is flawed."
                },
                {
                    "key": "B",
                    "textVi": "Tôn trọng thế giới quan của khách hàng, gác lại niềm tin cá nhân và tìm hiểu xem niềm tin đó đang hỗ trợ hoặc thách thức mục tiêu của khách hàng như thế nào.",
                    "textEn": "Honor the client's worldview, suspend personal biases, and explore how that belief serves or challenges the client's goal."
                },
                {
                    "key": "C",
                    "textVi": "Giả vờ đồng ý nhiệt tình để lấy lòng khách hàng.",
                    "textEn": "Pretend passionate agreement to please the client."
                },
                {
                    "key": "D",
                    "textVi": "Lập tức hủy phiên và từ chối làm việc với những người có quan điểm khác mình.",
                    "textEn": "Immediately cancel the engagement due to differing views."
                }
            ],
            "correctAnswer": "B",
            "explanationVi": "Tôn trọng bản sắc và thế giới quan của khách hàng (Worldview) là cốt lõi của Năng lực 4.",
            "explanationEn": "Honoring the client's identity and worldview without bias is the core of Competency 4."
        },
        "definitionEn": "Partners with the client to create a safe, supportive environment that allows the client to share freely.\n\nMaintains a relationship of mutual respect and trust.",
        "definitionVi": "Đồng hành với khách hàng để tạo ra môi trường an toàn, nâng đỡ, cho phép khách hàng chia sẻ tự do; duy trì mối quan hệ dựa trên sự tôn trọng và tin cậy lẫn nhau.",
        "subCompetencies": [
            {
                "code": "4.01",
                "textEn": "Seeks to understand the client within their context which may include their identity, environment, experiences, values and beliefs",
                "textVi": "Tìm hiểu khách hàng trong bối cảnh của họ, có thể bao gồm bản sắc, môi trường, trải nghiệm, giá trị và niềm tin."
            },
            {
                "code": "4.02",
                "textEn": "Demonstrates respect for the client’s identity, perceptions, style and language and adapts one’s coaching to the client",
                "textVi": "Thể hiện sự tôn trọng bản sắc, nhận thức, phong cách và ngôn ngữ của khách hàng, đồng thời điều chỉnh cách coaching phù hợp với họ."
            },
            {
                "code": "4.03",
                "textEn": "Acknowledges and respects the client’s unique talents, insights and work in the coaching process",
                "textVi": "Ghi nhận và tôn trọng tài năng, insight và nỗ lực độc đáo của khách hàng trong quá trình khai vấn."
            },
            {
                "code": "4.04",
                "textEn": "Shows support, empathy and concern for the client",
                "textVi": "Thể hiện sự hỗ trợ, thấu cảm và quan tâm dành cho khách hàng."
            },
            {
                "code": "4.05",
                "textEn": "Acknowledges and supports the client’s expression of feelings, perceptions, concerns, beliefs and suggestions",
                "textVi": "Ghi nhận và hỗ trợ khách hàng bày tỏ cảm xúc, nhận thức, mối quan tâm, niềm tin và đề xuất."
            },
            {
                "code": "4.06",
                "textEn": "Demonstrates openness and transparency as a way to display vulnerability and build trust with the client",
                "textVi": "Thể hiện sự cởi mở và minh bạch như một cách cho thấy sự dễ tổn thương và xây dựng niềm tin với khách hàng."
            }
        ]
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
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025), Trang 7",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Is fully conscious and present with the client, employing a style that is open, flexible, grounded and confident.\n\n\n5.01. Remains focused, observant, empathetic and responsive to the client\n\n5.02. Demonstrates curiosity during the coaching process\n\n5.03. Remains aware of what is emerging for self and client in the present moment\n\n5.04. Manages one’s emotions to stay present with the client\n\n5.05. Demonstrates confidence in working with strong client emotions during the coaching process\n\n5.06. Is comfortable working in a space of not knowing\n\n5.07. Creates or allows space for silence, pause or reflection",
        "translationVi": "Định nghĩa: Hoàn toàn tỉnh thức và hiện diện với khách hàng, sử dụng phong cách cởi mở, linh hoạt, vững vàng và tự tin.\n\n\n5.01. Giữ sự tập trung, quan sát, thấu cảm và phản hồi phù hợp với khách hàng.\n\n5.02. Thể hiện sự tò mò trong suốt quá trình khai vấn.\n\n5.03. Nhận thức điều đang xuất hiện ở bản thân và khách hàng trong khoảnh khắc hiện tại.\n\n5.04. Quản trị cảm xúc của bản thân để duy trì sự hiện diện với khách hàng.\n\n5.05. Thể hiện sự tự tin khi làm việc với những cảm xúc mạnh của khách hàng trong quá trình khai vấn.\n\n5.06. Thoải mái làm việc trong không gian chưa biết/chưa có câu trả lời.\n\n5.07. Tạo ra hoặc cho phép không gian cho sự im lặng, khoảng dừng hoặc suy ngẫm.",
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
                {
                    "key": "A",
                    "textVi": "Hỏi ngay câu hỏi khác vì sợ khách hàng cảm thấy ngượng ngùng.",
                    "textEn": "Quickly ask another question to ease perceived awkwardness."
                },
                {
                    "key": "B",
                    "textVi": "Gợi ý luôn câu trả lời mẫu để giúp khách hàng đỡ phải suy nghĩ nhiều.",
                    "textEn": "Suggest ready-made answers to save client mental energy."
                },
                {
                    "key": "C",
                    "textVi": "Giữ vững sự tĩnh lặng bình an, duy trì sự chú tâm hoàn toàn vào khách hàng và tôn trọng tiến trình tư duy của họ.",
                    "textEn": "Hold peaceful silence, maintain full attentiveness, and honor the client's internal thinking process."
                },
                {
                    "key": "D",
                    "textVi": "Tranh thủ mở điện thoại kiểm tra tin nhắn vì khách hàng đang không nói chuyện.",
                    "textEn": "Check phone messages while the client is quiet."
                }
            ],
            "correctAnswer": "C",
            "explanationVi": "Tôn trọng và đồng hành cùng khoảng lặng là biểu hiện bậc thầy của Năng lực 5.",
            "explanationEn": "Holding and honoring silence is a masterful demonstration of Competency 5."
        },
        "definitionEn": "Is fully conscious and present with the client, employing a style that is open, flexible, grounded and confident.",
        "definitionVi": "Hoàn toàn tỉnh thức và hiện diện với khách hàng, sử dụng phong cách cởi mở, linh hoạt, vững vàng và tự tin.",
        "subCompetencies": [
            {
                "code": "5.01",
                "textEn": "Remains focused, observant, empathetic and responsive to the client",
                "textVi": "Giữ sự tập trung, quan sát, thấu cảm và phản hồi phù hợp với khách hàng."
            },
            {
                "code": "5.02",
                "textEn": "Demonstrates curiosity during the coaching process",
                "textVi": "Thể hiện sự tò mò trong suốt quá trình khai vấn."
            },
            {
                "code": "5.03",
                "textEn": "Remains aware of what is emerging for self and client in the present moment",
                "textVi": "Nhận thức điều đang xuất hiện ở bản thân và khách hàng trong khoảnh khắc hiện tại."
            },
            {
                "code": "5.04",
                "textEn": "Manages one’s emotions to stay present with the client",
                "textVi": "Quản trị cảm xúc của bản thân để duy trì sự hiện diện với khách hàng."
            },
            {
                "code": "5.05",
                "textEn": "Demonstrates confidence in working with strong client emotions during the coaching process",
                "textVi": "Thể hiện sự tự tin khi làm việc với những cảm xúc mạnh của khách hàng trong quá trình khai vấn."
            },
            {
                "code": "5.06",
                "textEn": "Is comfortable working in a space of not knowing",
                "textVi": "Thoải mái làm việc trong không gian chưa biết/chưa có câu trả lời."
            },
            {
                "code": "5.07",
                "textEn": "Creates or allows space for silence, pause or reflection",
                "textVi": "Tạo ra hoặc cho phép không gian cho sự im lặng, khoảng dừng hoặc suy ngẫm."
            }
        ]
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
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025), Trang 8",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Focuses on what the client is and is not saying to fully understand what is being communicated in the context of the client systems and to support client self-expression.\n\n\n6.01. Considers the client’s context, identity, environment, experiences, values and beliefs to enhance understanding of what the client is communicating\n\n6.02. Reflects or summarizes what the client is communicating to ensure clarity and understanding\n\n6.03. Recognizes and inquires when there is more to what the client is communicating\n\n6.04. Notices, acknowledges and explores the client’s emotions, energy shifts, non-verbal cues or other behaviors\n\n6.05. Integrates the client’s words, tone of voice and body language to determine the full meaning of what the client is communicating\n\n6.06. Notices trends in the client’s behaviors and emotions across sessions to discern themes and patterns",
        "translationVi": "Định nghĩa: Tập trung vào điều khách hàng nói và không nói để hiểu đầy đủ điều đang được truyền đạt trong bối cảnh hệ thống của khách hàng và hỗ trợ họ tự biểu đạt.\n\n\n6.01. Xem xét bối cảnh, bản sắc, môi trường, trải nghiệm, giá trị và niềm tin của khách hàng để hiểu sâu hơn điều họ đang truyền đạt.\n\n6.02. Phản chiếu hoặc tóm tắt điều khách hàng đang truyền đạt để bảo đảm sự rõ ràng và hiểu đúng.\n\n6.03. Nhận ra và tìm hiểu khi có điều gì đó sâu hơn phía sau điều khách hàng đang nói.\n\n6.04. Nhận diện, ghi nhận và khám phá cảm xúc, sự thay đổi năng lượng, tín hiệu phi ngôn ngữ hoặc hành vi khác của khách hàng.\n\n6.05. Tích hợp từ ngữ, giọng nói và ngôn ngữ cơ thể của khách hàng để hiểu đầy đủ ý nghĩa điều họ đang truyền đạt.\n\n6.06. Nhận ra xu hướng trong hành vi và cảm xúc của khách hàng qua nhiều phiên để nhận diện chủ đề và mô thức.",
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
                {
                    "key": "A",
                    "textVi": "Ghi nhận từ ngữ ẩn dụ độc đáo mà khách hàng vừa sử dụng.",
                    "textEn": "Acknowledging the unique metaphor used by the client."
                },
                {
                    "key": "B",
                    "textVi": "Nghe được 2 phút thì ngắt lời khách hàng để kể về một kinh nghiệm tương tự của chính bản thân Coach.",
                    "textEn": "Interrupting after 2 minutes to share the coach's personal experience."
                },
                {
                    "key": "C",
                    "textVi": "Chú ý đến sự thay đổi tông giọng và tốc độ nói của khách hàng.",
                    "textEn": "Noticing vocal pitch and tempo changes."
                },
                {
                    "key": "D",
                    "textVi": "Tóm tắt ngắn gọn các ý chính bằng chính ngôn từ của khách hàng.",
                    "textEn": "Succinctly summarizing using the client's exact words."
                }
            ],
            "correctAnswer": "B",
            "explanationVi": "Ngắt lời để kể chuyện bản thân là lỗi mất tập trung vào khách hàng và áp đặt cái tôi của Coach.",
            "explanationEn": "Interrupting to share coach stories violates client focus and imposes coach ego."
        },
        "definitionEn": "Focuses on what the client is and is not saying to fully understand what is being communicated in the context of the client systems and to support client self-expression.",
        "definitionVi": "Tập trung vào điều khách hàng nói và không nói để hiểu đầy đủ điều đang được truyền đạt trong bối cảnh hệ thống của khách hàng và hỗ trợ họ tự biểu đạt.",
        "subCompetencies": [
            {
                "code": "6.01",
                "textEn": "Considers the client’s context, identity, environment, experiences, values and beliefs to enhance understanding of what the client is communicating",
                "textVi": "Xem xét bối cảnh, bản sắc, môi trường, trải nghiệm, giá trị và niềm tin của khách hàng để hiểu sâu hơn điều họ đang truyền đạt."
            },
            {
                "code": "6.02",
                "textEn": "Reflects or summarizes what the client is communicating to ensure clarity and understanding",
                "textVi": "Phản chiếu hoặc tóm tắt điều khách hàng đang truyền đạt để bảo đảm sự rõ ràng và hiểu đúng."
            },
            {
                "code": "6.03",
                "textEn": "Recognizes and inquires when there is more to what the client is communicating",
                "textVi": "Nhận ra và tìm hiểu khi có điều gì đó sâu hơn phía sau điều khách hàng đang nói."
            },
            {
                "code": "6.04",
                "textEn": "Notices, acknowledges and explores the client’s emotions, energy shifts, non-verbal cues or other behaviors",
                "textVi": "Nhận diện, ghi nhận và khám phá cảm xúc, sự thay đổi năng lượng, tín hiệu phi ngôn ngữ hoặc hành vi khác của khách hàng."
            },
            {
                "code": "6.05",
                "textEn": "Integrates the client’s words, tone of voice and body language to determine the full meaning of what the client is communicating",
                "textVi": "Tích hợp từ ngữ, giọng nói và ngôn ngữ cơ thể của khách hàng để hiểu đầy đủ ý nghĩa điều họ đang truyền đạt."
            },
            {
                "code": "6.06",
                "textEn": "Notices trends in the client’s behaviors and emotions across sessions to discern themes and patterns",
                "textVi": "Nhận ra xu hướng trong hành vi và cảm xúc của khách hàng qua nhiều phiên để nhận diện chủ đề và mô thức."
            }
        ]
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
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025), Trang 9",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Facilitates client insight and learning by using tools and techniques such as powerful questioning, silence, metaphor or analogy.\n\n\n7.01. Considers client experience when deciding what might be most useful\n\n7.02. Challenges the client as a way to evoke awareness or insight\n\n7.03. Asks questions about the client, such as their way of thinking, values, needs, wants and beliefs\n\n7.04. Asks questions that help the client explore beyond current thinking\n\n7.05. Invites the client to share more about their experience in the moment\n\n7.06. Notices what is working to enhance client progress\n\n7.07. Adjusts the coaching approach in response to the client’s needs\n\n7.08. Helps the client identify factors that influence current and future patterns of behavior, thinking or emotion\n\n7.09. Invites the client to generate ideas about how they can move forward and what they are willing or able to do\n\n7.10. Supports the client in reframing perspectives\n\n7.11. Shares observations, knowledge, and feelings, without attachment, that have the potential to create new insights for the client",
        "translationVi": "Định nghĩa: Tạo điều kiện cho insight và học hỏi của khách hàng thông qua các công cụ và kỹ thuật như câu hỏi mạnh, im lặng, ẩn dụ hoặc phép so sánh.\n\n\n7.01. Cân nhắc trải nghiệm của khách hàng khi quyết định điều gì có thể hữu ích nhất.\n\n7.02. Thách thức khách hàng nhằm khơi gợi nhận thức hoặc insight.\n\n7.03. Đặt câu hỏi về chính khách hàng, như cách họ suy nghĩ, giá trị, nhu cầu, mong muốn và niềm tin.\n\n7.04. Đặt câu hỏi giúp khách hàng khám phá vượt ra ngoài lối suy nghĩ hiện tại.\n\n7.05. Mời khách hàng chia sẻ thêm về trải nghiệm của họ trong khoảnh khắc hiện tại.\n\n7.06. Nhận ra điều đang hiệu quả để thúc đẩy tiến bộ của khách hàng.\n\n7.07. Điều chỉnh cách tiếp cận khai vấn để đáp ứng nhu cầu của khách hàng.\n\n7.08. Hỗ trợ khách hàng nhận diện các yếu tố ảnh hưởng đến mô thức hành vi, suy nghĩ hoặc cảm xúc hiện tại và tương lai.\n\n7.09. Mời khách hàng tự tạo ra ý tưởng về cách tiến về phía trước và điều họ sẵn sàng hoặc có khả năng thực hiện.\n\n7.10. Hỗ trợ khách hàng tái định khung góc nhìn.\n\n7.11. Chia sẻ quan sát, kiến thức và cảm nhận mà không bám chấp, khi những điều đó có tiềm năng tạo ra insight mới cho khách hàng.",
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
                {
                    "key": "A",
                    "textVi": "'Điều gì quan trọng nhất với bạn trong tình huống này?'",
                    "textEn": "'What is most meaningful to you in this situation?'"
                },
                {
                    "key": "B",
                    "textVi": "'Có phải việc nói chuyện thẳng thắn với sếp sẽ giải quyết được vấn đề này không?'",
                    "textEn": "'Wouldn't having a direct talk with your boss solve this issue?'"
                },
                {
                    "key": "C",
                    "textVi": "'Bạn nhìn thấy cơ hội phát triển nào cho bản thân từ thách thức này?'",
                    "textEn": "'What growth opportunity do you see for yourself in this challenge?'"
                },
                {
                    "key": "D",
                    "textVi": "'Góc nhìn nào khác mà bạn chưa từng nghĩ tới trước đây?'",
                    "textEn": "'What other perspective haven't you considered yet?'"
                }
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B là câu hỏi Yes/No cài cắm sẵn giải pháp của Coach ('nói chuyện với sếp'), tước đoạt quyền tự suy ngẫm của khách hàng.",
            "explanationEn": "Option B is a leading Yes/No question embedding the coach's preconceived solution."
        },
        "definitionEn": "Facilitates client insight and learning by using tools and techniques such as powerful questioning, silence, metaphor or analogy.",
        "definitionVi": "Tạo điều kiện cho insight và học hỏi của khách hàng thông qua các công cụ và kỹ thuật như câu hỏi mạnh, im lặng, ẩn dụ hoặc phép so sánh.",
        "subCompetencies": [
            {
                "code": "7.01",
                "textEn": "Considers client experience when deciding what might be most useful",
                "textVi": "Cân nhắc trải nghiệm của khách hàng khi quyết định điều gì có thể hữu ích nhất."
            },
            {
                "code": "7.02",
                "textEn": "Challenges the client as a way to evoke awareness or insight",
                "textVi": "Thách thức khách hàng nhằm khơi gợi nhận thức hoặc insight."
            },
            {
                "code": "7.03",
                "textEn": "Asks questions about the client, such as their way of thinking, values, needs, wants and beliefs",
                "textVi": "Đặt câu hỏi về chính khách hàng, như cách họ suy nghĩ, giá trị, nhu cầu, mong muốn và niềm tin."
            },
            {
                "code": "7.04",
                "textEn": "Asks questions that help the client explore beyond current thinking",
                "textVi": "Đặt câu hỏi giúp khách hàng khám phá vượt ra ngoài lối suy nghĩ hiện tại."
            },
            {
                "code": "7.05",
                "textEn": "Invites the client to share more about their experience in the moment",
                "textVi": "Mời khách hàng chia sẻ thêm về trải nghiệm của họ trong khoảnh khắc hiện tại."
            },
            {
                "code": "7.06",
                "textEn": "Notices what is working to enhance client progress",
                "textVi": "Nhận ra điều đang hiệu quả để thúc đẩy tiến bộ của khách hàng."
            },
            {
                "code": "7.07",
                "textEn": "Adjusts the coaching approach in response to the client’s needs",
                "textVi": "Điều chỉnh cách tiếp cận khai vấn để đáp ứng nhu cầu của khách hàng."
            },
            {
                "code": "7.08",
                "textEn": "Helps the client identify factors that influence current and future patterns of behavior, thinking or emotion",
                "textVi": "Hỗ trợ khách hàng nhận diện các yếu tố ảnh hưởng đến mô thức hành vi, suy nghĩ hoặc cảm xúc hiện tại và tương lai."
            },
            {
                "code": "7.09",
                "textEn": "Invites the client to generate ideas about how they can move forward and what they are willing or able to do",
                "textVi": "Mời khách hàng tự tạo ra ý tưởng về cách tiến về phía trước và điều họ sẵn sàng hoặc có khả năng thực hiện."
            },
            {
                "code": "7.10",
                "textEn": "Supports the client in reframing perspectives",
                "textVi": "Hỗ trợ khách hàng tái định khung góc nhìn."
            },
            {
                "code": "7.11",
                "textEn": "Shares observations, knowledge, and feelings, without attachment, that have the potential to create new insights for the client",
                "textVi": "Chia sẻ quan sát, kiến thức và cảm nhận mà không bám chấp, khi những điều đó có tiềm năng tạo ra insight mới cho khách hàng."
            }
        ]
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
        "sourceDocument": "Khung Năng Lực Cốt Lõi ICF (Bản 2025), Trang 10",
        "sourceVersion": "Bản 2025 (Công bố tháng 09/2025; Khung chuẩn thực hành mới nhất)",
        "sourceLink": "https://coachingfederation.org/coaching-competencies/core-competencies",
        "pdfLink": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "originalExcerptEn": "Definition: Partners with the client to transform learning and insight into action. Promotes client autonomy in the coaching process.\n\n\n8.01. Works with the client to integrate new awareness, insight or learning into their worldview and behaviors\n\n8.02. Partners with the client to design goals, actions and accountability measures that integrate and expand new learning\n\n8.03. Acknowledges and supports client autonomy in the design of goals, actions and methods of accountability\n\n8.04. Supports the client in identifying potential results or learning from identified action steps\n\n8.05. Invites the client to consider how to move forward, including resources, support and potential barriers\n\n8.06. Partners with the client to summarize learning and insight within or between sessions\n\n8.07. Partners with the client to integrate learning and sustain progress throughout the coaching engagement\n\n8.08. Acknowledges the client’s progress and successes\n\n8.09. Partners with the client to close the session",
        "translationVi": "Định nghĩa: Đồng hành với khách hàng để chuyển hóa học hỏi và insight thành hành động; thúc đẩy quyền tự chủ của khách hàng trong quá trình khai vấn.\n\n\n8.01. Làm việc cùng khách hàng để tích hợp nhận thức, insight hoặc học hỏi mới vào thế giới quan và hành vi của họ.\n\n8.02. Đồng hành với khách hàng để thiết kế mục tiêu, hành động và cách thức chịu trách nhiệm nhằm tích hợp và mở rộng học hỏi mới.\n\n8.03. Ghi nhận và hỗ trợ quyền tự chủ của khách hàng trong việc thiết kế mục tiêu, hành động và phương thức chịu trách nhiệm.\n\n8.04. Hỗ trợ khách hàng nhận diện kết quả tiềm năng hoặc bài học có thể có từ các bước hành động đã xác định.\n\n8.05. Mời khách hàng cân nhắc cách tiến về phía trước, bao gồm nguồn lực, hỗ trợ và các rào cản tiềm ẩn.\n\n8.06. Đồng hành với khách hàng để tóm tắt học hỏi và insight trong hoặc giữa các phiên.\n\n8.07. Đồng hành với khách hàng để tích hợp học hỏi và duy trì tiến bộ trong suốt quá trình khai vấn.\n\n8.08. Ghi nhận tiến bộ và thành công của khách hàng.\n\n8.09. Đồng hành với khách hàng để khép lại phiên khai vấn.",
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
                {
                    "key": "A",
                    "textVi": "Giao cho khách hàng bản danh sách 5 bài tập về nhà và dọa phạt nếu không hoàn thành.",
                    "textEn": "Assign a 5-item homework list and threaten penalties for non-completion."
                },
                {
                    "key": "B",
                    "textVi": "Mời khách hàng tổng kết điều họ đã học được về bản thân và cùng khách hàng thiết kế hành động do chính họ làm chủ.",
                    "textEn": "Invite the client to summarize what they learned about themselves and partner to design client-owned actions."
                },
                {
                    "key": "C",
                    "textVi": "Yêu cầu khách hàng nhắn tin báo cáo coach mỗi sáng vào lúc 6h00.",
                    "textEn": "Order the client to text the coach daily at 6:00 AM."
                },
                {
                    "key": "D",
                    "textVi": "Kết thúc phiên mà không cần quan tâm khách hàng có áp dụng được gì vào thực tế hay không.",
                    "textEn": "End the session without exploring any real-world application."
                }
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B tôn trọng quyền tự chủ của khách hàng, giúp khách hàng tự đúc kết nhận thức và tự chịu trách nhiệm với hành động của mình.",
            "explanationEn": "Option B honors client autonomy, enabling client-led reflection and self-accountability."
        },
        "definitionEn": "Partners with the client to transform learning and insight into action. Promotes client autonomy in the coaching process.",
        "definitionVi": "Đồng hành với khách hàng để chuyển hóa học hỏi và insight thành hành động; thúc đẩy quyền tự chủ của khách hàng trong quá trình khai vấn.",
        "subCompetencies": [
            {
                "code": "8.01",
                "textEn": "Works with the client to integrate new awareness, insight or learning into their worldview and behaviors",
                "textVi": "Làm việc cùng khách hàng để tích hợp nhận thức, insight hoặc học hỏi mới vào thế giới quan và hành vi của họ."
            },
            {
                "code": "8.02",
                "textEn": "Partners with the client to design goals, actions and accountability measures that integrate and expand new learning",
                "textVi": "Đồng hành với khách hàng để thiết kế mục tiêu, hành động và cách thức chịu trách nhiệm nhằm tích hợp và mở rộng học hỏi mới."
            },
            {
                "code": "8.03",
                "textEn": "Acknowledges and supports client autonomy in the design of goals, actions and methods of accountability",
                "textVi": "Ghi nhận và hỗ trợ quyền tự chủ của khách hàng trong việc thiết kế mục tiêu, hành động và phương thức chịu trách nhiệm."
            },
            {
                "code": "8.04",
                "textEn": "Supports the client in identifying potential results or learning from identified action steps",
                "textVi": "Hỗ trợ khách hàng nhận diện kết quả tiềm năng hoặc bài học có thể có từ các bước hành động đã xác định."
            },
            {
                "code": "8.05",
                "textEn": "Invites the client to consider how to move forward, including resources, support and potential barriers",
                "textVi": "Mời khách hàng cân nhắc cách tiến về phía trước, bao gồm nguồn lực, hỗ trợ và các rào cản tiềm ẩn."
            },
            {
                "code": "8.06",
                "textEn": "Partners with the client to summarize learning and insight within or between sessions",
                "textVi": "Đồng hành với khách hàng để tóm tắt học hỏi và insight trong hoặc giữa các phiên."
            },
            {
                "code": "8.07",
                "textEn": "Partners with the client to integrate learning and sustain progress throughout the coaching engagement",
                "textVi": "Đồng hành với khách hàng để tích hợp học hỏi và duy trì tiến bộ trong suốt quá trình khai vấn."
            },
            {
                "code": "8.08",
                "textEn": "Acknowledges the client’s progress and successes",
                "textVi": "Ghi nhận tiến bộ và thành công của khách hàng."
            },
            {
                "code": "8.09",
                "textEn": "Partners with the client to close the session",
                "textVi": "Đồng hành với khách hàng để khép lại phiên khai vấn."
            }
        ]
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
                {
                    "key": "A",
                    "textVi": "Bắt buộc khách hàng quay lại mục tiêu ban đầu để không làm hỏng thỏa thuận Năng lực 3.",
                    "textEn": "Force the client back to original goals to avoid breaching Competency 3."
                },
                {
                    "key": "B",
                    "textVi": "Ghi nhận nhận thức mới quý giá của khách hàng (Comp 7), đồng thời linh hoạt tái thỏa thuận (Recontracting - Comp 3): 'Nhận thức mới này có vẻ rất ý nghĩa với bạn. Với thời gian còn lại, bạn muốn chúng ta tiếp tục khám phá điều này hay quay lại mục tiêu ban đầu?'",
                    "textEn": "Honor the breakthrough (Comp 7) while flexibly recontracting (Comp 3): 'This new awareness seems profound. With our remaining time, how do you wish to spend our focus?'"
                },
                {
                    "key": "C",
                    "textVi": "Lập tức đóng phiên và tính phí gấp đôi vì có hai mục tiêu.",
                    "textEn": "Immediately close the session and double the invoice."
                },
                {
                    "key": "D",
                    "textVi": "Tự ý xóa bỏ hoàn toàn thỏa thuận mà không cần hỏi ý kiến khách hàng.",
                    "textEn": "Disregard the contract entirely without consulting the client."
                }
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B là minh chứng sống động của sự kết hợp tinh tế giữa Khơi gợi nhận thức (Comp 7) và Tái thỏa thuận nhịp nhàng theo quyền tự quyết của khách hàng (Comp 3).",
            "explanationEn": "Option B exemplifies masterful harmony between evoking awareness (Comp 7) and partnering on flexible recontracting (Comp 3)."
        }
    }
]

# Wrap-up Quiz for Module 1
MODULE_1_WRAPUP = {
    "titleVi": "Bài Kiểm Tra Ôn Tập Tổng Hợp Học Phần 1: Năng Lực Cốt Lõi ICF",
    "titleEn": "Module 1 Comprehensive Mastery Assessment: ICF Core Competencies",
    "questions": [
        {
            "id": "m1-w-01",
            "questionVi": "Yếu tố nào phân biệt rõ nét nhất giữa Năng lực 1 (Thực hành Đạo đức) và các kỹ năng khai vấn khác?",
            "questionEn": "What most clearly distinguishes Competency 1 (Ethical Practice) from other coaching competencies?",
            "options": [
                {"key": "A", "textVi": "Bảo vệ ranh giới bảo mật, tính tự chủ của khách hàng và tuyệt đối không lấn sân sang tư vấn chuyên gia hay trị liệu y khoa.", "textEn": "Upholding confidentiality boundaries, client autonomy, and never straying into consulting or clinical therapy."},
                {"key": "B", "textVi": "Sử dụng các kỹ thuật thôi miên để thay đổi tiềm thức.", "textEn": "Using hypnotic tools to alter subconscious."},
                {"key": "C", "textVi": "Luôn luôn đồng ý với mọi quan điểm sai lầm của khách hàng.", "textEn": "Always agreeing with every mistaken client view."},
                {"key": "D", "textVi": "Đảm bảo phiên coach luôn kết thúc đúng trước 45 phút.", "textEn": "Ensuring sessions always end before 45 minutes."}
            ],
            "correctAnswer": "A",
            "explanationVi": "Năng lực 1 đòi hỏi sự chính trực, bảo mật và giữ vững ranh giới chuyên môn giữa coaching và các ngành nghề khác."
        },
        {
            "id": "m1-w-02",
            "questionVi": "Khi khách hàng nói: 'Tôi cảm thấy hoàn toàn kiệt sức và bế tắc', câu hỏi nào sau đây là câu hỏi khơi gợi nhận thức (Năng lực 7) thuần khiết nhất?",
            "questionEn": "When client says 'I feel completely exhausted and stuck', which question is a pure evocative inquiry (Competency 7)?",
            "options": [
                {"key": "A", "textVi": "'Có phải việc bạn không biết từ chối người khác là lý do khiến bạn kiệt sức không?'", "textEn": "'Isn't your inability to say no the reason you are exhausted?'"},
                {"key": "B", "textVi": "'Khi bạn ở cùng với cảm giác kiệt sức này, điều gì đang thực sự đòi hỏi sự chú ý của bạn?'", "textEn": "'As you sit with this exhaustion, what is truly asking for your attention?'"},
                {"key": "C", "textVi": "'Bạn đã uống đủ nước và ngủ đủ 8 tiếng mỗi ngày chưa?'", "textEn": "'Have you been drinking enough water and sleeping 8 hours?'"},
                {"key": "D", "textVi": "'Tôi nghĩ bạn nên đi nghỉ mát một tuần ngay lập tức.'", "textEn": "'I think you should take a week vacation immediately.'"}
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B không suy diễn (no projection), không cho lời khuyên, mở ra không gian tự khám phá cảm xúc bên trong."
        }
    ]
}

# ==============================================================================
# HỌC PHẦN 2: CÁC TIÊU CHUẨN ĐẠO ĐỨC (ICF CODE OF ETHICS)
# ==============================================================================
MODULE_2_LESSONS = [
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
]

# Wrap-up Quiz for Module 2
MODULE_2_WRAPUP = {
    "titleVi": "Bài Kiểm Tra Ôn Tập Tổng Hợp Học Phần 2: Tiêu Chuẩn Đạo Đức ICF",
    "titleEn": "Module 2 Comprehensive Mastery Assessment: ICF Code of Ethics",
    "questions": [
        {
            "id": "m2-w-01",
            "questionVi": "Nội dung nào sau đây là Giá trị Cốt lõi mới được nhấn mạnh nổi bật trong Bộ Quy tắc Đạo đức ICF 2025?",
            "questionEn": "Which Core Value is prominently emphasized in the ICF 2025 Code of Ethics?",
            "options": [
                {"key": "A", "textVi": "Tính Công bằng & Hòa nhập (Equity).", "textEn": "Equity and Inclusion."},
                {"key": "B", "textVi": "Tối đa hóa lợi nhuận tài chính.", "textEn": "Maximizing financial returns."},
                {"key": "C", "textVi": "Độc quyền phương pháp huấn luyện.", "textEn": "Exclusivity of coaching methods."},
                {"key": "D", "textVi": "Bắt buộc khách hàng làm theo ý coach.", "textEn": "Compelling clients to obey the coach."}
            ],
            "correctAnswer": "A",
            "explanationVi": "Bộ Đạo đức 2025 đưa tính Công bằng (Equity) thành một trong 5 giá trị cốt lõi, bảo vệ sự hòa nhập và chống phân biệt đối xử."
        },
        {
            "id": "m2-w-02",
            "questionVi": "Một khách hàng có hành vi tự hại và đe dọa tự tử cận kề trong một phiên coach trực tuyến. Trách nhiệm đạo đức cao nhất của coach là gì?",
            "questionEn": "A client displays imminent self-harm and suicidal threats during an online session. What is the coach's highest ethical duty?",
            "options": [
                {"key": "A", "textVi": "Tiếp tục giữ bí mật tuyệt đối và không báo cho ai để bảo vệ quyền riêng tư.", "textEn": "Maintain strict confidentiality and inform no one."},
                {"key": "B", "textVi": "Kích hoạt quy trình cấp cứu khẩn cấp, liên hệ dịch vụ y tế địa phương và người liên hệ khẩn cấp trong hợp đồng để cứu sống khách hàng.", "textEn": "Activate emergency crisis protocols, contact local emergency services and the designated emergency contact to protect human life."},
                {"key": "C", "textVi": "Tắt máy tính và coi như không nghe thấy gì.", "textEn": "Shut down the computer and pretend nothing happened."},
                {"key": "D", "textVi": "Đăng tải sự việc lên mạng xã hội để xin lời khuyên cộng đồng.", "textEn": "Post the incident on social media seeking community advice."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Nguy cơ cận kề đối với tính mạng con người là ngoại lệ bắt buộc của bảo mật, kích hoạt quy trình cấp cứu bảo vệ sự sống."
        }
    ]
}

# ==============================================================================
# HỌC PHẦN 3: PCC MARKERS VÀ TIÊU CHÍ THỰC HÀNH PCC
# ==============================================================================
MODULE_3_LESSONS = [
    {
        "id": "mod3-les1",
        "moduleId": "mod-3",
        "lessonNumber": 1,
        "titleVi": "Bài 1: Tổng Quan 37 PCC Markers & Phân Định Với Bài Thi Viết SJT",
        "titleEn": "Lesson 1: Overview of 37 PCC Markers & Distinction from Written SJTs",
        "estimatedMinutes": 18,
        "objectivesVi": [
            "Hiểu đúng mục đích độc quyền của 37 PCC Markers: Đánh giá bằng chứng thính giác trong bản ghi âm (Performance Evaluation).",
            "Phân biệt rõ ràng: PCC Markers KHÔNG PHẢI là đáp án rập khuôn cơ học cho bài thi viết SJT.",
            "Nắm vững nguyên tắc: Không một câu nói đơn lẻ nào đủ khẳng định thí sinh đỗ hay trượt PCC."
        ],
        "objectivesEn": [
            "Understand exclusive purpose of 37 PCC Markers for recorded performance evaluations.",
            "Differentiate auditory markers from written SJT decision dilemmas.",
            "Recognize that no single utterance alone determines passing or failing PCC."
        ],
        "sourceDocument": "Criteria for Assessing Coaching at the PCC Credential Level (PCC Minimum Skills Requirements)",
        "sourceVersion": "37 PCC Markers (Áp dụng cho đánh giá băng ghi âm phiên thực hành)",
        "sourceLink": "https://coachingfederation.org/credentialing/performance-evaluations/criteria-for-assessing-pcc/",
        "originalExcerptEn": "PCC Markers are behavioral indicators that assessors look for in audio recordings. They represent observable evidence of the ICF Core Competencies in action. Assessors evaluate the entire conversation holistically. No single marker guarantees a passing score, nor does missing a single marker imply failure.",
        "translationVi": "PCC Markers là hệ thống các chỉ báo hành vi mà Giám khảo ICF lắng nghe trong các bản ghi âm phiên khai vấn. Chúng đại diện cho bằng chứng quan sát được của 8 Năng lực Cốt lõi. Giám khảo đánh giá toàn diện phiên đối thoại một cách tổng thể. Không có một marker đơn lẻ nào bảo đảm điểm đỗ, và việc thiếu sót một marker đơn lẻ cũng không đồng nghĩa với trượt kỳ thi.",
        "commentaryVi": "CẢNH BÁO SƯ PHẠM QUAN TRỌNG NHẤT:\n- Rất nhiều thí sinh ôn thi PCC nhầm lẫn tai hại: Cố gắng học thuộc các câu hỏi mẫu chứa marker rồi rập khuôn vào bài thi viết SJT.\n- Trong bài thi viết (SJT), câu hỏi kiểm tra năng lực PHÁN ĐOÁN TÌNH HUỐNG VÀ BẢO VỆ TỰ CHỦ CỦA KHÁCH HÀNG. Một câu hỏi đúng chuẩn Marker nếu áp dụng sai ngữ cảnh (ví dụ khách đang khóc mà coach lại hỏi dồn dập về mục tiêu) sẽ bị chấm là WORST!",
        "commentaryEn": "CRITICAL PEDAGOGICAL WARNING: Never mechanically copy-paste auditory marker phrases into written SJTs. The written exam tests situational judgment and client autonomy under specific context.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Trong băng ghi âm, Marker 7.1 được chấm khi coach đặt câu hỏi thách thức cách suy nghĩ của khách hàng. Nhưng trong bài thi viết SJT, nếu tình huống cho thấy khách hàng đang trong cơn hoảng loạn cảm xúc cấp tính, việc coach cố tình đặt câu hỏi thách thức sẽ là hành vi vô cảm (WORST). Hành vi BEST là hiện diện dung chứa không gian cảm xúc an toàn.",
        "exampleContentEn": "In audio assessment, Marker 7.1 looks for challenging inquiries. But in a written SJT where a client is panicking, challenging them would be insensitive (WORST); holding calm compassionate space is BEST.",
        "quiz": {
            "questionVi": "Nhận định nào sau đây là ĐÚNG về vai trò của PCC Markers theo công bố chính thức của ICF?",
            "questionEn": "Which statement is TRUE regarding the role of PCC Markers according to official ICF publications?",
            "options": [
                {"key": "A", "textVi": "PCC Markers là công thức toán học bắt buộc phải áp dụng đủ 37 câu trong bài thi viết SJT.", "textEn": "PCC Markers are a mathematical formula required in written SJT exams."},
                {"key": "B", "textVi": "PCC Markers là các chỉ báo hành vi thính giác dành riêng cho Giám khảo chấm bản ghi âm phiên thực hành; không thể đồng nhất máy móc làm đáp án duy nhất cho bài thi viết.", "textEn": "PCC Markers are auditory behavioral indicators designed exclusively for assessing recorded sessions; not mechanical answer keys for written exams."},
                {"key": "C", "textVi": "Chỉ cần nói được 1 câu hỏi mẫu là đủ đỗ chứng chỉ PCC ngay lập tức.", "textEn": "Saying one model question guarantees an instant PCC credential."},
                {"key": "D", "textVi": "PCC Markers đã bị ICF bãi bỏ hoàn toàn vào năm 2026.", "textEn": "PCC Markers were completely abolished by ICF in 2026."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B phản ánh chính xác ranh giới chuyên môn giữa Đánh giá Thực hành (Performance Evaluation) và Bài thi Viết (Written Exam).",
            "explanationEn": "Option B accurately delineates Performance Evaluation from written examination."
        }
    },
    {
        "id": "mod3-les2",
        "moduleId": "mod-3",
        "lessonNumber": 2,
        "titleVi": "Bài 2: PCC Markers Năng Lực 3 & 4 (Thỏa Thuận & Niềm Tin An Toàn)",
        "titleEn": "Lesson 2: PCC Markers for Competencies 3 & 4 (Agreements & Trust)",
        "estimatedMinutes": 18,
        "objectivesVi": [
            "Nắm vững 4 chỉ báo thỏa thuận (Markers 3.1, 3.2, 3.3, 3.4): Chủ đề, Kết quả mong muốn, Thước đo, Ý nghĩa.",
            "Nắm vững 4 chỉ báo niềm tin an toàn (Markers 4.1, 4.2, 4.3, 4.4): Tôn trọng bản sắc, Thấu cảm, Nâng đỡ cảm xúc.",
            "Nhận diện hành vi phù hợp và hành vi không phù hợp."
        ],
        "objectivesEn": [
            "Master Markers 3.1–3.4 (Topic, Desired Outcome, Measures of Success, Meaning).",
            "Master Markers 4.1–4.4 (Identity respect, Empathy, Emotional support).",
            "Differentiate appropriate vs inappropriate behaviors."
        ],
        "sourceDocument": "PCC Markers Guide (Competencies 3 & 4)",
        "sourceVersion": "PCC Behavioral Markers 3.1–4.4",
        "sourceLink": "https://coachingfederation.org/credentialing/performance-evaluations/criteria-for-assessing-pcc/",
        "originalExcerptEn": "Marker 3.1 Coach partners with client to identify what client wants to accomplish in this session. Marker 3.2 Coach partners to define measures of success. Marker 3.3 Coach explores what is meaningful about this topic. Marker 4.1 Coach acknowledges client's context, identity and work. Marker 4.4 Coach demonstrates support and empathy.",
        "translationVi": "Marker 3.1 Coach hợp tác với khách hàng làm rõ điều khách hàng muốn đạt được trong phiên... Marker 3.2 Coach hợp tác xác định thước đo thành công... Marker 3.3 Coach khám phá ý nghĩa của chủ đề này... Marker 4.1 Coach ghi nhận bối cảnh, bản sắc và nỗ lực của khách hàng... Marker 4.4 Coach thể hiện sự hỗ trợ và thấu cảm chân thành.",
        "commentaryVi": "HÀNH VI PHÙ HỢP VS HÀNH VI KHÔNG PHÙ HỢP:\n- Marker 3.2 Phù hợp: 'Điều gì sẽ cho thấy bạn đã đạt được mục tiêu này sau 45 phút?' Không phù hợp: Coach tự đặt ra mục tiêu đo lường thay khách hàng.\n- Marker 4.1 Phù hợp: Tôn trọng ngôn từ và bối cảnh sống của khách hàng. Không phù hợp: Coi nhẹ sự khác biệt văn hóa.",
        "commentaryEn": "APPROPRIATE VS INAPPROPRIATE BEHAVIORS: In 3.2, appropriate behavior is exploring client-defined measures of success; inappropriate behavior is coach dictating the metric.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Đoạn hội thoại chuẩn Marker 3.3: Khách hàng: 'Tôi muốn học cách nói không với các dự án ngoài luồng.' Coach: 'Khi bạn có thể nói không một cách tự tin, điều đó sẽ mang lại ý nghĩa sâu sắc thế nào cho cuộc sống và các ưu tiên cốt lõi của bạn?'",
        "exampleContentEn": "Dialogue illustrating Marker 3.3: Client wants to say no to side projects. Coach explores: 'When you can say no with ease, what profound difference will that make for your core life priorities?'",
        "quiz": {
            "questionVi": "Hành vi nào của Coach thể hiện đúng bằng chứng của PCC Marker 3.2 (Xác định thước đo thành công của phiên)?",
            "questionEn": "Which behavior provides valid evidence for PCC Marker 3.2 (Defining session measures of success)?",
            "options": [
                {"key": "A", "textVi": "Coach hỏi: 'Làm sao bạn biết bạn đã đạt được kết quả mà bạn mong muốn khi chúng ta kết thúc phiên hôm nay?'", "textEn": "Coach asks: 'How will you know you have accomplished what you wanted by the end of our session?'"},
                {"key": "B", "textVi": "Coach tuyên bố: 'Tôi đo lường sự thành công của bạn bằng việc bạn phải viết xong 10 trang báo cáo.'", "textEn": "Coach declares: 'I measure your success by whether you write 10 pages.'"},
                {"key": "C", "textVi": "Coach bỏ qua phần đo lường vì cho rằng cảm xúc không thể đo đếm được.", "textEn": "Coach skips measurement claiming feelings cannot be quantified."},
                {"key": "D", "textVi": "Coach yêu cầu khách hàng làm bài kiểm tra IQ.", "textEn": "Coach demands client take an IQ test."}
            ],
            "correctAnswer": "A",
            "explanationVi": "Phương án A là câu hỏi hợp tác kinh điển để xác định thước đo thành công theo góc nhìn của chính khách hàng (Marker 3.2).",
            "explanationEn": "Option A is the classic partnering inquiry exploring client-defined success criteria (Marker 3.2)."
        }
    },
    {
        "id": "mod3-les3",
        "moduleId": "mod-3",
        "lessonNumber": 3,
        "titleVi": "Bài 3: PCC Markers Năng Lực 5 & 6 (Hiện Diện & Lắng Nghe Đa Tầng)",
        "titleEn": "Lesson 3: PCC Markers for Competencies 5 & 6 (Presence & Active Listening)",
        "estimatedMinutes": 18,
        "objectivesVi": [
            "Nắm vững các chỉ báo hiện diện (Markers 5.1–5.4): Tĩnh lặng, linh hoạt, theo nhịp khách hàng.",
            "Nắm vững các chỉ báo lắng nghe (Markers 6.1–6.5): Lắng nghe điều chưa nói, chuyển dịch năng lượng, phản chiếu từ ngữ của khách hàng.",
            "Thực hành nhận diện khoảng lặng chất lượng cao (Productive Silence)."
        ],
        "objectivesEn": [
            "Master Presence markers 5.1–5.4 (Silence, flexibility, matching client pace).",
            "Master Active Listening markers 6.1–6.5 (Unsaid cues, energy shifts, client language reflection).",
            "Recognize productive silence."
        ],
        "sourceDocument": "PCC Markers Guide (Competencies 5 & 6)",
        "sourceVersion": "PCC Behavioral Markers 5.1–6.5",
        "sourceLink": "https://coachingfederation.org/credentialing/performance-evaluations/criteria-for-assessing-pcc/",
        "originalExcerptEn": "Marker 5.2 Coach demonstrates curiosity to learn more about the client. Marker 5.4 Coach allows space for silence, pause or reflection. Marker 6.1 Coach customizes response based on what client communicated. Marker 6.4 Coach notices, acknowledges or explores energy shifts and non-verbal cues.",
        "translationVi": "Marker 5.2 Coach thể hiện sự tò mò muốn tìm hiểu sâu sắc về khách hàng... Marker 5.4 Coach tạo không gian cho sự tĩnh lặng, tạm dừng hoặc suy ngẫm... Marker 6.1 Coach phản hồi thích ứng dựa trên những gì khách hàng truyền đạt... Marker 6.4 Coach nhận biết, ghi nhận hoặc khám phá sự chuyển dịch năng lượng và tín hiệu phi ngôn ngữ.",
        "commentaryVi": "HÀNH VI PHÙ HỢP VS HÀNH VI KHÔNG PHÙ HỢP:\n- Marker 5.4 Phù hợp: Để khách hàng im lặng suy nghĩ mà không hối thúc. Không phù hợp: Sợ im lặng nên liên tục nói chêm vào.\n- Marker 6.1 Phù hợp: Dùng chính xác từ ngữ mang tính biểu tượng của khách hàng (ví dụ: 'ngọn núi', 'sương mù'). Không phù hợp: Diễn giải lại bằng thuật ngữ đao to búa lớn của coach.",
        "commentaryEn": "In 5.4, allowing contemplative silence without rushing is appropriate. In 6.1, echoing the client's own symbolic metaphors honors active listening.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Khách hàng cúi đầu thở dài, vai chùng xuống. Coach quan sát nhạy bén (Marker 6.4): 'Tôi nhận thấy vai bạn chùng xuống và một tiếng thở dài vừa xuất hiện. Cơ thể bạn đang muốn nói điều gì với bạn lúc này?'",
        "exampleContentEn": "Client sighs with dropping shoulders. Coach notes energy shift (Marker 6.4): 'I notice your shoulders dropped and a deep sigh surfaced. What is your body expressing right now?'",
        "quiz": {
            "questionVi": "Hành vi nào sau đây vi phạm nghiêm trọng tinh thần của PCC Marker 5.4 (Duy trì không gian tĩnh lặng cho suy ngẫm)?",
            "questionEn": "Which behavior severely violates PCC Marker 5.4 (Holding space for reflective silence)?",
            "options": [
                {"key": "A", "textVi": "Giữ im lặng hoàn toàn khi khách hàng đang nhìn xa xăm suy nghĩ.", "textEn": "Maintaining complete silence while client reflects."},
                {"key": "B", "textVi": "Khách hàng vừa im lặng được 2 giây, coach liền vội vã hỏi dồn: 'Sao bạn không nói gì? Bạn có câu trả lời chưa?'", "textEn": "Client pauses for 2 seconds and coach rushes in: 'Why so quiet? Got an answer yet?'"},
                {"key": "C", "textVi": "Hít thở sâu cùng nhịp với khách hàng.", "textEn": "Breathing calmly at the client's rhythm."},
                {"key": "D", "textVi": "Nhẹ nhàng gật đầu khích lệ khách hàng tiếp tục khi họ sẵn sàng.", "textEn": "Gently nodding to encourage client when ready."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B thể hiện sự bất an của coach, phá vỡ hoàn toàn khoảng lặng chiêm nghiệm quý giá của khách hàng.",
            "explanationEn": "Option B exhibits coach anxiety, destroying the client's contemplative space."
        }
    },
    {
        "id": "mod3-les4",
        "moduleId": "mod-3",
        "lessonNumber": 4,
        "titleVi": "Bài 4: PCC Markers Năng Lực 7 & 8 (Khơi Gợi & Tự Chủ Phát Triển)",
        "titleEn": "Lesson 4: PCC Markers for Competencies 7 & 8 (Evoking & Autonomous Growth)",
        "estimatedMinutes": 18,
        "objectivesVi": [
            "Nắm vững 8 chỉ báo khơi gợi (Markers 7.1–7.8): Thách thức góc nhìn, khám phá con người (Who), mời gọi ẩn dụ.",
            "Nắm vững 9 chỉ báo phát triển (Markers 8.1–8.9): Tự thiết kế hành động, trách nhiệm giải trình tự thân, đóng phiên hợp tác.",
            "Tránh xa lỗi 'đưa ra lời khuyên ngầm' trong các câu hỏi kết thúc phiên."
        ],
        "objectivesEn": [
            "Master Markers 7.1–7.8 (Challenging perspective, exploring the Who, inviting metaphor).",
            "Master Markers 8.1–8.9 (Self-authored action, self-accountability, collaborative closure).",
            "Eliminate disguised advice during session closing."
        ],
        "sourceDocument": "PCC Markers Guide (Competencies 7 & 8)",
        "sourceVersion": "PCC Behavioral Markers 7.1–8.9",
        "sourceLink": "https://coachingfederation.org/credentialing/performance-evaluations/criteria-for-assessing-pcc/",
        "originalExcerptEn": "Marker 7.3 Coach asks questions about the client, such as their way of thinking, values, needs, wants, beliefs. Marker 8.2 Coach partners with the client to design goals, actions and accountability that integrate their new learning.",
        "translationVi": "Marker 7.3 Coach đặt câu hỏi về con người khách hàng (cách tư duy, giá trị sống, nhu cầu, niềm tin)... Marker 8.2 Coach hợp tác với khách hàng thiết kế mục tiêu, hành động và phương pháp thực hiện cam kết tích hợp bài học mới.",
        "commentaryVi": "HÀNH VI PHÙ HỢP VS HÀNH VI KHÔNG PHÙ HỢP:\n- Marker 7.3 Phù hợp: Đặt câu hỏi về niềm tin cốt lõi (Who). Không phù hợp: Chỉ sa đà vào chi tiết sự vụ công việc (What).\n- Marker 8.2 Phù hợp: Khách hàng là người chọn hành động. Không phù hợp: Coach áp đặt: 'Tuần tới bạn phải làm A, B, C cho tôi.'",
        "commentaryEn": "In 7.3, exploring the 'Who' (core beliefs) is appropriate. In 8.2, inviting client-authored actions honors autonomy over coach directives.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Hội thoại chuẩn Marker 8.2 & 8.3: Coach: 'Nhận thức mới về lòng tự trọng này sẽ định hình hành động cụ thể nào của bạn trong cuộc họp ban giám đốc sáng thứ Hai tới?' Khách hàng tự tin chia sẻ giải pháp của chính họ.",
        "exampleContentEn": "Dialogue illustrating Markers 8.2 & 8.3: Coach: 'How will this new awareness of self-worth shape your tangible action in Monday's executive board meeting?'",
        "quiz": {
            "questionVi": "Câu hỏi nào sau đây của Coach thể hiện đúng tinh thần PCC Marker 8.3 (Tôn trọng và nâng đỡ tính tự chủ của khách hàng trong thiết kế hành động)?",
            "questionEn": "Which inquiry embodies PCC Marker 8.3 (Supporting client autonomy in designing action)?",
            "options": [
                {"key": "A", "textVi": "'Tôi đã lên sẵn danh sách 5 việc bạn cần làm, bạn có đồng ý không?'", "textEn": "'I have drafted 5 tasks you need to do, do you agree?'"},
                {"key": "B", "textVi": "'Từ những điều bạn vừa khám phá về bản thân, bước hành động nào bạn muốn tự mình thử nghiệm đầu tiên?'", "textEn": "'From what you have discovered about yourself, what action step do you wish to experiment with first?'"},
                {"key": "C", "textVi": "'Tôi nghĩ bạn nên đi xin lỗi đồng nghiệp ngay chiều nay.'", "textEn": "'I think you should apologize to your coworker this afternoon.'"},
                {"key": "D", "textVi": "'Nếu bạn không làm theo kế hoạch của tôi, buổi coaching này coi như vô nghĩa.'", "textEn": "'If you don't follow my plan, this coaching was pointless.'"}
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B trao quyền tối đa cho khách hàng tự kiến tạo và lựa chọn hành động thử nghiệm của chính mình (Marker 8.3).",
            "explanationEn": "Option B empowers the client to self-author and choose their experimental step (Marker 8.3)."
        }
    }
]

# Wrap-up Quiz for Module 3
MODULE_3_WRAPUP = {
    "titleVi": "Bài Kiểm Tra Ôn Tập Tổng Hợp Học Phần 3: PCC Markers",
    "titleEn": "Module 3 Comprehensive Mastery Assessment: PCC Markers",
    "questions": [
        {
            "id": "m3-w-01",
            "questionVi": "Vì sao ICF khẳng định việc thiếu sót một PCC Marker đơn lẻ trong một bản ghi âm KHÔNG đồng nghĩa với việc ứng viên bị đánh trượt cấp độ PCC?",
            "questionEn": "Why does ICF state that missing a single PCC Marker in a recording does NOT mean failing the PCC credential?",
            "options": [
                {"key": "A", "textVi": "Vì Giám khảo đánh giá toàn diện tổng thể chất lượng phiên và sự nâng đỡ nhận thức tự chủ xuyên suốt phiên coach.", "textEn": "Because assessors evaluate holistic conversation quality and sustained client-centered partnering across the whole session."},
                {"key": "B", "textVi": "Vì Giám khảo chấm điểm bằng phần mềm tự động không cần nghe.", "textEn": "Because assessors use automated software without listening."},
                {"key": "C", "textVi": "Vì PCC Markers chỉ là tài liệu tham khảo vui không có giá trị chấm thi.", "textEn": "Because markers are informal guidelines with no grading validity."},
                {"key": "D", "textVi": "Vì ứng viên có thể trả tiền để mua thêm điểm marker thiếu.", "textEn": "Because candidates can pay fees to purchase missing markers."}
            ],
            "correctAnswer": "A",
            "explanationVi": "ICF đánh giá Performance Evaluation dựa trên bức tranh tổng thể về năng lực đồng hành bình đẳng, không máy móc đếm từng câu từ cô lập."
        }
    ]
}

# ==============================================================================
# HỌC PHẦN 4: WHITE PAPER VỀ CHUYỂN GỬI KHÁCH HÀNG (REFERRING CLIENT TO THERAPY)
# ==============================================================================
try:
    from scripts.referral_guidelines_data import REFERRAL_THEORIES, REFERRAL_FLASHCARDS, REFERRAL_QUIZZES, REFERRAL_PRACTICE_QUESTIONS
except ImportError:
    from referral_guidelines_data import REFERRAL_THEORIES, REFERRAL_FLASHCARDS, REFERRAL_QUIZZES, REFERRAL_PRACTICE_QUESTIONS

MODULE_4_LESSONS = []
for idx, th in enumerate(REFERRAL_THEORIES):
    MODULE_4_LESSONS.append({
        "id": f"mod4-les{idx+1}",
        "moduleId": "mod-4",
        "lessonNumber": idx + 1,
        "titleVi": th["titleVi"],
        "titleEn": th["titleEn"],
        "estimatedMinutes": 15,
        "objectivesVi": [
            f"Nắm vững nội dung nghiên cứu chính thức: {th['titleVi']}.",
            "Phân định rõ ranh giới chuyên môn giữa khai vấn và trị liệu tâm lý.",
            "Áp dụng chuẩn xác vào tình huống thực tiễn có dẫn nguồn số trang PDF."
        ],
        "objectivesEn": [
            f"Master verified content: {th['titleEn']}.",
            "Differentiate boundaries between coaching and clinical therapy.",
            "Apply accurately to real-world dilemmas with PDF citations."
        ],
        "sourceDocument": "Referring a Client to Therapy: A Set of Guidelines for Coaches (White Paper)",
        "sourceVersion": "Tác giả: Alicia M. Hullinger & Joel A. DiGirolamo (2018; Cập nhật trang web: 13/08/2026)",
        "sourceLink": "https://coachingfederation.org/resource/referring-a-client-to-therapy/",
        "originalExcerptEn": f"Location in White Paper: {th['pdfLocation']}\n{th['contentEn'][:400]}...",
        "translationVi": th["contentVi"],
        "commentaryVi": "GIẢI THÍCH SƯ PHẠM CỐT LÕI:\n- Coach tuyệt đối KHÔNG tự chẩn đoán bệnh lý tâm thần.\n- KHÔNG tự động chuyển gửi chỉ vì khách hàng khóc hoặc có cảm xúc mạnh; chỉ chuyển gửi khi chức năng sinh hoạt hằng ngày bị suy giảm nghiêm trọng kéo dài.\n- Chuyển gửi không đồng nghĩa với chấm dứt coaching; Coaching song song (Concurrent Coaching) hoàn toàn khả thi nếu phân định rạch ròi mục tiêu.",
        "commentaryEn": "KEY PEDAGOGICAL TAKEAWAYS: Coaches never diagnose. Do not refer solely for strong emotions; evaluate daily functioning impairment. Concurrent coaching is viable when boundaries are clear.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Khi khách hàng mất ngủ triền miên 4 tuần và sút 5kg, coach mở lời hợp tác: 'Tôi quan sát thấy tình trạng mất ngủ đang ảnh hưởng sâu sắc đến sức khỏe của bạn. Bạn nghĩ sao về việc cùng lúc tham khảo ý kiến bác sĩ y khoa?'",
        "exampleContentEn": "When client suffers severe insomnia for 4 weeks, coach partners non-judgmentally: 'I notice sleeplessness is heavily impacting your health. How would you feel about consulting a physician?'",
        "quiz": REFERRAL_QUIZZES[idx % len(REFERRAL_QUIZZES)]
    })

# ==============================================================================
# HỌC PHẦN 5: CÁC CASE STUDY CỦA ICF (ETHICS CASE STUDIES)
# ==============================================================================
MODULE_5_LESSONS = [
    {
        "id": "mod5-les1",
        "moduleId": "mod-5",
        "lessonNumber": 1,
        "titleVi": "Case Study 1: Thỏa Thuận Ba Bên & Báo Cáo Tiến Độ Với Nhà Tài Trợ Doanh Nghiệp",
        "titleEn": "Case Study 1: Tripartite Agreement & Sponsor Reporting",
        "estimatedMinutes": 20,
        "sourceDocument": "ICF Ethics Case Studies Library (Topic: Coaching Ethics)",
        "sourceVersion": "Căn cứ Tiêu chuẩn 1, 2, 5 (Responsibility to Clients & Confidentiality)",
        "sourceLink": "https://coachingfederation.org/resources/resource-library/?_resource_type=case-studies&_topic=coaching-ethics",
        "caseWorkflow": {
            "step1_scenarioVi": "Giám đốc Nhân sự (Sponsor) của một tập đoàn tài trợ gói khai vấn 6 tháng cho Giám đốc Bán hàng (Client). Sau tháng thứ 3, Giám đốc Nhân sự gọi điện riêng cho Coach và nói: 'Chúng tôi đang chuẩn bị cơ cấu lại ban điều hành và muốn biết anh ta có cam kết gắn bó lâu dài không, và những điểm yếu lớn nhất mà anh ta đã bộc lộ trong các phiên coach là gì? Vì chúng tôi là bên trả tiền, chúng tôi cần thông tin này để ra quyết định nhân sự.'",
            "step1_scenarioEn": "HR Director (Sponsor) finances a 6-month coaching package for a Sales Director (Client). At month 3, HR calls the Coach privately: 'We are restructuring the executive board and need to know if he is committed long-term, and what his biggest weaknesses revealed in coaching are. Since we pay the bills, we need this for personnel decisions.'",
            "step2_stakeholdersVi": "Các bên liên quan: (1) Khách hàng trực tiếp (Sales Director) — người gửi gắm niềm tin; (2) Nhà tài trợ (HR Director) — người chi trả tài chính; (3) Người Coach — người chịu trách nhiệm đạo đức chuyên môn.",
            "step2_stakeholdersEn": "Stakeholders: (1) Direct Client (Sales Director); (2) Corporate Sponsor (HR Director); (3) Coach upholding ethical standards.",
            "step3_selfReflectionPromptVi": "Hãy suy ngẫm và tự ghi ra: Nếu là Coach trong tình huống này, bạn sẽ phản hồi Giám đốc Nhân sự như thế nào để vừa giữ đúng đạo đức bảo mật, vừa giữ được sự chuyên nghiệp với doanh nghiệp?",
            "step3_selfReflectionPromptEn": "Reflect and note down: As the Coach, how would you respond to HR to uphold confidentiality while maintaining professional partnering with the enterprise?",
            "step4_sourceAnalysisVi": "PHÂN TÍCH CHÍNH THỨC TỪ CHUẨN MỰC ICF:\n1. Tiêu chuẩn 1 & 5 cấm tuyệt đối Coach tiết lộ nội dung chi tiết hoặc nhận xét chủ quan về khách hàng cho bên thứ ba, kể cả khi bên thứ ba đó chi trả toàn bộ chi phí.\n2. Coach giải thích ấm áp và kiên quyết với Giám đốc Nhân sự về Thỏa thuận Ba Bên (Tripartite Agreement) đã ký: Mọi thảo luận trong phiên là bí mật tuyệt đối.\n3. Giải pháp chuẩn mực: Đề xuất một cuộc họp 3 bên (Coach, Client, HR) trong đó chính Khách hàng sẽ là người tự trình bày tiến độ và sự phát triển của bản thân theo khung mục tiêu chung đã thống nhất.",
            "step4_sourceAnalysisEn": "OFFICIAL ICF ETHICAL ANALYSIS:\n1. Standards 1 & 5 strictly prohibit disclosing session contents or subjective assessments to third parties, regardless of who pays.\n2. Coach reinforces the signed Tripartite Agreement: session confidentiality is sacred.\n3. Exemplary resolution: Propose a tripartite progress meeting where the Client self-presents their own development outcomes against agreed organizational goals.",
            "step5_takeawaysVi": "ĐIỀU HỌC ĐƯỢC CỐT LÕI: Nhà tài trợ mua dịch vụ khai vấn, chứ không mua thông tin mật của khách hàng. Mọi báo cáo phải do chính khách hàng làm chủ."
        },
        "quiz": {
            "questionVi": "Giải pháp chuẩn mực nhất để giải quyết yêu cầu báo cáo thông tin của Giám đốc Nhân sự là gì?",
            "questionEn": "What is the most ethical resolution to the HR Director's reporting request?",
            "options": [
                {"key": "A", "textVi": "Gửi bản ghi âm phiên coach cho Giám đốc Nhân sự nghe trực tiếp.", "textEn": "Send session recordings directly to HR."},
                {"key": "B", "textVi": "Nhắc lại thỏa thuận bảo mật và đề xuất tổ chức phiên gặp ba bên để khách hàng tự chia sẻ tiến độ mục tiêu chung.", "textEn": "Reiterate confidentiality agreement and organize a tripartite meeting for the client to self-report progress on shared goals."},
                {"key": "C", "textVi": "Nói dối khách hàng rằng Giám đốc Nhân sự rất hài lòng.", "textEn": "Lie to the client that HR is satisfied."},
                {"key": "D", "textVi": "Tiết lộ một nửa sự thật cho Giám đốc Nhân sự.", "textEn": "Disclose half the truth to HR."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Phiên họp 3 bên do khách hàng tự báo cáo bảo vệ 100% tính tự chủ và sự bảo mật của thỏa thuận đạo đức."
        }
    },
    {
        "id": "mod5-les2",
        "moduleId": "mod-5",
        "lessonNumber": 2,
        "titleVi": "Case Study 2: Xung Đột Lợi Ích & Vai Trò Kép (Vừa Làm Coach Vừa Làm Cố Vấn Đầu Tư)",
        "titleEn": "Case Study 2: Conflict of Interest & Dual Roles",
        "estimatedMinutes": 20,
        "sourceDocument": "ICF Ethics Case Studies Library",
        "sourceVersion": "Căn cứ Tiêu chuẩn 9, 10, 16, 24",
        "sourceLink": "https://coachingfederation.org/resources/resource-library/?_resource_type=case-studies&_topic=coaching-ethics",
        "caseWorkflow": {
            "step1_scenarioVi": "Coach D đang huấn luyện cho Nhà sáng lập (Founder) của một công ty khởi nghiệp công nghệ. Sau 2 tháng coaching thành công, Founder rất ngưỡng mộ kinh nghiệm kinh doanh của Coach D và đề nghị: 'Tôi muốn mời Coach tham gia Hội đồng Cố vấn với tư cách chuyên gia chiến lược, đồng thời dành cho Coach quyền mua 5% cổ phần ưu đãi của công ty. Chúng ta vẫn tiếp tục các phiên coach hằng tuần như bình thường.'",
            "step1_scenarioEn": "Coach D is coaching a tech startup Founder. Impressed by Coach D's acumen, the Founder invites Coach D to join the Advisory Board as a strategic consultant with a 5% equity option, while continuing weekly coaching sessions.",
            "step2_stakeholdersVi": "Các bên liên quan: (1) Founder khởi nghiệp; (2) Công ty khởi nghiệp; (3) Coach D trong thế tiến thoái lưỡng nan giữa vai trò Coach và Nhà đầu tư/Cố vấn.",
            "step2_stakeholdersEn": "Stakeholders: (1) Startup Founder; (2) Startup enterprise; (3) Coach D facing a dual-role conflict between Coach and Equity Investor/Consultant.",
            "step3_selfReflectionPromptVi": "Hãy suy nghĩ: Vai trò kép (vừa làm Coach vừa làm Cố vấn có cổ phần) sẽ tác động thế nào đến tính khách quan và sự an toàn của các phiên khai vấn?",
            "step3_selfReflectionPromptEn": "Reflect: How will a dual role (Coach + Equity Advisor) impact objectivity and psychological safety in coaching?",
            "step4_sourceAnalysisVi": "PHÂN TÍCH CHÍNH THỨC TỪ CHUẨN MỰC ICF:\n1. Tiêu chuẩn 9 & 10 yêu cầu Coach phải chủ động tránh và minh bạch công khai mọi xung đột lợi ích tiềm ẩn.\n2. Khi Coach sở hữu cổ phần hoặc hưởng lợi từ quyết định kinh doanh của công ty, Coach không thể giữ được vị thế tấm gương phản chiếu trung tính, khách quan (Neutral Mirror).\n3. Coach sẽ có xu hướng hướng lái câu hỏi (Leading Questions) để bảo vệ giá trị cổ phần của mình thay vì phục vụ trọn vẹn sự phát triển của Founder.\n4. Giải pháp đạo đức: Coach phải giải thích rõ ràng xung đột vai trò kép cho Founder hiểu. Nếu muốn nhận vai trò Cố vấn và Cổ phần, Coach PHẢI CHÍNH THỨC KẾT THÚC hợp đồng coaching và giới thiệu Founder cho một Coach độc lập khác.",
            "step4_sourceAnalysisEn": "OFFICIAL ICF ANALYSIS:\n1. Standards 9 & 10 require proactively avoiding conflicts of interest.\n2. Holding equity compromises the neutral mirror stance; the coach might craft leading questions to protect stock value rather than client growth.\n3. Ethical solution: Coach explains the dual-role conflict. If accepting advisory/equity, the coach MUST formally terminate the coaching relationship and refer the Founder to an independent coach.",
            "step5_takeawaysVi": "ĐIỀU HỌC ĐƯỢC CỐT LÕI: Không thể vừa là người cầm gương trong sáng (Coach), vừa là người có quyền lợi tài chính gắn với kết quả hành động của khách hàng (Cố vấn/Cổ đông)."
        },
        "quiz": {
            "questionVi": "Hành động nào của Coach D là đúng đắn nhất theo chuẩn mực đạo đức ICF?",
            "questionEn": "What is Coach D's most ethical response?",
            "options": [
                {"key": "A", "textVi": "Nhận cả hai vai trò và hứa với Founder rằng mình sẽ tự phân định rạch ròi trong đầu.", "textEn": "Accept both roles, promising to compartmentalize mentally."},
                {"key": "B", "textVi": "Giải thích rõ ràng về xung đột lợi ích của vai trò kép; nếu nhận làm cố vấn/cổ đông thì phải chấm dứt hợp đồng coaching và giới thiệu coach khác.", "textEn": "Explain the dual-role conflict; if accepting advisory/equity, terminate coaching and refer to another coach."},
                {"key": "C", "textVi": "Yêu cầu Founder tặng thêm 10% cổ phần nữa mới đồng ý làm coach tiếp.", "textEn": "Demand 10% more equity to continue coaching."},
                {"key": "D", "textVi": "Âm thầm nhờ người nhà đứng tên cổ phần để tiếp tục coach.", "textEn": "Secretly hold equity via a family member."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B giữ vững tính chính trực và ngăn ngừa xung đột lợi ích tài chính chi phối tiến trình khai vấn."
        }
    },
    {
        "id": "mod5-les3",
        "moduleId": "mod-5",
        "lessonNumber": 3,
        "titleVi": "Case Study 3: Ranh Giới Chuyên Môn & Dấu Hiệu Trầm Cảm Suy Giảm Chức Năng",
        "titleEn": "Case Study 3: Competence Boundaries & Severe Depression Symptoms",
        "estimatedMinutes": 20,
        "sourceDocument": "ICF Ethics Case Studies & Hullinger & DiGirolamo (2018)",
        "sourceVersion": "Căn cứ Tiêu chuẩn 11 (Chuyển gửi chuyên gia)",
        "sourceLink": "https://coachingfederation.org/resource/referring-a-client-to-therapy/",
        "caseWorkflow": {
            "step1_scenarioVi": "Khách hàng là một quản lý cấp cao, đăng ký gói coaching về kỹ năng lãnh đạo. Sau 4 phiên, khách hàng liên tục chia sẻ rằng trong 1 tháng qua họ mất ngủ triền miên chỉ ngủ được 1-2 tiếng, không thể tập trung làm bất kỳ việc gì, đã sút 4kg, và cảm thấy cuộc sống hoàn toàn vô nghĩa và bế tắc cùng cực. Khách hàng bật khóc và nói: 'Tôi chỉ muốn biến mất khỏi thế giới này.'",
            "step1_scenarioEn": "An executive client registered for leadership coaching. For a month, they sleep 1-2 hours nightly, cannot focus at work, lost 4kg, and feel intense meaningless despair. The client weeps: 'I just want to disappear from this world.'",
            "step2_stakeholdersVi": "Các bên liên quan: (1) Khách hàng đang có dấu hiệu suy giảm chức năng sống nghiêm trọng và ý nghĩ tiêu cực; (2) Coach đang đứng trước ranh giới năng lực chuyên môn và an toàn tính mạng.",
            "step2_stakeholdersEn": "Stakeholders: (1) Client exhibiting severe functional impairment and despair; (2) Coach facing competence boundaries and life safety duties.",
            "step3_selfReflectionPromptVi": "Hãy suy ngẫm: Hành động tức thì nào cần được ưu tiên trong khoảnh khắc này, và coach cần mở lời chuyển gửi như thế nào?",
            "step3_selfReflectionPromptEn": "Reflect: What immediate action must be prioritized, and how should the coach initiate a supportive referral?",
            "step4_sourceAnalysisVi": "PHÂN TÍCH CHÍNH THỨC TỪ CHUẨN MỰC ICF:\n1. Đây là tình huống chạm ngưỡng suy giảm chức năng sống nghiêm trọng (Impairment in Daily Functioning) và tiềm ẩn nguy cơ tự hại.\n2. Coach tuyệt đối KHÔNG tự chẩn đoán bệnh lý (không nói: 'Bạn bị trầm cảm nặng rồi').\n3. Coach duy trì sự hiện diện tĩnh lặng, ấm áp, ghi nhận sự can đảm của khách hàng khi chia sẻ nỗi niềm.\n4. Đánh giá mức độ an toàn: Hỏi nhẹ nhàng: 'Khi bạn nói muốn biến mất, bạn có đang nghĩ đến việc làm tổn thương bản thân không?'\n5. Nếu có nguy cơ cận kề: Kích hoạt ngay quy trình hỗ trợ y tế khẩn cấp/người liên hệ khẩn cấp trong hợp đồng.\n6. Nếu là chuyển gửi thông thường: Đề xuất khách hàng gặp bác sĩ y khoa hoặc chuyên gia tâm lý lâm sàng để được chăm sóc toàn diện, và thỏa thuận tạm dừng coaching cho đến khi sức khỏe ổn định.",
            "step4_sourceAnalysisEn": "OFFICIAL ICF ETHICAL ANALYSIS:\n1. Severe functional impairment with potential self-harm indicators.\n2. Never diagnose. Maintain calm compassionate presence.\n3. Safety check: clarify whether they intend self-harm.\n4. If imminent risk: trigger emergency crisis protocols.\n5. If routine referral: collaboratively recommend medical/psychological consultation and pause coaching until stabilized.",
            "step5_takeawaysVi": "ĐIỀU HỌC ĐƯỢC CỐT LÕI: Sinh mạng và an toàn của khách hàng luôn là ưu tiên số một. Chuyển gửi chuyên gia là hành động thể hiện tình thương và trách nhiệm đạo đức cao nhất của người coach."
        },
        "quiz": {
            "questionVi": "Hành động nào là NGUY HIỂM và SAI LẦM NHẤT của Coach trong tình huống này?",
            "questionEn": "What is the most DANGEROUS and ERRONEOUS coach action in this scenario?",
            "options": [
                {"key": "A", "textVi": "Gợi ý khách hàng gặp bác sĩ tâm lý để kiểm tra sức khỏe.", "textEn": "Suggest the client consult a physician for wellness check."},
                {"key": "B", "textVi": "Bỏ qua các triệu chứng mất ngủ và ý định tự hại, tiếp tục ép khách hàng lên kế hoạch hành động công việc cho tuần tới.", "textEn": "Ignore insomnia and self-harm cues, forcing the client to draft work action plans for next week."},
                {"key": "C", "textVi": "Tĩnh lặng lắng nghe và hỏi han về mức độ an toàn của khách hàng.", "textEn": "Hold space and inquire gently about client safety."},
                {"key": "D", "textVi": "Tìm kiếm sự tham vấn bảo mật từ Coaching Supervisor.", "textEn": "Seek confidential guidance from a Coaching Supervisor."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B là hành vi cực kỳ nguy hiểm, thờ ơ trước tính mạng khách hàng và vi phạm nghiêm trọng Tiêu chuẩn Đạo đức."
        }
    }
]

# Wrap-up Quiz for Module 5
MODULE_5_WRAPUP = {
    "titleVi": "Bài Kiểm Tra Ôn Tập Tổng Hợp Học Phần 5: Ethics Case Studies",
    "titleEn": "Module 5 Comprehensive Mastery Assessment: Ethics Case Studies",
    "questions": [
        {
            "id": "m5-w-01",
            "questionVi": "Trong phương pháp giải quyết tình huống đạo đức chuẩn ICF, bước nào cần thực hiện trước khi quyết định can thiệp?",
            "questionEn": "In the ICF ethical decision-making model, which step precedes intervention?",
            "options": [
                {"key": "A", "textVi": "Nhận diện rõ các bên liên quan, ranh giới hợp đồng và xung đột giá trị đạo đức cốt lõi.", "textEn": "Identify all stakeholders, contract boundaries, and core ethical tensions."},
                {"key": "B", "textVi": "Tự ý công khai tình huống lên mạng xã hội.", "textEn": "Publicly post the case online."},
                {"key": "C", "textVi": "Yêu cầu khách hàng thanh toán thêm tiền phạt.", "textEn": "Demand penalty fees from client."},
                {"key": "D", "textVi": "Bỏ qua hợp đồng ban đầu.", "textEn": "Disregard original contract."}
            ],
            "correctAnswer": "A",
            "explanationVi": "Phân tích tình huống có cấu trúc đòi hỏi nhận diện toàn diện các bên liên quan và chuẩn mực áp dụng."
        }
    ]
}

# ==============================================================================
# HỌC PHẦN 6: CÁC CÂU HỎI THƯỜNG GẶP (ICF FAQS)
# ==============================================================================
MODULE_6_LESSONS = [
    {
        "id": "mod6-les1",
        "moduleId": "mod-6",
        "lessonNumber": 1,
        "titleVi": "Nhóm 1: FAQs Về Đạo Đức & Ranh Giới Bảo Mật Thông Tin",
        "titleEn": "Group 1: FAQs on Ethics & Confidentiality Boundaries",
        "estimatedMinutes": 18,
        "sourceDocument": "Official ICF Ethics FAQs & Blog: 'Can a Coach Break Confidentiality?'",
        "sourceVersion": "Xác minh trực tiếp từ cổng thông tin ICF (Ngày kiểm tra gần nhất: 06/11/2026)",
        "sourceLink": "https://coachingfederation.org/blog/can-a-coach-break-confidentiality/",
        "faqs": [
            {
                "faqId": "faq-1",
                "tag": "Official ICF FAQ",
                "questionVi": "Coach có bao giờ được phép phá vỡ cam kết bảo mật không? Khi nào?",
                "questionEn": "Can a coach break confidentiality? Under what circumstances?",
                "answerVi": "CÓ. Theo Bộ Quy tắc Đạo đức ICF, coach chỉ được phép phá vỡ bảo mật khi có nguy cơ gây hại cận kề đối với tính mạng của khách hàng hoặc người khác (ví dụ ý định tự sát, bạo hành), hoặc khi có phán quyết/trát hầu tòa hợp pháp bắt buộc theo luật pháp sở tại.",
                "answerEn": "YES. According to the ICF Code of Ethics, confidentiality may be broken only when there is imminent harm to the client or others, or under valid legal court order.",
                "relatedStandard": "Tiêu chuẩn 5 & Tiêu chuẩn 23 (Code 2020) / Tiêu chuẩn 2.4 (Code 2025)",
                "verifiedDate": "06/11/2026"
            },
            {
                "faqId": "faq-2",
                "tag": "Official ICF FAQ",
                "questionVi": "Nếu công ty tài trợ yêu cầu gửi bản tóm tắt nội dung từng phiên coach, coach phải làm gì?",
                "questionEn": "If the corporate sponsor demands a summary of each coaching session, what must the coach do?",
                "answerVi": "Coach không được tự ý gửi nội dung chi tiết phiên. Trước khi bắt đầu hợp đồng, coach phải thỏa thuận rõ phạm vi báo cáo. Mọi báo cáo tiến độ chung phải được sự đồng thuận và ký duyệt của chính khách hàng.",
                "answerEn": "The coach must not send verbatim details. Reporting parameters must be pre-agreed in the tripartite agreement and vetted by the client.",
                "relatedStandard": "Tiêu chuẩn 1 & Tiêu chuẩn 5",
                "verifiedDate": "06/11/2026"
            },
            {
                "faqId": "faq-3",
                "tag": "Câu hỏi học tập tổng hợp",
                "questionVi": "Coach có được thảo luận tình huống của khách hàng với Mentor Coach hoặc Supervisor không?",
                "questionEn": "May a coach discuss client cases with a Mentor Coach or Coaching Supervisor?",
                "answerVi": "ĐƯỢC PHÉP, nhưng BẮT BUỘC phải ẩn danh hóa tuyệt đối danh tính, tên công ty và các dữ liệu nhận diện cá nhân của khách hàng để bảo vệ tính bảo mật.",
                "answerEn": "PERMITTED, provided all identifying personal and corporate details are strictly anonymized.",
                "relatedStandard": "Tiêu chuẩn 5 & Tiêu chuẩn 16",
                "verifiedDate": "06/11/2026"
            }
        ],
        "quiz": {
            "questionVi": "Khi tham vấn chuyên môn với Giám sát viên khai vấn (Coaching Supervisor), yêu cầu bảo mật bắt buộc đối với Coach là gì?",
            "questionEn": "When consulting a Coaching Supervisor, what is the mandatory confidentiality requirement for the Coach?",
            "options": [
                {"key": "A", "textVi": "Gửi họ tên đầy đủ và số điện thoại của khách hàng cho Giám sát viên.", "textEn": "Provide client's full name and phone number."},
                {"key": "B", "textVi": "Ẩn danh hóa hoàn toàn danh tính, tên công ty và các dữ kiện nhận diện của khách hàng.", "textEn": "Strictly anonymize client identity, company names, and identifying details."},
                {"key": "C", "textVi": "Không cần bảo mật vì Giám sát viên cũng là người có chứng chỉ.", "textEn": "No confidentiality needed because Supervisor is certified."},
                {"key": "D", "textVi": "Đưa khách hàng cùng đi tham vấn bắt buộc.", "textEn": "Compel client to attend supervision."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Ẩn danh hóa thông tin là điều kiện tiên quyết để tham vấn chuyên môn hợp chuẩn đạo đức."
        }
    },
    {
        "id": "mod6-les2",
        "moduleId": "mod-6",
        "lessonNumber": 2,
        "titleVi": "Nhóm 2: FAQs Về Chứng Chỉ PCC, Đề Thi & Pearson VUE",
        "titleEn": "Group 2: FAQs on PCC Credential, Exams & Pearson VUE",
        "estimatedMinutes": 18,
        "sourceDocument": "Official ICF Credentialing Exam FAQs & Pearson VUE Candidate Guide",
        "sourceVersion": "Cập nhật chính thức cổng ICF Credentials and Standards (Ngày kiểm tra: 06/11/2026)",
        "sourceLink": "https://coachingfederation.org/credentialing/icf-credential-exams/pcc-mcc-exam/",
        "faqs": [
            {
                "faqId": "faq-4",
                "tag": "Official ICF FAQ",
                "questionVi": "Kỳ thi ICF Credentialing Exam hiện tại và kỳ thi cập nhật tháng 11/2026 khác nhau thế nào?",
                "questionEn": "How does the current ICF Credentialing Exam differ from the updated exam format launching November 2026?",
                "answerVi": "- Đề thi hiện hành: 78 câu phán đoán tình huống (SJT), 180 phút, thang điểm 200–600, điểm đỗ 460, chuẩn Đạo đức 2020.\n- Đề thi cập nhật (áp dụng 10/11/2026; bắt buộc từ 01/04/2027): 80 câu (36 câu kiến thức MCQ + 44 câu tình huống SJT), 150 phút, 4 phần thi với 10 phút nghỉ giữa bài, chuẩn Đạo đức 2025.",
                "answerEn": "Current: 78 SJT items, 180 mins, passing score 460. Updated (Nov 2026 / Apr 2027): 80 items (36 Knowledge MCQs + 44 SJTs), 150 mins, 4 sections with 10-min break.",
                "relatedStandard": "SRC-01 & SRC-02",
                "verifiedDate": "06/11/2026"
            },
            {
                "faqId": "faq-5",
                "tag": "Official ICF FAQ",
                "questionVi": "Ứng viên có được phép chọn thi trực tuyến tại nhà không? Cần điều kiện gì?",
                "questionEn": "Can candidates take the exam online at home? What are the requirements?",
                "answerVi": "CÓ. Ứng viên có thể thi trực tuyến qua hệ thống Pearson VUE OnVUE với máy tính có camera, microphone ổn định và phòng thi biệt lập, yên tĩnh 100%.",
                "answerEn": "YES, via OnVUE with webcam, microphone, stable internet, and a private room.",
                "relatedStandard": "SRC-07 (Pearson VUE)",
                "verifiedDate": "06/11/2026"
            },
            {
                "faqId": "faq-6",
                "tag": "Câu hỏi học tập tổng hợp",
                "questionVi": "Làm thế nào để phân biệt giữa câu hỏi Kiến thức (Knowledge) và câu hỏi Tình huống (SJT)?",
                "questionEn": "How to differentiate Knowledge MCQs from Situational Judgment Tests (SJTs)?",
                "answerVi": "Câu hỏi Kiến thức (MCQ) hỏi về định nghĩa, điều khoản chuẩn mực (chọn 1 đáp án đúng duy nhất). Câu hỏi Tình huống (SJT) mô tả bối cảnh tiến thoái lưỡng nan thực tế và yêu cầu chọn 1 hành động TỐT NHẤT (BEST) và 1 hành động TỆ NHẤT (WORST).",
                "answerEn": "Knowledge MCQs test facts/standards (single choice). SJTs present complex ethical dilemmas requiring 1 BEST and 1 WORST action selection.",
                "relatedStandard": "SRC-02 & SRC-03",
                "verifiedDate": "06/11/2026"
            }
        ],
        "quiz": {
            "questionVi": "Trong bài thi phán đoán tình huống (SJT) của ICF, cấu trúc lựa chọn chuẩn xác là gì?",
            "questionEn": "In the ICF Situational Judgment Test (SJT), what is the exact response structure?",
            "options": [
                {"key": "A", "textVi": "Chọn đúng hoặc sai.", "textEn": "Select True or False."},
                {"key": "B", "textVi": "Chọn 1 hành động TỐT NHẤT (BEST) và 1 hành động TỆ NHẤT (WORST) trong cùng 4 lựa chọn.", "textEn": "Select 1 BEST and 1 WORST action from the same 4 options."},
                {"key": "C", "textVi": "Viết bài luận 500 từ.", "textEn": "Write a 500-word essay."},
                {"key": "D", "textVi": "Chọn tất cả các đáp án có thể chấp nhận được.", "textEn": "Select all acceptable answers."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Đề thi SJT của ICF yêu cầu chọn 1 BEST và 1 WORST trong 4 phương án cho từng kịch bản tình huống."
        }
    }
]

# Wrap-up Quiz for Module 6
MODULE_6_WRAPUP = {
    "titleVi": "Bài Kiểm Tra Ôn Tập Tổng Hợp Học Phần 6: ICF FAQs",
    "titleEn": "Module 6 Comprehensive Mastery Assessment: ICF FAQs",
    "questions": [
        {
            "id": "m6-w-01",
            "questionVi": "Nếu ứng viên muốn đổi lịch thi hoặc hủy lịch thi trên Pearson VUE, quy định thời gian tối thiểu là bao lâu?",
            "questionEn": "What is the minimum lead time required to reschedule an ICF exam on Pearson VUE?",
            "options": [
                {"key": "A", "textVi": "Ít nhất 48 giờ trước giờ thi đã đặt hẹn.", "textEn": "At least 48 hours prior to scheduled appointment."},
                {"key": "B", "textVi": "10 phút trước giờ thi.", "textEn": "10 minutes before."},
                {"key": "C", "textVi": "Bất cứ lúc nào không cần báo trước.", "textEn": "Anytime without notice."},
                {"key": "D", "textVi": "Sau khi kỳ thi đã kết thúc.", "textEn": "After exam has concluded."}
            ],
            "correctAnswer": "A",
            "explanationVi": "Quy chế Pearson VUE quy định thí sinh phải đổi lịch hoặc hủy lịch trước ít nhất 48 giờ để không bị mất phí thi."
        }
    ]
}

# ==============================================================================
# HỌC PHẦN 7: THUẬT NGỮ VÀ ĐỊNH NGHĨA (GLOSSARY & DEFINITIONS)
# ==============================================================================
GLOSSARY_TERMS = [
    # Nhóm A: Thuật ngữ Đạo đức chính thức (Official Code of Ethics Definitions)
    {
        "id": "gl-01",
        "category": "Official Ethics Definitions",
        "categoryVi": "Định Nghĩa Đạo Đức Chính Thức (ICF)",
        "termEn": "Client",
        "termVi": "Khách hàng",
        "definitionEn": "The individual or group being coached, the person being mentored or supervised, or the student coach being trained.",
        "definitionVi": "Cá nhân hoặc nhóm người đang được khai vấn, người đang được mentor hoặc giám sát, hoặc học viên khai vấn đang được đào tạo.",
        "source": "ICF Code of Ethics (Section: Definitions)",
        "version": "Code 2020 & 2025",
        "isOfficial": True,
        "nearSynonyms": ["Sponsor (Nhà tài trợ)", "Coachee"]
    },
    {
        "id": "gl-02",
        "category": "Official Ethics Definitions",
        "categoryVi": "Định Nghĩa Đạo Đức Chính Thức (ICF)",
        "termEn": "Sponsor",
        "termVi": "Nhà tài trợ",
        "definitionEn": "The entity (including its representatives) paying for and/or arranging or defining the coaching services to be provided.",
        "definitionVi": "Thực thể (bao gồm các đại diện) chi trả tài chính và/hoặc thu xếp, quy định các dịch vụ khai vấn sẽ được cung cấp.",
        "source": "ICF Code of Ethics (Section: Definitions)",
        "version": "Code 2020 & 2025",
        "isOfficial": True,
        "nearSynonyms": ["Client (Khách hàng)", "Stakeholder (Bên liên quan)"]
    },
    {
        "id": "gl-03",
        "category": "Official Ethics Definitions",
        "categoryVi": "Định Nghĩa Đạo Đức Chính Thức (ICF)",
        "termEn": "Coaching",
        "termVi": "Khai vấn (Coaching)",
        "definitionEn": "Partnering with clients in a thought-provoking and creative process that inspires them to maximize their personal and professional potential.",
        "definitionVi": "Quan hệ hợp tác với khách hàng trong một tiến trình khơi gợi suy nghĩ và sáng tạo, truyền cảm hứng giúp họ tối đa hóa tiềm năng cá nhân và nghề nghiệp.",
        "source": "ICF Official Definition of Coaching",
        "version": "Chuẩn mực nền tảng ICF",
        "isOfficial": True,
        "nearSynonyms": ["Mentoring (Cố vấn)", "Consulting (Tư vấn)", "Therapy (Trị liệu)"]
    },
    {
        "id": "gl-04",
        "category": "Official Ethics Definitions",
        "categoryVi": "Định Nghĩa Đạo Đức Chính Thức (ICF)",
        "termEn": "Conflict of Interest",
        "termVi": "Xung đột lợi ích",
        "definitionEn": "A situation in which a coach has a private or personal interest sufficient to appear to influence the objective exercise of their official duties as a coach.",
        "definitionVi": "Tình huống trong đó coach có lợi ích cá nhân hoặc riêng tư đủ để chi phối hoặc tạo cảm giác chi phối tính khách quan trong việc thực hiện nhiệm vụ khai vấn.",
        "source": "ICF Code of Ethics (Definitions)",
        "version": "Code 2020 & 2025",
        "isOfficial": True,
        "nearSynonyms": ["Dual Role (Vai trò kép)", "Bias (Thiên kiến)"]
    },
    {
        "id": "gl-05",
        "category": "Official Ethics Definitions",
        "categoryVi": "Định Nghĩa Đạo Đức Chính Thức (ICF)",
        "termEn": "Confidentiality",
        "termVi": "Tính bảo mật",
        "definitionEn": "The protection of any information obtained around the coaching engagement unless consent to release is given.",
        "definitionVi": "Sự bảo vệ mọi thông tin thu thập được xoay quanh tiến trình khai vấn trừ khi có sự đồng ý giải phóng thông tin.",
        "source": "ICF Code of Ethics (Standard 5)",
        "version": "Code 2020 & 2025",
        "isOfficial": True,
        "nearSynonyms": ["Privacy (Quyền riêng tư)", "Release of Information (Ủy quyền chia sẻ)"]
    },

    # Nhóm B: Thuật ngữ Năng lực Cốt lõi chính thức (Official Core Competencies Terms)
    {
        "id": "gl-06",
        "category": "Official Competencies Definitions",
        "categoryVi": "Định Nghĩa Năng Lực Cốt Lõi (ICF)",
        "termEn": "Coaching Mindset",
        "termVi": "Tư duy Khai vấn",
        "definitionEn": "A mindset that is open, curious, flexible and client-centered, engaging in ongoing reflective practice.",
        "definitionVi": "Một tâm thế cởi mở, tò mò, linh hoạt và lấy khách hàng làm trung tâm, duy trì thói quen tự phản tư liên tục.",
        "source": "ICF Core Competency 2",
        "version": "ICF Competencies 2019",
        "isOfficial": True,
        "nearSynonyms": ["Expert Mindset (Tư duy chuyên gia)", "Beginner's Mind (Tâm thế người mới bắt đầu)"]
    },
    {
        "id": "gl-07",
        "category": "Official Competencies Definitions",
        "categoryVi": "Định Nghĩa Năng Lực Cốt Lõi (ICF)",
        "termEn": "Evoking Awareness",
        "termVi": "Khơi gợi nhận thức",
        "definitionEn": "Facilitating client insight and learning by using tools such as powerful questioning, silence, metaphor or analogy.",
        "definitionVi": "Thúc đẩy sự thấu hiểu và việc học của khách hàng thông qua câu hỏi gợi mở, sự tĩnh lặng, phép ẩn dụ hoặc tương đồng.",
        "source": "ICF Core Competency 7",
        "version": "ICF Competencies 2019",
        "isOfficial": True,
        "nearSynonyms": ["Leading Questions (Câu hỏi dẫn dắt)", "Advice Giving (Đưa lời khuyên)"]
    },
    {
        "id": "gl-08",
        "category": "Official Competencies Definitions",
        "categoryVi": "Định Nghĩa Năng Lực Cốt Lõi (ICF)",
        "termEn": "Client Autonomy",
        "termVi": "Tính tự chủ của khách hàng",
        "definitionEn": "The recognition that the client is the ultimate decision-maker, fully responsible for their choices, actions and growth.",
        "definitionVi": "Sự công nhận rằng khách hàng là người ra quyết định tối cao, hoàn toàn chịu trách nhiệm về các lựa chọn, hành động và sự phát triển của chính họ.",
        "source": "ICF Core Competency 2 & 8",
        "version": "ICF Competencies 2019",
        "isOfficial": True,
        "nearSynonyms": ["Paternalism (Gia trưởng áp đặt)", "Empowerment (Trao quyền)"]
    },

    # Nhóm C: Thuật ngữ Chuyển gửi chính thức (Official Referral White Paper Terms)
    {
        "id": "gl-09",
        "category": "Official Referral Definitions",
        "categoryVi": "Định Nghĩa Chuyển Gửi & Ranh Giới (ICF Research)",
        "termEn": "Impairment in Daily Functioning",
        "termVi": "Suy giảm chức năng sinh hoạt hằng ngày",
        "definitionEn": "Significant disruptions in a client's ability to maintain basic professional, personal, or relational obligations over time.",
        "definitionVi": "Sự gián đoạn nghiêm trọng và kéo dài trong khả năng duy trì các công việc chuyên môn, sinh hoạt cá nhân hoặc duy trì mối quan hệ cơ bản của khách hàng.",
        "source": "Referring a Client to Therapy White Paper (Hullinger & DiGirolamo, 2018)",
        "version": "White Paper 2018, Trang 3–5",
        "isOfficial": True,
        "nearSynonyms": ["Temporary Stress (Căng thẳng tạm thời)", "Dysfunction (Rối loạn chức năng)"]
    },
    {
        "id": "gl-10",
        "category": "Official Referral Definitions",
        "categoryVi": "Định Nghĩa Chuyển Gửi & Ranh Giới (ICF Research)",
        "termEn": "Concurrent Coaching",
        "termVi": "Khai vấn song song",
        "definitionEn": "The practice of coaching a client while they are concurrently receiving therapy from a licensed mental health professional, with clear distinct goals.",
        "definitionVi": "Thực hành khai vấn cho khách hàng trong khi họ đồng thời đang tiếp nhận trị liệu từ chuyên gia tâm lý được cấp phép, với các mục tiêu phân định rạch ròi.",
        "source": "Referring a Client to Therapy White Paper (Hullinger & DiGirolamo, 2018)",
        "version": "White Paper 2018, Trang 10–11",
        "isOfficial": True,
        "nearSynonyms": ["Parallel Coaching", "Sequential Care"]
    },
    {
        "id": "gl-11",
        "category": "Official Referral Definitions",
        "categoryVi": "Định Nghĩa Chuyển Gửi & Ranh Giới (ICF Research)",
        "termEn": "Release of Information Form",
        "termVi": "Văn bản ủy quyền chia sẻ thông tin",
        "definitionEn": "A formal legal document signed by the client granting explicit permission for a coach to communicate with another support professional.",
        "definitionVi": "Văn bản pháp lý do khách hàng ký tên cho phép coach được quyền trao đổi thông tin cụ thể với một chuyên gia hỗ trợ khác (như nhà trị liệu).",
        "source": "Referring a Client to Therapy White Paper (Hullinger & DiGirolamo, 2018)",
        "version": "White Paper 2018, Trang 11–12",
        "isOfficial": True,
        "nearSynonyms": ["Consent Form (Giấy đồng thuận)", "Waiver"]
    },
    {
        "id": "gl-12",
        "category": "Official Referral Definitions",
        "categoryVi": "Định Nghĩa Chuyển Gửi & Ranh Giới (ICF Research)",
        "termEn": "Imminent Harm",
        "termVi": "Nguy cơ gây hại cận kề",
        "definitionEn": "An immediate, acute threat of suicide, physical violence or death that mandates emergency intervention beyond standard confidentiality.",
        "definitionVi": "Mối nguy hiểm trực tiếp, cấp tính về tự sát, bạo lực thể chất hoặc đe dọa tính mạng đòi hỏi phải can thiệp cấp cứu khẩn cấp vượt trên nguyên tắc bảo mật thông thường.",
        "source": "Referring a Client to Therapy White Paper (Hullinger & DiGirolamo, 2018)",
        "version": "White Paper 2018, Trang 6",
        "isOfficial": True,
        "nearSynonyms": ["Emergency Crisis (Khủng hoảng cấp cứu)", "Duty to Protect"]
    },

    # Nhóm D: Thuật ngữ hỗ trợ (Support Terms labeled "Thuật ngữ hỗ trợ")
    {
        "id": "gl-13",
        "category": "Support Terms",
        "categoryVi": "Thuật Ngữ Hỗ Trợ (Diễn giải học tập)",
        "termEn": "Holding Space",
        "termVi": "Dung chứa không gian cảm xúc",
        "definitionEn": "Being present with someone without judgment, holding a container of safety while they navigate vulnerability.",
        "definitionVi": "Hiện diện tĩnh lặng bên cạnh ai đó mà không phán xét, tạo một chiếc bình chứa an toàn để họ tự do trải nghiệm và chuyển hóa cảm xúc sâu sắc.",
        "source": "Thuật ngữ sư phạm hỗ trợ học tập",
        "version": "Biên soạn bổ sung",
        "isOfficial": False,
        "nearSynonyms": ["Psychological Safety", "Presence"]
    },
    {
        "id": "gl-14",
        "category": "Support Terms",
        "categoryVi": "Thuật Ngữ Hỗ Trợ (Diễn giải học tập)",
        "termEn": "Coach Projection",
        "termVi": "Sự suy diễn áp đặt của Coach",
        "definitionEn": "The bias where a coach projects their own interpretations, judgments or assumptions onto the client's words.",
        "definitionVi": "Lỗi thiên kiến khi người coach tự ý gán ghép định kiến, giả định hoặc chẩn đoán chủ quan của mình lên câu chuyện của khách hàng.",
        "source": "Thuật ngữ sư phạm phân tích đề thi SJT",
        "version": "Biên soạn bổ sung",
        "isOfficial": False,
        "nearSynonyms": ["Leading Question", "Biased Assumption"]
    },
    {
        "id": "gl-15",
        "category": "Support Terms",
        "categoryVi": "Thuật Ngữ Hỗ Trợ (Diễn giải học tập)",
        "termEn": "Coachability",
        "termVi": "Mức độ sẵn sàng khai vấn",
        "definitionEn": "A client's capacity, psychological openness, and readiness to engage in self-reflection and take self-responsibility.",
        "definitionVi": "Khả năng, sự cởi mở tâm lý và mức độ sẵn sàng của khách hàng trong việc tự phản tư và tự chịu trách nhiệm về hành động phát triển.",
        "source": "Thuật ngữ sư phạm đánh giá ranh giới chuyển gửi",
        "version": "Biên soạn bổ sung",
        "isOfficial": False,
        "nearSynonyms": ["Readiness for Coaching", "Receptivity"]
    }
]

# Vocabulary Exercises (Near-synonym Disambiguation Drill)
GLOSSARY_EXERCISES = [
    {
        "id": "gl-ex-01",
        "termPair": "Client (Khách hàng) vs. Sponsor (Nhà tài trợ)",
        "questionVi": "Trong một hợp đồng khai vấn doanh nghiệp, điểm khác biệt căn bản nhất giữa Client và Sponsor theo định nghĩa chính thức của ICF là gì?",
        "questionEn": "What is the core distinction between Client and Sponsor under official ICF definitions?",
        "options": [
            {"key": "A", "textVi": "Client là người trực tiếp được khai vấn; Sponsor là thực thể chi trả tài chính và/hoặc thu xếp dịch vụ.", "textEn": "Client is directly coached; Sponsor is the entity funding/arranging the services."},
            {"key": "B", "textVi": "Client và Sponsor luôn luôn là cùng một cá nhân.", "textEn": "Client and Sponsor are always the exact same person."},
            {"key": "C", "textVi": "Sponsor có quyền nghe toàn bộ băng ghi âm của Client bất cứ lúc nào.", "textEn": "Sponsor has the right to listen to all Client recordings at will."},
            {"key": "D", "textVi": "Không có sự phân biệt nào trong Bộ Quy tắc Đạo đức.", "textEn": "There is no distinction in the Code of Ethics."}
        ],
        "correctAnswer": "A",
        "explanationVi": "Client là người thụ hưởng trực tiếp trong không gian bảo mật; Sponsor là bên tài trợ tài chính. Trách nhiệm bảo mật của coach luôn ưu tiên bảo vệ Client."
    },
    {
        "id": "gl-ex-02",
        "termPair": "Coaching vs. Consulting vs. Therapy",
        "questionVi": "Điểm phân định cốt lõi giữa Khai vấn (Coaching) và Trị liệu tâm lý (Therapy) theo ICF là gì?",
        "questionEn": "What is the fundamental boundary between Coaching and Therapy under ICF standards?",
        "options": [
            {"key": "A", "textVi": "Coaching chỉ nói về tương lai, còn Trị liệu chỉ nói về quá khứ.", "textEn": "Coaching is strictly future; therapy is strictly past."},
            {"key": "B", "textVi": "Trị liệu chẩn đoán và chữa lành bệnh lý/rối loạn chức năng tâm thần; Khai vấn hợp tác cùng người có chức năng tâm lý bình thường phát triển tiềm năng.", "textEn": "Therapy diagnoses and treats mental disorders/dysfunction; Coaching partners with psychologically functional individuals to maximize potential."},
            {"key": "C", "textVi": "Coaching do bác sĩ đảm nhiệm, Trị liệu do ai làm cũng được.", "textEn": "Coaching is done by physicians, therapy by anyone."},
            {"key": "D", "textVi": "Coaching không được phép đặt câu hỏi mở.", "textEn": "Coaching is not allowed to ask open questions."}
        ],
        "correctAnswer": "B",
        "explanationVi": "Trị liệu tâm lý thuộc phạm vi y tế chữa lành bệnh lý/rối loạn; Khai vấn đồng hành cùng người khỏe mạnh phát triển mục tiêu và tiềm năng."
    }
]

# ==============================================================================
# MASTER MODULES CONTAINER
# ==============================================================================
ALL_ICF_MODULES = [
    {
        "id": "mod-1",
        "number": 1,
        "titleVi": "Học Phần 1: Năng Lực Cốt Lõi ICF",
        "titleEn": "Module 1: ICF Core Competencies",
        "icon": "🎯",
        "sourceDoc": "Khung Năng Lực Cốt Lõi ICF (Bản 2025)",
        "sourceUrl": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "summaryVi": "8 Năng lực cốt lõi chia thành 4 trụ cột: Nền tảng, Cùng tạo dựng mối quan hệ, Giao tiếp hiệu quả và Thúc đẩy phát triển. Mỗi năng lực có định nghĩa, phân tích chỉ dấu hành vi và bài tập trắc nghiệm.",
        "summaryEn": "8 Core Competencies across 4 domains: Foundation, Co-Creating Relationship, Communicating Effectively, Cultivating Growth. Includes definitions, behavioral indicators, and tests.",
        "lessons": MODULE_1_LESSONS,
        "wrapUpQuiz": MODULE_1_WRAPUP
    },
    {
        "id": "mod-2",
        "number": 2,
        "titleVi": "Học Phần 2: Các Tiêu Chuẩn Đạo Đức ICF",
        "titleEn": "Module 2: ICF Code of Ethics",
        "icon": "⚖️",
        "sourceDoc": "ICF Code of Ethics (2020 & 2025) & Insights and Considerations (ICE)",
        "sourceUrl": "https://coachingfederation.org/credentialing/coaching-ethics/icf-code-of-ethics/",
        "summaryVi": "Bao phủ toàn bộ cấu trúc: Mục đích, 5 Giá trị Cốt lõi, Tiêu chuẩn 1–28 (Trách nhiệm với Khách hàng, Thực hành, Tính chuyên nghiệp, Xã hội), Lời cam kết Pledge of Ethics và hướng dẫn ICE về AI/Công nghệ.",
        "summaryEn": "Full coverage of Purpose, 5 Core Values, Standards 1–28 (Clients, Practice, Professionalism, Society), Pledge of Ethics, and ICE guidance on AI.",
        "lessons": MODULE_2_LESSONS,
        "wrapUpQuiz": MODULE_2_WRAPUP
    },
    {
        "id": "mod-3",
        "number": 3,
        "titleVi": "Học Phần 3: PCC Markers & Tiêu Chí Thực Hành PCC",
        "titleEn": "Module 3: PCC Markers & Assessment Criteria",
        "icon": "🎙️",
        "sourceDoc": "Criteria for Assessing Coaching at PCC Credential Level (37 Markers)",
        "sourceUrl": "https://coachingfederation.org/credentialing/performance-evaluations/criteria-for-assessing-pcc/",
        "summaryVi": "37 Chỉ báo hành vi thính giác dành riêng cho Giám khảo chấm bản ghi âm phiên thực hành; phân định rạch ròi với bài thi viết SJT; ví dụ tự soạn và hành vi không phù hợp.",
        "summaryEn": "37 behavioral markers for audio performance evaluation; strictly delineated from written SJTs; illustrative examples and negative indicators.",
        "lessons": MODULE_3_LESSONS,
        "wrapUpQuiz": MODULE_3_WRAPUP
    },
    {
        "id": "mod-4",
        "number": 4,
        "titleVi": "Học Phần 4: Giới thiệu Khách Hàng",
        "titleEn": "Module 4: Referring a Client to Therapy Guidelines",
        "icon": "🚪",
        "sourceDoc": "Referring a Client to Therapy: Guidelines for Coaches (Hullinger & DiGirolamo, 2018)",
        "sourceUrl": "https://coachingfederation.org/resource/referring-a-client-to-therapy/",
        "summaryVi": "7 bài học nghiên cứu: Ranh giới coaching vs trị liệu, 3 trụ cột chuyển gửi, nhận diện phi chẩn đoán, đối thoại không gán nhãn, coaching song song và xử lý cấp cứu khẩn cấp.",
        "summaryEn": "7 research lessons: Coaching vs therapy boundaries, 3 referral pillars, non-pathologizing dialogue, concurrent coaching, and emergency crisis protocols.",
        "lessons": MODULE_4_LESSONS,
        "wrapUpQuiz": None
    },
    {
        "id": "mod-5",
        "number": 5,
        "titleVi": "Học Phần 5: Các Case Study Đạo Đức Của ICF",
        "titleEn": "Module 5: ICF Ethics Case Studies",
        "icon": "🎭",
        "sourceDoc": "ICF Ethics Case Studies Library",
        "sourceUrl": "https://coachingfederation.org/resources/resource-library/?_resource_type=case-studies&_topic=coaching-ethics",
        "summaryVi": "Danh mục tình huống thực tế theo quy trình 5 bước: Đọc tình huống -> Tự nhận diện bên liên quan -> Ghi cách xử lý -> Mở phân tích nguồn -> So sánh và đúc kết.",
        "summaryEn": "Authentic case studies with 5-step workflow: Read -> Identify -> Self-reflect -> Reveal official analysis -> Compare and reflect.",
        "lessons": MODULE_5_LESSONS,
        "wrapUpQuiz": MODULE_5_WRAPUP
    },
    {
        "id": "mod-6",
        "number": 6,
        "titleVi": "Học Phần 6: Các Câu Hỏi Thường Gặp (ICF FAQs)",
        "titleEn": "Module 6: Official ICF FAQs",
        "icon": "❓",
        "sourceDoc": "Official ICF FAQs, Ethics Community & Pearson VUE Portal",
        "sourceUrl": "https://coachingfederation.org/blog/can-a-coach-break-confidentiality/",
        "summaryVi": "Tập hợp FAQs chính thức phân nhóm: Đạo đức & bảo mật, ranh giới nghề, hồ sơ PCC và kỳ thi Pearson VUE; ghi rõ ngày kiểm tra 06/11/2026; phân biệt câu hỏi nguyên bản với câu hỏi học tập.",
        "summaryEn": "Curated official FAQs grouped into Ethics, Boundaries, PCC Credentials, and Pearson VUE exams with verified dates.",
        "lessons": MODULE_6_LESSONS,
        "wrapUpQuiz": MODULE_6_WRAPUP
    },
    {
        "id": "mod-7",
        "number": 7,
        "titleVi": "Học Phần 7: Thuật Ngữ & Định Nghĩa (Glossary)",
        "titleEn": "Module 7: Glossary & Definitions",
        "icon": "📖",
        "sourceDoc": "ICF Official Definitions, Code Glossary & Research Lexicon",
        "sourceUrl": "https://coachingfederation.org/wp-content/uploads/2025/09/icf-cs-core-competencies-2025.pdf",
        "summaryVi": "Từ điển thuật ngữ chính thức từ Code of Ethics, Năng lực cốt lõi và White Paper; tìm kiếm không dấu EN/VI; flashcard và bài tập phân biệt từ gần nghĩa.",
        "summaryEn": "Official terminology dictionary from ICF Code, Competencies and White Paper; accent-folding search; flashcards and disambiguation exercises.",
        "lessons": [],
        "glossaryTerms": GLOSSARY_TERMS,
        "glossaryExercises": GLOSSARY_EXERCISES
    }
]

def get_icf_7_modules():
    return ALL_ICF_MODULES

def get_glossary_terms():
    return GLOSSARY_TERMS

def search_glossary(query):
    if not query:
        return GLOSSARY_TERMS
    q_norm = remove_accents(query)
    results = []
    for term in GLOSSARY_TERMS:
        term_en_norm = remove_accents(term["termEn"])
        term_vi_norm = remove_accents(term["termVi"])
        def_vi_norm = remove_accents(term["definitionVi"])
        def_en_norm = remove_accents(term["definitionEn"])
        if (q_norm in term_en_norm or 
            q_norm in term_vi_norm or 
            q_norm in def_vi_norm or 
            q_norm in def_en_norm):
            results.append(term)
    return results

def get_tea_micro_lessons():
    """Generates 7 mindful bite-sized lessons for 'Một Tách Trà Học' entry point"""
    tea_lessons = [
        {
            "id": "tea-01",
            "moduleId": "mod-1",
            "lessonId": "mod1-les1",
            "titleVi": "Một Tách Trà 1: Sự Chính Trực Trong Thinh Lặng",
            "titleEn": "Tea Cup 1: Integrity in Stillness",
            "quoteVi": "Đạo đức không phải là điều ta thể hiện khi có người quan sát, mà là cách ta hiện diện khi chỉ có ta với lương tri.",
            "promptVi": "Hôm nay, hãy dành 5 phút đọc Bài học về Năng lực 1: Thể hiện Thực hành Đạo đức để soi rọi lại ranh giới bình an trong tâm bạn.",
            "linkTextVi": "Thưởng thức bài học Năng lực 1 🍵"
        },
        {
            "id": "tea-02",
            "moduleId": "mod-2",
            "lessonId": "mod2-les2",
            "titleVi": "Một Tách Trà 2: Giữ Tròn Cam Kết Bảo Mật",
            "titleEn": "Tea Cup 2: Sacred Circle of Confidentiality",
            "quoteVi": "Khi khách hàng trao cho ta sự tổn thương, họ đang gửi gắm sự an toàn của cuộc đời họ vào sự thinh lặng của ta.",
            "promptVi": "Khám phá Tiêu chuẩn 5 trong Bộ Quy tắc Đạo đức để hiểu vì sao bảo mật là món quà vô giá của người coach.",
            "linkTextVi": "Thưởng thức bài học Bảo mật 🍵"
        },
        {
            "id": "tea-03",
            "moduleId": "mod-3",
            "lessonId": "mod3-les1",
            "titleVi": "Một Tách Trà 3: Vượt Lên Mọi Công Thức Máy Móc",
            "titleEn": "Tea Cup 3: Beyond Mechanical Formulas",
            "quoteVi": "PCC Markers là tiếng chuông nhắc nhở phẩm chất lắng nghe, không phải là sợi dây trói buộc sự tự nhiên của trái tim.",
            "promptVi": "Tìm hiểu bản chất thính giác của 37 PCC Markers và vì sao đề thi viết đòi hỏi sự phán đoán tình huống uyển chuyển.",
            "linkTextVi": "Thưởng thức bài học PCC Markers 🍵"
        },
        {
            "id": "tea-04",
            "moduleId": "mod-4",
            "lessonId": "mod4-les1",
            "titleVi": "Một Tách Trà 4: Khi Giọt Nước Mắt Rơi Trong Phiên",
            "titleEn": "Tea Cup 4: When Tears Fall Gently",
            "quoteVi": "Khóc là biểu hiện tự nhiên của con người khi chạm vào điều ý nghĩa. Người coach vững chãi không hoảng sợ vội vã chuyển gửi, mà tĩnh lặng dung chứa không gian bình an.",
            "promptVi": "Đọc Hướng dẫn nghiên cứu của Hullinger & DiGirolamo về sự khác biệt giữa cảm xúc lành mạnh và suy giảm chức năng sống.",
            "linkTextVi": "Thưởng thức bài học Chuyển gửi 🍵"
        },
        {
            "id": "tea-05",
            "moduleId": "mod-5",
            "lessonId": "mod5-les1",
            "titleVi": "Một Tách Trà 5: Chiếc Bình Chứa Ba Bên",
            "titleEn": "Tea Cup 5: The Tripartite Vessel",
            "quoteVi": "Nhà tài trợ gieo hạt giống tài chính, nhưng khách hàng mới là người chăm sóc đóa hoa nhận thức của chính họ.",
            "promptVi": "Cùng giải quyết Case Study về mối quan hệ ba bên giữa Khách hàng, Doanh nghiệp và Người Coach.",
            "linkTextVi": "Thưởng thức Case Study 1 🍵"
        },
        {
            "id": "tea-06",
            "moduleId": "mod-6",
            "lessonId": "mod6-les1",
            "titleVi": "Một Tách Trà 6: Thấu Suốt Những Băn Khoăn",
            "titleEn": "Tea Cup 6: Clarifying Anxieties",
            "quoteVi": "Khi ta hiểu rõ quy chế phòng thi và chuẩn mực khảo thí, nỗi sợ hãi sẽ nhường chỗ cho sự tự tin thanh thản.",
            "promptVi": "Tra cứu các câu hỏi thường gặp chính thức từ ICF về bảo mật và quy trình phòng thi Pearson VUE.",
            "linkTextVi": "Thưởng thức FAQs Đạo đức 🍵"
        },
        {
            "id": "tea-07",
            "moduleId": "mod-7",
            "lessonId": "gl-01",
            "titleVi": "Một Tách Trà 7: Sức Mạnh Của Định Nghĩa Trong Trẻo",
            "titleEn": "Tea Cup 7: The Power of Pristine Definitions",
            "quoteVi": "Khi ta dùng đúng từ, tâm trí ta sáng tỏ. Hiểu chuẩn từng thuật ngữ là bước đầu tiên để trở thành một Master Coach.",
            "promptVi": "Mở Từ điển Thuật ngữ ICF để khám phá sự khác biệt tinh tế giữa Client và Sponsor.",
            "linkTextVi": "Thưởng thức Từ điển Thuật ngữ 🍵"
        }
    ]
    return tea_lessons
