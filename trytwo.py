import os
from api_authentication import df
import datetime as dt

df2 = df[df["Phone #"] != '#N/A'] # delete non na rows

date_today = dt.date.today().strftime("%m/%d/%Y")


for row in df2.iterrows():
    if df2.loc[row, 'Reminder Date'] == date_today:
        phone_num = df2.loc[row, 'Phone #']

phone_num = df.loc[3, 'Phone #']

apple = '14157268044'
cmd = """
    osascript -e '
    tell application "Messages"
	
	    set targetBuddy to "14157268044"
	    set targetService to id of 1st account whose service type = iMessage
	
	    set textMessage to "This is an automated message that Anna has sent you. So cool!"
	
	    set theBuddy to participant targetBuddy of account id targetService
	    send textMessage to theBuddy
	
	    delay (random number from 10 to 30)
	
    end tell
    '
    """

os.system(cmd)