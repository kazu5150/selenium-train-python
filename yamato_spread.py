import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


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

# セルの値を取得するには acell() メソッドを使う
shipping_name = worksheet.acell("B2").value
contact_number = worksheet.acell("C2").value

# print(f"発送先：【{shipping_name}】  問い合わせ番号：【{contact_number}】")

df = pd.DataFrame(worksheet.get_all_values())
df.columns = df.iloc[0]
df = df.drop(df.index[0])


print(df["問い合わせ番号"])


contact_numbers = df["問い合わせ番号"].tolist()
print(contact_numbers)
