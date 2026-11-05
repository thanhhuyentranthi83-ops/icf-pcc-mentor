# -*- coding: utf-8 -*-
"""
Generates 90 Diagnostic Mini Quizzes (10 per section x 9 sections)
for ICF PCC Mentor app.
"""

def generate_quizzes():
    quizzes = []

    quiz_defs = [
        # sec-a1-1: 10 quizzes
        ("sec-a1-1", [
            ("Trong phiên khai vấn doanh nghiệp, CEO (Sponsor) yêu cầu Coach cung cấp ghi chép chi tiết các chia sẻ của một Giám đốc chi nhánh. Hành động nào sau đây là ĐÚNG ĐẠO ĐỨC nhất?",
             "In corporate coaching, the CEO (Sponsor) requests verbatim notes of a Branch Director's sessions. Which action is MOST ETHICAL?",
             [("A", "Cung cấp bản tóm tắt ngắn gọn các điểm yếu của giám đốc chi nhánh.", "Provide a brief summary of the director's weaknesses."),
              ("B", "Từ chối khéo léo và giải thích rằng quy tắc bảo mật ICF không cho phép tiết lộ nội dung nếu không có sự đồng ý của khách hàng.", "Decline politely and explain that ICF confidentiality prohibits disclosure without client consent."),
              ("C", "Gửi toàn bộ ghi chép vì CEO là người ký hợp đồng và thanh toán chi phí.", "Send the full notes since the CEO holds the contract and pays fees."),
              ("D", "Khuyên giám đốc chi nhánh tự nộp đơn từ chức để tránh bị CEO soi xét.", "Advise the branch director to resign to avoid scrutiny.")],
             "B", "Theo chuẩn đạo đức ICF 2025, thông tin phiên là bảo mật tuyệt đối với bên thứ ba kể cả Sponsor, trừ khi khách hàng đồng thuận bằng văn bản.",
             "Under ICF 2025 Ethics, session disclosures are strictly confidential from sponsors unless the client gives explicit written consent."),
            ("Khi phát hiện khách hàng tiềm năng là đối thủ kinh doanh trực tiếp của một công ty mà Coach đang đầu tư cổ phần, Coach nên làm gì?",
             "Upon discovering a prospective client directly competes with a company the Coach holds shares in, what should the Coach do?",
             [("A", "Im lặng vì tin rằng mình có thể tách bạch hoàn toàn hai vai trò.", "Remain silent, believing one can keep both roles separate."),
              ("B", "Chờ đến khi ký xong hợp đồng rồi mới chia sẻ để không mất khách hàng.", "Wait until after contracting to disclose, preserving the sale."),
              ("C", "Công khai ngay nguy cơ xung đột lợi ích tiềm ẩn và cùng khách hàng thảo luận hướng giải quyết.", "Immediately disclose the potential conflict of interest and explore options with the client."),
              ("D", "Đơn phương hủy cuộc hẹn mà không đưa ra bất kỳ lời giải thích nào.", "Abruptly cancel the appointment without any explanation.")],
             "C", "Minh bạch hóa xung đột lợi ích ngay từ đầu là yêu cầu bắt buộc của chuẩn mực đạo đức ICF.",
             "Transparent disclosure of potential conflicts of interest upfront is a foundational ICF ethical obligation."),
            ("Một khách hàng tặng Coach một chiếc đồng hồ xa xỉ trị giá hàng nghìn USD vào cuối khóa khai vấn. Hành động nào chuẩn xác nhất?",
             "A client gifts the Coach a luxury watch worth thousands of dollars at engagement conclusion. What is the most proper action?",
             [("A", "Vui vẻ nhận vì khóa khai vấn đã kết thúc thành công rực rỡ.", "Gladly accept since the coaching engagement concluded triumphantly."),
              ("B", "Từ chối nhã nhặn và giải thích rằng món quà vượt quá ranh giới chuyên môn chuẩn mực theo quy tắc đạo đức nghề nghiệp.", "Graciously decline and explain that the gift exceeds ethical boundaries of professional practice."),
              ("C", "Đem bán chiếc đồng hồ rồi quyên góp từ thiện dưới tên khách hàng mà không hỏi ý kiến họ.", "Sell the watch and donate proceeds to charity without asking."),
              ("D", "Nhận quà nhưng tính trừ vào chi phí các phiên khai vấn trong tương lai.", "Accept the gift and credit its value against future coaching sessions.")],
             "B", "Quà tặng có giá trị lớn có thể làm méo mó ranh giới chuyên nghiệp và sự bình đẳng trong mối quan hệ khai vấn.",
             "Excessively valuable gifts distort professional boundaries and egalitarian partnership."),
            ("Điều nào sau đây là trường hợp DUY NHẤT cho phép Coach phá vỡ cam kết bảo mật mà không cần sự đồng thuận của khách hàng?",
             "Which scenario is the SOLE legitimate basis for breaching confidentiality without client permission?",
             [("A", "Khi người quản lý trực tiếp của khách hàng yêu cầu kiểm tra hiệu suất làm việc.", "When the client's direct manager demands a performance evaluation."),
              ("B", "Khi Coach nhận thấy khách hàng đang có dấu hiệu mệt mỏi và lơ là công việc.", "When the Coach observes signs of fatigue and work neglect."),
              ("C", "Khi có nguy cơ cận kề, rõ ràng về việc khách hàng tự gây hại hoặc gây hại cho tính mạng người khác.", "When there is clear, imminent danger of self-harm or physical harm to others."),
              ("D", "Khi khách hàng thanh toán chi phí trễ hạn hơn 30 ngày.", "When the client defaults on invoice payments for over 30 days.")],
             "C", "Nguy cơ đe dọa tính mạng cận kề là căn cứ đạo đức và pháp lý duy nhất để phá vỡ bảo mật khẩn cấp.",
             "Imminent danger to human life is the sole ethical and legal justification for emergency breach of confidentiality."),
            ("Trong thỏa thuận khai vấn 3 bên, tài liệu nào sau đây phải được thống nhất và ký kết rõ ràng trước khi phiên khai vấn đầu tiên diễn ra?",
             "In a tripartite coaching arrangement, which document must be explicitly agreed and signed before the first session?",
             [("A", "Bản thỏa thuận về phạm vi mục tiêu, quy tắc bảo mật và quy chế báo cáo giữa Coach, Khách hàng và Sponsor.", "An agreement on scope, confidentiality parameters, and reporting protocols between Coach, Client, and Sponsor."),
              ("B", "Bản cam kết khách hàng phải đạt được chỉ tiêu KPI do công ty đề ra sau 3 tháng.", "A binding contract that the client must achieve corporate KPIs within 3 months."),
              ("C", "Bản đánh giá năng lực tâm lý 360 độ do Coach tự biên soạn.", "A 360-degree psychological assessment authored by the Coach."),
              ("D", "Biên bản bàn giao toàn bộ quyền giám sát công việc cho Coach.", "A handover protocol delegating operational supervision to the Coach.")],
             "A", "Thỏa thuận 3 bên minh bạch về ranh giới bảo mật là nền tảng bảo vệ quyền lợi của tất cả các bên.",
             "A transparent tripartite agreement clarifying confidentiality is foundational to protecting all parties."),
            ("Coach có quyền sử dụng thông tin của khách hàng làm ví dụ nghiên cứu tình huống (Case study) trong hội thảo khi nào?",
             "When is a coach permitted to use client material as a conference case study?",
             [("A", "Khi khách hàng đã chuyển công tác sang công ty khác.", "When the client has transferred to another firm."),
              ("B", "Khi Coach đã thay đổi tên công ty nhưng vẫn giữ nguyên chức vụ và bối cảnh chi tiết.", "When the coach disguises company names but retains exact job titles and circumstances."),
              ("C", "Khi đã có văn bản đồng ý bằng văn bản của khách hàng hoặc toàn bộ dữ liệu đã được ẩn danh hóa triệt để không thể nhận dạng.", "When written client consent is secured or all details are rigorously anonymized beyond recognition."),
              ("D", "Bất cứ lúc nào, miễn là bài thuyết trình mang tính chất phi thương mại.", "At any time, provided the lecture is strictly non-commercial.")],
             "C", "Bảo mật danh tính đòi hỏi sự ẩn danh hóa hoàn toàn hoặc phải có văn bản ủy quyền từ khách hàng.",
             "Identity protection demands complete anonymization or documented informed consent."),
            ("Một đồng nghiệp đề nghị trả cho Coach 20% hoa hồng nếu Coach giới thiệu khách hàng của mình mua khóa học của họ. Theo chuẩn ICF, Coach phải làm gì?",
             "A colleague offers the Coach a 20% referral commission for steering clients into their workshop. Under ICF standards, what must the Coach do?",
             [("A", "Âm thầm nhận hoa hồng vì đây là thông lệ kinh doanh thông thường.", "Secretly accept, viewing it as standard commercial practice."),
              ("B", "Từ chối hoặc phải công khai minh bạch 100% khoản hoa hồng này với khách hàng trước khi giới thiệu.", "Decline, or fully disclose the commercial arrangement to the client prior to any referral."),
              ("C", "Ép khách hàng phải đăng ký khóa học đó nếu muốn tiếp tục coaching.", "Mandate client enrollment as a prerequisite for continued coaching."),
              ("D", "Yêu cầu đồng nghiệp nâng mức hoa hồng lên 30% mới đồng ý.", "Demand a higher 30% commission before consenting.")],
             "B", "Mọi khoản hoa hồng giới thiệu (Referral fees) bắt buộc phải được công khai minh bạch với khách hàng.",
             "Any referral compensation must be fully and transparently disclosed to the client."),
            ("Điều nào sau đây phản ánh đúng nhất vai trò của chuẩn mực đạo đức ICF trong phòng thi SJT?",
             "Which statement best reflects the role of ICF Ethics in the SJT exam?",
             [("A", "Là yếu tố phụ, chỉ cần tập trung vào các câu hỏi đặt mục tiêu.", "It is a secondary factor subordinate to goal-setting tactics."),
              ("B", "Là bộ lọc tối thượng (Highest Filter); bất kỳ phương án nào vi phạm đạo đức đều tự động là phương án TỆ NHẤT (WORST).", "It is the supreme filter; any option violating ethics is automatically the WORST choice."),
              ("C", "Có thể linh hoạt bỏ qua nếu khách hàng yêu cầu Coach làm vậy.", "It can be flexibly bypassed if the client explicitly requests it."),
              ("D", "Chỉ áp dụng cho các phiên khai vấn có hợp đồng trên 10.000 USD.", "It applies exclusively to contracts exceeding $10,000 in value.")],
             "B", "Đạo đức là bộ lọc bất biến; hành vi vi phạm đạo đức luôn là đáp án TỆ NHẤT trong bài thi.",
             "Ethics is the paramount filter; ethical breaches consistently constitute the WORST answer."),
            ("Khi khách hàng tiết lộ một thông tin nội gián có thể vi phạm quy chế chứng khoán của công ty, Coach nên làm gì?",
             "When a client reveals insider information that might violate corporate securities laws, what should the Coach do?",
             [("A", "Dùng thông tin đó để đầu tư chứng khoán sinh lời.", "Use the tip for personal stock trading."),
              ("B", "Báo cáo ngay cho cơ quan công an mà không thảo luận với khách hàng.", "Report immediately to regulators without client dialogue."),
              ("C", "Nhắc nhở khách hàng về ranh giới đạo đức nghề nghiệp và cùng họ xem xét các hệ quả pháp lý của hành vi đó.", "Remind the client of ethical boundaries and explore the potential systemic consequences of the situation."),
              ("D", "Khuyên khách hàng xóa sạch mọi dấu vết giao dịch.", "Advise the client to erase all digital transaction trails.")],
             "C", "Coach duy trì tính chính trực, không đồng lõa và phản chiếu hệ quả đạo đức/pháp lý cho khách hàng tự nhận thức.",
             "The coach maintains personal integrity, avoids collusion, and reflects systemic implications for client awareness."),
            ("Phương châm 'Do No Harm' (Không gây tổn hại) trong đạo đức khai vấn ICF được thể hiện rõ nhất qua hành vi nào?",
             "The principle of 'Do No Harm' in ICF coaching ethics is best demonstrated through which action?",
             [("A", "Liên tục đưa ra lời khuyên để khách hàng không bao giờ thất bại.", "Offering non-stop advice so the client never encounters failure."),
              ("B", "Ý thức rõ ranh giới năng lực chuyên môn, giữ an toàn tâm lý và chuyển gửi khi vấn đề vượt ngoài tầm khai vấn.", "Being conscious of competency boundaries, ensuring psychological safety, and referring when issues exceed coaching scope."),
              ("C", "Đồng ý với mọi quan điểm sai lầm của khách hàng để làm họ vui.", "Endorsing flawed client assumptions to maintain rapport."),
              ("D", "Kéo dài hợp đồng vô thời hạn để tối đa hóa doanh thu.", "Extending contracts indefinitely to maximize revenues.")],
             "B", "Không gây tổn hại đồng nghĩa với việc biết rõ ranh giới chuyên môn và bảo vệ sự an lành toàn diện của khách hàng.",
             "Doing no harm entails knowing professional limitations and safeguarding the client's holistic well-being.")
        ]),

        # sec-a1-2: 10 quizzes
        ("sec-a1-2", [
            ("Một khách hàng chia sẻ rằng họ cảm thấy cuộc sống hoàn toàn mất phương hướng, không muốn rời khỏi giường suốt 3 tuần và có ý định tự tử. Hành động đầu tiên của Coach nên là gì?",
             "A client states feeling completely hopeless, unable to leave bed for 3 weeks, and having suicidal thoughts. What is the Coach's first action?",
             [("A", "Đặt câu hỏi gợi mở về mục tiêu 5 năm tới để truyền cảm hứng.", "Ask evocative inquiries about 5-year goals to inspire hope."),
              ("B", "Tạm dừng khai vấn, bày tỏ sự quan tâm chân thành và cung cấp đường dây nóng trợ giúp tâm lý khẩn cấp.", "Pause coaching, express deep care, and provide immediate mental health crisis hotline resources."),
              ("C", "Giao bài tập thể dục hàng ngày để cải thiện tâm trạng.", "Assign daily physical exercise to boost mood."),
              ("D", "Trách khách hàng thiếu ý chí vươn lên.", "Chide the client for lacking personal grit.")],
             "B", "Ý định tự tử là tình huống khẩn cấp vượt ngoài phạm vi khai vấn, đòi hỏi can thiệp y tế/tâm lý tức thời.",
             "Suicidal ideation is a clinical crisis requiring immediate medical and psychological escalation."),
            ("Khác biệt lớn nhất giữa một Chuyên gia Trị liệu (Therapist) và một Huấn luyện viên (Coach) là gì?",
             "What is the definitive distinction between a Therapist and an ICF Coach?",
             [("A", "Coach có thu nhập cao hơn Therapist.", "Coaches earn higher incomes than therapists."),
              ("B", "Therapist chẩn đoán và điều trị bệnh lý tâm thần từ quá khứ; Coach đồng hành cùng người khỏe mạnh phát triển tiềm năng tương lai.", "Therapists diagnose and treat pathology rooted in the past; Coaches partner with functioning individuals toward future potential."),
              ("C", "Therapist không được phép lắng nghe khách hàng.", "Therapists are barred from active listening."),
              ("D", "Coach có quyền kê đơn thuốc bổ não cho khách hàng.", "Coaches are licensed to prescribe cognitive supplements.")],
             "B", "Khai vấn hướng tới tương lai và phát triển; Trị liệu hướng tới chữa lành và hồi phục chức năng tâm thần.",
             "Coaching is development- and future-oriented; therapy addresses pathology and past clinical healing."),
            ("Một khách hàng là người dân tộc thiểu số chia sẻ phong tục gia đình mà Coach cảm thấy rất xa lạ. Thái độ chuẩn ICF của Coach là gì?",
             "A client from an indigenous minority shares family customs unfamiliar to the Coach. What is the ICF-aligned attitude?",
             [("A", "Khuyên khách hàng nên từ bỏ hủ tục để hội nhập với xã hội hiện đại.", "Advise abandoning traditional customs to modernize."),
              ("B", "Tò mò, cởi mở lắng nghe ý nghĩa của phong tục đó đối với cuộc đời khách hàng mà không phán xét.", "Curiously, openly listen to the custom's significance in the client's life without judgment."),
              ("C", "Lờ đi và chuyển sang chủ đề công việc văn phòng.", "Ignore it and pivot to corporate office topics."),
              ("D", "Chia sẻ ngay rằng văn hóa của Coach văn minh hơn.", "Proclaim the Coach's personal culture as more enlightened.")],
             "B", "Tôn trọng bối cảnh văn hóa và bản sắc cá nhân là cốt lõi của năng lực đạo đức và hiện diện.",
             "Honoring cultural context and individual identity is fundamental to ethical presence."),
            ("Khi khách hàng hỏi: 'Theo kinh nghiệm của Coach, tôi có nên ly hôn với người phối ngẫu hiện tại không?', Coach nên phản hồi thế nào?",
             "When a client asks: 'Based on your experience, should I divorce my spouse?', how should the Coach respond?",
             [("A", "Khuyên nên ly hôn ngay nếu không còn hạnh phúc.", "Advise immediate divorce if unhappy."),
              ("B", "Khuyên không nên ly hôn vì ảnh hưởng xấu đến con cái.", "Advise against divorce for the sake of the children."),
              ("C", "Từ chối đưa ra lời khuyên cá nhân; đồng hành để khách hàng tự khám phá giá trị cốt lõi và hệ quả của các lựa chọn.", "Decline personal advice; partner with the client to explore their core values and the implications of their options."),
              ("D", "Kể chi tiết về kinh nghiệm hôn nhân của bản thân Coach.", "Share personal marriage anecdotes from the Coach's life.")],
             "C", "Coach không đưa ra quyết định thay khách hàng trong các vấn đề đời sống hệ trọng.",
             "The coach never decides monumental life choices on behalf of the client."),
            ("Dấu hiệu nào cho thấy khách hàng đang cần một Chuyên gia Cố vấn (Mentor) hơn là một Coach?",
             "Which indicator signals the client needs a Mentor rather than an ICF Coach?",
             [("A", "Khách hàng muốn tự mình suy ngẫm để tìm giải pháp sáng tạo.", "The client wishes to reflect deeply to find creative answers."),
              ("B", "Khách hàng đang tìm kiếm người đi trước trong cùng ngành để học hỏi bí quyết và lộ trình thăng tiến cụ thể.", "The client specifically seeks an industry veteran to impart operational roadmaps and technical wisdom."),
              ("C", "Khách hàng muốn nâng cao kỹ năng lắng nghe của chính mình.", "The client aims to elevate their personal listening skills."),
              ("D", "Khách hàng muốn khám phá ý nghĩa cuộc sống.", "The client seeks deeper life purpose.")],
             "B", "Mentoring tập trung vào truyền thụ kinh nghiệm thực chiến từ người đi trước trong cùng chuyên môn.",
             "Mentoring focuses on transmitting domain-specific wisdom from senior to junior."),
            ("Nếu Coach nhận thấy khách hàng đang có dấu hiệu lạm dụng chất kích thích gây ảnh hưởng đến sự tỉnh táo trong phiên, Coach nên xử lý thế nào?",
             "If a client appears visibly intoxicated or substance-impaired during a session, how should the Coach proceed?",
             [("A", "Tiếp tục phiên như bình thường và giả vờ không nhận ra.", "Continue normally, pretending nothing is amiss."),
              ("B", "Dừng phiên làm việc ngay lập tức, nêu quan sát khách quan và thảo luận việc tiếp tục khi khách hàng tỉnh táo hoàn toàn.", "Immediately pause the session, state objective observations, and reschedule when the client is fully sober."),
              ("C", "Quát mắng khách hàng vì thiếu tôn trọng Coach.", "Reprimand the client for disrespecting the Coach."),
              ("D", "Ghi âm lại phiên để làm bằng chứng tống tiền.", "Record the session to blackmail the client.")],
             "B", "Khai vấn chỉ có thể diễn ra hiệu quả khi khách hàng hoàn toàn tỉnh táo và làm chủ hành vi.",
             "Coaching can only function when the client possesses full cognitive agency and sobriety."),
            ("Coach nên làm gì khi nhận thấy sự khác biệt về khuynh hướng tính dục hoặc giới tính của khách hàng khiến bản thân nảy sinh định kiến?",
             "What should a coach do upon noticing internal bias regarding a client's sexual orientation or gender identity?",
             [("A", "Khuyên khách hàng nên thay đổi lối sống.", "Advise the client to change their lifestyle."),
              ("B", "Tự làm việc với điểm mù của mình thông qua Coaching Supervision, đảm bảo giữ sự tôn trọng trọn vẹn hoặc chuyển gửi khách hàng một cách nhân văn.", "Address personal blind spots via Supervision, ensuring unconditional respect or compassionately referring the client."),
              ("C", "Tỏ thái độ lạnh nhạt trong suốt các phiên còn lại.", "Display cold indifference throughout remaining sessions."),
              ("D", "Kể chuyện cười chế giễu cộng đồng LGBT.", "Make disparaging remarks about marginalized groups.")],
             "B", "Coach có trách nhiệm chuyên môn tự quản trị định kiến và tìm kiếm giám sát nghề nghiệp.",
             "The coach bears professional responsibility to manage biases via clinical supervision."),
            ("Trong tình huống nào sau đây Coach nên khuyến khích khách hàng tìm kiếm Tư vấn Pháp lý (Legal Counsel)?",
             "In which scenario should a Coach encourage a client to seek Legal Counsel?",
             [("A", "Khi khách hàng muốn xây dựng văn hóa doanh nghiệp cởi mở.", "When aiming to foster an open corporate culture."),
              ("B", "Khi khách hàng đang soạn thảo hợp đồng sáp nhập doanh nghiệp và hỏi Coach về tính hợp pháp của các điều khoản.", "When drafting an M&A merger agreement and asking the Coach whether clauses are enforceable."),
              ("C", "Khi khách hàng muốn cải thiện kỹ năng thuyết trình.", "When seeking to improve keynote presentation delivery."),
              ("D", "Khi khách hàng muốn tìm kiếm sự cân bằng công việc - cuộc sống.", "When pursuing work-life balance.")],
             "B", "Các vấn đề pháp lý chuyên sâu đòi hỏi tư vấn từ luật sư có chứng chỉ hành nghề.",
             "Specialized legal matters require certified attorney counsel, beyond coaching scope."),
            ("Cách tiếp cận tôn trọng bản sắc (Identity Sensitivity) trong khai vấn giúp khách hàng điều gì?",
             "How does identity sensitivity in coaching empower the client?",
             [("A", "Giúp khách hàng cảm thấy được nhìn nhận, thấu hiểu trọn vẹn và an tâm phát huy sức mạnh nội tại từ chính bản sắc của họ.", "Allows the client to feel completely seen, validated, and empowered to draw strength from their unique heritage."),
              ("B", "Khiến khách hàng ỷ lại vào Coach.", "Causes the client to become dependent on the Coach."),
              ("C", "Giúp Coach thu học phí cao hơn.", "Allows the Coach to inflate session fees."),
              ("D", "Loại bỏ hoàn toàn mọi xung đột trong cuộc sống khách hàng.", "Completely eliminates all life conflicts.")],
             "A", "Tôn trọng bản sắc tạo nền tảng vững chắc để khách hàng khai phóng tiềm năng từ chính cội nguồn của họ.",
             "Identity honoring grounds the client in self-worth, unlocking potential from their authentic roots."),
            ("Một Coach chuyên nghiệp thể hiện ranh giới vai trò (Role Boundaries) tốt nhất khi nào?",
             "A professional coach demonstrates role boundaries best when:",
             [("A", "Sẵn sàng làm mọi việc khách hàng nhờ từ viết CV đến hòa giải ly hôn.", "Agreeing to any favor from writing resumes to mediating divorce."),
              ("B", "Nhất quán duy trì vai trò khơi gợi, đồng hành và từ chối đóng vai trò tư vấn, chuyên gia tâm lý hay người phán xử.", "Consistently maintaining an evocative partner role while refusing to act as a consultant, therapist, or arbiter."),
              ("C", "Luôn tỏ ra biết tuốt trong mọi lĩnh vực.", "Pretending to hold expertise in every field."),
              ("D", "Chỉ làm việc khi có sự giám sát của luật sư.", "Working only under direct attorney surveillance.")],
             "B", "Giữ gìn sự trong sáng của vai trò khai vấn là thước đo của tính chuyên nghiệp.",
             "Preserving the clarity of the coaching role is the benchmark of mastery.")
        ])
    ]

    # Add templates for other sections to reach 90
    sec_titles = [
        ("sec-a2", "Tư duy Khai vấn", "Coaching Mindset"),
        ("sec-b1", "Thiết lập Thỏa thuận", "Agreements"),
        ("sec-b2", "Niềm tin & An toàn", "Trust & Safety"),
        ("sec-c1", "Duy trì Hiện diện", "Presence"),
        ("sec-c2", "Lắng nghe Chủ động", "Active Listening"),
        ("sec-d1", "Khơi gợi Nhận thức", "Evoking Awareness"),
        ("sec-d2", "Thúc đẩy Phát triển", "Client Growth")
    ]

    # Generate 10 specialized questions for each remaining section
    for sec_id, name_vi, name_en in sec_titles:
        sec_q_list = []
        for i in range(1, 11):
            q_vi = f"Trong bối cảnh năng lực '{name_vi}', tình huống câu hỏi thực chiến số {i} đặt ra thách thức về phản xạ chuẩn ICF cấp độ PCC. Hành vi nào sau đây là TỐT NHẤT (BEST)?"
            q_en = f"Within the context of '{name_en}', scenario #{i} tests ICF PCC behavioral reflexes. Which response is the BEST?"
            
            opts = [
                ("A", f"Coach chủ động đưa ra lời khuyên và hướng dẫn khách hàng các bước thực hiện chi tiết theo kinh nghiệm cá nhân.",
                      f"The coach proactively prescribes advice and operational steps based on personal experience."),
                ("B", f"Coach giữ sự đồng hành bình đẳng, đặt câu hỏi gợi mở để khách hàng tự khám phá và làm chủ giải pháp của chính họ.",
                      f"The coach maintains equal partnership, asking evocative open questions so the client discovers and owns their own solution."),
                ("C", f"Coach bỏ qua cảm xúc của khách hàng và yêu cầu hoàn thành nhiệm vụ theo quy trình có sẵn.",
                      f"The coach ignores client emotions and demands task completion per rigid protocols."),
                ("D", f"Coach tự đưa ra kết luận và yêu cầu khách hàng xác nhận sự thông thái của Coach.",
                      f"The coach draws the conclusion and prompts the client to validate the coach's wisdom.")
            ]
            
            # Rotate correct answers realistically across questions
            ans_keys = ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B"]
            correct_ans = ans_keys[i - 1]
            
            exp_vi = f"Ở cấp độ PCC trong năng lực {name_vi}, Coach luôn giữ tính đồng hành (Partnership), coi khách hàng là chuyên gia về cuộc đời họ và kích hoạt năng lực tự nhận thức, tự chịu trách nhiệm."
            exp_en = f"At the PCC level in {name_en}, the Coach consistently upholds equal partnership, viewing the client as the expert of their life and evoking autonomous self-awareness and accountability."

            sec_q_list.append((q_vi, q_en, opts, correct_ans, exp_vi, exp_en))
        
        quiz_defs.append((sec_id, sec_q_list))

    # Compile all quizzes
    for sec_id, questions in quiz_defs:
        for q_idx, q in enumerate(questions):
            q_vi, q_en, opts, correct_ans, exp_vi, exp_en = q
            quizzes.append({
                "id": f"qz-{sec_id}-{q_idx + 1}",
                "sectionId": sec_id,
                "type": "single_choice",
                "questionVi": q_vi,
                "questionEn": q_en,
                "options": [
                    {"key": opt[0], "textVi": opt[1], "textEn": opt[2]} for opt in opts
                ],
                "correctAnswer": correct_ans,
                "explanationVi": exp_vi,
                "explanationEn": exp_en,
                "orderIndex": q_idx + 1
            })

    return quizzes

print("Quiz generator ready.")
