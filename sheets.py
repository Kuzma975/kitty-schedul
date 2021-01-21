from __future__ import print_function
import pickle
import os.path
from calendar import month_abbr
from datetime import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = ''
KITTY_NAME = ''
# SAMPLE_RANGE_NAME = '2017!C1:C15'
# SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
# SAMPLE_RANGE_NAME = 'Class Data!A2:E'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    # Search current month
    not_current = True
    iterator = 1
    current_month = month_abbr[datetime.now().month]
    previous_month = month_abbr[(datetime.now().month + 11) % 12 or 12]
    current_year = datetime.now().year
    previous_year = (datetime.now().year - 1, current_year)[datetime.now().month > 1]
    begin_row = 0
    while not_current:
        sheet_range = '2017!C' + str(iterator)
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=sheet_range).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            # print('Name, Major:')
            # print(values)
            value_arr = values[0][0].split(' ')
            if value_arr[0] == current_month and value_arr[1] == str(datetime.now().year):
                print(sheet_range)
                begin_row = iterator
            elif begin_row and value_arr[0] in month_abbr:
                end_row = iterator
                break
        if iterator > 30:
            break
        iterator += 1
    print(begin_row)
    print(end_row)
    sheet_range = '2017!A' + str(begin_row) + ':D' + str(end_row)
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=sheet_range).execute()
    values = result.get('values', [])
    for i in values:
        if not i:
            print('No data found.')
        elif i[0] == KITTY_NAME:
            print(i)
        # for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        # print('%s, %s' % (row[0], row[4]))


if __name__ == '__main__':
    main()
