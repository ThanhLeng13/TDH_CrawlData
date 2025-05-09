from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import schedule

# 1. Vào website đã chọn.
# hàm crawl_data() sẽ tự động mở trình duyệt và thu thập dữ liệu từ trang web
def crawl_data():
    driver = webdriver.Chrome()

    results = []
    count_page = 0

    # 2. Click chọn bất kì Tỉnh/TP Đà Nẵng. Chọn loại nhà đất.
    # 3. Bấm tìm kiếm(nếu trang web không có Button tìm kiếm thì có thể bỏ qua).
    # 5. Lấy tất cả dữ liệu của các trang.
    while True: 
        count_page += 1
        url = f"https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/3/da-nang/trang--{count_page}.html"
        driver.get(url)
        time.sleep(2)

        # 4. Lấy tất cả dữ liệu(Tiêu đề, Mô tả, Địa chỉ, Diện tích, Giá) hiển thị ở bài viết.
        titles = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[1]/div[1]/a')
        descriptions = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[1]')
        prices = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[4]/div[1]')
        areas = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[3]/div[1]')
        addresses = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[4]/div[2]')

        # Đồng bộ số lượng phần tử nhỏ nhất giữa các trường
        min_len = min(len(titles), len(descriptions), len(prices), len(areas), len(addresses))
        print(f"Trang {count_page}: thu được {min_len} bài đăng")

        if min_len == 0:
            print("Không còn dữ liệu để thu thập, dừng lại.")
            break

        for idx in range(min_len):
            results.append({
                'Tiêu đề': titles[idx].text,
                'Mô tả': descriptions[idx].text,
                'Giá': prices[idx].text,
                'Diện tích': areas[idx].text,
                'Địa chỉ': addresses[idx].text
            })

    driver.quit()

    # 6. Lưu dữ liệu đã lấy được vào file excel.
    df = pd.DataFrame(results)
    df.to_excel('alonhadat_data.xlsx', index=False)
    print(f"Đã lưu {len(df)} bài đăng vào file alonhadat_data.xlsx")

# 7. Set lịch chạy vào lúc 6h sáng hằng ngày.
# Thiết lập chạy lúc 6h sáng hằng ngày
schedule.every().day.at("06:00").do(crawl_data)

print("Đang chờ đến 6h sáng để chạy... Nhấn Ctrl+C để dừng.")
while True:
    schedule.run_pending()
    time.sleep(10)
