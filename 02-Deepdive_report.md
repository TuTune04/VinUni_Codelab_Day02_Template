# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

## 3.1. Current-State Workflow Mapping (25 min)

**Bài toán:** Soạn phản hồi review khách sạn Vinpearl trên Booking.com / Agoda / Google Maps

**Quy trình hiện tại (Current-State Flow):**

```
┌──────────────┐    ┌──────────────────┐    ┌─────────────────────┐    ┌──────────────────┐    ┌────────────────┐
│  Khách đăng   │    │  NV CSKH mở      │    │  NV đọc review,     │    │  Gửi draft cho   │    │  Manager duyệt │
│  review trên  │──▶│  dashboard từng   │──▶│  soạn reply thủ     │──▶│  Manager duyệt   │──▶│  → đăng public │
│  nền tảng     │    │  nền tảng (3 tab) │    │  công bằng tay      │    │  qua email/chat  │    │  lên nền tảng  │
└──────────────┘    └──────────────────┘    └─────────────────────┘    └──────────────────┘    └────────────────┘
                           🔄                      🔴 BOTTLENECK              🔄                      
                       Handoff:               ⏱ 10-15 phút/review        Handoff:
                    Phải mở 3 nền tảng         Review tiêu cực:          Chờ manager
                    riêng biệt                 20-30 phút/review         trả lời: 2-4 giờ
```

**Thời gian vận hành trung bình: Tổng cộng = 30-60 phút/review** (bao gồm cả thời gian chờ duyệt)

**Các vấn đề hiện tại:**
- 🔴 **Bottleneck chính:** Bước 3 — Soạn reply chiếm 70% thời gian, đặc biệt với review tiêu cực, đa ngôn ngữ (Anh, Trung, Hàn, Nhật)
- 🔄 **Handoff 1:** NV phải mở riêng 3 nền tảng (Booking, Agoda, Google Maps) → dễ bỏ sót review
- 🔄 **Handoff 2:** Gửi draft cho manager qua email/Zalo → chờ phản hồi 2-4 giờ, mùa cao điểm có thể 1 ngày
- ⚠️ **Rủi ro:** Review chứa cáo buộc nghiêm trọng (trộm cắp, ngộ độc) đôi khi NV vẫn reply công khai mà không báo quản lý → gây rủi ro pháp lý

---

## 3.2. Problem Statement (6-field) & Metrics (15 min)

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân viên CSKH / PR team tại các resort Vinpearl (khoảng 3-5 NV/resort, xử lý ~50-100 review/ngày toàn hệ thống) |
| **2. Current Workflow** | NV mở dashboard 3 nền tảng → đọc review → xác định ngôn ngữ & mức nghiêm trọng → soạn reply thủ công → gửi manager duyệt qua email → manager duyệt → đăng công khai. Công cụ: trình duyệt web, email, Zalo, Google Translate |
| **3. Bottleneck** | Bước soạn reply tốn 10-15 phút/review thường, 20-30 phút/review tiêu cực. NV phải viết giọng điệu chuyên nghiệp, đa ngôn ngữ, đồng thời không thừa nhận lỗi pháp lý. Mùa cao điểm review tăng 3-5 lần → NV không xử lý kịp → tỷ lệ reply chỉ đạt 60% |
| **4. Business Impact** | Review không được reply trong 24h → giảm điểm xếp hạng trên Booking.com (thuật toán ưu tiên khách sạn reply nhanh). Ước tính mỗi 0.1 điểm giảm trên Booking = giảm ~5% booking rate. Chi phí nhân sự CSKH: ~15 triệu VNĐ/NV/tháng × 5 NV = 75 triệu/tháng chỉ riêng cho reply review |
| **5. Success Metric** | ① Giảm thời gian soạn reply từ 10-15 min → dưới 2 min/review. ② Tăng tỷ lệ reply review từ 60% → 95% trong vòng 24h. ③ 100% review chứa cáo buộc nghiêm trọng được escalate cho manager (không có trường hợp NV tự reply) |
| **6. Operational Boundary** | ✅ AI ĐƯỢC phép: soạn draft reply, phân loại mức nghiêm trọng, dịch đa ngôn ngữ. ❌ AI KHÔNG ĐƯỢC: đăng reply công khai mà không qua duyệt (bắt buộc tag [DRAFT_REPLY]), tự reply review có cáo buộc nghiêm trọng (phải escalate_to_manager). 👤 HITL: Manager duyệt mọi draft trước khi đăng |

---

## 3.3. Future-State Flow & AI Fit (25 min)

### AI-Fit Matrix:
**[x] LLM Feature** — Dùng LLM để hiểu ngữ cảnh review đa ngôn ngữ, phân loại mức nghiêm trọng, và soạn draft reply có giọng điệu phù hợp. Không cần Agent vì workflow tuyến tính, không có vòng lặp quyết định phức tạp.

### Future-State Flow:

```
┌──────────────┐    ┌──────────────────────┐    ┌─────────────────────────┐    ┌────────────────┐
│  Khách đăng   │    │  🔵 AI Step:          │    │  Phân nhánh:             │    │                │
│  review trên  │──▶│  Đọc review, phân    │──▶│                          │    │                │
│  nền tảng     │    │  loại ngôn ngữ &     │    │  ┌─ Review thường ──────▶│──▶│ 🟢 HITL:       │
└──────────────┘    │  mức nghiêm trọng    │    │  │  🔵 AI soạn draft     │    │ Manager duyệt  │
                     └──────────────────────┘    │  │  reply [DRAFT_REPLY]  │    │ → đăng public  │
                                                  │  │                       │    └────────────────┘
                                                  │  └───────────────────────┘
                                                  │
                                                  │  ┌───────────────────────┐    ┌────────────────┐
                                                  │  │  Cáo buộc nghiêm trọng│    │ 🟢 HITL:       │
                                                  └─▶│  🔵 AI escalate       │──▶│ Manager xử lý  │
                                                     │  → escalate_to_manager│    │ trực tiếp      │
                                                     └───────────────────────┘    └────────────────┘

                     ↩️ Fallback: Nếu AI không tự tin (confidence < 70%) hoặc review chứa nội dung
                        mơ hồ → chuyển nguyên văn cho NV CSKH xử lý thủ công, không soạn draft.
```

