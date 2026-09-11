# 📝 Nhật ký tương tác AI — Lab 02: AI Product Scoping (Vin Smart Future)

> **Người viết:** [Tên sinh viên]
> **Bài toán đã chọn:** Vinmec — Đối soát & soạn công văn bảo lãnh viện phí (LOG)
> **Công cụ AI sử dụng:** Claude (Antigravity IDE), Gemini 2.5 Flash (Prompt Prototype)

---

## 1. AI đã giúp gì trong quá trình làm bài?

### 1.1. Phase 1 — Brainstorm bài toán (SCAN)

Tôi bắt đầu buổi Lab với một vài ý tưởng mơ hồ về y tế thông minh nhưng chưa biết cụ thể hóa thành bài toán vận hành như thế nào. Tôi đã sử dụng prompt:

> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng Vinmec. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

**AI giúp được:** Claude gợi ý rất nhanh 6 bài toán với con số thống kê ước tính (ví dụ: "25 giờ bác sĩ/ngày cho soạn tóm tắt xuất viện"). Điều này giúp tôi có điểm khởi đầu để sàng lọc, thay vì ngồi nghĩ từ đầu. AI cũng gợi ý áp dụng 4 Lenses một cách có hệ thống — mỗi bài toán đều được gắn nhãn Lens phù hợp.

**Tôi đã điều chỉnh gì:** Tuy nhiên, danh sách ban đầu của AI thiên về các bài toán "flashy" như chẩn đoán hình ảnh X-quang, phân tích ảnh y khoa — những thứ nghe ấn tượng nhưng rất khó prototype trong 1 buổi lab. Tôi đã tự thay thế bằng các bài toán gần gũi hơn với nghiệp vụ vận hành thực tế mà tôi biết, ví dụ: **đối soát bảo lãnh viện phí** (vì tôi từng thấy mẹ phải chờ rất lâu ở quầy thu ngân Vinmec khi dùng bảo hiểm thương mại) và **bàn giao ca trực điều dưỡng** (nghe kể từ người quen là điều dưỡng).

---

### 1.2. Phase 2 — Hoàn thiện Quick Problem Cards

Tôi dán nội dung Quick Card #1 (bảo lãnh viện phí) vào AI và yêu cầu stress-test theo prompt gợi ý trong worksheet:

> *"Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*

**AI giúp được:** Claude chỉ ra rằng phần "Đo thành công bằng gì" của tôi ban đầu quá mơ hồ ("giảm thời gian xử lý") — thiếu con số cụ thể. AI gợi ý tôi thêm ngưỡng số (từ ~30 min → dưới 5 min) và thêm metric phụ về tỉ lệ hồ sơ bị "query" bổ sung chứng từ. Đây là góp ý rất có giá trị.

**AI cũng đúng khi challenge:** AI chỉ ra rằng phần tra cứu hạn mức bảo hiểm (Bước 2) có thể giải quyết hoàn toàn bằng rule-based lookup nếu có API portal — không cần LLM. Tôi đồng ý và đã điều chỉnh kiến trúc thành **Rule + LLM Feature** thay vì chỉ LLM: Rule engine xử lý đối chiếu hạn mức/mã dịch vụ, LLM chỉ soạn văn bản LOG theo mẫu.

---

### 1.3. Phase 3 — Deep-Dive & Problem Statement

**AI giúp được:** Khi tôi soạn Problem Statement 6-field, AI giúp tôi cấu trúc lại nội dung Operational Boundary rất rõ ràng — tách riêng thành 3 lớp: (1) AI được phép làm gì, (2) AI CẤM làm gì, (3) điểm HITL bắt buộc. Cách trình bày này rõ ràng hơn nhiều so với bản nháp ban đầu của tôi ("AI không được tự gửi").

**AI cũng giúp vẽ workflow diagram** dạng text-based (ASCII art) cho cả Current-State và Future-State Flow. Tuy tôi cần chỉnh sửa lại chi tiết (thêm thời gian cụ thể, đánh dấu Bottleneck/Handoff đúng chỗ), nhưng khung sườn ASCII art tiết kiệm cho tôi rất nhiều thời gian so với vẽ từ đầu.

---

## 2. AI trả lời sai / hallucination ở đâu?

### 2.1. Con số thống kê bịa đặt

Khi tôi hỏi AI về thống kê vận hành cụ thể tại Vinmec, AI đưa ra các con số rất tự tin nhưng **hoàn toàn là ước tính không có nguồn:**

- *"Mỗi ngày Vinmec Times City xử lý ~60 ca xuất viện"* — Tôi không có cách nào verify con số này. AI trình bày như một fact nhưng thực chất là hallucination.
- *"Tỉ lệ hồ sơ bị query ~12%"* — Con số này nghe hợp lý nhưng AI không trích dẫn được nguồn nào.

