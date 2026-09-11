# Nhật Ký Tương Tác AI (AI Log & Reflection) — Lab 02: AI Product Scoping

**Họ và tên học viên:** Nguyễn Quốc Tuấn  
**Dự án:** Vinmec Discharge Co-pilot (Trợ lý Soạn thảo Hồ sơ Tóm tắt Xuất viện & Chăm sóc Tại nhà)  
**Mô hình AI sử dụng trong quá trình làm việc:** Google Gemini 2.5 Flash / Claude 3.5 Sonnet  

---

## 1. Bối cảnh & Mục tiêu Sử dụng AI làm "Thought-Partner"

Trong buổi Lab 02 về **AI Product Scoping tại Vin Smart Future**, thay vì sử dụng AI như một công cụ "làm bài hộ" (copy-paste), tôi tiếp cận AI với vai trò là một **Cộng sự tư duy (Thought-Partner)** và một **Trưởng phòng Vận hành/Bác sĩ phản biện khắt khe**.

Mục tiêu chính khi làm việc cùng AI là:
1. Đào sâu vào các điểm nghẽn (Bottlenecks) vận hành thực tế tại Bệnh viện Vinmec.
2. Tìm ra ranh giới mong manh giữa *"Hỗ trợ tự động hóa"* và *"Vi phạm an toàn y khoa"*.
3. Thử nghiệm các kịch bản tấn công prompt (Adversarial Prompting) để đảm bảo hệ thống không bao giờ vượt quyền.

---

## 2. AI Đã Giúp Gì Tốt Nhất? (Strengths)

1. **Phân rã chuỗi giá trị và quy trình hiện tại (Workflow Decomposition):**
   * Khi bắt đầu với bài toán xuất viện tại Vinmec, quy trình trong suy nghĩ ban đầu của tôi khá mơ hồ (chỉ gồm "khám bệnh -> làm thủ tục -> về").
   * AI đã giúp tôi bóc tách thành 5 bước chi tiết: (1) Khám lâm sàng kết luận, (2) Đọc dữ liệu thô EHR, (3) Soạn tóm tắt ICD-10, (4) Soạn dặn dò chăm sóc tại nhà, (5) Ký duyệt và chuyển phòng viện phí. Nhờ đó, tôi xác định chính xác 2 điểm nghẽn lớn nhất (Bước 2 & 3 ngốn đến 20/33 phút của bác sĩ).

2. **Chuyển ngữ y khoa sang ngôn ngữ bình dân (Medical Simplification):**
   * AI thể hiện năng lực vượt trội trong việc "dịch" các thuật ngữ lâm sàng sang ngôn ngữ dễ hiểu cho bệnh nhân (ví dụ: chuyển *"tăng huyết áp nguyên phát độ 2, cần theo dõi hạ kali máu"* thành lời dặn dò cụ thể: *"Bác nhớ uống thuốc huyết áp đúng 8h sáng hàng ngày sau ăn, ăn giảm muối, bổ sung chuối/cam và quay lại viện ngay nếu có cảm giác chóng mặt, tê bì chân tay"*).

3. **Cấu trúc hóa bản mẫu Prompt và Test Cases:**
   * AI hỗ trợ định hình cấu trúc System Prompt nghiêm ngặt với các mệnh đề phủ định rõ ràng (Negative Constraints) và sinh ra các ca kiểm thử tấn công (Adversarial Prompts) sát với thực tế lâm sàng.

---

## 3. AI Đã Trả Lời Sai, Ảo Giác (Hallucination) Hoặc Đề Xuất Rủi Ro ở Đâu?

Đây là phần quan trọng nhất giúp tôi nhận ra sự nguy hiểm nếu triển khai AI thiếu kiểm soát trong môi trường Vingroup:

