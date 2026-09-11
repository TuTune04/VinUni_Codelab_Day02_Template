# 🔍 Phase 1 — SCAN (Cá nhân)

### 📝 List bài toán của tôi:
| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|-------------------------------------------------------------|---------------------|
| 1 | **Vinmec × Xanh SM × Vinhomes** | Repetitive / Time-consuming / AI-upgrade / Stakeholder Pain | **Điều phối khám và giảm no-show:** Dự đoán bệnh nhân vắng mặt/đến muộn, tự động nhắc lịch, hỗ trợ đổi lịch, lấp slot trống và kết hợp điều phối Xanh SM cho bệnh nhân cần di chuyển. |
| 2 | **Vinmec** | Repetitive / Time-consuming / AI-upgrade / Stakeholder Pain | **Ambient AI Scribe và chuẩn hóa bệnh án:** Chuyển hội thoại khám bệnh thành văn bản, tạo bản nháp bệnh án/tóm tắt/chỉ định để bác sĩ kiểm tra và phê duyệt. |
| 3 | **Vinmec** | Repetitive / Time-consuming / AI-upgrade / Stakeholder Pain | **Điều phối luồng bệnh nhân xuyên khoa:** Dự báo thời gian chờ và tình trạng quá tải tại khám, xét nghiệm, CĐHA, thanh toán, nhà thuốc; tối ưu routing và hàng đợi theo thời gian thực. |
| 4 | **Vinmec** | Repetitive / Time-consuming / AI-upgrade / Stakeholder Pain | **Ưu tiên đọc phim và theo dõi kết quả bất thường:** AI ưu tiên worklist CĐHA, theo dõi ca bất thường/kết quả chưa được xác nhận và tạo quy trình closed-loop từ phát hiện đến xử lý. |
| 5 | **Vinmec × Xanh SM × Vinhomes** | Repetitive / Time-consuming / AI-upgrade / Stakeholder Pain | **Tối ưu xuất viện, giường bệnh và hậu xuất viện:** Dự báo thời điểm sẵn sàng xuất viện, theo dõi task còn thiếu, dự báo giường trống và kết nối vận chuyển/chăm sóc sau xuất viện. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân)

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Chuyển hội thoại khám bệnh thành văn bản, │
│ tạo bản nháp bệnh án tự động để bác sĩ kiểm tra và duyệt.   │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ lâm sàng / Thư ký y khoa.       │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Vừa khám vừa ghi chép tay/nhớ ──> 2. Gõ lại triệu      │
│   chứng vào hệ thống EMR ──> 3. Lên chỉ định cận lâm sàng   │
│   ──> 4. Hoàn thiện và ký hồ sơ.                            │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 và Bước 4 do phải   │
│ phân tâm giữa bệnh nhân và màn hình máy tính (⏱ 5-8 phút/ca).│
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Thu âm hội thoại      │
│ (Bước 1), tự động transcribe và cấu trúc hóa thành bệnh án  │
│ chuẩn (SOAP) để bác sĩ chỉ cần review (Bước 2, 4).          │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian nhập   │
│ liệu hệ thống EMR từ 8 phút ──> dưới 2 phút/ca.             │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Dự báo thời gian chờ và tối ưu định tuyến │
│ bệnh nhân xuyên khoa theo thời gian thực (real-time).       │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Bệnh nhân / Điều phối viên sảnh.       │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. In phiếu thứ tự ──> 2. Bệnh nhân tự tìm đến các phòng  │
│   xét nghiệm/CĐHA ──> 3. Xếp hàng chờ thụ động ──> 4. NV    │
│   điều phối chạy tay hoặc gọi loa khi có phòng trống.       │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (Chờ đợi vô định)   │
│ và Bước 4 (Điều phối thủ công cục bộ) (⏱ 15-30 phút/lượt chờ).│
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? AI thu thập data tải  │
│ các phòng (real-time) và tính toán thuật toán xếp hàng      │
│ (Bước 3, 4) để tự động push thông báo phòng trống lên App.  │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian chờ    │
│ rảnh (idle time) của bệnh nhân từ 30 phút ──> dưới 10 phút. │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Dự đoán bệnh nhân vắng mặt (no-show), tự  │
│ động lấp slot trống và kết hợp gọi xe Xanh SM di chuyển.    │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [x] Vinhomes  │
│                     [x] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Quản lý phòng khám / Tổng đài viên.    │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Bệnh nhân đặt lịch ──> 2. NV gọi điện confirm trước 1  │
│   ngày ──> 3. Nếu khách hủy sát giờ, slot bị bỏ trống ──>   │
│   4. Khách đến muộn làm xô lệch lịch của bác sĩ.            │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 (Gọi điện thủ công) │
│ và Bước 3 (Tài nguyên bác sĩ bị lãng phí) (⏱ 30 phút/ca).   │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Dự báo tỷ lệ no-show  │
│ để overbook an toàn, dùng Agent tự động nhắn tin nhắc lịch  │
│ và gợi ý xe Xanh SM đón tận nơi (Bước 2, 3).                │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm tỷ lệ No-show    │
│ phòng khám từ 15% ──> dưới 5%.                              │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent │
└─────────────────────────────────────────────────────────────┘