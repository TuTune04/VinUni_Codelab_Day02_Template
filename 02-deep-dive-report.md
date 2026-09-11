# Báo Cáo Phân Tích Chuyên Sâu (Deep-Dive Report)
## Dự án: Vinmec Discharge Co-pilot — Trợ lý Soạn thảo Hồ sơ Tóm tắt Xuất viện & Hướng dẫn Chăm sóc Tại nhà

**Đơn vị thực hiện:** AI Product Engineering — Vin Smart Future  
**Công ty thành viên thụ hưởng:** Hệ thống Y tế Vinmec (Bệnh viện Đa khoa Quốc tế Vinmec)  
**Nhóm tác giả:** Nguyễn Quốc Tuấn & Cộng sự  

---

## 🏛️ 1. Bối cảnh Vận hành & Nỗi đau Thực tế tại Vinmec

Tại Bệnh viện Đa khoa Quốc tế Vinmec (Hà Nội & TP.HCM), mỗi ngày có trung bình từ 40 đến 60 bệnh nhân nội trú hoàn tất đợt điều trị và làm thủ tục xuất viện tại mỗi khoa lâm sàng (Nội, Ngoại, Nhi, Tim mạch). 

Để một bệnh nhân có thể hoàn tất viện phí và rời viện an toàn, bác sĩ điều trị và điều dưỡng trưởng phải hoàn thiện **Hồ sơ Tóm tắt Xuất viện (Discharge Summary)** và **Bản Hướng dẫn Chăm sóc Tại nhà (Patient Home-Care Guide)**.

Tuy nhiên, khảo sát thực tế tại các khoa lâm sàng cho thấy:
* **Gánh nặng hành chính khổng lồ:** Bác sĩ mất trung bình **30 phút/bệnh nhân** chỉ để đọc lại lịch sử bệnh án điện tử (EHR), đối chiếu 15–30 chỉ số xét nghiệm sinh hóa, ảnh chụp X-quang, đọc đơn thuốc và gõ tay văn bản tóm tắt.
* **Ngôn ngữ y khoa phức tạp gây hiểu lầm:** Bản dặn dò xuất viện hiện tại thường chứa nhiều thuật ngữ chuyên môn hoặc viết vội, dẫn đến việc người nhà bệnh nhân uống nhầm liều thuốc hoặc không nhận diện kịp thời các dấu hiệu chuyển biến nguy hiểm tại nhà, làm tăng tỉ lệ tái nhập viện trong 30 ngày đầu.
* **Thời gian chờ đợi viện phí kéo dài:** Khâu tóm tắt bệnh án bị chậm trễ kéo theo việc phòng Kế toán không thể chốt viện phí, khiến bệnh nhân phải chờ từ 3–5 tiếng trong ngày xuất viện.

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow Mapping (Quy trình Hiện tại)

Quy trình 5 bước thực hiện thủ công hiện nay của Bác sĩ điều trị và Điều dưỡng Vinmec:

```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Bước 1          │       │ Bước 2          │       │ Bước 3          │       │ Bước 4          │
│ Quyết định      │       │ Đọc và tổng hợp │       │ Soạn Tóm tắt    │       │ Soạn Dặn dò     │
│ cho xuất viện   │ ───-> │ dữ liệu thô EHR │ ───-> │ Y khoa (ICD-10) │ ───-> │ Chăm sóc tại nhà│
│                 │       │                 │       │                 │       │                 │
│ Ai: Bác sĩ điều │       │ Ai: Bác sĩ điều │       │ Ai: Bác sĩ điều │       │ Ai: Bác sĩ /    │
│ trị             │       │ trị             │       │ trị             │       │ Điều dưỡng      │
│ ⏱ 3 phút        │       │ ⏱ 8 phút 🔴     │       │ ⏱ 12 phút 🔴    │       │ ⏱ 7 phút        │
│ In: Thăm khám   │       │ In: EHR, Labs   │       │ In: Dữ liệu thô │       │ In: Đơn thuốc   │
│ Out: Lệnh xuất  │       │ Out: Ghi chú nháp│      │ Out: Discharge  │       │ Out: Bản hướng  │
│ viện            │       │                 │       │ Summary y khoa  │       │ dẫn bệnh nhân   │
└─────────────────┘       └─────────────────┘       └─────────────────┘       └─────────────────┘
                                                                                       │
                                                                                       ▼ 🔄 Handoff
                                                                              ┌─────────────────┐
                                                                              │ Bước 5          │
                                                                              │ In, Ký duyệt và │
                                                                              │ chuyển Kế toán  │
                                                                              │                 │
                                                                              │ Ai: Bác sĩ &    │
                                                                              │ Điều dưỡng      │
                                                                              │ ⏱ 3 phút        │
                                                                              │ Out: Hồ sơ giấy │
                                                                              └─────────────────┘

🔴 = Bottlenecks (Bước 2 và 3 chiếm tới 20 phút vì phải rà soát dữ liệu thô và gõ tay văn bản)
🔄 = Handoff (Chuyển giao giữa Bác sĩ sang Điều dưỡng và Phòng Kế toán viện phí)
⏱ TỔNG THỜI GIAN VẬN HÀNH THỦ CÔNG: 33 phút / bệnh nhân.
```

