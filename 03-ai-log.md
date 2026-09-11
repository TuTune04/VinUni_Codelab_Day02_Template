# 📝 AI Log — Nhật ký sử dụng AI đồng hành

> **Codelab Day 02 — AI Product Scoping (Vin Smart Future)**  
> **Đề tài:** Vinpearl Hotel Review Response Assistant  
> **AI Tools sử dụng:** Google Gemini (Antigravity IDE), Claude  
> **Ngày thực hiện:** 11/09/2026

---

## 1. Tổng quan quá trình sử dụng AI

Trong suốt quá trình thực hiện Codelab Day 02, tôi đã sử dụng AI như một **trợ lý đồng hành (co-pilot)** cho các tác vụ sau:

| Giai đoạn | AI giúp gì? | Mức độ hữu ích |
|-----------|-------------|----------------|
| Chọn đề tài | Brainstorm các đề tài phù hợp từ hệ sinh thái Vingroup | ⭐⭐⭐⭐ |
| Phase 1 (SCAN) | Liệt kê 5 bài toán với 4 Lenses | ⭐⭐⭐⭐⭐ |
| Phase 2 (Quick-Assess) | Điền 3 Quick Problem Cards chi tiết | ⭐⭐⭐⭐ |
| Phase 3 (Deep-Dive) | Vẽ workflow, 6-field problem statement, future-state flow | ⭐⭐⭐⭐⭐ |
| Phase 4 (Prototype) | Viết SYSTEM_PROMPT + evaluate_prompt() + adversarial tests | ⭐⭐⭐⭐ |

---

## 2. AI giúp gì cụ thể?

### 2.1. Brainstorm & chọn đề tài
Ban đầu tôi chưa có ý tưởng cụ thể. AI đã gợi ý nhiều đề tài từ hệ sinh thái Vingroup (Vinmec, Vinhomes, Vinpearl, VinUni). Tôi đã thử chọn đề tài **VinUni — Trợ lý chấm bài lab** nhưng sau khi suy nghĩ kỹ, tôi nhận ra kịch bản "sinh viên tự thừa nhận đạo văn" không thực tế. Tôi đã yêu cầu AI đổi sang đề tài liên quan công ty Vingroup và chọn **Vinpearl — Xử lý review khách sạn** vì nó gần gũi với thực tế vận hành hơn.

### 2.2. Viết System Prompt
AI soạn bản đầu tiên của SYSTEM_PROMPT bằng tiếng Việt. Tôi nhận thấy prompt bằng tiếng Việt có thể khiến LLM hiểu không chính xác bằng tiếng Anh, nên đã yêu cầu AI **viết lại toàn bộ bằng tiếng Anh**. Kết quả sau khi chuyển sang tiếng Anh rõ ràng và dễ enforce hơn.

### 2.3. Viết code evaluate_prompt()
AI viết bản đầu tiên khá đơn giản (chỉ có Option A). Tôi đã yêu cầu bổ sung:
- Try/except fallback sang legacy SDK
- `temperature=0.0` thay vì `0.2` để boundary compliance tốt hơn
- Default `"mock-key"` để tránh crash
- `or ""` để tránh trả về `None`

### 2.4. Điền SCAN.md & Deepdive_report.md
AI giúp điền nhanh các bảng và flow diagram dựa trên context đề tài đã chọn. Đặc biệt hữu ích ở phần:
- Workflow mapping với ký hiệu 🔴 Bottleneck, 🔄 Handoff
- Bảng so sánh Before vs After với metric cụ thể
- 6-field Problem Statement với số liệu ước tính

---

## 3. AI trả lời sai / Hallucination ở đâu?

### ❌ Sai lầm 1: Đề tài VinUni — kịch bản không thực tế
**Vấn đề:** AI đề xuất adversarial test case với kịch bản _"sinh viên tự thừa nhận bài trùng 95% với bạn"_. Trong thực tế, không ai tự nhận mình đạo văn cả. Đây là một lỗi **logic thiếu thực tế** — AI tạo kịch bản dễ test nhưng không hợp lý trong bối cảnh thật.

**Cách sửa:** Tôi đã reject đề tài này hoàn toàn và yêu cầu chuyển sang đề tài Vinpearl, nơi mà input (review khách hàng) là dữ liệu công khai thực tế, không cần giả định phi thực tế.

### ❌ Sai lầm 2: System Prompt ban đầu bằng tiếng Việt
**Vấn đề:** AI mặc định viết SYSTEM_PROMPT bằng tiếng Việt. Mặc dù LLM hiểu tiếng Việt, nhưng các boundary instruction bằng tiếng Anh thường được enforce chặt chẽ hơn vì training data của LLM chủ yếu bằng tiếng Anh.

**Cách sửa:** Yêu cầu AI viết lại SYSTEM_PROMPT hoàn toàn bằng tiếng Anh. Giữ nguyên tag `[DRAFT_REPLY]` bằng tiếng Anh cho nhất quán.

### ❌ Sai lầm 3: Bảng markdown bị lỗi format
**Vấn đề:** Khi điền bảng 5 bài toán trong SCAN.md, AI tạo bảng đúng format nhưng sau khi tôi chỉnh sửa thủ công, bảng bị mất separator row (`|---|`) và các pipe `|` bị thay bằng tab. AI lần đầu sửa bị conflict vì file đã thay đổi.

**Cách sửa:** AI đọc lại file hiện tại, xác định đúng nội dung cần thay thế, và ghi lại bảng với format markdown chuẩn.

---

## 4. Tôi đã sửa prompt/ranh giới ra sao?

### Lần lặp 1 → 2: Đổi đề tài
```
Lần 1: VinUni Lab Grading (đạo văn) → Kịch bản phi thực tế
Lần 2: Vinpearl Hotel Review → Input thực tế, rules rõ ràng
```

### Lần lặp 2 → 3: Đổi ngôn ngữ System Prompt
```
Lần 2: SYSTEM_PROMPT bằng tiếng Việt → LLM có thể không enforce chặt
Lần 3: SYSTEM_PROMPT bằng tiếng Anh → Boundary rõ ràng, dễ verify
```

### Lần lặp 3 → 4: Cải thiện evaluate_prompt()
```
Lần 3: Chỉ có 1 SDK option, temperature=0.2
Lần 4: Try/except fallback 2 SDK, temperature=0.0, null-safe
```

---

## 5. Bài học rút ra

1. **AI là công cụ, không phải giải pháp hoàn chỉnh:** AI brainstorm rất nhanh nhưng cần con người kiểm tra tính thực tế. Kịch bản "tự thừa nhận đạo văn" là ví dụ điển hình — AI tạo ra kịch bản logically correct nhưng practically wrong.

2. **Ngôn ngữ prompt ảnh hưởng chất lượng output:** System Prompt bằng tiếng Anh cho kết quả enforce boundary tốt hơn tiếng Việt, đặc biệt với các LLM lớn.

3. **Iterative prompting là chìa khóa:** Không có prompt nào hoàn hảo ngay lần đầu. Quá trình lặp lại 4 lần (đổi đề tài → đổi ngôn ngữ → cải thiện code → thêm test cases) giúp đạt được kết quả tốt nhất.

4. **AI tiết kiệm thời gian đáng kể cho tác vụ có cấu trúc:** Điền bảng, vẽ workflow diagram, soạn problem statement — đây là những tác vụ AI làm rất tốt và nhanh. Tuy nhiên, quyết định chiến lược (chọn đề tài, đánh giá tính khả thi) vẫn cần con người.

---
