# google検索ページにワードを入力して結果を受け取ります
# 仮装環境で動きます。 source selenium_env/bin/activate

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument("--disable-extensions")

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Googleのホームページを開く
    driver.get("https://www.google.com")

    # 検索ボックスを見つけて "Python Selenium" と入力
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("python selenium")
    search_box.send_keys(Keys.RETURN)

    # 結果が表示されるまで少し待つ
    time.sleep(2)

    # 検索結果のタイトルを取得して表示
    search_results = driver.find_elements(By.CSS_SELECTOR, "h3")
    result_num = len(search_results)
    print(f"{result_num}件の情報が取得できました。")
    for result in search_results[:5]:  # 最初の5つの結果を表示
        print(result.text)

except Exception as e:
    print(f"エラーが発生しました: {e}")

finally:
    # ブラウザを閉じる
    driver.quit()
