# Báo Cáo Phân Tích Chuyên Sâu (Deep-Dive Report)



## Dự án: Vinmec Ambient AI Scribe — Trợ lý Lắng nghe & Tự động Soạn thảo Bệnh án Lâm sàng

**Đơn vị thực hiện:** AI Product Engineering — Vin Smart Future

**Công ty thành viên thụ hưởng:** Hệ thống Y tế Vinmec (Phòng khám Ngoại trú)

**Nhóm tác giả:** Đinh Công Tú

---

## 🏛️ 1. Bối cảnh Vận hành & Nỗi đau Thực tế tại Vinmec



Tại các phòng khám ngoại trú của hệ thống Vinmec, mỗi bác sĩ lâm sàng thường phải tiếp nhận từ 30 đến 40 ca khám mỗi ngày. Khối lượng công việc lớn đòi hỏi sự tập trung cao độ, nhưng quy trình hiện tại đang bộc lộ nhiều điểm nghẽn:

* **Gánh nặng nhập liệu (Screen-gazing):** Bác sĩ phải liên tục chuyển sự chú ý giữa việc lắng nghe bệnh nhân và gõ phím nhập liệu vào hệ thống EMR (Bệnh án điện tử), tiêu tốn trung bình 5-8 phút cho mỗi ca.
* **Đứt gãy sự thấu cảm (Empathy Gap):** Việc phải nhìn vào màn hình máy tính khiến bác sĩ mất đi giao tiếp bằng mắt (eye-contact) với bệnh nhân, làm giảm trải nghiệm dịch vụ y tế chuẩn quốc tế.
* **Nguy cơ kiệt sức (Burn-out):** Thao tác gõ lặp đi lặp lại các triệu chứng, tiền sử bệnh và chỉ định gây mệt mỏi về thể chất và tâm lý cho đội ngũ y khoa vào cuối ngày làm việc.

---

# 🏗️ Phase 3 — DEEP-DIVE



## 3.1. Current-State Workflow Mapping (Quy trình Hiện tại)



Quy trình 4 bước khám và ghi chép thủ công hiện nay tại phòng khám:

```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Bước 1          │       │ Bước 2          │       │ Bước 3          │       │ Bước 4          │
│ Khám lâm sàng & │       │ Gõ tay triệu    │       │ Lên chỉ định    │       │ Hoàn thiện & Ký │
│ Hội thoại với BN│ ───-> │ chứng vào EMR   │ ───-> │ Cận lâm sàng /  │ ───-> │ duyệt hồ sơ     │
│                 │       │                 │       │ Đơn thuốc       │       │                 │
│ Ai: Bác sĩ      │       │ Ai: Bác sĩ      │       │ Ai: Bác sĩ      │       │ Ai: Bác sĩ      │
│ ⏱ 5-10 phút     │       │ ⏱ 5-8 phút 🔴   │       │ ⏱ 2-3 phút      │       │ ⏱ 1 phút        │
│ In: Lời kể BN   │       │ In: Trí nhớ BS  │       │ In: Chẩn đoán   │       │ In: Nháp EMR    │
│ Out: Đánh giá   │       │ Out: Note SOAP  │       │ Out: Lệnh y tế  │       │ Out: EMR lưu trữ│
└─────────────────┘       └─────────────────┘       └─────────────────┘       └─────────────────┘

🔴 = Bottleneck (Bước 2 chiếm nhiều thời gian tĩnh, bác sĩ phải nhớ lại toàn bộ ngữ cảnh hội thoại)
⏱ TỔNG THỜI GIAN VẬN HÀNH THỦ CÔNG: ~ 15-22 phút / ca khám.

```

---

## 3.2. Problem Statement (6-field) — Vin Smart Future Standard



| Trường thông tin (Field)

 | Nội dung chi tiết |
| --- | --- |
| **1. Actor / Operator**<br> | Bác sĩ lâm sàng tại các phòng khám ngoại trú Vinmec. |
| **2. Current Workflow**<br> | Trong và sau khi giao tiếp với bệnh nhân, bác sĩ phải quay sang màn hình máy tính để gõ lại toàn bộ phàn nàn chính, tiền sử bệnh, và các dấu hiệu lâm sàng vào hệ thống EMR theo cấu trúc SOAP (Subjective, Objective, Assessment, Plan). |
| **3. Bottleneck**<br> | **Bước 2:** Nhập liệu thủ công làm gián đoạn luồng suy nghĩ lâm sàng, dễ bỏ sót chi tiết nhỏ do phụ thuộc vào trí nhớ ngắn hạn. |
| **4. Business Impact**<br> | Giảm công suất phòng khám (số ca/ngày); tăng chi phí overtime; điểm hài lòng của bệnh nhân (CSAT) bị ảnh hưởng do cảm giác "bác sĩ chỉ lo nhìn máy tính". |
| **5. Success Metric**<br> | **1. Hiệu suất:** Giảm thời gian nhập liệu EMR từ 8 phút xuống **dưới 2 phút / ca khám**.<br>