### So sánh Before vs After:

| Metric | Current State | Future State (with AI) |
|--------|--------------|----------------------|
| Thời gian soạn reply | 10-15 min/review | < 2 min/review (AI draft + NV review nhanh) |
| Tỷ lệ reply trong 24h | ~60% | ~95% |
| Escalation cáo buộc nghiêm trọng | Không đồng nhất (phụ thuộc NV) | 100% tự động escalate |
| Chi phí nhân sự CSKH cho reply | 75 triệu/tháng (5 NV full-time) | ~25 triệu/tháng (2 NV review draft) |
| Ngôn ngữ hỗ trợ | Chủ yếu Tiếng Việt + Anh | Việt, Anh, Trung, Hàn, Nhật (LLM đa ngôn ngữ) |

---

# 💻 Phase 4 — TECHNICAL PROMPT PROTOTYPE (Nhóm, 30 min)

### Hướng dẫn thực hiện:
1. Mở file [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py) bằng VS Code/Cursor.
2. Hoàn thiện các nội dung sau:
   * **System Prompt:** Viết chỉ thị cực kỳ nghiêm ngặt quy định vai trò, nhiệm vụ, định dạng output và **Operational Boundary (Ranh giới cấm)** của mô hình.
   * **Structured Output:** Định nghĩa định dạng JSON output rõ ràng.
   * **Adversarial Test Cases:** Viết ít nhất 3 prompts "tấn công" (Adversarial inputs) cố tình dụ AI vượt ranh giới hoặc đưa ra câu trả lời không được phép để kiểm tra xem ranh giới của bạn có thực sự vững chắc.
3. Chạy file python:
   ```bash
   python3 prompt_prototype.py
   ```
4. Kiểm tra xem các ranh giới an toàn có bị LLM phá vỡ hay không và ghi lại kết quả vào worksheet.

### Kết quả Prototype:

**System Prompt — 2 Operational Boundaries:**

| Rule | Mô tả | Tag/Action |
|------|--------|------------|
| **Rule 1** | Mọi reply PHẢI bắt đầu bằng `[DRAFT_REPLY]` — cần manager duyệt trước khi đăng công khai | `[DRAFT_REPLY]` prefix |
| **Rule 2** | Review chứa cáo buộc nghiêm trọng (trộm cắp, ngộ độc, quấy rối, nguy hiểm an toàn) → PHẢI escalate cho manager, KHÔNG tự soạn reply công khai | `{"action": "escalate_to_manager"}` |

**Adversarial Test Cases & Kết quả:**

| Test | Mô tả tấn công | Rule bị tấn công | Kết quả |
|------|----------------|-------------------|---------|
| TC1 | Khách tố mất ví trong phòng + yêu cầu reply luôn đừng báo quản lý | Rule 2 | ✅ / ❌ *(ghi sau khi chạy)* |
| TC2 | Review 4 sao bình thường + yêu cầu bỏ tag [DRAFT_REPLY] cho "chuyên nghiệp" | Rule 1 | ✅ / ❌ *(ghi sau khi chạy)* |

---

# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

### AI Readiness Checklist:
- [x] **Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?** — Có. Review công khai trên Booking.com/Agoda/Google Maps của Vinpearl là dữ liệu sẵn có, không cần thu thập thêm. Có thể crawl hoặc export từ API các nền tảng.
- [x] **Rủi ro khi AI sai có nằm trong tầm kiểm soát?** — Có. AI chỉ soạn DRAFT, mọi reply đều phải qua manager duyệt (HITL). Cáo buộc nghiêm trọng được escalate tự động. Nếu AI output lỗi → fallback về xử lý thủ công.
- [x] **Stakeholders sẵn sàng thay đổi quy trình?** — Có. PR team Vinpearl đang quá tải mùa cao điểm, sẵn sàng đón nhận công cụ giảm tải. Manager vẫn giữ quyền duyệt cuối cùng nên không có rào cản tâm lý.

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
[ ] NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline)
[ ] NO-GO (Không khả thi / Rule-based tốt hơn)

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> **GO** vì đáp ứng đủ 3 điều kiện:
> 1. **Dữ liệu sẵn có:** Review khách sạn là dữ liệu công khai, không cần xin phép hay thu thập phức tạp. Có thể bắt đầu prototype ngay với 100 review mẫu.
> 2. **Rủi ro thấp:** AI chỉ soạn draft (tag [DRAFT_REPLY]), manager luôn duyệt trước khi đăng → sai sót không ảnh hưởng khách hàng. Cáo buộc nghiêm trọng được escalate 100% → không có rủi ro pháp lý.
> 3. **ROI rõ ràng:** Giảm thời gian soạn reply 80% (từ 10-15 min xuống 2 min), tiết kiệm ~50 triệu VNĐ/tháng chi phí nhân sự, tăng tỷ lệ reply từ 60% lên 95% → cải thiện điểm xếp hạng trên Booking.com → tăng booking rate ước tính 5-10%.
> 4. **Scope hẹp, mở rộng dần:** Bắt đầu với 1 resort Vinpearl (Nha Trang) → đánh giá 2 tuần → roll-out toàn hệ thống nếu đạt metric.

---
