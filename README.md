# 🏡 Bất động sản Đà Nẵng Crawler – Alonhadat.com.vn

Trình crawler thu thập dữ liệu bất động sản tại Đà Nẵng từ website [alonhadat.com.vn](https://alonhadat.com.vn), bao gồm các thông tin:
- Tiêu đề
- Mô tả
- Giá
- Diện tích
- Địa chỉ

Kết quả sẽ được lưu vào file Excel `alonhadat_data.xlsx`.

## 🚀 Tính năng

- Crawl dữ liệu từ trang 1 đến 99 tại Đà Nẵng
- Lấy đầy đủ thông tin mỗi bài viết
- Lưu dữ liệu vào file Excel
- Tự động chạy vào **6h sáng mỗi ngày**

## 🧰 Yêu cầu

- Python 3.7+
- Google Chrome
- ChromeDriver tương thích với Chrome
- Các thư viện Python:
  ```bash
  pip install selenium pandas schedule openpyxl
