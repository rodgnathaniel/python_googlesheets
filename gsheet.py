import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client.json', scope)

gsheet = client.open('test').sheet1

test = gsheet.get_all_records()
print(test)