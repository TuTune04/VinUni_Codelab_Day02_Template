# Phase 1 & 2 — Problem Scan & Quick Problem Cards

**Họ và tên học viên:** Nguyễn Quốc Tuấn  
**Đơn vị:** Vin Smart Future — AI Engineering Team  
**Mục tiêu:** Quét các cơ hội tối ưu hóa vận hành bằng AI xuyên suốt các công ty thành viên Vingroup và sàng lọc bài toán tiềm năng nhất để Deep-Dive.

---

# 🔍 Phase 1 — SCAN: Bảng Quét Cơ Hội Vận Hành (4 Lenses)

Sử dụng **4 Lenses** (Lặp lại, Tốn thời gian, AI-upgrade, Pain từ người khác) để quét qua các mảng vận hành của Vingroup, phát hiện 5 bài toán thực tế:

| # | Công ty thành viên | Lens áp dụng | Mô tả ngắn bài toán & Nỗi đau vận hành (Bottleneck) |
|---|-------------------|--------------|-----------------------------------------------------|
| 1 | **Vinmec** | **Tốn thời gian** | **Soạn thảo tóm tắt xuất viện (Discharge Summary) & Dặn dò chăm sóc tại nhà:** Bác sĩ điều trị mất 25–35 phút/bệnh nhân để đọc lại toàn bộ bệnh án điện tử (EHR), xét nghiệm máu, chẩn đoán hình ảnh và đơn thuốc nhằm gõ tay bản tóm tắt xuất viện và bản dặn dò cho người nhà. |
| 2 | **VinFast** | **AI-upgrade** | **Chẩn đoán sơ bộ mã lỗi kỹ thuật xe từ mô tả tiếng Việt của khách hàng:** Khách hàng mang xe đến Xưởng dịch vụ (Service Workshop) mô tả lỗi bằng ngôn ngữ đời thường (ví dụ: *"đi qua gờ giảm tốc kêu lục cục ở bánh trước bên phụ"*). Cố vấn dịch vụ ghi chép lộn xộn, kỹ thuật viên mất nhiều giờ chạy thử để mò lỗi. |
| 3 | **Vinhomes** | **Lặp lại** | **Phân loại và điều hướng phản ánh sự cố cư dân trên App Vinhomes Resident:** Hàng nghìn phản ánh mỗi ngày (rò rỉ nước, hỏng đèn hành lang, kẹt thang máy, chó mèo thả rông) cần bộ phận lễ tân ban quản lý đọc thủ công từng tin nhắn để chuyển tiếp cho đội Kỹ thuật, An ninh hoặc Vệ sinh. |
| 4 | **Vinpearl / VinWonders** | **Pain từ người khác** | **Phân tích review tiêu cực & Phản ứng khẩn cấp giải quyết phàn nàn du khách:** Khách hàng đánh giá 1-2 sao hoặc khiếu nại chất lượng phòng/dịch vụ ăn uống. Đội ngũ CSKH mất 6–12 tiếng mới phối hợp xong các phòng ban để phản hồi, dẫn đến việc khách đã check-out và đăng bài bóc phốt trên mạng xã hội. |
| 5 | **VinFast** | **Lặp lại** | **Đối chiếu và so khớp số liệu trạm sạc điện đối tác bên ngoài:** Đội tài chính kế toán phải tải và so khớp thủ công hàng trăm bảng kê giao dịch sạc điện hàng tuần từ các đối tác nhượng quyền trạm sạc với dữ liệu viễn thông từ máy chủ xe điện. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn **Top 3 bài toán** tiềm năng nhất từ danh sách SCAN để phân tích nhanh:

---

