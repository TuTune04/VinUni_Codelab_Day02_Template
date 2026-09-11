# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **🤖 AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Vinpearl | Tốn thời gian | Soạn reply review khách sạn trên Booking/Agoda/Google Maps |
| 2 | Vinhomes | Lặp lại | Phân loại & điều hướng phản ánh cư dân qua App |
| 3 | VinFast | Lặp lại | Đối chiếu hóa đơn sạc điện với đối tác |
| 4 | Vinpearl | AI có thể tốt hơn | Phân tích sentiment review đa nền tảng, cảnh báo real-time |
| 5 | Vingroup (TT) | Pain từ người khác | Giám sát tin đồn thất thiệt trên MXH |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

---

### QUICK PROBLEM CARD #1 ⭐ (Bài toán chính — dùng cho Prototype)

| Mục | Nội dung |
|-----|----------|
| **Bài toán (1 câu)** | Soạn thảo tự động phản hồi chuyên nghiệp cho review khách sạn Vinpearl trên các nền tảng Booking.com, Agoda, Google Maps |
| **Công ty thành viên** | [x] Vinpearl |
| **Ai đang đau (Actor)?** | Nhân viên CSKH / PR team của Vinpearl — phải đọc và soạn reply thủ công cho hàng trăm review mỗi ngày, đặc biệt quá tải vào mùa cao điểm du lịch |

**Workflow thủ công hiện tại (5 bước):**
```
1. Nhân viên mở dashboard review từ Booking/Agoda/Google Maps
   ──> 2. Đọc nội dung review, xác định ngôn ngữ & mức độ nghiêm trọng
   ──> 3. Soạn reply phù hợp (xin lỗi / cảm ơn / giải thích)
   ──> 4. Gửi cho quản lý duyệt trước khi đăng
   ──> 5. Đăng reply công khai lên nền tảng
```

| Mục | Nội dung |
|-----|----------|
| **Bước tốn thời gian nhất?** | Bước 3 — Soạn reply (⏱ 10-15 phút/review, review tiêu cực có thể lên 20-30 phút) |
| **AI nhảy vào ở bước nào?** | Bước 2 + 3: AI tự động phân loại mức độ nghiêm trọng và soạn draft reply. Nếu review chứa cáo buộc nghiêm trọng (trộm cắp, ngộ độc) → escalate thẳng cho manager thay vì soạn reply |
| **Metric đo thành công** | Giảm thời gian soạn reply từ 10-15 min ──> dưới 2 min/review. Tăng tỷ lệ reply review từ 60% ──> 95% trong vòng 24h |
| **Quick Architecture** | [x] LLM — Dùng LLM để hiểu ngữ cảnh review đa ngôn ngữ và soạn reply có giọng điệu phù hợp |

---

### QUICK PROBLEM CARD #2

| Mục | Nội dung |
|-----|----------|
| **Bài toán (1 câu)** | Tự động phân loại và điều hướng phản ánh của cư dân Vinhomes đến đúng bộ phận xử lý |
| **Công ty thành viên** | [x] Vinhomes |
| **Ai đang đau (Actor)?** | Nhân viên ban quản lý tòa nhà — phải đọc từng phản ánh trên App Resident rồi phân loại thủ công (điện, nước, thang máy, an ninh, tiếng ồn...) |

**Workflow thủ công hiện tại (4 bước):**
```
1. Cư dân gửi phản ánh qua App Vinhomes Resident
   ──> 2. Nhân viên BQL đọc và phân loại loại vấn đề
   ──> 3. Chuyển tiếp đến bộ phận phụ trách (kỹ thuật / an ninh / vệ sinh)
   ──> 4. Soạn phản hồi xác nhận cho cư dân
```

| Mục | Nội dung |
|-----|----------|
| **Bước tốn thời gian nhất?** | Bước 2 + 3 — Đọc, phân loại và chuyển tiếp (⏱ 5-8 phút/phản ánh, dễ chuyển nhầm bộ phận) |
| **AI nhảy vào ở bước nào?** | Bước 2 + 3 + 4: AI tự phân loại vấn đề, chuyển đúng bộ phận, và soạn tin xác nhận. Nếu phản ánh liên quan an toàn (cháy, rò gas, ngập) → gửi cảnh báo khẩn cấp |
| **Metric đo thành công** | Giảm thời gian phân loại từ 5-8 min ──> dưới 30 giây. Giảm tỷ lệ chuyển nhầm bộ phận từ 15% ──> dưới 3% |
| **Quick Architecture** | [x] LLM — Cần NLU để hiểu phản ánh tiếng Việt tự nhiên, phân loại đa nhãn |

---

### QUICK PROBLEM CARD #3

| Mục | Nội dung |
|-----|----------|
| **Bài toán (1 câu)** | Tự động đối chiếu và so khớp hóa đơn sạc điện từ đối tác bên ngoài với dữ liệu nội bộ VinFast |
| **Công ty thành viên** | [x] VinFast |
| **Ai đang đau (Actor)?** | Nhân viên tài chính VinFast — phải so khớp thủ công dữ liệu sạc từ hàng nghìn trụ sạc liên kết mỗi tuần |

**Workflow thủ công hiện tại (4 bước):**
```
1. Nhận file dữ liệu sạc từ đối tác (EVN, trạm sạc liên kết)
   ──> 2. So khớp từng dòng với dữ liệu hệ thống nội bộ VinFast
   ──> 3. Đánh dấu các dòng sai lệch, ghi chú lý do
   ──> 4. Tổng hợp báo cáo chênh lệch gửi bộ phận kế toán
```

| Mục | Nội dung |
|-----|----------|
| **Bước tốn thời gian nhất?** | Bước 2 + 3 — So khớp thủ công (⏱ 2-3 ngày/tuần cho hàng nghìn giao dịch) |
| **AI nhảy vào ở bước nào?** | Bước 2 + 3 + 4: AI tự động match dữ liệu, phát hiện sai lệch bất thường và tạo báo cáo |
| **Metric đo thành công** | Giảm thời gian đối chiếu từ 2-3 ngày ──> dưới 2 giờ. Giảm sai sót so khớp từ 5% ──> dưới 0.5% |
| **Quick Architecture** | [x] Rule — Chủ yếu dùng rule-based matching + AI hỗ trợ phát hiện anomaly |

---

> [!TIP]
> **🤖 AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> *"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*

---