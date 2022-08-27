import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# establish credentials
scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(credentials)


# Open the spreadsheet
sheet = client.open("Tasks + Deadlines").sheet1

# get values and headers for df
data = sheet.get_all_values()
headers = data.pop(0)

# construct df
df = pd.DataFrame(data, columns=headers)