<br>**2. Chất lượng:** Độ chính xác trích xuất thực thể y khoa (NER) đạt > 95%. |
| **6. Operational Boundary (Ranh giới an toàn)**<br> | **QUYỀN HẠN CỦA AI:** Thu âm hội thoại thực tế (Ambient listening), chuyển đổi Speech-to-Text (STT), và dùng LLM tóm tắt, map thông tin vào các trường EMR.<br>

<br>⛔ **RANH GIỚI CẤM:**<br>

<br>1. AI **TUYỆT ĐỐI KHÔNG ĐƯỢC** tự động đưa ra Chẩn đoán xác định (Diagnosis) hoặc tự ý kê đơn thuốc mới.<br>

<br>2. Toàn bộ văn bản tạo ra phải hiển thị dưới dạng nháp (Draft).<br>

<br>3. Bắt buộc có thao tác xác nhận, chỉnh sửa và lưu (Human-in-the-loop) từ bác sĩ trước khi đồng bộ vào hệ thống EMR chính thức.

 |

---

## 3.3. Future-State Flow & AI Fit (Quy trình Tương lai có AI)



### Phân tích AI-Fit Matrix:

* **Rule-based:** Không thể giải quyết vì hội thoại y khoa rất tự nhiên, lộn xộn, chứa nhiều nhiễu và từ địa phương.
* **Agentic Loop:** Không cần thiết và rủi ro cao vì không cần AI tự động thực thi các action ra bên ngoài.
* 👉 **LỰA CHỌN TỐI ƯU: LLM Feature (Ambient Scribe với RAG & Local Deployment)**. Cấu trúc này ứng dụng mô hình nhận diện giọng nói kết hợp LLM khả năng xử lý ngữ cảnh dài (long-context). Để đảm bảo quyền riêng tư dữ liệu y tế, các mô hình xử lý ngôn ngữ nhỏ gọn nhưng sắc bén có thể được deploy nội bộ (local deployment qua các runtime engine tối ưu hóa VRAM) kết hợp với kỹ thuật Retrieval-Augmented Generation (RAG) để tham chiếu danh mục thuốc của viện.

### Quy trình Tương lai (Future-State Workflow):

```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Bước 1          │       │ Bước 2          │       │ Bước 3          │       │ Bước 4          │
│ Khám & Bật app  │       │ 🔵 AI STT &     │       │ 🟢 Bác sĩ       │       │ Hoàn thiện      │
│ ghi âm nền      │ ───-> │ Draft SOAP Note │ ───-> │ Review & Edit   │ ───-> │ Chỉ định & Lưu  │
│ (0 giây extra)  │       │ (real-time)     │       │ (HITL - 1 phút) │       │ (1 phút)        │
└─────────────────┘       └─────────────────┘       └─────────────────┘       └─────────────────┘
                                                                                       │
                                                                                       ▼
                                                                              ↩️ FALLBACK:
                                                                              Nếu nhận diện 
                                                                              giọng nói lỗi 
                                                                              do ồn, bác sĩ 
                                                                              chủ động gõ tay 
                                                                              như cũ.

🔵 = Bước do AI xử lý[cite: 3]
🟢 = Bước Bác sĩ phê duyệt (Human-in-the-loop)[cite: 3]
↩️ = Kế hoạch dự phòng (Fallback)[cite: 3]
⏱ TỔNG THỜI GIAN NHẬP LIỆU: ~ 2 PHÚT / CA (Tiết kiệm tới 75% thời gian tương tác với máy tính).

```

---

# 🏁 Phase 5 — EVALUATE & DECISION



### AI Readiness Checklist

:

1. **[x] Dữ liệu mẫu/logs sạch để test:** Có sẵn kho dữ liệu audio mô phỏng và form mẫu bệnh án SOAP của Vinmec.


2. **[x] Rủi ro khi AI sai nằm trong tầm kiểm soát:** Hệ thống chỉ soạn nháp; bác sĩ là người chịu trách nhiệm cuối cùng khi bấm "Lưu".


3. **[x] Stakeholders sẵn sàng thay đổi quy trình:** Hội đồng y khoa và các bác sĩ rất ủng hộ việc áp dụng công nghệ để giảm tải hành chính.



### Quyết định Cuối Cùng của Ban Giám Đốc Vin Smart Future:



# 🟢 **QUYẾT ĐỊNH: GO (Bắt đầu xây dựng Prototype)**

### Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):



Giải pháp **Ambient AI Scribe** đáp ứng chính xác nhu cầu cốt lõi của ngành y tế hiện đại: trả lại thời gian cho bác sĩ để chăm sóc bệnh nhân thay vì làm thủ tục hành chính. Về mặt kỹ thuật, việc triển khai các mô hình LLM tại chỗ xử lý ngữ cảnh dài hoàn toàn khả thi với hạ tầng hiện tại, ngăn chặn tuyệt đối rủi ro rò rỉ dữ liệu lên cloud công cộng. Chi phí đầu tư hạ tầng máy chủ cục bộ sẽ được hoàn vốn nhanh chóng thông qua việc tăng công suất khám bệnh (thêm 3-5 ca/bác sĩ/ngày) và nâng cao đáng kể chỉ số hài lòng khách hàng cao cấp của Vinmec.