---

## 3.2. Problem Statement (6-field) — Vin Smart Future Standard

| Trường thông tin (Field) | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Bác sĩ điều trị lâm sàng và Điều dưỡng trưởng tại các khoa nội trú Bệnh viện Đa khoa Quốc tế Vinmec. |
| **2. Current Workflow** | Sau khi khám kết luận cho bệnh nhân xuất viện, bác sĩ mở hệ thống phần mềm Bệnh án điện tử (EHR), lần giở lịch sử điều trị nhiều ngày, đọc thủ công các kết quả xét nghiệm huyết học, sinh hóa, hình ảnh X-quang/CT và đơn thuốc đã kê. Bác sĩ gõ tay bản Tóm tắt bệnh án y khoa kèm mã ICD-10, sau đó soạn bản dặn dò dùng thuốc và chế độ ăn uống cho bệnh nhân. Mất trung bình 30–35 phút/bệnh nhân. |
| **3. Bottleneck** | **Bước 2 và Bước 3:** Tốn 20 phút để tổng hợp thông tin phân tán từ nhiều tab phần mềm và gõ văn bản tóm tắt lặp đi lặp lại. Bác sĩ thường xuyên bị ngắt quãng bởi các ca cấp cứu đột xuất, dẫn đến việc bản tóm tắt bị chậm trễ hoặc viết tắt gây khó hiểu. |
| **4. Business Impact** | Mỗi bác sĩ phụ trách 10–15 ca xuất viện/tuần, gây lãng phí khoảng **120–150 giờ làm việc hành chính mỗi tháng** tại mỗi khoa. Bệnh nhân bức xúc vì phải chờ đợi thủ tục xuất viện từ sáng tới trưa. Tỉ lệ tái nhập viện trong 30 ngày do bệnh nhân không tuân thủ đúng đơn thuốc và chế độ chăm sóc tại nhà ước tính gây thất thoát ~8% chi phí quản trị chất lượng y tế của Vinmec. |
| **5. Success Metric** | **1. Hiệu suất (Efficiency):** Giảm thời gian bác sĩ soạn thảo hồ sơ từ 33 phút xuống **dưới 5 phút / bệnh nhân**.<br>**2. Chất lượng (Clinical Quality):** 98% bản tóm tắt trích xuất chính xác chẩn đoán và thuốc, được bác sĩ điều trị xác nhận.<br>**3. Trải nghiệm người bệnh (Patient Experience):** 100% bệnh nhân nhận được bản hướng dẫn dễ hiểu bằng tiếng Việt (đạt chuẩn đọc hiểu Flesch-Kincaid mức phổ thông); giảm 15% tỉ lệ tái nhập viện ngoài ý muốn. |
| **6. Operational Boundary (Ranh giới an toàn)** | **QUYỀN HẠN CỦA AI:** AI được phép trích xuất dữ liệu EHR (kết quả xét nghiệm, lịch sử dùng thuốc, chẩn đoán ban đầu), chuẩn hóa mã ICD-10, dịch thuật ngữ chuyên môn sang ngôn ngữ phổ thông, và tự động soạn bản thảo dạng nháp.<br>⛔ **RANH GIỚI CẤM (STRICT BOUNDARY):**<br>1. AI **TUYỆT ĐỐI KHÔNG ĐƯỢC** tự ý thay đổi loại thuốc, đổi liều lượng hoặc thêm bớt bất kỳ chỉ định y khoa nào ngoài dữ liệu đã có trong EHR.<br>2. Mọi văn bản do AI sinh ra bắt buộc phải mang tiền tố `[DRAFT_FOR_PHYSICIAN_REVIEW]`.<br>3. Hệ thống cấm không được tự động xuất file PDF có chữ ký số ra cổng thanh toán hoặc gửi cho bệnh nhân nếu **chưa có xác nhận và chữ ký điện tử trực tiếp của Bác sĩ điều trị (Bắt buộc Human-in-the-loop 100%)**. |

---

## 3.3. Future-State Flow & AI Fit (Quy trình Tương lai có AI)

### Phân tích AI-Fit Matrix:
* **Rule-based:** Không phù hợp vì dữ liệu bệnh án ghi chú lâm sàng là ngôn ngữ tự nhiên không đồng nhất, diễn đạt theo phong cách của từng bác sĩ.
* **Agentic Loop (Agent tự trị):** Rủi ro y khoa quá lớn, luật khám chữa bệnh không cho phép hệ thống tự động đưa ra quyết định độc lập.
* 👉 **LỰA CHỌN TỐI ƯU: LLM Feature (Co-pilot với Human-in-the-loop)**. Mô hình LLM đóng vai trò là "Thư ký y khoa thông minh", chỉ đọc và soạn nháp, con người giữ toàn quyền quyết định.

