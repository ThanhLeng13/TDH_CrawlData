# 🏡 Alonhadat Crawler - Bất động sản Đà Nẵng

Một trình thu thập dữ liệu tự động (crawler) sử dụng Python và Selenium để lấy thông tin các bài đăng bất động sản tại **Đà Nẵng** từ website [alonhadat.com.vn](https://alonhadat.com.vn).

Dữ liệu bao gồm:
- ✅ Tiêu đề
- ✅ Mô tả
- ✅ Giá
- ✅ Diện tích
- ✅ Địa chỉ

Kết quả được lưu vào file Excel `alonhadat_data.xlsx`.

---

## 🚀 Tính năng chính

- Crawl dữ liệu từ **trang 1 đến trang 99** tại khu vực Đà Nẵng
- Trích xuất đầy đủ thông tin mỗi bài viết bất động sản
- Lưu dữ liệu thành file `.xlsx`
- Hẹn lịch **tự động chạy lúc 6h sáng mỗi ngày**
- Chạy ở chế độ **ẩn (headless)** – không cần mở trình duyệt

---

## ⚙️ Cài đặt

### Yêu cầu hệ thống:

- Python 3.x 
- Google Chrome
- ChromeDriver (phù hợp với phiên bản Chrome đang dùng)

### Cài đặt thư viện:

Chạy lệnh sau để cài đặt các thư viện cần thiết:

```bash
pip install selenium pandas schedule openpyxl

```

### Hướng dẫn chạy:

```bash
python nhadat_crawl.py
```
