from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import schedule

def crawl_data():
    options = Options()
    options.add_argument('--headless')  # Chạy ẩn không hiện trình duyệt
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    results = []

    for i in range(1, 100):  
        url = f"https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/3/da-nang/trang--{i}.html"
        driver.get(url)
        time.sleep(2)

        titles = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[1]/div[1]/a')
        descriptions = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[1]')
        prices = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[4]/div[1]')
        areas = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[3]/div[1]')
        addresses = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[4]/div[2]')

        # Đồng bộ số lượng phần tử nhỏ nhất giữa các trường
        min_len = min(len(titles), len(descriptions), len(prices), len(areas), len(addresses))
        print(f"Trang {i}: thu được {min_len} bài đăng")

        for idx in range(min_len):
            results.append({
                'Tiêu đề': titles[idx].text,
                'Mô tả': descriptions[idx].text,
                'Giá': prices[idx].text,
                'Diện tích': areas[idx].text,
                'Địa chỉ': addresses[idx].text
            })

    driver.quit()

    # Ghi dữ liệu ra file Excel
    df = pd.DataFrame(results)
    df.to_excel('alonhadat_data.xlsx', index=False)
    print(f"Đã lưu {len(df)} bài đăng vào file alonhadat_data.xlsx")

# Thiết lập chạy lúc 6h sáng hằng ngày
schedule.every().day.at("06:00").do(crawl_data)

print("Đang chờ đến 6h sáng để chạy... Nhấn Ctrl+C để dừng.")
while True:
    schedule.run_pending()
    time.sleep(60)