## 1: Vinmec — Soạn Thảo Hồ Sơ Tóm Tắt Xuất Viện & Hướng Dẫn Chăm Sóc Tại Nhà (ĐƯỢC CHỌN DEEP-DIVE)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1 (CHỌN DEEP-DIVE)                                      │
│                                                                             │
│ Bài toán (1 câu): Bác sĩ mất quá nhiều thời gian hành chính để tổng hợp     │
│ bệnh án điện tử thành bản tóm tắt xuất viện và hướng dẫn bệnh nhân tại nhà. │
│ Công ty thành viên: [x] Vinmec                                              │
│                                                                             │
│ Ai đang đau (Actor)? Bác sĩ điều trị (quá tải), Điều dưỡng trưởng,          │
│                      Bệnh nhân/Người nhà (chờ đợi lâu để thanh toán).       │
│                                                                             │
│ Workflow thủ công hiện tại (5 bước):                                        │
│   1. Bác sĩ ra quyết định cho bệnh nhân xuất viện.                          │
│   → 2. Mở bệnh án điện tử (EHR), đọc lại kết quả xét nghiệm & diễn tiến.    │
│   → 3. Gõ tay bản Tóm tắt xuất viện y khoa chuẩn mã ICD-10.                 │
│   → 4. Soạn văn bản dặn dò chế độ dinh dưỡng, dùng thuốc và dấu hiệu nguy cơ│
│   → 5. In hồ sơ, ký tay và chuyển phòng Kế toán viện phí xuất viện.         │
│                                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & Bước 4 (⏱ 20-25 phút/bệnh nhân)    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4                            │
│ (AI trích xuất dữ liệu EHR -> Soạn nháp Discharge Summary & Dặn dò tại nhà) │
│                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                       │
│   1. Giảm thời gian soạn thảo hồ sơ từ 30 phút/bệnh nhân ──> dưới 5 phút.   │
│   2. 98% bác sĩ xác nhận bản draft chính xác, không cần viết lại từ đầu.   │
│   3. Tỉ lệ tái nhập viện ngoài ý muốn do dùng sai thuốc giảm 15%.           │
│                                                                             │
│ Quick Architecture: [x] LLM Feature (Kết hợp Human-in-the-loop phê duyệt)   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2: VinFast — Chẩn Đoán Lỗi Xe Từ Ngôn Ngữ Tự Nhiên Khách Hàng

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                       │
│                                                                             │
│ Bài toán (1 câu): Cố vấn dịch vụ không chuẩn hóa được mô tả tiếng Việt đời  │
│ thường của khách thành mã lỗi kỹ thuật chính xác cho thợ sửa chữa.          │
│ Công ty thành viên: [x] VinFast                                             │
│                                                                             │
│ Ai đang đau (Actor)? Cố vấn dịch vụ (Service Advisor), Kỹ thuật viên xưởng. │
│                                                                             │
│ Workflow thủ công hiện tại (4 bước):                                        │
│   1. Tiếp nhận khách lái xe đến xưởng, nghe khách mô tả triệu chứng tiếng lóng│
│   → 2. Cố vấn gõ văn bản tự do vào hệ thống quản trị phiếu dịch vụ (DMS).   │
│   → 3. Thợ sửa chữa nhận phiếu, đọc mô tả mơ hồ và phải lái thử xe tìm lỗi.│
│   → 4. Cắm máy quét OBD tra cứu mã chẩn đoán DTC thủ công.                  │
│                                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 25-40 phút/xe)               │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2                                │
│ (AI phân tích mô tả -> Gợi ý top 3 cụm mã lỗi kỹ thuật & linh kiện nghi ngờ)│
│                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                       │
│   1. Rút ngắn thời gian tiếp nhận và khoanh vùng lỗi từ 30 phút ──> 8 phút. │
│   2. Độ chính xác khớp lỗi ban đầu đạt trên 85%.                            │
│                                                                             │
│ Quick Architecture: [x] LLM Feature (Search Knowledge Base / RAG)           │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3: Vinhomes — Phân Loại & Điều Phối Khẩn Cấp Phản Ánh Cư Dân

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                       │
│                                                                             │
│ Bài toán (1 câu): Phản ánh khẩn cấp của cư dân (kẹt thang máy, tràn nước) bị│
│ trôi lẫn trong hàng nghìn khiếu nại dịch vụ thông thường do phân loại chậm. │
│ Công ty thành viên: [x] Vinhomes                                            │
│                                                                             │
│ Ai đang đau (Actor)? Cư dân (bức xúc), Lễ tân ban quản lý (quá tải).        │
│                                                                             │
│ Workflow thủ công hiện tại (4 bước):                                        │
│   1. Cư dân gửi phản ánh bằng văn bản/ảnh qua App Vinhomes Resident.        │
│   → 2. Lễ tân tòa nhà mở danh sách phản ánh, đọc từng mục và gắn nhãn thủ công│
│   → 3. Gọi bộ đàm hoặc tạo phiếu giao việc cho Kỹ thuật/An ninh/Vệ sinh.   │
│   → 4. Gõ tin nhắn phản hồi tiếp nhận gửi lại cư dân.                       │
│                                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 (⏱ Mất 2-4 tiếng trong giờ cao điểm)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 4                            │
│ (AI phân loại mức độ khẩn cấp P1-P4 -> Điều phối tự động -> Soạn phản hồi)  │
│                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                       │
│   1. Sự cố P1 (đe dọa an toàn) được điều phối dưới 60 giây (trước đây 15p). │
│   2. Độ chính xác phân loại bộ phận xử lý đạt 92%.                          │
│                                                                             │
│ Quick Architecture: [x] Rule + LLM Classifier                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Quyết Định Lựa Chọn Của Nhóm

Nhóm quyết định chọn **Bài toán #1 — Vinmec Discharge Co-pilot** để tiến hành **Deep-Dive** (Phase 3) vì các lý do chiến lược sau:
1. **Giá trị kinh tế & vận hành vượt trội:** Giảm áp lực hành chính trực tiếp cho đội ngũ y bác sĩ chất lượng cao của Vinmec, cho phép bác sĩ dành nhiều thời gian hơn để cứu chữa và chăm sóc bệnh nhân.
2. **Tính chất an toàn nghiêm ngặt (Operational Boundary):** Lĩnh vực y tế đòi hỏi ranh giới trách nhiệm cực kỳ chặt chẽ giữa AI và Bác sĩ (Human-in-the-loop), đây là cơ hội tốt nhất để thể hiện năng lực thiết kế hệ thống AI có trách nhiệm và tin cậy theo đúng chuẩn mực của Vin Smart Future.
3. **Tính khả thi kỹ thuật:** Dữ liệu hồ sơ bệnh án EHR có cấu trúc và trường thông tin chuẩn y khoa, cực kỳ phù hợp để LLM trích xuất, tóm tắt và chuyển hóa thành ngôn ngữ dễ hiểu.