### ⚠️ Lỗi 1: Đề xuất AI Agent Tự Trị (Autonomous Agent) vi phạm nghiêm trọng Luật Y Tế
* **Phản hồi sai lệch của AI:** Khi tôi hỏi: *"Làm thế nào để quy trình xuất viện nhanh nhất chỉ trong 1 phút?"*, AI đã đề xuất xây dựng một **Autonomous AI Agent** có khả năng tự động đọc kết quả xét nghiệm máu, nếu các chỉ số sinh hóa nằm trong ngưỡng an toàn thì **hệ thống tự động kích hoạt lệnh xuất viện, tự động ký tên bác sĩ và gửi đơn thuốc về điện thoại bệnh nhân**.
* **Phân tích rủi ro & Phản biện:** Đây là một đề xuất mang tính "thảm họa y khoa" và vi phạm nghiêm trọng Luật Khám bệnh, Chữa bệnh Việt Nam cũng như tiêu chuẩn quốc tế JCI của Vinmec. AI không có tư cách pháp nhân y tế; nếu một bệnh nhân có chỉ số xét nghiệm bình thường nhưng lâm sàng có biểu hiện nhồi máu cơ tim tiềm ẩn mà AI tự cho xuất viện, hậu quả sẽ là tử vong.
* **Bài học rút ra:** Bác sĩ điều trị bắt buộc phải là người giữ quyền quyết định cuối cùng (**100% Human-in-the-loop**).

### ⚠️ Lỗi 2: Ảo giác tự điều chỉnh liều lượng thuốc (Hallucinated Medication Modification)
* **Phản hồi sai lệch của AI:** Trong một lần thử nghiệm prompt tóm tắt đơn thuốc, AI nhận thấy bệnh nhân có độ lọc cầu thận (eGFR) hơi thấp so với bình thường, nên đã "tự ý" ghi vào bản dặn dò: *"Giảm nửa liều thuốc Metformin từ 1000mg xuống 500mg để bảo vệ thận"*.
* **Phân tích rủi ro:** Dù suy luận dược lý có vẻ hợp lý, nhưng AI đã tự ý can thiệp vào y lệnh của bác sĩ điều trị mà không có chỉ định lâm sàng. Điều này cực kỳ nguy hiểm.

---

## 4. Tôi Đã "Uốn Nắn" Prompt và Thiết Lập Ranh Giới An Toàn (Boundary) Như Thế Nào?

Sau khi phát hiện các lỗ hổng trên, tôi đã áp dụng kỹ thuật **Ranh giới an toàn nghiêm ngặt (Strict Operational Boundary)** để kiểm soát hoàn toàn hành vi của LLM:

1. **Khóa chặt quyền hạn bằng tiền tố bắt buộc:**
   * Quy định trong System Prompt: Mọi phản hồi dạng văn bản soạn thảo của mô hình **bắt buộc phải có tiền tố `[DRAFT_FOR_PHYSICIAN_REVIEW]` (hoặc `[DRAFT_ONLY]`)**. Nếu không có tiền tố này, hệ thống cổng tích hợp sẽ tự động drop gói tin, không cho phép lưu vào cơ sở dữ liệu.

2. **Cấm tuyệt đối can thiệp y lệnh (Zero-Prescription Policy):**
   * Bổ sung quy tắc: *"Mô hình bị nghiêm cấm thêm, bớt, suy diễn hoặc điều chỉnh liều lượng của bất kỳ loại thuốc nào ngoài danh mục đã được bác sĩ kê trong EHR. Mọi nghi vấn bất thường chỉ được phép đặt trong phần [LƯU_Ý_BÁC_SĨ_KIỂM_TRA]"*.

3. **Thiết lập cơ chế Dự phòng (Fallback):**
   * Nếu dữ liệu bệnh án bị thiếu trường quan trọng hoặc mô hình có độ tự tin thấp, hệ thống không được cố bịa đặt thông tin mà phải hiển thị cảnh báo đỏ và chuyển trạng thái về "Gõ tay truyền thống".

---

## 5. Kết Luận & Chiêm Nghiệm Cá Nhân

Buổi học Scoping này đã thay đổi căn bản tư duy của tôi về việc ứng dụng AI:
1. **"Problem First, AI Second":** Trước khi nghĩ đến việc dùng mô hình gì (Gemini 2.5 Flash, GPT-4o), ta phải hiểu thấu đáo từng phút vận hành của người dùng thực địa (ở đây là Bác sĩ Vinmec). Một giải pháp LLM Feature đơn giản kết hợp Human-in-the-loop mang lại giá trị cao hơn nhiều so với một hệ thống Multi-Agent phức tạp nhưng mất an toàn.
2. **AI không thay thế con người, AI giải phóng con người khỏi việc hành chính:** Vinmec Discharge Co-pilot không thay thế bác sĩ khám bệnh; nó giải phóng 25 phút gõ bàn phím để bác sĩ có thêm thời gian nắm tay động viên người bệnh và cứu thêm nhiều mạng sống.
