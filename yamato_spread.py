"""
この関数を実行すると、spreadsheetから問い合わせ番号を取得し、kuroneko_yamato.pyにてseleniumを実行し、
結果を受け取ります。
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import time
from datetime import datetime

from kuroneko_yamato import check_yamato_delivery


SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = 'selenium-spreadhseet-yamato-f83687fbeb1a.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    SERVICE_ACCOUNT_FILE, SCOPE)

gs = gspread.authorize(credentials)

SPREADSHEET_KEY = "1PGug0gq780SLrf3mFqHMep1rpr2i6OUqBeXOsPBYH28"
workbook = gs.open_by_key(SPREADSHEET_KEY)
worksheet = workbook.worksheet("発送管理")
# print(workbook.title)
# print(workbook.id)

df = pd.DataFrame(worksheet.get_all_values())
df.columns = df.iloc[0]
df = df.drop(df.index[0])

contact_numbers = df["問い合わせ番号"].tolist()
print(contact_numbers)

# contact_number = contact_numbers[1]

# result = check_yamato_delivery(contact_number)
# print(f"【{contact_number}】のお荷物：【{result}】")

results = []
for contact_number in contact_numbers:
    result = check_yamato_delivery(contact_number)
    print(f"【{contact_number}】のお荷物：【{result}】")
    results.append(result)
    time.sleep(3)

print(results)
worksheet.update([[result] for result in results], 'D2:D8')

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(current_time)
worksheet.update_cell(2, 5, current_time)
worksheet.update_cell(3, 5, current_time)
worksheet.update_cell(4, 5, current_time)
worksheet.update_cell(5, 5, current_time)
worksheet.update_cell(6, 5, current_time)
worksheet.update_cell(7, 5, current_time)
worksheet.update_cell(8, 5, current_time)
