# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

### 📝 List bài toán của tôi (hoàn chỉnh)

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | Vinmec – Quầy tiếp đón/Thu ngân | Lặp lại | Đối soát & soạn công văn bảo lãnh viện phí (LOG) với hàng chục hãng bảo hiểm thương mại/quốc tế khác nhau |
| 2 | Vinmec – Điều dưỡng nội trú | Lặp lại | Bàn giao ca trực (handover) 3 lần/ngày/khoa vẫn ghi tay hoặc gõ lại thủ công |
| 3 | VinFast – Trung tâm dịch vụ / Bảo hành | AI có thể tốt hơn | Đánh giá mức độ hư hại & tính hợp lệ bảo hành từ ảnh/video khách hàng gửi. Kỹ thuật viên phải xem thủ công từng bộ ảnh/video để phân loại lỗi (do người dùng / lỗi sản xuất / hao mòn tự nhiên) và ước lượng chi phí sửa chữa — không thể scale khi số yêu cầu bảo hành tăng theo doanh số xe |
| 4 | Vinhomes – Ban quản lý đô thị | Tốn thời gian + Pain từ Stakeholder | Phân loại & định tuyến khiếu nại cư dân đa kênh (app, hotline, email, trực tiếp). Nhân viên CSKH đọc và gán nhãn thủ công từng phản ánh (kỹ thuật, an ninh, vệ sinh, phí dịch vụ, thái độ nhân viên…), thường xuyên định tuyến sai gây "đùn đẩy trách nhiệm" và làm cư dân bức xúc |
| 5 | Xanh SM – Trung tâm điều phối | Lặp lại + Pain từ Stakeholder | Điều phối & gán chuyến thủ công khi thuật toán tự động thất bại. Khi tài xế từ chối đơn hoặc không có xe trong bán kính, đội vận hành phải can thiệp: kiểm tra bản đồ, gọi điện thuyết phục, gán tay. Tài xế phàn nàn vì bị gán chuyến xa, khách phàn nàn |

