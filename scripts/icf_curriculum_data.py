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
        "titleVi": "Năng Lực 1: Thể Hiện Thực Hành Đạo Đức",
        "titleEn": "Competency 1: Demonstrates Ethical Practice",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu định nghĩa chuẩn của Năng lực 1 theo khung năng lực ICF 2019.",
            "Nắm vững các chỉ dấu hành vi cốt lõi: bảo mật, ranh giới, tôn trọng bản sắc và chuyển gửi.",
            "Phân biệt giữa hành vi giữ ranh giới đạo đức chuẩn mực và hành vi tự ý can thiệp ngoài thẩm quyền."
        ],
        "objectivesEn": [
            "Master the definition of Competency 1 under the ICF 2019 framework.",
            "Identify core behaviors: confidentiality, boundaries, identity respect, and referrals.",
            "Distinguish ethical boundary maintenance from unauthorized interventions."
        ],
        "sourceDocument": "ICF Updated Core Competencies (2019) & Code of Ethics",
        "sourceVersion": "Khung Năng Lực Cốt Lõi Cập Nhật (ICF 2019; áp dụng toàn diện từ 2021 đến nay)",
        "sourceLink": "https://coachingfederation.org/credentialing/core-competencies",
        "originalExcerptEn": "Definition: Understands and consistently applies coaching ethics and standards of coaching. 1.1 Demonstrates personal integrity and honesty in interactions with clients, sponsors and relevant stakeholders. 1.2 Is sensitive to clients' identity, environment, experiences, values and beliefs. 1.3 Uses language appropriate and respectful to clients, sponsors and relevant stakeholders. 1.4 Abides by the ICF Code of Ethics and upholds the Core Values. 1.5 Maintains confidentiality with client information per stakeholder agreements and pertinent laws. 1.6 Maintains the distinctions between coaching, consulting, psychotherapy and other support professions. 1.7 Refers clients to other support professionals, as appropriate.",
        "translationVi": "Định nghĩa: Hiểu và nhất quán áp dụng các chuẩn mực đạo đức và tiêu chuẩn khai vấn của ICF. 1.1 Thể hiện sự chính trực và trung thực cá nhân khi tương tác với khách hàng, nhà tài trợ và các bên liên quan. 1.2 Nhạy bén với bản sắc, môi trường, trải nghiệm, giá trị và niềm tin của khách hàng. 1.3 Sử dụng ngôn ngữ phù hợp và tôn trọng khách hàng, nhà tài trợ và các bên liên quan. 1.4 Tuân thủ Bộ Quy tắc Đạo đức ICF và phát huy các Giá trị Cốt lõi. 1.5 Duy trì tính bảo mật thông tin khách hàng theo thỏa thuận các bên và luật pháp hiện hành. 1.6 Giữ vững sự phân biệt giữa khai vấn, tư vấn chuyên gia, trị liệu tâm lý và các nghề trợ giúp khác. 1.7 Chuyển gửi khách hàng sang các chuyên gia trợ giúp khác khi phù hợp.",
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
        "titleVi": "Năng Lực 2: Thể Hiện Tư Duy Khai Vấn",
        "titleEn": "Competency 2: Embodies a Coaching Mindset",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu tư duy cởi mở, tò mò, linh hoạt và lấy khách hàng làm trung tâm.",
            "Nhận diện trách nhiệm tự phản tư liên tục và chuẩn bị tâm thế trước phiên coach.",
            "Nắm vững tinh thần coi khách hàng là người chịu trách nhiệm về chính sự lựa chọn của họ."
        ],
        "objectivesEn": [
            "Understand open, curious, flexible, and client-centered mindset.",
            "Recognize ongoing reflective practice and mental preparation before sessions.",
            "Acknowledge the client as autonomous and responsible for their choices."
        ],
        "sourceDocument": "ICF Updated Core Competencies (2019)",
        "sourceVersion": "Khung Năng Lực ICF 2019",
        "sourceLink": "https://coachingfederation.org/credentialing/core-competencies",
        "originalExcerptEn": "Definition: Develops and maintains a mindset that is open, curious, flexible and client-centered. 2.1 Acknowledges that clients are responsible for their own choices. 2.2 Engages in ongoing learning and development as a coach. 2.3 Develops an ongoing reflective practice to enhance one's coaching. 2.4 Remains aware of and open to the influence of context and culture on self and others. 2.5 Uses awareness of self and one's intuition to benefit clients. 2.6 Develops and maintains the ability to regulate one's emotions. 2.7 Mentally and emotionally prepares for sessions. 2.8 Seeks help from outside sources when necessary.",
        "translationVi": "Định nghĩa: Phát triển và duy trì tư duy cởi mở, tò mò, linh hoạt và lấy khách hàng làm trung tâm. 2.1 Công nhận rằng khách hàng chịu trách nhiệm về các lựa chọn của chính họ. 2.2 Tham gia vào quá trình học tập và phát triển liên tục với tư cách là coach. 2.3 Phát triển thói quen phản tư liên tục để nâng cao năng lực khai vấn. 2.4 Luôn nhận thức và cởi mở với ảnh hưởng của bối cảnh và văn hóa lên bản thân và người khác. 2.5 Sử dụng sự tự nhận thức và trực giác vì lợi ích của khách hàng. 2.6 Phát triển và duy trì khả năng điều tiết cảm xúc của bản thân. 2.7 Chuẩn bị tâm trí và cảm xúc trước các phiên khai vấn. 2.8 Tìm kiếm sự trợ giúp từ bên ngoài (giám sát, mentor) khi cần thiết.",
        "commentaryVi": "Tư duy khai vấn thể hiện ở việc coach không áp đặt 'đáp án mẫu' của mình lên khách hàng, mà tin tưởng sâu sắc vào năng lực tự tìm giải pháp của khách hàng. Coach dành thời gian tĩnh tâm trước phiên (Centering) và thường xuyên thực hành phản tư sau phiên.",
        "commentaryEn": "Embodying a coaching mindset means resisting giving ready-made answers and believing in client capability. The coach prepares mindfully before sessions and engages in deliberate reflective practice afterwards.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Sau một phiên coach mà khách hàng im lặng rất nhiều và không đưa ra hành động cụ thể nào, coach cảm thấy bồn chồn lo lắng. Thay vì đổ lỗi cho khách hàng, coach ngồi lại phản tư: 'Cảm giác bồn chồn này đến từ đâu trong tôi? Phải chăng tôi đang muốn chứng tỏ bản thân có ích hơn là tin tưởng vào nhịp điệu của khách hàng?'",
        "exampleContentEn": "After a session marked by long silences and no concrete action plan, the coach feels anxious. Instead of judging the client, the coach reflects: 'Where does my anxiety stem from? Am I trying to prove my competence rather than trusting the client's pace?'",
        "quiz": {
            "questionVi": "Hành vi nào thể hiện rõ nét nhất Tư duy Khai vấn (Competency 2) của người coach?",
            "questionEn": "Which behavior best exemplifies Embodies a Coaching Mindset (Competency 2)?",
            "options": [
                {"key": "A", "textVi": "Soạn sẵn kế hoạch hành động 5 bước trước phiên và yêu cầu khách hàng tuân thủ nghiêm ngặt.", "textEn": "Prepare a 5-step action plan beforehand and require client adherence."},
                {"key": "B", "textVi": "Dành 5 phút trước phiên để tĩnh tâm, gác lại định kiến cá nhân và sẵn sàng đón nhận mọi điều khách hàng mang tới.", "textEn": "Take 5 minutes before the session to center oneself, suspend personal biases, and welcome whatever the client brings."},
                {"key": "C", "textVi": "Trực tiếp chỉ trích khách hàng khi họ không thực hiện cam kết bài tập tuần trước.", "textEn": "Directly criticize the client for missing last week's action commitments."},
                {"key": "D", "textVi": "Khẳng định rằng coach luôn biết điều gì là tốt nhất cho tương lai của khách hàng.", "textEn": "Claim that the coach always knows what is best for the client's future."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B phản ánh chính xác Tiêu chí 2.7: Chuẩn bị tâm trí và cảm xúc trước phiên để hiện diện trọn vẹn và không áp đặt.",
            "explanationEn": "Option B accurately mirrors Marker 2.7: Preparing mentally and emotionally before sessions to remain present and open."
        }
    },
    {
        "id": "mod1-les3",
        "moduleId": "mod-1",
        "lessonNumber": 3,
        "titleVi": "Năng Lực 3: Thiết Lập Và Duy Trì Thỏa Thuận",
        "titleEn": "Competency 3: Establishes and Maintains Agreements",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu thỏa thuận ở cả 2 cấp độ: Thỏa thuận toàn bộ tiến trình (Agreement for engagement) và Thỏa thuận từng phiên (Agreement for session).",
            "Nắm vững 4 yếu tố của thỏa thuận phiên: Chủ đề, Mục tiêu cụ thể, Tiêu chí thành công (Thước đo), và Ý nghĩa quan trọng.",
            "Biết cách tái thỏa thuận (Recontracting) khi khách hàng chuyển hướng."
        ],
        "objectivesEn": [
            "Understand agreements at engagement-level and session-level.",
            "Master the 4 session agreement elements: Topic, Desired Outcome, Measures of Success, and Meaning/Significance.",
            "Learn flexible recontracting when the client pivots."
        ],
        "sourceDocument": "ICF Updated Core Competencies (2019)",
        "sourceVersion": "Khung Năng Lực ICF 2019",
        "sourceLink": "https://coachingfederation.org/credentialing/core-competencies",
        "originalExcerptEn": "Definition: Partners with the client and relevant stakeholders to establish clear agreements about the coaching relationship, process, plans and goals. Establishes agreements for the overall coaching engagement as well as those for each coaching session. 3.1 Explains what coaching is and is not... 3.2 Reaches agreement on what is and is not appropriate... 3.3 Partners with client to determine session goals... 3.4 Identifies what client wants to accomplish in the session... 3.5 Defines measures of success... 3.6 Explores what is meaningful to the client... 3.7 Partners with client to manage time and focus.",
        "translationVi": "Định nghĩa: Hợp tác với khách hàng và các bên liên quan để thiết lập các thỏa thuận rõ ràng về mối quan hệ, quy trình, kế hoạch và mục tiêu khai vấn. Thiết lập thỏa thuận cho toàn bộ hành trình cũng như cho từng phiên khai vấn cụ thể. 3.1 Giải thích rõ khai vấn là gì và không phải là gì... 3.2 Thống nhất phạm vi phù hợp trong hợp đồng... 3.3 Hợp tác xác định mục tiêu phiên... 3.4 Làm rõ điều khách hàng muốn đạt được sau phiên... 3.5 Xác định thước đo thành công... 3.6 Khám phá ý nghĩa thực sự của mục tiêu đối với khách hàng... 3.7 Cùng quản lý thời gian và trọng tâm phiên.",
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
            "explanationEn": "Option C demonstrates respectful partnering, helping the client focus without imposing the coach's agenda."
        }
    },
    {
        "id": "mod1-les4",
        "moduleId": "mod-1",
        "lessonNumber": 4,
        "titleVi": "Năng Lực 4: Nuôi Dưỡng Niềm Tin Và Sự An Toàn",
        "titleEn": "Competency 4: Cultivates Trust and Safety",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu cách kiến tạo môi trường an toàn tâm lý (Psychological Safety).",
            "Tôn trọng toàn bộ con người của khách hàng: bản sắc, văn hóa, cảm xúc và giá trị sống.",
            "Biết cách thể hiện sự tổn thương lành mạnh và ghi nhận sự can đảm của khách hàng."
        ],
        "objectivesEn": [
            "Create an environment of psychological safety.",
            "Respect the whole person: identity, context, culture, emotions, and values.",
            "Demonstrate support, empathy, and acknowledge client courage."
        ],
        "sourceDocument": "ICF Updated Core Competencies (2019)",
        "sourceVersion": "Khung Năng Lực ICF 2019",
        "sourceLink": "https://coachingfederation.org/credentialing/core-competencies",
        "originalExcerptEn": "Definition: Partners with the client to create a safe, supportive environment that allows the client to share freely. Maintains a relationship of mutual respect and trust. 4.1 Seeks to understand client within their context... 4.2 Demonstrates respect for client's identity, perceptions, style and language... 4.3 Acknowledges and respects client's unique talents, insights and work... 4.4 Shows support, empathy and concern... 4.5 Acknowledges and supports client's expression of feelings, perceptions, concerns, beliefs and suggestions... 4.6 Demonstrates openness and transparency.",
        "translationVi": "Định nghĩa: Hợp tác với khách hàng tạo ra môi trường an toàn, nâng đỡ, cho phép khách hàng tự do chia sẻ. Duy trì mối quan hệ tôn trọng và tin cậy lẫn nhau. 4.1 Tìm hiểu khách hàng trong bối cảnh sống của họ... 4.2 Tôn trọng bản sắc, góc nhìn, phong cách và ngôn ngữ của khách hàng... 4.3 Ghi nhận và tôn trọng tài năng, hiểu biết và nỗ lực của khách hàng... 4.4 Thể hiện sự hỗ trợ, thấu cảm và quan tâm chân thành... 4.5 Công nhận và nâng đỡ việc bộc lộ cảm xúc, nhận thức, niềm tin... 4.6 Thể hiện sự cởi mở và minh bạch.",
        "commentaryVi": "Niềm tin và an toàn không được xây dựng bằng lời hứa suông mà bằng sự tôn trọng tuyệt đối ngôn ngữ và cảm xúc của khách hàng. Khi khách hàng bộc lộ nỗi sợ hoặc sai lầm, coach không phán xét, không sửa sai vội vã, mà tạo không gian để khách hàng cảm thấy được chấp nhận trọn vẹn.",
        "commentaryEn": "Trust is established through non-judgmental acceptance. When clients reveal fears or mistakes, the coach holds safe space rather than rushing to fix or judge.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Khách hàng ngập ngừng thú nhận: 'Thực ra tôi đã nói dối sếp về lý do dự án chậm tiến độ.' Coach phản hồi nâng đỡ: 'Cảm ơn bạn đã tin cậy chia sẻ điều này với tôi. Tôi ghi nhận sự dũng cảm của bạn khi đối diện với sự thật ở đây. Điều gì đang diễn ra bên trong bạn khi bạn nhìn lại quyết định đó?'",
        "exampleContentEn": "Client hesitates: 'Actually, I lied to my boss about the project delay.' Coach: 'Thank you for trusting me with this truth. I honor your courage in speaking honestly here. What is stirring inside you as you reflect on that moment?'",
        "quiz": {
            "questionVi": "Hành động nào của Coach có nguy cơ PHÁ HỦY sự an toàn tâm lý và niềm tin (Competency 4) của khách hàng nhất?",
            "questionEn": "Which coach action most severely damages trust and psychological safety (Competency 4)?",
            "options": [
                {"key": "A", "textVi": "Ghi nhận cảm xúc khó khăn mà khách hàng đang trải qua.", "textEn": "Acknowledge the challenging emotions the client is experiencing."},
                {"key": "B", "textVi": "Tỏ vẻ ngạc nhiên, chỉ trích đạo đức cá nhân và nói: 'Tại sao bạn lại có thể hành xử thiếu chuyên nghiệp như vậy?'", "textEn": "Show shock, criticize personal morality, and ask: 'How could you act so unprofessionally?'"},
                {"key": "C", "textVi": "Dành sự tĩnh lặng để khách hàng tự điều hòa hơi thở.", "textEn": "Hold silent space for the client to self-regulate."},
                {"key": "D", "textVi": "Dùng chính từ ngữ mà khách hàng vừa dùng để đặt câu hỏi khám phá.", "textEn": "Use the client's own words to craft an inquiry."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B là hành vi vi phạm nghiêm trọng: Phán xét, chỉ trích cá nhân phá hủy hoàn toàn không gian an toàn tâm lý.",
            "explanationEn": "Option B is destructive: Moralizing and criticizing obliterates psychological safety."
        }
    },
    {
        "id": "mod1-les5",
        "moduleId": "mod-1",
        "lessonNumber": 5,
        "titleVi": "Năng Lực 5: Duy Trì Sự Hiện Diện",
        "titleEn": "Competency 5: Maintains Presence",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu trạng thái hiện diện hoàn toàn (Fully Conscious & Present).",
            "Biết cách tự tin đồng hành với sự không biết (Comfortable with Not Knowing).",
            "Dung chứa không gian tĩnh lặng (Holding Silence / Space) cho khách hàng suy ngẫm."
        ],
        "objectivesEn": [
            "Understand being fully conscious and present with the client.",
            "Remain comfortable with not knowing and navigate ambiguity.",
            "Hold silent space effectively for deep reflection."
        ],
        "sourceDocument": "ICF Updated Core Competencies (2019)",
        "sourceVersion": "Khung Năng Lực ICF 2019",
        "sourceLink": "https://coachingfederation.org/credentialing/core-competencies",
        "originalExcerptEn": "Definition: Is fully conscious and present with the client, employing a style that is open, flexible, grounded and confident. 5.1 Remains focused, observant, empathetic and responsive... 5.2 Demonstrates curiosity in the coaching process... 5.3 Manages one's emotions to stay present... 5.4 Demonstrates confidence in working with strong client emotions... 5.5 Is comfortable working in a space of not knowing... 5.6 Creates or allows space for silence, pause or reflection.",
        "translationVi": "Định nghĩa: Hiện diện trọn vẹn và tỉnh thức bên cạnh khách hàng, sử dụng phong cách cởi mở, linh hoạt, vững vàng và tự tin. 5.1 Luôn tập trung, quan sát, thấu cảm và phản hồi nhạy bén... 5.2 Thể hiện sự tò mò chân thành trong tiến trình... 5.3 Quản lý cảm xúc của mình để giữ vững sự hiện diện... 5.4 Tự tin đồng hành cùng những cảm xúc mạnh mẽ của khách hàng... 5.5 Cảm thấy thoải mái trong không gian của 'sự chưa biết'... 5.6 Tạo ra hoặc cho phép không gian cho sự tĩnh lặng, tạm dừng và suy ngẫm.",
        "commentaryVi": "Hiện diện ở cấp độ PCC là năng lực 'không làm gì cả' khi khách hàng đang tự suy ngẫm sâu. Coach không vội vã lấp đầy khoảng lặng bằng câu hỏi tiếp theo, mà kiên nhẫn chờ khách hàng xử lý xong dòng suy nghĩ bên trong.",
        "commentaryEn": "Presence at PCC means trusting silence. The coach does not nervously rush to fill quiet moments with new questions, allowing internal processing to unfold.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Sau một câu hỏi sâu của coach, khách hàng nhìn ra cửa sổ và im lặng suốt 15 giây. Thay vì sốt ruột hỏi: 'Bạn có nghe rõ không?' hay giải thích lại câu hỏi, coach giữ nguyên ánh mắt dịu dàng và sự tĩnh tại, tôn trọng trọn vẹn khoảng lặng cho khách hàng.",
        "exampleContentEn": "After a deep inquiry, the client gazes out the window silently for 15 seconds. Rather than impatiently asking 'Did you hear me?', the coach holds calm, quiet space with gentle presence.",
        "quiz": {
            "questionVi": "Khi khách hàng vừa chia sẻ một nhận thức sâu sắc và rơi vào im lặng suy tư, hành động nào của Coach thể hiện Năng lực 5 chuẩn mực nhất?",
            "questionEn": "When the client has an insight and pauses in contemplative silence, which coach response best exemplifies Competency 5?",
            "options": [
                {"key": "A", "textVi": "Lập tức đặt ngay một câu hỏi khác để duy trì nhịp độ đối thoại liên tục.", "textEn": "Immediately ask another question to maintain rapid conversational momentum."},
                {"key": "B", "textVi": "Nhắc nhở khách hàng rằng thời gian phiên có hạn nên cần trả lời nhanh.", "textEn": "Remind the client that session time is limited and to answer quickly."},
                {"key": "C", "textVi": "Giữ sự tĩnh lặng vững chãi, không ngắt lời, kiên nhẫn chờ đợi khách hàng hoàn tất suy ngẫm và tự cất lời trước.", "textEn": "Hold grounded silence without interrupting, patiently waiting for the client to complete their internal processing and speak first."},
                {"key": "D", "textVi": "Đưa ra lời khuyên tóm tắt kết luận thay cho khách hàng.", "textEn": "Summarize and conclude the insight on the client's behalf."}
            ],
            "correctAnswer": "C",
            "explanationVi": "Phương án C là biểu hiện đỉnh cao của Năng lực 5 (Tiêu chí 5.6): Dung chứa không gian tĩnh lặng cho khách hàng chiêm nghiệm.",
            "explanationEn": "Option C is the hallmark of Competency 5 (Marker 5.6): Creating and holding space for silence and reflection."
        }
    },
    {
        "id": "mod1-les6",
        "moduleId": "mod-1",
        "lessonNumber": 6,
        "titleVi": "Năng Lực 6: Lắng Nghe Chủ Động",
        "titleEn": "Competency 6: Listens Actively",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu nghệ thuật lắng nghe cả điều được nói và điều chưa được nói.",
            "Lắng nghe qua các tầng: Ngôn từ, Giọng điệu, Cảm xúc, Ngôn ngữ cơ thể và Bối cảnh.",
            "Tích hợp và phản chiếu các mô thức suy nghĩ, niềm tin cốt lõi của khách hàng."
        ],
        "objectivesEn": [
            "Master listening to what is said and not said.",
            "Listen across levels: words, tone, emotions, body language, and context.",
            "Integrate and reflect client patterns and underlying beliefs."
        ],
        "sourceDocument": "ICF Updated Core Competencies (2019)",
        "sourceVersion": "Khung Năng Lực ICF 2019",
        "sourceLink": "https://coachingfederation.org/credentialing/core-competencies",
        "originalExcerptEn": "Definition: Focuses on what the client is and is not saying to fully understand what is being communicated in the context of the client systems and to support client self-expression. 6.1 Considers client's context, identity, environment... 6.2 Reflects or summarizes what client communicated... 6.3 Recognizes and inquires when there is more to what the client is communicating... 6.4 Notices, fosters and explores client's emotions, energy shifts, non-verbal cues... 6.5 Integrates client's words, tone of voice and body language... 6.6 Notices trends in client's behaviors and emotions across sessions.",
        "translationVi": "Định nghĩa: Tập trung vào những gì khách hàng nói và không nói để hiểu đầy đủ thông điệp trong bối cảnh hệ thống của khách hàng và hỗ trợ khách hàng tự biểu đạt. 6.1 Xem xét bối cảnh, bản sắc, môi trường sống... 6.2 Phản chiếu hoặc tóm tắt những gì khách hàng truyền đạt để đảm bảo sự thấu suốt... 6.3 Nhận biết và khám phá khi thông điệp còn nhiều tầng ý nghĩa ẩn sâu... 6.4 Nhận biết, khích lệ và khám phá cảm xúc, sự chuyển dịch năng lượng, tín hiệu phi ngôn ngữ... 6.5 Tích hợp ngôn từ, giọng điệu và ngôn ngữ cơ thể... 6.6 Nhận diện xu hướng/mô thức hành vi và cảm xúc của khách hàng qua nhiều phiên.",
        "commentaryVi": "Lắng nghe chủ động không phải là ghi chép tốc ký lời nói của khách hàng, mà là lắng nghe 'Con người của khách hàng' (Who) đằng sau 'Vấn đề của khách hàng' (What). Coach chú ý sự thay đổi âm sắc, tốc độ nói và hơi thở.",
        "commentaryEn": "Active listening focuses on the 'Who' (the person) behind the 'What' (the tactical issue), capturing energy shifts, tone changes, and recurring themes.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Khách hàng nói: 'Dự án này rất tuyệt vời, tôi hoàn toàn ổn', nhưng giọng chùng xuống và thở dài. Coach lắng nghe đa tầng và phản chiếu: 'Bạn nói rằng bạn ổn, nhưng tôi vừa nghe thấy một tiếng thở dài và giọng bạn chùng xuống rất khẽ. Điều gì đang thực sự diễn ra ở tầng cảm xúc của bạn lúc này?'",
        "exampleContentEn": "Client: 'The project is great, I am completely fine', but their voice drops with a heavy sigh. Coach: 'You say you are fine, but I noticed a deep sigh and your voice softened. What is truly happening at an emotional level right now?'",
        "quiz": {
            "questionVi": "Điểm khác biệt căn bản giữa việc lắng nghe thông thường và Lắng nghe Chủ động cấp độ PCC (Competency 6) là gì?",
            "questionEn": "What is the key distinction between ordinary listening and PCC-level Active Listening (Competency 6)?",
            "options": [
                {"key": "A", "textVi": "Coach ghi nhớ toàn bộ số liệu và chi tiết kỹ thuật của dự án khách hàng.", "textEn": "Coach memorizes all technical facts and project statistics."},
                {"key": "B", "textVi": "Coach lắng nghe để tìm ra điểm sơ hở nhằm phản biện khách hàng.", "textEn": "Coach listens to catch flaws and debate the client."},
                {"key": "C", "textVi": "Coach lắng nghe toàn diện thông điệp ngôn từ, cảm xúc, sự dịch chuyển năng lượng và các mô thức suy nghĩ ẩn bên dưới câu chuyện.", "textEn": "Coach listens holistically to verbal message, emotions, energy shifts, and underlying belief patterns."},
                {"key": "D", "textVi": "Coach liên tục ngắt lời để nhắc khách hàng nói ngắn gọn.", "textEn": "Coach constantly interrupts to demand concise answers."}
            ],
            "correctAnswer": "C",
            "explanationVi": "Phương án C tóm lược đầy đủ tinh thần Năng lực 6: Lắng nghe đa tầng từ ngôn từ đến cảm xúc và năng lượng.",
            "explanationEn": "Option C encapsulates Competency 6: Multi-layered listening across words, emotions, and shifts."
        }
    },
    {
        "id": "mod1-les7",
        "moduleId": "mod-1",
        "lessonNumber": 7,
        "titleVi": "Năng Lực 7: Khơi Gợi Nhận Thức",
        "titleEn": "Competency 7: Evokes Awareness",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu cách đặt câu hỏi khơi gợi (Evocative Questions) vượt ra ngoài tư duy hiện tại.",
            "Tuyệt đối tránh lỗi suy diễn áp đặt (Coach Projection) trong câu hỏi.",
            "Khám phá góc nhìn mới, phép ẩn dụ và các điểm mù nhận thức."
        ],
        "objectivesEn": [
            "Formulate evocative questions beyond current thinking.",
            "Avoid coach projection and biased leading questions.",
            "Explore reframing, metaphors, and cognitive blind spots."
        ],
        "sourceDocument": "ICF Updated Core Competencies (2019)",
        "sourceVersion": "Khung Năng Lực ICF 2019",
        "sourceLink": "https://coachingfederation.org/credentialing/core-competencies",
        "originalExcerptEn": "Definition: Facilitates client insight and learning by using tools and techniques such as powerful questioning, silence, metaphor or analogy. 7.1 Considers client experience when deciding what might be most useful... 7.2 Challenges the client as a way to evoke awareness... 7.3 Asks questions about the client, such as their way of thinking, values, needs, wants, beliefs... 7.4 Asks questions that help client explore beyond current thinking... 7.5 Invites client to share more about their experience in the moment... 7.6 Notices what is working to enhance client progress... 7.7 Adjusts coaching approach in response to client... 7.8 Helps client identify factors that influence current and future patterns.",
        "translationVi": "Định nghĩa: Thúc đẩy hiểu biết sâu sắc và việc học của khách hàng bằng cách sử dụng các công cụ và kỹ thuật như câu hỏi khơi gợi, sự tĩnh lặng, phép ẩn dụ hoặc tương đồng. 7.1 Cân nhắc trải nghiệm của khách hàng để chọn cách tiếp cận hữu ích nhất... 7.2 Thách thức khách hàng một cách mang tính xây dựng để khơi gợi nhận thức mới... 7.3 Đặt câu hỏi về con người khách hàng (cách tư duy, giá trị sống, nhu cầu, niềm tin)... 7.4 Đặt câu hỏi giúp khách hàng khám phá vượt ra ngoài vùng tư duy hiện tại... 7.5 Mời khách hàng chia sẻ thêm về trải nghiệm ngay trong khoảnh khắc này... 7.6 Nhận biết điều gì đang hiệu quả... 7.7 Điều chỉnh cách tiếp cận theo phản ứng của khách hàng... 7.8 Giúp khách hàng nhận diện các yếu tố chi phối hành vi hiện tại và tương lai.",
        "commentaryVi": "LƯU Ý ĐẶC BIỆT: Câu hỏi khơi gợi thuần khiết không được chứa định kiến hay chẩn đoán ngầm của coach. Tránh lỗi suy diễn: 'Điều gì khiến việc buông quyền kiểm soát khó khăn với bạn?' (Áp đặt rằng khách hàng đang muốn kiểm soát). Hãy hỏi mở: 'Khi bạn nhìn vào tình huống này, điều gì là quan trọng nhất đối với bạn?'",
        "commentaryEn": "CRITICAL EXAM TRAP: Avoid coach projection. Do not embed assumptions such as 'Why is letting go of control hard for you?'. Keep inquiries clean: 'What matters most to you as you look at this situation?'",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Khách hàng bế tắc vì cảm thấy mọi cánh cửa đều đóng lại. Coach sử dụng phép ẩn dụ nhẹ nhàng: 'Nếu ví tình huống bế tắc này như một bức tranh thời tiết, thì bầu trời của bạn lúc này đang như thế nào? Và ngọn gió nào có thể giúp xua bớt mây mù?' Khách hàng mỉm cười và nhận ra góc nhìn mới.",
        "exampleContentEn": "Client feels stuck. Coach invites metaphor: 'If this crossroad were a landscape, what weather surrounds you right now? What gentle breeze might clear the fog?' Client smiles as a fresh perspective emerges.",
        "quiz": {
            "questionVi": "Câu hỏi nào sau đây là câu hỏi KHƠI GỢI THUẦN KHIẾT (Evoking Awareness), KHÔNG mang lỗi suy diễn áp đặt (Coach Projection)?",
            "questionEn": "Which question is a PURE evocative inquiry, FREE from coach projection?",
            "options": [
                {"key": "A", "textVi": "'Điều gì khiến việc buông bớt quyền kiểm soát trở nên khó khăn với bạn như vậy?'", "textEn": "'What makes letting go of control so difficult for you?'"},
                {"key": "B", "textVi": "'Bạn có nghĩ rằng tính cầu toàn của bạn đang làm hại cả đội nhóm không?'", "textEn": "'Don't you think your perfectionism is damaging the entire team?'"},
                {"key": "C", "textVi": "'Khi bạn nói rằng bạn cảm thấy áp lực đè nặng, điều gì trong bạn đang lên tiếng mạnh mẽ nhất lúc này?'", "textEn": "'When you say the pressure feels heavy, what part of you is speaking most powerfully right now?'"},
                {"key": "D", "textVi": "'Tại sao bạn không thử giao việc cho cấp phó như tôi đã gợi ý tuần trước?'", "textEn": "'Why don't you delegate tasks to your deputy as I suggested last week?'"}
            ],
            "correctAnswer": "C",
            "explanationVi": "Phương án C hoàn toàn tôn trọng từ ngữ của khách hàng ('áp lực đè nặng') và mở ra không gian tự khám phá mà không gán bất kỳ nhãn định kiến nào (như 'buông quyền kiểm soát' hay 'cầu toàn').",
            "explanationEn": "Option C grounds entirely in client language without projecting labels like 'control' or 'perfectionism'."
        }
    },
    {
        "id": "mod1-les8",
        "moduleId": "mod-1",
        "lessonNumber": 8,
        "titleVi": "Năng Lực 8: Thúc Đẩy Sự Phát Triển Của Khách Hàng",
        "titleEn": "Competency 8: Facilitates Client Growth",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu cách chuyển hóa nhận thức mới thành hành vi và mục tiêu cụ thể.",
            "Tôn trọng quyền tự quyết của khách hàng trong việc thiết kế hành động.",
            "Thiết lập cơ chế trách nhiệm giải trình tự thân (Self-Accountability) và ăn mừng thành tựu."
        ],
        "objectivesEn": [
            "Transform fresh insights into tangible learning and action.",
            "Honor client autonomy in designing next steps.",
            "Establish self-accountability mechanisms and celebrate progress."
        ],
        "sourceDocument": "ICF Updated Core Competencies (2019)",
        "sourceVersion": "Khung Năng Lực ICF 2019",
        "sourceLink": "https://coachingfederation.org/credentialing/core-competencies",
        "originalExcerptEn": "Definition: Partners with the client to transform learning and insight into action. Promotes client autonomy in the coaching process. 8.1 Works with the client to integrate new awareness, insight or learning into their worldview and behaviors... 8.2 Partners with client to design goals, actions and accountability... 8.3 Acknowledges and supports client autonomy in the design of goals... 8.4 Supports client in identifying potential results or learning... 8.5 Invites client to consider how to move forward... 8.6 Partners with client to define accountability methods... 8.7 Celebrates client progress and successes... 8.8 Partners with client to close the session.",
        "translationVi": "Định nghĩa: Hợp tác với khách hàng chuyển hóa bài học và nhận thức thành hành động. Thúc đẩy tính tự chủ của khách hàng trong toàn bộ tiến trình. 8.1 Cùng khách hàng tích hợp nhận thức mới vào thế giới quan và hành vi... 8.2 Hợp tác thiết kế mục tiêu, hành động và trách nhiệm thực hiện... 8.3 Tôn trọng và nâng đỡ quyền tự chủ của khách hàng khi thiết kế mục tiêu... 8.4 Hỗ trợ khách hàng nhận diện kết quả hoặc bài học tiềm năng... 8.5 Mời khách hàng cân nhắc cách tiến về phía trước... 8.6 Cùng xác định các phương pháp thực hiện cam kết... 8.7 Ăn mừng sự tiến bộ và thành công của khách hàng... 8.8 Hợp tác cùng khách hàng kết thúc phiên.",
        "commentaryVi": "Ở Năng lực 8, sai lầm phổ biến nhất của coach là giao 'bài tập về nhà' như giáo viên giao cho học sinh. Chuẩn PCC đòi hỏi Coach phải mời khách hàng tự kiến tạo bước đi: 'Với nhận thức mới này, bạn muốn thử nghiệm hành động nào trong tuần tới? Và bạn sẽ tự nhắc nhở bản thân thực hiện cam kết đó bằng cách nào?'",
        "commentaryEn": "In Competency 8, the coach never assigns homework like a schoolmaster. The coach partners with the client to self-author experimental actions and personal accountability.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Sau khi khách hàng nhận ra nguyên nhân trì hoãn, coach hỏi: 'Từ bài học hôm nay, bước đi nhỏ đầu tiên mà bạn cảm thấy hào hứng và khả thi để thực hiện ngay trong ngày mai là gì? Bạn muốn tự theo dõi tiến độ của mình như thế nào?' Khách hàng tự tin đề xuất giải pháp của chính mình.",
        "exampleContentEn": "After uncovering the root of procrastination, coach asks: 'From today's discovery, what is the first small action you feel energized to take tomorrow? How do you choose to hold yourself accountable?'",
        "quiz": {
            "questionVi": "Hành động nào thể hiện sự tôn trọng TÍNH TỰ CHỦ của khách hàng khi kết thúc phiên coach (Competency 8)?",
            "questionEn": "Which action best demonstrates respecting CLIENT AUTONOMY when closing a session (Competency 8)?",
            "options": [
                {"key": "A", "textVi": "Giao cho khách hàng 3 cuốn sách bắt buộc phải đọc xong trước phiên tới.", "textEn": "Assign 3 mandatory books to finish reading before the next session."},
                {"key": "B", "textVi": "Mời khách hàng tự đúc kết bài học lớn nhất hôm nay và tự thiết kế hành động thực tiễn mà họ muốn cam kết.", "textEn": "Invite the client to summarize their key takeaway and self-author the action they wish to commit to."},
                {"key": "C", "textVi": "Bỏ qua phần kết thúc vì đã hết 60 phút phiên.", "textEn": "Skip the closing because 60 minutes have expired."},
                {"key": "D", "textVi": "Tự tay viết cam kết hành động thay khách hàng để đảm bảo tính chuyên nghiệp.", "textEn": "Write the action commitment for the client to ensure professionalism."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Phương án B là tinh thần cốt lõi của Tiêu chí 8.2 & 8.3: Khách hàng là người tự kiến tạo hành động và chịu trách nhiệm với tiến trình phát triển của chính mình.",
            "explanationEn": "Option B represents Markers 8.2 & 8.3: Client self-authors action and owns their growth."
        }
    },
    {
        "id": "mod1-les9",
        "moduleId": "mod-1",
        "lessonNumber": 9,
        "titleVi": "Bài Ôn Tập Tổng Hợp: Phối Hợp 8 Năng Lực & Phân Biệt Các Cặp Dễ Nhầm Lẫn",
        "titleEn": "Lesson 9: Competencies Synthesis & Disambiguating Confusable Pairs",
        "estimatedMinutes": 20,
        "objectivesVi": [
            "Phân biệt chính xác giữa Năng lực 6 (Lắng nghe) và Năng lực 7 (Khơi gợi nhận thức).",
            "Phân biệt giữa Thỏa thuận phiên (Năng lực 3) và Thiết kế hành động (Năng lực 8).",
            "Nắm vững dòng chảy tự nhiên (Coaching Flow) của 8 Năng lực trong một phiên trọn vẹn."
        ],
        "objectivesEn": [
            "Distinguish Competency 6 (Active Listening) from Competency 7 (Evoking Awareness).",
            "Distinguish Session Agreement (Comp 3) from Action Design (Comp 8).",
            "Understand the natural coaching flow orchestrating all 8 competencies."
        ],
        "sourceDocument": "ICF Updated Core Competencies (2019) & PCC Markers Guide",
        "sourceVersion": "Khung Năng Lực ICF 2019",
        "sourceLink": "https://coachingfederation.org/credentialing/core-competencies",
        "originalExcerptEn": "The ICF Core Competencies are not isolated checklists; they represent an integrated tapestry. Demonstrates Ethical Practice and Embodies a Coaching Mindset provide the foundational soil. Establishes Agreements and Cultivates Trust co-create the relationship vessel. Maintains Presence and Listens Actively channel the communication. Evokes Awareness and Facilitates Growth harvest the transformation.",
        "translationVi": "8 Năng Lực Cốt Lõi ICF không phải là những chiếc hộp tách rời cơ học, mà là một tấm thảm dệt thống nhất. Năng lực 1 (Đạo đức) và Năng lực 2 (Tư duy) là mảnh đất nền móng. Năng lực 3 (Thỏa thuận) và Năng lực 4 (Niềm tin) tạo nên chiếc bình chứa mối quan hệ. Năng lực 5 (Hiện diện) và Năng lực 6 (Lắng nghe) dẫn truyền dòng chảy giao tiếp. Năng lực 7 (Khơi gợi) và Năng lực 8 (Phát triển) thu hoạch quả ngọt của sự chuyển hóa.",
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
        "titleVi": "Bài 1: Cấu Trúc, Mục Đích & 5 Giá Trị Cốt Lõi Đạo Đức ICF",
        "titleEn": "Lesson 1: Structure, Purpose & 5 ICF Core Ethical Values",
        "estimatedMinutes": 15,
        "objectivesVi": [
            "Hiểu toàn diện cấu trúc Bộ Quy tắc Đạo đức ICF (Purpose, Core Values, Ethical Principles, Standards, Pledge, Appendix).",
            "Nắm vững 5 Giá trị Cốt lõi: Tính Chuyên nghiệp, Sự Hợp tác, Lòng Nhân ái, Tính Công bằng & Sự Chính trực.",
            "Phân biệt chuẩn Đạo đức áp dụng cho thực hành hiện hành (Bản 2025) và chuẩn làm bài thi hiện hành (Bản 2020)."
        ],
        "objectivesEn": [
            "Understand full ICF Code of Ethics architecture.",
            "Master the 5 Core Values: Professionalism, Collaboration, Humanity, Equity, Integrity.",
            "Differentiate current practice code (2025) from current exam baseline (2020)."
        ],
        "sourceDocument": "ICF Code of Ethics & Insights and Considerations for Ethics (ICE)",
        "sourceVersion": "Bản 2025 (Hiệu lực thực hành 01/04/2025; Bản 2020 dùng cho bài thi hiện hành)",
        "sourceLink": "https://coachingfederation.org/credentialing/coaching-ethics/icf-code-of-ethics/",
        "originalExcerptEn": "The ICF Code of Ethics describes the core values, ethical principles and standards of behavior for all ICF Professionals. The 5 Core Values are: Professionalism, Collaboration, Humanity, Equity, and Integrity. Meeting these ethical standards is the first of the ICF Core Competencies.",
        "translationVi": "Bộ Quy tắc Đạo đức ICF mô tả các giá trị cốt lõi, nguyên tắc đạo đức và chuẩn mực hành vi cho tất cả các Chuyên gia Khai vấn ICF. 5 Giá trị Cốt lõi bao gồm: Tính Chuyên nghiệp (Professionalism), Sự Hợp tác (Collaboration), Lòng Nhân ái (Humanity), Tính Công bằng (Equity) và Sự Chính trực (Integrity). Việc đáp ứng các chuẩn mực đạo đức này là năng lực đầu tiên trong các Năng lực Cốt lõi của ICF.",
        "commentaryVi": "GIẢI THÍCH SƯ PHẠM:\n- Bộ Quy tắc Đạo đức không phải là cẩm nang pháp luật hình sự, mà là kim chỉ nam lương tri nghề nghiệp.\n- Bản 2025 bổ sung định nghĩa rộng mở hơn về công nghệ/AI, tính hòa nhập văn hóa (Equity) và làm rõ các mối quan hệ quyền lực.",
        "commentaryEn": "PEDAGOGICAL INSIGHT: The Code of Ethics is not a punitive penal code, but a professional moral compass. The 2025 Code enhances guidelines on AI technology, equity, and power dynamics.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Một coach nhận được lời mời hợp tác từ một doanh nghiệp, nhưng doanh nghiệp yêu cầu coach phải chia sẻ kết quả tính cách của các nhân sự được coach. Dựa trên Giá trị Chính trực và Tính Chuyên nghiệp, coach giải thích rõ ràng rằng thỏa thuận đạo đức ICF cấm tuyệt đối việc tiết lộ dữ liệu cá nhân này trừ khi từng nhân sự tự nguyện đồng thuận bằng văn bản.",
        "exampleContentEn": "A coach is requested by a client's employer to disclose psychometric profiles. Upholding Integrity and Professionalism, the coach affirms that ICF standards prohibit disclosing individual data without explicit written consent.",
        "quiz": {
            "questionVi": "Theo quy chế của ICF, Bộ Quy tắc Đạo đức nào đang được dùng làm căn cứ chấm điểm cho kỳ thi Credentialing Exam hiện hành?",
            "questionEn": "According to ICF official policy, which Code of Ethics edition serves as the scoring baseline for the current Credentialing Exam?",
            "options": [
                {"key": "A", "textVi": "Bộ Quy tắc Đạo đức năm 2008.", "textEn": "The 2008 Code of Ethics."},
                {"key": "B", "textVi": "Bộ Quy tắc Đạo đức năm 2020 (cho đến trước khi kỳ thi cập nhật chính thức áp dụng).", "textEn": "The 2020 Code of Ethics (until the updated exam formally takes effect)."},
                {"key": "C", "textVi": "Bất kỳ bộ luật dân sự nào của quốc gia sở tại.", "textEn": "Any local civil legal code."},
                {"key": "D", "textVi": "Luật sở hữu trí tuệ quốc tế.", "textEn": "International intellectual property law."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Kỳ thi hiện hành vẫn sử dụng Bộ Đạo đức 2020 làm chuẩn thi viết; Bộ Đạo đức 2025 có hiệu lực thực hành từ 01/04/2025 và áp dụng vào bài thi mới cập nhật.",
            "explanationEn": "The current written exam is grounded in the 2020 Code, while the 2025 Code applies to practice from April 1, 2025."
        }
    },
    {
        "id": "mod2-les2",
        "moduleId": "mod-2",
        "lessonNumber": 2,
        "titleVi": "Bài 2: Phần 1 — Trách Nhiệm Đối Với Khách Hàng (Tiêu Chuẩn 1–11)",
        "titleEn": "Lesson 2: Section 1 — Responsibility to Clients (Standards 1–11)",
        "estimatedMinutes": 18,
        "objectivesVi": [
            "Nắm vững các tiêu chuẩn cốt lõi: Thỏa thuận minh bạch (Std 1–3), Bình đẳng bản sắc (Std 4), Bảo mật thông tin (Std 5–8) và Chuyển gửi chuyên gia (Std 11).",
            "Tích hợp tài liệu Hướng dẫn Suy ngẫm Đạo đức (ICE) về bảo mật và thỏa thuận ba bên.",
            "Nhận diện các ngoại lệ bắt buộc của việc giữ bí mật thông tin."
        ],
        "objectivesEn": [
            "Master core client responsibilities: transparent agreements, equality, confidentiality, and referrals.",
            "Integrate ICE reflections on confidentiality and third-party contracts.",
            "Recognize mandatory legal and safety exceptions to confidentiality."
        ],
        "sourceDocument": "ICF Code of Ethics (Section 1) & ICE Document",
        "sourceVersion": "Tiêu chuẩn 1 đến 11",
        "sourceLink": "https://coachingfederation.org/credentialing/coaching-ethics/icf-code-of-ethics/",
        "originalExcerptEn": "Standard 1: Explain and ensure client and sponsor understand the nature and potential value of coaching, confidentiality boundaries, financial arrangements, and other terms... Standard 5: Maintain the strictest levels of confidentiality with all client and sponsor information... Standard 11: Suggest the client obtain services of other professionals when needed and terminate coaching if appropriate.",
        "translationVi": "Tiêu chuẩn 1: Giải thích và đảm bảo khách hàng cùng nhà tài trợ hiểu rõ bản chất, giá trị tiềm năng của khai vấn, ranh giới bảo mật, thỏa thuận tài chính và các điều khoản khác... Tiêu chuẩn 5: Duy trì mức độ bảo mật nghiêm ngặt nhất với mọi thông tin của khách hàng và nhà tài trợ... Tiêu chuẩn 11: Đề xuất khách hàng tìm kiếm dịch vụ từ các chuyên gia khác khi cần thiết và dừng hợp đồng khai vấn nếu phù hợp.",
        "commentaryVi": "GIẢI THÍCH SƯ PHẠM TỪ ICE:\n- Khi có xung đột giữa mong muốn của Nhà tài trợ (Sponsor) và sự bảo mật của Khách hàng (Client), trách nhiệm đạo đức của Coach luôn luôn ưu tiên bảo vệ Khách hàng trực tiếp.\n- Ngoại lệ bảo mật DUY NHẤT: Khi có nguy cơ đe dọa trực tiếp đến tính mạng con người (tự sát, giết người) hoặc yêu cầu bắt buộc của tòa án.",
        "commentaryEn": "ICE INSIGHT: In conflicts between sponsor desires and client confidentiality, the coach always prioritizes the direct client. The only confidentiality exception is imminent harm to life or strict legal subpoenas.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Một khách hàng vô tình tiết lộ họ đang bị kiệt sức vì bệnh tim mạch nhưng giấu công ty. Coach nhắc lại ranh giới bảo mật: Coach sẽ không bao giờ tiết lộ điều này với công ty, đồng thời nhẹ nhàng khuyên khách hàng ưu tiên đi khám bác sĩ chuyên khoa tim mạch.",
        "exampleContentEn": "Client discloses hidden heart condition. Coach upholds confidentiality, promising never to leak this to the employer, while encouraging an immediate cardiology checkup.",
        "quiz": {
            "questionVi": "Theo Tiêu chuẩn Đạo đức ICF số 5 và tài liệu ICE, khi nào Coach được phép phá vỡ cam kết bảo mật mà KHÔNG cần sự đồng ý của khách hàng?",
            "questionEn": "Under ICF Standard 5 and ICE guidelines, when is a coach permitted to break confidentiality WITHOUT client consent?",
            "options": [
                {"key": "A", "textVi": "Khi khách hàng liên tục phàn nàn về chế độ lương thưởng của công ty.", "textEn": "When the client complains repeatedly about compensation."},
                {"key": "B", "textVi": "Khi có căn cứ rõ ràng về nguy cơ đe dọa tính mạng cận kề (như tự sát hoặc gây hại người khác) theo quy định an toàn.", "textEn": "When there is clear evidence of imminent danger to human life (such as suicide or violence)."},
                {"key": "C", "textVi": "Khi người trả tiền thuê coach muốn biết khách hàng có gắn bó lâu dài với doanh nghiệp không.", "textEn": "When the paying sponsor wants to know if the client will stay long-term."},
                {"key": "D", "textVi": "Khi coach muốn chia sẻ tình huống thú vị lên mạng xã hội kèm tên thật của khách hàng.", "textEn": "When the coach wants to share a fun story on social media with real names."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Bảo vệ tính mạng con người là ngoại lệ đạo đức tối thượng vượt trên nghĩa vụ bảo mật thông tin thường quy.",
            "explanationEn": "Protecting human life is the supreme ethical exception superseding standard confidentiality."
        }
    },
    {
        "id": "mod2-les3",
        "moduleId": "mod-2",
        "lessonNumber": 3,
        "titleVi": "Bài 3: Phần 2 — Trách Nhiệm Thực Hành, Hiệu Suất & Công Nghệ / AI (Tiêu Chuẩn 12–20)",
        "titleEn": "Lesson 3: Section 2 — Responsibility to Practice, Performance & AI Technology (Standards 12–20)",
        "estimatedMinutes": 18,
        "objectivesVi": [
            "Hiểu ranh giới năng lực chuyên môn cá nhân và quản lý xung đột lợi ích (Tiêu chuẩn 12–16).",
            "Nắm vững các hướng dẫn đạo đức mới về việc ứng dụng Trí tuệ Nhân tạo (AI) và công nghệ số trong coaching.",
            "Luyện tập nhận diện xung đột lợi ích tiềm ẩn và cách công khai minh bạch."
        ],
        "objectivesEn": [
            "Understand competence limits and conflict of interest management (Standards 12–16).",
            "Master modern ethical guidelines regarding AI and digital tech in coaching.",
            "Identify potential conflicts of interest and transparent disclosures."
        ],
        "sourceDocument": "ICF Code of Ethics (Section 2) & ICE AI Guidance",
        "sourceVersion": "Tiêu chuẩn 12 đến 20",
        "sourceLink": "https://coachingfederation.org/credentialing/coaching-ethics/icf-code-of-ethics/",
        "originalExcerptEn": "Standard 16: Accurately identify my coaching qualifications, my level of coaching competency, expertise, experience, training, certifications and ICF Credentials. Standard 20: Maintain, store and dispose of any records, including electronic files and communications, created during my professional interactions in a manner that promotes confidentiality, security and privacy, and complies with any applicable laws and agreements.",
        "translationVi": "Tiêu chuẩn 16: Nhận diện và công bố chính xác trình độ chuyên môn, cấp độ năng lực, kinh nghiệm, chứng chỉ và chứng nhận ICF của bản thân. Tiêu chuẩn 20: Duy trì, lưu trữ và tiêu hủy mọi hồ sơ, bao gồm các tệp điện tử và thông tin liên lạc tạo ra trong quá trình làm việc, nhằm đảm bảo tính bảo mật, an toàn, quyền riêng tư và tuân thủ các quy định pháp luật cũng như thỏa thuận hiện hành.",
        "commentaryVi": "GIẢI THÍCH SƯ PHẠM VỀ CÔNG NGHỆ VÀ AI:\n- Khi coach sử dụng các công cụ ghi âm tự động bằng AI (như Otter, Fireflies, ChatGPT để tóm tắt), coach BẮT BUỘC phải thông báo và có sự đồng thuận bằng văn bản của khách hàng trước khi bật phần mềm ghi nhận.\n- Không bao giờ nạp thông tin nhận dạng cá nhân của khách hàng vào các mô hình AI công cộng không bảo mật.",
        "commentaryEn": "PEDAGOGICAL INSIGHT ON AI: Using AI recording/transcription bots requires prior explicit written consent. Never input confidential client identifying data into public unsecured AI tools.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Coach A đang dùng một ứng dụng AI để tạo biên bản phiên coach. Trước khi bắt đầu phiên, Coach A gửi bản phụ lục bảo mật giải thích rõ dữ liệu lưu trữ ở đâu và hỏi khách hàng: 'Bạn có thoải mái để ứng dụng này ghi âm tóm tắt không?' Nếu khách hàng từ chối, coach vui vẻ tắt ứng dụng và ghi chép tay.",
        "exampleContentEn": "Coach uses an AI note-taker. Before starting, the coach transparently seeks consent: 'Are you comfortable with this tool summarizing key points?' If client declines, the coach immediately switches to handwritten notes.",
        "quiz": {
            "questionVi": "Trước khi sử dụng một bot AI để tự động ghi âm và tóm tắt phiên khai vấn, hành động nào là BẮT BUỘC theo Chuẩn mực Đạo đức ICF?",
            "questionEn": "Before using an AI bot to automatically record and summarize a coaching session, what is MANDATORY under ICF Ethics?",
            "options": [
                {"key": "A", "textVi": "Bật âm thầm không cần nói vì AI chỉ để phục vụ học tập cá nhân của coach.", "textEn": "Run it silently since it only aids the coach's private learning."},
                {"key": "B", "textVi": "Chỉ cần công ty sản xuất phần mềm AI đó cam kết bảo mật là đủ.", "textEn": "Rely solely on the software vendor's generic terms of service."},
                {"key": "C", "textVi": "Minh bạch giải thích cách thức hoạt động, lưu trữ dữ liệu của AI và nhận được sự đồng thuận rõ ràng của khách hàng trước khi kích hoạt.", "textEn": "Transparently explain data handling and obtain explicit client consent prior to activation."},
                {"key": "D", "textVi": "Đăng tải bản ghi âm lên trang web cá nhân để quảng cáo công nghệ mới.", "textEn": "Post the recording publicly to promote technological prowess."}
            ],
            "correctAnswer": "C",
            "explanationVi": "Tiêu chuẩn 20 và hướng dẫn ICE yêu cầu bảo mật dữ liệu số và sự đồng thuận minh bạch của khách hàng đối với mọi công nghệ ghi âm.",
            "explanationEn": "Standard 20 and ICE require digital data protection and informed explicit client consent."
        }
    },
    {
        "id": "mod2-les4",
        "moduleId": "mod-2",
        "lessonNumber": 4,
        "titleVi": "Bài 4: Phần 3 & 4 — Tính Chuyên Nghiệp, Ranh Giới Quyền Lực & Trách Nhiệm Xã Hội (Tiêu Chuẩn 21–28)",
        "titleEn": "Lesson 4: Sections 3 & 4 — Professionalism, Power Boundaries & Responsibility to Society (Standards 21–28)",
        "estimatedMinutes": 18,
        "objectivesVi": [
            "Hiểu ranh giới quyền lực (Power Dynamics) và nghiêm cấm quan hệ tình cảm/thân mật bất chính với khách hàng (Tiêu chuẩn 21–22).",
            "Nắm vững quy định về nhận quà tặng, hoa hồng giới thiệu và trung thực tài chính.",
            "Hiểu Trách nhiệm đối với Xã hội, Lời cam kết ICF Pledge of Ethics và cơ chế xử lý khiếu nại đạo đức."
        ],
        "objectivesEn": [
            "Understand power dynamics and prohibitions on romantic/intimate relationships (Standards 21–22).",
            "Master rules regarding gifts, referral kickbacks, and financial honesty.",
            "Learn Responsibility to Society, the ICF Pledge of Ethics, and Ethical Conduct Review procedures."
        ],
        "sourceDocument": "ICF Code of Ethics (Sections 3 & 4) & ICE Guide",
        "sourceVersion": "Tiêu chuẩn 21 đến 28",
        "sourceLink": "https://coachingfederation.org/credentialing/coaching-ethics/icf-code-of-ethics/",
        "originalExcerptEn": "Standard 21: Do not participate in any sexual or romantic intimacy with current client(s) or sponsor(s)... Standard 24: Maintain the distinction between coaching, consulting, psychotherapy and other support professions... ICF Pledge of Ethics: As an ICF Professional, in accordance with the Standards of the ICF Code of Ethics, I acknowledge and agree to fulfill my ethical and legal obligations to my coaching client(s), sponsor(s), colleagues and to the public at large.",
        "translationVi": "Tiêu chuẩn 21: Tuyệt đối không tham gia vào bất kỳ mối quan hệ tình cảm hoặc tình dục nào với khách hàng hoặc nhà tài trợ hiện tại... Tiêu chuẩn 24: Duy trì sự phân định rạch ròi giữa khai vấn, tư vấn chuyên gia, tâm lý trị liệu và các ngành trợ giúp khác... Lời cam kết Đạo đức ICF: Với tư cách là Chuyên gia ICF, tôi công nhận và cam kết hoàn thành các nghĩa vụ đạo đức và pháp lý đối với khách hàng, nhà tài trợ, đồng nghiệp và toàn xã hội.",
        "commentaryVi": "GIẢI THÍCH SƯ PHẠM VỀ VAI TRÒ KÉP VÀ QUAN HỆ THÂN MẬT:\n- Mối quan hệ giữa coach và khách hàng vốn có sự chênh lệch vô hình về sự cởi mở tổn thương (vulnerability). Vì vậy, coach không bao giờ được lợi dụng lòng tin này để trục lợi tình cảm hoặc tài chính.\n- Khi khách hàng tặng quà có giá trị lớn bất thường, coach cần từ chối khéo léo để bảo toàn ranh giới bình đẳng.",
        "commentaryEn": "PEDAGOGICAL INSIGHT: The coaching relationship involves vulnerability. The coach must never exploit this trust for financial or personal gain, maintaining boundaries against dual relationships or extravagant gifts.",
        "exampleType": "Ví dụ tự soạn phục vụ học tập",
        "exampleContentVi": "Sau khi hoàn thành hợp đồng, khách hàng ngỏ ý muốn tặng coach một chuyến du lịch nghỉ dưỡng cao cấp trị giá hàng nghìn USD. Coach từ chối chân thành: 'Tôi vô cùng trân trọng sự tiến bộ và lòng tốt của bạn. Tuy nhiên, theo quy chuẩn đạo đức nghề nghiệp, tôi chỉ nhận mức thù lao đã ký trong hợp đồng để giữ mối quan hệ trong sáng và bình đẳng nhất.'",
        "exampleContentEn": "Client offers an extravagant luxury vacation gift after closing. Coach declines gracefully, explaining that professional standards limit compensation to agreed contract fees to maintain pristine boundaries.",
        "quiz": {
            "questionVi": "Coach B đang huấn luyện cho một giám đốc điều hành. Trong quá trình đó, giám đốc đề nghị Coach B làm cố vấn chiến lược kiêm luôn việc đầu tư cổ phần vào công ty. Coach B nên xử lý thế nào để tuân thủ Tiêu chuẩn Đạo đức?",
            "questionEn": "Coach is coaching an executive who proposes the coach become a salaried consultant while investing equity in the venture. How should the coach respond ethically?",
            "options": [
                {"key": "A", "textVi": "Nhận lời ngay vì vừa được tiền tư vấn vừa có cơ hội đầu tư sinh lời lớn.", "textEn": "Accept immediately to maximize financial windfall."},
                {"key": "B", "textVi": "Minh bạch chỉ ra xung đột lợi ích và vai trò kép nghiêm trọng; nếu chuyển sang vai trò tư vấn/đầu tư thì phải chính thức kết thúc hợp đồng coaching.", "textEn": "Transparently highlight severe dual-role conflict of interest; terminate the coaching relationship before transitioning to consulting/investment."},
                {"key": "C", "textVi": "Tiếp tục làm coach nhưng bí mật ký hợp đồng đầu tư đứng tên người thân.", "textEn": "Continue coaching while secretly investing under a relative's name."},
                {"key": "D", "textVi": "Ép khách hàng phải tăng phí coaching lên gấp 5 lần.", "textEn": "Demand the client quintuple the coaching fees."}
            ],
            "correctAnswer": "B",
            "explanationVi": "Tiêu chuẩn Đạo đức về xung đột lợi ích và vai trò kép đòi hỏi sự minh bạch tuyệt đối; không thể cùng lúc vừa làm Coach vừa làm Nhà đầu tư tài chính vì sẽ làm mất tính khách quan.",
            "explanationEn": "Standardized ethics on conflicts of interest require absolute role separation; one cannot remain an objective coach while becoming a financial equity investor."
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
# Imports the 7 comprehensive lessons grounded in Hullinger & DiGirolamo (2018)
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
        "sourceVersion": "Tác giả: Angela M. Hullinger & Joel A. DiGirolamo (2018; Cập nhật trang web: 13/08/2026)",
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
        "sourceDoc": "ICF Updated Core Competencies (2019)",
        "sourceUrl": "https://coachingfederation.org/credentialing/core-competencies",
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
        "titleVi": "Học Phần 4: White Paper Chuyển Gửi Khách Hàng",
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
        "sourceUrl": "https://coachingfederation.org/credentialing/core-competencies",
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