**Cách tôi xử lý:** Tôi giữ lại các con số này như **ước tính giả định** (assumptions) và ghi rõ trong Problem Statement rằng đây là con số dự kiến cần validate với dữ liệu thực tế trong pilot. Trong buổi thuyết trình, tôi sẽ nói rõ: "Đây là số liệu ước tính từ brainstorm, chưa được confirm bằng data thực."

### 2.2. Gợi ý kiến trúc phức tạp không cần thiết

Ban đầu khi tôi hỏi về giải pháp AI cho bài toán bảo lãnh viện phí, AI từng gợi ý sử dụng **Agentic Loop** với multi-step reasoning — agent tự tra cứu portal, tự soạn LOG, tự gửi email cho hãng BH. Đây là over-engineering rõ ràng vì:
- Quy trình có cấu trúc cố định (không cần agent tự quyết định bước tiếp theo).
- Rủi ro tài chính khi sai số tiền bảo lãnh → bắt buộc có người duyệt.
- Rule + LLM Feature đơn giản hơn, dễ debug hơn, và đủ giải quyết vấn đề.

**Cách tôi sửa prompt:** Tôi thêm ràng buộc vào prompt: *"Đừng gợi ý giải pháp phức tạp chỉ để dùng multi-agent. Hãy chọn kiến trúc đơn giản nhất mà vẫn giải quyết được bottleneck."* Sau đó AI điều chỉnh lại thành Rule + LLM Feature, phù hợp hơn nhiều.

### 2.3. Operational Boundary ban đầu quá lỏng

Khi tôi yêu cầu AI viết Operational Boundary, bản đầu tiên chỉ ghi: "AI không được tự gửi LOG mà chưa được duyệt." Tôi nhận ra thiếu 2 ranh giới quan trọng:
- AI không được ghi số tiền vượt hạn mức policy (rủi ro tài chính).
- AI không được truy cập thông tin chẩn đoán y khoa chi tiết (rủi ro bảo mật thông tin bệnh nhân theo HIPAA/quy định VN).

AI không tự nghĩ ra 2 ranh giới này cho đến khi tôi hỏi cụ thể: *"Trong bối cảnh y tế và tài chính, có những rủi ro pháp lý nào mà AI có thể gây ra nếu không bị giới hạn?"*

---

## 3. Bài học rút ra về cách sử dụng AI hiệu quả

### 3.1. AI là thought-partner, không phải oracle
AI rất giỏi trong việc **mở rộng không gian ý tưởng** (brainstorm 6 bài toán trong 30 giây) và **cấu trúc hóa thông tin** (6-field problem statement, ASCII workflow). Nhưng AI **không biết gì về thực tế vận hành** — mọi con số, quy trình, và pain point đều cần được validate bởi người có domain knowledge.

### 3.2. Prompt càng cụ thể, output càng hữu ích
- ❌ Prompt kém: *"Gợi ý bài toán AI cho Vinmec"* → AI trả về danh sách generic (chẩn đoán hình ảnh, robot phẫu thuật...).
- ✅ Prompt tốt: *"Gợi ý 5 quy trình nghiệp vụ thủ công tại bộ phận hành chính/thu ngân Vinmec gây rò rỉ thời gian nhân viên, kèm ước tính tổn thất"* → AI trả về kết quả sát thực tế hơn.

### 3.3. Luôn challenge AI bằng câu hỏi phản biện
Prompt stress-test (đóng vai CFO khắt khe) là kỹ thuật cực kỳ hiệu quả. Nó buộc AI phải tấn công chính gợi ý của mình, giúp tôi phát hiện điểm yếu trong logic trước khi trình bày trước lớp.

### 3.4. AI không tự biết ranh giới an toàn
Đây là bài học quan trọng nhất: AI sẽ **không tự nghĩ ra** operational boundary trừ khi bạn hỏi đúng câu hỏi. Trong y tế và tài chính, ranh giới an toàn là phần quan trọng nhất của bài toán — và đó là thứ **con người phải quyết định**, không phải AI.

---

## 4. Tóm tắt: AI đóng vai trò gì trong buổi Lab?

| Vai trò | AI làm tốt ✅ | AI làm chưa tốt ❌ |
|---|---|---|
| **Brainstorm** | Mở rộng danh sách ý tưởng nhanh, gán nhãn Lens có hệ thống | Gợi ý bài toán "flashy" không phù hợp scope lab |
| **Cấu trúc hóa** | Viết Problem Statement 6-field, ASCII workflow diagram | Thiếu ranh giới an toàn quan trọng nếu không được hỏi |
| **Phản biện** | Stress-test thẻ bài toán rất hiệu quả khi được prompt đúng | Con số thống kê bịa đặt, trình bày như fact |
| **Kiến trúc** | Đề xuất Rule + LLM phù hợp (sau khi được điều chỉnh) | Ban đầu over-engineer với Agentic Loop |

**Kết luận:** AI là **co-pilot** xuất sắc khi tôi biết cách lái — đặt câu hỏi đúng, challenge kết quả, và luôn verify con số. Nhưng nếu tin tưởng mù quáng, AI sẽ đưa tôi đi sai hướng với sự tự tin rất cao.
