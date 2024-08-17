from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 問い合わせ番号を渡されると、seleniumが起動し、荷物の状況を取得し返します。
def check_yamato_delivery(contact_number):
    driver = webdriver.Chrome()
    try:
        driver.get("https://toi.kuronekoyamato.co.jp/cgi-bin/tneko")
        input_field = driver.find_element(By.NAME, "number01")
        input_field.send_keys(contact_number)
        submit_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit'][name='category'][value='0']")
        submit_button.click()
        wait = WebDriverWait(driver, 10)
        result_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "js-tracking-detail")))
        return result_element.text
    finally:
        driver.quit()
