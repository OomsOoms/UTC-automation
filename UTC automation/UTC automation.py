# import moudules
from googleapiclient.discovery import build
from google.oauth2 import service_account
import os
import time

# finds file path
platform = input("Linux - 1\nWindows - 2\n")
if str(platform) == "1":
    print("1")
    keys_file_path = f"{os.getcwd()}/keys.json"
    
if str(platform) == "2":
    keys_file_path = f"{os.getcwd()}\keys.json"

# user inputs - The ID of the spreadsheet
spreadsheet_1 = input("url of spreadsheets that it will read from ")
spreadsheet_1 = spreadsheet_1.split("/")[5]
print(f"the id is {spreadsheet_1} for the spreadsheet you are reading from")

spreadsheet_2 = input("url of spreadsheets that it will read from ")
spreadsheet_2 = spreadsheet_2.split("/")[5]
print(f"the id is {spreadsheet_2} for the spreadsheet you are writing to")
input("YOU ARE ABOUT TO OVERWRITE THE SECOND SHPREADSHEET YOU HAVE ENTERED. PRESS ENTER TO CONTUINUE")

# location of .json file + cred stuff
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
credentials = service_account.Credentials.from_service_account_file(
        keys_file_path, scopes=SCOPES)

# The ID of the spreadsheet
service = build('sheets', 'v4', credentials=credentials)

while True:
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_1,
                                range="Form responses 1!c2:o").execute()
    values = result.get('values', [])

# works out averages - converts to correct format and writes to the spreadsheet 2

    entry_number = 0
    write = []
    number_of_solves = []

    for x in range (len(values)):
        times = [] 
        total = []
        if len(values[entry_number]) == 12:
            video_proof = "No"
        else:
            video_proof = "Yes"
        
        entry = values[entry_number]
        entry_number += 1
       
        
        name = entry[0]
        total.append(name)
        entry = entry[2:]
        
        for x in range(0, 10, 2):
            penalties = entry[x+1]
            
            mins, temp = entry[x].split(":")
            sec, ms = temp.split(".")
            if mins == "00":
                mins_display = ""

            else:
                if int(mins) < 10:
                    mins_display = f"{mins[1]}:"
                else:
                    mins_display = f"{mins}:"
                
            if penalties == "No Penalties":
                total.append(f"'{mins_display}{sec}.{ms}")
                times.append(str(int(mins)*60+int(sec)+int(ms)/100))
                
                
            elif penalties == "+2":
                total.append(f"'{mins_display}{int(sec)+2}.{ms}+")
                
                times.append(str(int(mins)*60+int(sec)+2+int(ms)/100))
                
            else:
                times.append("-1")
                total.append("DNF")
        times.remove(max(times))
        times.remove(min(times))
        average = 0
        if min(times) == "-1":
            average = "DNF"
            total.append("DNF")
        else:
            for x in range(3):
                average += float(times[x])
            average /= 3

            mins = int(average/60)
            sec = float(average%60)

            if mins == 0:
                if float(sec) < 10:
                    average = f"' {sec:.2f}"

                else:
                    average = f"'{sec:.2f}"

            else:
                if float(sec) < 10:
                    average = f"{mins}:0{sec:.2f}"
                else:
                    average = f"'{mins}:{sec:.2f}"
            
            total.append(average)
            total.append(video_proof)
            
        write.append(total)
        write = (sorted(write, key=lambda x:x[6]))
        number = [entry_number]
        
        
        number_of_solves.append(number)
        

    request = sheet.values().update(spreadsheetId=spreadsheet_2,range="3x3!b3", valueInputOption="USER_ENTERED", body={"values":write}).execute()
    request = sheet.values().update(spreadsheetId=spreadsheet_2,range="3x3!a3:a", valueInputOption="USER_ENTERED", body={"values":number_of_solves}).execute()
    print("Done!")

    time.sleep(10)