---
# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1__                                      │
│                                                             │
│ Bài toán (1 câu): Nhân viên tiếp đón/thu ngân phải tra cứu   │
│ và đối chiếu tay quyền lợi bảo lãnh viện phí với hàng chục   │
│ hãng bảo hiểm khác nhau cho mỗi ca nhập/xuất viện.  │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [X] Vinmec   [ ] Khác (Ghi rõ)_________  │
│                                                             │
│ Ai đang đau? (Nhân viên, Khách hàng, Cấp trên...) Nhân viên tiếp đón &                                                            |
thu ngân, kế toán bảo hiểm — gián tiếp là khách hàng phải chờ ở quầy   │
│                                                                │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                       │
│   1. Khách đưa thẻ bảo hiểm_______  │
│   2. NV tra hạn mức chi trả qua portal/gọi điện riêng từng hãng___  │
│   3. Soạn công văn bảo lãnh (LOG) theo mẫu riêng hãng đó____  │
│   4. Xuất viện, đối chiếu lại lần 2 để chốt số tiền thực tế     │
│   5. _____________________________________________________  │
│                                                             │
│ Bước nào tốn nhất? Bước 2(⏱ 20 - 30 phút/lượt) _____________________   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3 — đọc thẻ + │
│ policy wording, đối chiếu rule hạn mức, soạn nháp LOG ____  │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?"Giảm thời gian |
|xử lý bảo lãnh từ ~30 min ──> under 5 min;giảm tỷ lệ hồ sơ |
|bị hãng bảo hiểm 'query' bổ sung chứng từ   │
│                                                             │
│ Quick Architecture: [X] Rule | [X] LLM | [ ] Agent Feature │
└─────────────────────────────────────────────────────────────┘
```
```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                        │
│                                                               │
│ Bài toán (1 câu): Điều dưỡng phải ghi tay/gõ lại thông tin   │
│ bệnh nhân mỗi ca trực vì dữ liệu không tự tổng hợp từ HIS,   │
│ gây tốn thời gian và rủi ro thất lạc thông tin bàn giao.     │
│                                                               │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes   │
│                     [X] Vinmec   [ ] Khác___________________ │
│                                                               │
│ Ai đang đau (Actor)? Điều dưỡng trực (đặc biệt trưởng ca) —  │
│ gián tiếp là bệnh nhân nội trú (rủi ro an toàn nếu sót info) │
│                                                               │
│ Workflow thủ công hiện tại (3-5 bước):                       │
│   1. Cuối ca, ĐD rà từng bệnh nhân trên HIS ──> 2. Ghi/gõ    │
│   tóm tắt tay lên sổ giao ban/Excel riêng của khoa ──> 3. Họp│
│   giao ca, đọc miệng cả khoa (20-30 giường) ──> 4. ĐD ca sau │
│   ghi chú lại trong lúc nghe, bắt đầu ca dựa trên ghi chú đó │
│                                                               │
│ Bước nào tốn thời gian/lỗi nhất? Bước 1+3 (⏱ ~30-45 phút/ca  │
│ cho 1 khoa 20-30 giường)                                     │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1 — tự trích xuất │
│ thuốc/sinh hiệu/y lệnh mới từ HIS thành bản tóm tắt chuẩn    │
│                                                               │
│ Đo thành công bằng gì (Metric có số)?                        │
│   "Giảm thời gian bàn giao ca từ 30-45 min ──> under 15 min; │
│   giảm số lần phát hiện thiếu thông tin sau bàn giao"        │
│                                                               │
│ Quick Architecture: [ ] No AI  [X] Rule  [X] LLM  [ ] Agent  │
└─────────────────────────────────────────────────────────────┘
```
```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                        │
│                                                               │
│ Bài toán (1 câu): KTV trung tâm dịch vụ phải xem thủ công    │
│ từng bộ ảnh/video khách gửi để phân loại lỗi bảo hành và ước │
│ tính chi phí sửa, không scale được khi lượng claim tăng.     │
│                                                               │
│ Công ty thành viên: [X] VinFast  [ ] Xanh SM  [ ] Vinhomes   │
│                     [ ] Vinmec   [ ] Khác___________________ │
│                                                               │
│ Ai đang đau (Actor)? Kỹ thuật viên/nhân viên xử lý claim bảo │
│ hành — gián tiếp là khách hàng chờ duyệt claim quá lâu.      │
│                                                               │
│ Workflow thủ công hiện tại (3-5 bước):                       │
│   1. Khách gửi ảnh/video mô tả sự cố qua app/hotline ──> 2.  │
│   NV tiếp nhận, chuyển hồ sơ cho KTV chuyên trách ──> 3. KTV │
│   xem từng ảnh/video, đối chiếu tiêu chuẩn kỹ thuật để phân  │
│   loại lỗi (sản xuất / người dùng / hao mòn) ──> 4. KTV ước  │
│   tính chi phí sửa, nhập vào hệ thống claim ──> 5. Trưởng bộ │
│   phận duyệt trước khi phản hồi khách                        │
│                                                               │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (⏱ ~15-20 phút/ca,   │
│ tăng nếu ảnh/video chất lượng kém phải yêu cầu gửi lại)      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 — model thị     │
│ giác tiền phân loại hư hại + đối chiếu lịch sử bảo dưỡng/số  │
│ km để gợi ý nguyên nhân, KTV chỉ xác nhận/điều chỉnh         │
│                                                               │
│ Đo thành công bằng gì (Metric có số)?                        │
│   "Giảm thời gian phân loại + ước tính từ ~18 min ──> under  │
│   5 min/ca; tăng tỷ lệ claim xử lý trong ngày từ X% ──> Y%"  │
│                                                               │
│ Quick Architecture: [ ] No AI  [X] Rule  [X] LLM  [ ] Agent  │
└─────────────────────────────────────────────────────────────┘
```
```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #4                                        │
│                                                               │
│ Bài toán (1 câu): Nhân viên CSKH BQL đọc và gán nhãn thủ công│
│ từng phản ánh cư dân đa kênh, thường định tuyến sai gây đùn  │
│ đẩy trách nhiệm giữa các bộ phận và làm cư dân bức xúc.      │
│                                                               │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [X] Vinhomes   │
│                     [ ] Vinmec   [ ] Khác___________________ │
│                                                               │
│ Ai đang đau (Actor)? Nhân viên CSKH/tổng đài BQL — gián tiếp │
│ là cư dân (bị chuyển lòng vòng) và bộ phận nhận nhầm ticket. │
│                                                               │
│ Workflow thủ công hiện tại (3-5 bước):                       │
│   1. Cư dân gửi phản ánh qua app/hotline/email/tại quầy ──>  │
│   2. NV CSKH đọc/nghe để hiểu nội dung ──> 3. Gán nhãn phân  │
│   loại (kỹ thuật/an ninh/vệ sinh/phí DV/thái độ NV...) theo  │
│   kinh nghiệm cá nhân ──> 4. Chuyển ticket tới bộ phận phụ   │
│   trách ──> 5. Nếu sai bộ phận, ticket bị trả lại/chuyển tiếp│
│   lặp lại bước 3-4                                           │
│                                                               │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (⏱ ~3-5 phút/ticket, │
│ nhưng lỗi định tuyến khiến một phần ticket phải xử lý lại)   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 — model phân    │
│ loại văn bản gán nhãn + độ ưu tiên theo danh mục chuẩn, tự   │
│ động route tới đúng bộ phận, NV chỉ xử lý case biên          │
│                                                               │
│ Đo thành công bằng gì (Metric có số)?                        │
│   "Giảm tỷ lệ ticket bị định tuyến sai từ X% ──> dưới Y%;    │
│   giảm thời gian từ lúc nhận phản ánh đến khi tới đúng bộ    │
│   phận từ Z giờ ──> dưới 10 phút"                            │
│                                                               │
│ Quick Architecture: [ ] No AI  [X] Rule  [X] LLM  [ ] Agent  │
└─────────────────────────────────────────────────────────────┘
```
```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #5                                        │
│                                                               │
│ Bài toán (1 câu): Khi thuật toán auto-matching thất bại      │
│ (tài xế từ chối/không có xe trong bán kính), dispatcher phải │
│ tìm & thuyết phục tài xế thủ công, gây phàn nàn từ cả hai    │
│ phía tài xế và khách hàng.                                   │
│                                                               │
│ Công ty thành viên: [ ] VinFast  [X] Xanh SM  [ ] Vinhomes   │
│                     [ ] Vinmec   [ ] Khác___________________ │
│                                                               │
│ Ai đang đau (Actor)? Dispatcher tại trung tâm điều phối —    │
│ gián tiếp là tài xế (bị gán chuyến xa) và khách (chờ lâu).   │
│                                                               │
│ Workflow thủ công hiện tại (3-5 bước):                       │
│   1. Hệ thống auto-matching fail (bị từ chối liên tiếp hoặc  │
│   không có xe trong bán kính) ──> 2. Ticket escalate lên     │
│   dispatcher ──> 3. Dispatcher mở bản đồ, dò tài xế gần nhất │
│   thủ công, kiểm tra trạng thái (rảnh/đang chở khách) ──> 4. │
│   Gọi điện/nhắn thuyết phục tài xế nhận chuyến (nhiều khi    │
│   phải gọi 2-3 người) ──> 5. Gán tay chuyến trên hệ thống    │
│                                                               │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3+4 (⏱ ~5-10 phút/ca,  │
│ tăng theo số lần bị tài xế từ chối)                          │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 — thuật toán    │
│ ranking gợi ý top 3 tài xế phù hợp nhất (khoảng cách, hướng  │
│ di chuyển, tỷ lệ nhận chuyến lịch sử) thay vì dò tay bản đồ  │
│                                                               │
│ Đo thành công bằng gì (Metric có số)?                        │
│   "Giảm thời gian xử lý mỗi ca điều phối thủ công từ ~8 min  │
│   ──> under 3 min; giảm tỷ lệ chuyến huỷ do không tìm được   │
│   tài xế trong 5 phút từ X% ──> Y%"                          │
│                                                               │
│ Quick Architecture: [ ] No AI  [X] Rule  [ ] LLM  [ ] Agent  │
└─────────────────────────────────────────────────────────────┘
```