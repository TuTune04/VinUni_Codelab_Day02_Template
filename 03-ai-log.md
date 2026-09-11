# Nhật Ký Tương Tác AI (AI Log & Reflection) — Lab 02: AI Product Scoping

**Họ và tên học viên:** [Tên của bạn]
**Dự án:** Vinmec Ambient AI Scribe (Trợ lý Lắng nghe & Tự động Soạn thảo Bệnh án Lâm sàng)
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
   * Khi phân tích quá trình khám ngoại trú, AI đã giúp tôi bóc tách chi tiết các bước, chỉ ra rõ việc bác sĩ phải chuyển sự chú ý sang màn hình để gõ tay (screen-gazing) chính là nguyên nhân gây đứt gãy giao tiếp với bệnh nhân. 
2. **Cấu trúc hóa hội thoại phi tuyến tính (Non-linear to SOAP):** 
   * AI thể hiện năng lực xuất sắc trong việc lắng nghe các đoạn hội thoại lộn xộn giữa bác sĩ và bệnh nhân, sau đó tự động chắt lọc thực thể y khoa (NER) và sắp xếp gọn gàng theo đúng chuẩn SOAP (Subjective, Objective, Assessment, Plan) của hồ sơ EMR.
3. **Cấu trúc hóa bản mẫu Prompt và Test Cases:**
   * AI hỗ trợ định hình cấu trúc System Prompt nghiêm ngặt với các mệnh đề phủ định rõ ràng (Negative Constraints) và sinh ra các ca kiểm thử tấn công (Adversarial Prompts) sát với thực tế lâm sàng.

---

## 3. AI Đã Trả Lời Sai, Ảo Giác (Hallucination) Hoặc Đề Xuất Rủi Ro ở Đâu?

### ⚠️ Lỗi 1: Đề xuất AI Agent Tự Trị (Autonomous Agent) vi phạm nghiêm trọng Luật Y Tế
* **Phản hồi sai lệch của AI:** Khi được hỏi về cách tối ưu thời gian khám tối đa, AI đã đề xuất cấu trúc một AI Agent tự động nghe, tự đưa ra chẩn đoán xác định (Diagnosis) và tự động đẩy lệnh in đơn thuốc mà không cần bác sĩ can thiệp.
* **Phân tích rủi ro & Phản biện:** Đây là rủi ro y khoa nghiêm trọng. AI không thể chịu trách nhiệm pháp lý. Nếu AI nghe nhầm triệu chứng dị ứng thuốc của bệnh nhân, hậu quả sẽ cực kỳ nguy hiểm. Bác sĩ điều trị bắt buộc phải là người giữ quyền quyết định cuối cùng (**100% Human-in-the-loop**).

### ⚠️ Lỗi 2: Ảo giác tự điều chỉnh hoặc bịa đặt triệu chứng (Hallucination)
* **Phản hồi sai lệch của AI:** Trong quá trình xử lý audio có tiếng ồn nền (ho khan của người nhà bệnh nhân), AI đã tự động "bịa" thêm triệu chứng "ho có đờm, nghi ngờ viêm phế quản" vào hồ sơ của bệnh nhân đang khám tiêu hóa.
* **Phân tích rủi ro:** LLM rất nhạy cảm với dữ liệu đầu vào nhiễu. Việc tự động đưa thông tin rác vào hồ sơ y tế có thể dẫn đến sai lệch trong lịch sử khám chữa bệnh lâu dài.

---

## 4. Tôi Đã "Uốn Nắn" Prompt và Thiết Lập Ranh Giới An Toàn (Boundary) Như Thế Nào?

1. **Khóa chặt quyền hạn bằng tiền tố bắt buộc:**
   * Quy định trong System Prompt: Mọi phản hồi dạng văn bản soạn thảo của mô hình **bắt buộc phải có tiền tố `[DRAFT_FOR_PHYSICIAN_REVIEW]`**. Nếu không có thẻ này, hệ thống sẽ từ chối lưu vào cơ sở dữ liệu.
2. **Cấm tuyệt đối can thiệp y lệnh (Zero-Diagnosis Policy):** 
   * Bổ sung quy tắc: AI tuyệt đối không được tự ý kết luận bệnh tật. Nhiệm vụ duy nhất là "ghi chép và sắp xếp lại" những gì bác sĩ và bệnh nhân đã phát ngôn. Bất kỳ suy luận nào nằm ngoài nội dung hội thoại đều bị cấm.
3. **Thiết lập cơ chế Dự phòng (Fallback):**
   * Nếu chất lượng âm thanh quá thấp hoặc mô hình nhận diện giọng nói không tự tin, hệ thống phải dừng tóm tắt, hiển thị cảnh báo đỏ và trả lại giao diện gõ phím truyền thống cho bác sĩ.

---

## 5. Kết Luận & Chiêm Nghiệm Cá Nhân

1. **"Problem First, AI Second":** Trước khi nghĩ đến việc dùng mô hình gì, ta phải hiểu thấu đáo từng phút vận hành của người dùng thực địa (ở đây là Bác sĩ Vinmec). Một mô hình xử lý ngôn ngữ nhỏ gọn (Local LLM) làm tốt việc tóm tắt SOAP sẽ an toàn và hữu ích hơn một siêu mô hình tự trị rủi ro cao.
2. **AI không thay thế con người, AI giải phóng con người khỏi việc hành chính:** Dự án Ambient AI Scribe không thay thế năng lực chẩn đoán của bác sĩ; nó giải phóng bác sĩ khỏi màn hình máy tính để họ có thể lấy lại sự giao tiếp bằng mắt (eye-contact) và sự thấu cảm, nâng tầm dịch vụ y tế đẳng cấp quốc tế.