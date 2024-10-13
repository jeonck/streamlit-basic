# https://chatgpt.com/share/6709f894-35b8-8005-b949-ab9940e330f5

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

def collect_yes24_bestsellers():
    # Chrome 옵션 설정 (헤드리스 모드 사용 시 주석 해제)
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # 브라우저 창을 표시하지 않음
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    # 웹드라이버 초기화
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # 타겟 URL 설정
        base_url = "https://www.yes24.com"
        url = f"{base_url}/Product/Category/BestSeller?CategoryNumber=001&sumgb=06"
        driver.get(url)

        # 페이지 로딩 대기 (최대 10초)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "item_info")))

        # 모든 item_info 요소 찾기
        items = driver.find_elements(By.CLASS_NAME, "item_info")

        data = []

        for item in items:
            # 제목 및 링크 추출
            try:
                title_elem = item.find_element(By.CSS_SELECTOR, ".info_name .gd_name")
                title = title_elem.text.strip()
                link = title_elem.get_attribute("href")
                if link.startswith('/'):
                    link = base_url + link
            except:
                title = ""
                link = ""

            # 저자 추출
            try:
                author_elem = item.find_element(By.CSS_SELECTOR, ".info_pubGrp .info_auth a")
                author = author_elem.text.strip()
            except:
                author = ""

            # 가격 추출
            try:
                price_elem = item.find_element(By.CSS_SELECTOR, ".info_price .txt_num .yes_b")
                price = price_elem.text.strip()
            except:
                price = ""

            # 데이터 저장
            data.append({
                "제목": title,
                "저자": author,
                "가격": price,
                "링크": link
            })

        # CSV 파일로 저장
        csv_file = "yes24_bestsellers.csv"
        with open(csv_file, mode='w', newline='', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=["제목", "저자", "가격", "링크"])
            writer.writeheader()
            writer.writerows(data)

        print(f"데이터가 '{csv_file}' 파일에 성공적으로 저장되었습니다.")

    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        # 웹드라이버 종료
        driver.quit()

if __name__ == "__main__":
    collect_yes24_bestsellers()