### Quy trình Tương lai (Future-State Workflow):

```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Bước 1          │       │ Bước 2          │       │ Bước 3          │       │ Bước 4          │
│ Bác sĩ click    │       │ 🔵 AI Auto-Pull │       │ 🔵 AI Draft     │       │ 🟢 Bác sĩ       │
│ nút "Đề xuất    │ ───-> │ EHR Data &      │ ───-> │ Discharge &     │ ───-> │ Review & Ký số  │
│ Xuất Viện"      │       │ Lab Results     │       │ Home-Care Guide │       │ (HITL - 3 phút) │
│ (10 giây)       │       │ (5 giây)        │       │ (10 giây)       │       │                 │
└─────────────────┘       └─────────────────┘       └─────────────────┘       └─────────────────┘
                                                                                       │
                                                                                       ▼ 🔄 Handoff
                                                                              ┌─────────────────┐
                                                                              │ Bước 5          │
                                                                              │ Tự động đồng    │
                                                                              │ bộ Kế toán &    │
                                                                              │ Gửi App Vinmec  │
                                                                              │ (Tức thì)       │
                                                                              └─────────────────┘
                                                                                       │
                                                                                       ▼
                                                                              ↩️ FALLBACK:
                                                                              Nếu AI sinh lỗi
                                                                              hoặc thông tin
                                                                              EHR thiếu dữ liệu,
                                                                              hệ thống cảnh báo đỏ;
                                                                              Bác sĩ chuyển sang
                                                                              gõ tay truyền thống.

🔵 = Bước do AI / Tự động hóa xử lý
🟢 = Bước Bác sĩ phê duyệt (Human-in-the-loop)
↩️ = Kế hoạch dự phòng (Fallback)
⏱ TỔNG THỜI GIAN QUY TRÌNH MỚI: ~ 4 PHÚT / BỆNH NHÂN (Giảm 88% thời gian).
```

---

# 🏁 Phase 5 — EVALUATE & DECISION

### AI Readiness Checklist:
1. **[x] Dữ liệu mẫu/logs sạch để test:** Bệnh viện Vinmec sử dụng hệ thống EHR chuẩn quốc tế (JCI standard), dữ liệu khám chữa bệnh có định dạng số hóa rõ ràng.
2. **[x] Rủi ro khi AI sai nằm trong tầm kiểm soát:** Toàn bộ bản thảo đều có nhãn `[DRAFT_FOR_PHYSICIAN_REVIEW]`, bắt buộc bác sĩ đọc lướt và ký số xác nhận trước khi phát hành. Có nút khôi phục viết tay (Fallback).
3. **[x] Stakeholders sẵn sàng thay đổi quy trình:** Các bác sĩ đang cực kỳ mệt mỏi với giấy tờ hành chính và Ban Giám Đốc Vinmec đang ưu tiên chuyển đổi số y tế toàn diện.

---

### Quyết định Cuối Cùng của Ban Giám Đốc Vin Smart Future:

# 🟢 **QUYẾT ĐỊNH: GO (Bắt đầu xây dựng MVP Prototype)**

### Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật & hiệu quả đầu tư):
1. **Hiệu quả kinh tế (ROI) rõ rệt:** Tiết kiệm hơn 1.200 giờ làm việc/tháng cho toàn bộ khối bác sĩ nội trú tại một cơ sở bệnh viện Vinmec, tương đương giải phóng sức lao động trị giá hàng trăm triệu đồng/tháng để chuyển sang phục vụ chuyên môn khám chữa bệnh.
2. **Kiến trúc công nghệ an toàn, chi phí thấp:** Không cần xây dựng hệ thống Agent tự trị phức tạp; chỉ cần áp dụng mô hình LLM Feature kết hợp RAG (Retrieval-Augmented Generation) trên dữ liệu EHR nội bộ.
3. **Tuân thủ pháp lý y tế nghiêm ngặt:** Thiết kế Human-in-the-loop 100% giúp Vinmec hoàn toàn tuân thủ các quy định về an toàn y tế của Bộ Y tế và tiêu chuẩn quốc tế JCI.

---

## 💻 Ranh Giới An Toàn trong Lập Trình Prompt Prototype (Prompt Boundary)

Trong quá trình lập trình thử nghiệm tại [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py), nhóm kỹ sư Vin Smart Future đã cài đặt các ràng buộc an toàn cốt lõi:
* Mọi phản hồi draft của mô hình đều phải giữ vững thẻ cảnh báo bản thảo.
* Kiểm soát các ngưỡng an toàn khẩn cấp, ngăn chặn người dùng ép mô hình phá vỡ quy chuẩn vận hành.
* Các ca kiểm thử tấn công (Adversarial Tests) đã chứng minh hệ thống từ chối mọi yêu cầu vượt ranh giới an toàn.
