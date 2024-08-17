# 仮装環境で動きます。 source selenium_env/bin/activate

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 問い合わせ番号を入力して下さい。
contact_number = input("問い合わせ番号を入力して下さい。")

# WebDriverの初期化（ChromeDriverの場合）
driver = webdriver.Chrome()

# お問い合わせページにアクセス
driver.get("https://toi.kuronekoyamato.co.jp/cgi-bin/tneko")

# ページソースを確認
# print(driver.page_source)

# 問い合わせ番号を入力
input_field = driver.find_element(By.NAME, "number01")
input_field.send_keys(contact_number)  # 画像の番号を使用

# お問い合わせ開始ボタンをクリック
submit_button = driver.find_element(
    By.CSS_SELECTOR, "button[type='submit'][name='category'][value='0']")
submit_button.click()

# 結果が表示されるまで待機
wait = WebDriverWait(driver, 10)
result_element = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "js-tracking-detail")))

# テキストを取得
result_text = result_element.text

print(f"【{contact_number}】のお荷物：【{result_text}】")  # "伝票番号未登録" が表示されるはず

# ブラウザを閉じる
driver.quit()
