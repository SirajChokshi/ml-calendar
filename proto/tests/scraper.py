from __future__ import print_function
import datetime
from dateutil.parser import parse as dtparse
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

START_TIME = datetime.datetime(2020, 1, 27, 0, 0, 0, 0).isoformat('T') + "Z"
END_TIME = datetime.datetime(2020, 3, 16, 0, 0, 0, 0).isoformat('T') + "Z"

class Day:
    def __init__(self, weekday=None, events=[], date = None):
        self.date = date
        self.weekday = weekday
        self.events = events

    def __str__(self):
        out = "{} - Weekday #{}\n".format(self.date, self.weekday)
        for event in self.events:
            out += str(event)
            out += "\n"
        return out

class Week:
    def __init__(self, start, days):
        self.start = start
        self.days = days
    
    def __str__(self):
        out = "Week of {}\n".format(self.start)
        for day in self.days:
            out += "\t{}\n".format(day.date)
        return out

class Calendar:
    def __init__(self, weeks):
        self.weeks = weeks

    def __str__(self):
        out = ""
        for week in self.weeks:
            out += "Week of {}\n".format(week.start)
        return out

def get_api_service():
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

    return build('calendar', 'v3', credentials=creds)

def get_calendars(service):
    calendars = service.calendarList().list().execute()

    calendar_list = []

    for calendar in calendars["items"]:
        if calendar['accessRole'] == 'owner':
            calendar_list.append(calendar['id'])
    
    return calendar_list

def get_events(service, calendar_id, start, end, time_zone = "America/New_York"):
    events_result = service.events().list(calendarId=calendar_id, timeMin = start, timeMax = end, maxResults=400, 
                                        singleEvents=True, orderBy='startTime', timeZone=time_zone).execute()
    events = events_result.get('items', [])

    if not events:
        return []
    else:
        out = []
        for event in events:
            # start = event['start'].get('dateTime', event['start'].get('date'))
            # end = event['end'].get('dateTime', event['end'].get('date'))
            try:
                start = dtparse(event['start']['dateTime'])
                end = dtparse(event['end']['dateTime'])
            except:
                print(event['start'])
            curr = {
                'start': start,
                'end': end,
                'name': event['summary']
            }
            out.append(curr)
        return out

def get_calendar(service, start_time, end_time):
    calendars = get_calendars(service)

    all_events = []

    for calendar_id in calendars:
        all_events += get_events(service, calendar_id, start_time, end_time)

    # for c in all_events:
    #     print(c['start'], c['name'])
    # print()

    all_events = sorted(all_events, key = lambda i: (i['start'], i['end'])) 

    # for c in all_events:
    #     print(c['start'].strftime("%D"), c['name'])

    event_dict = {}

    for c in all_events:
        try:
            event_dict[c['start'].strftime("%D")].append(c)
        except:
            event_dict[c['start'].strftime("%D")] = [c]

    day_list = []

    for key in event_dict:
        current_day = Day()
        events = []
        current_day.date = key

        for event in event_dict[key]:
            current_day.weekday = event['start'].weekday()

            start = event['start']
            end = event['end']

            start_of_day = start.replace(hour=0, minute=0, second=0, microsecond=0)

            start_seconds = (start - start_of_day).total_seconds()
            end_seconds = (end - start_of_day).total_seconds()

            events.append((start_seconds, end_seconds))

        current_day.events = events

        day_list.append(current_day)

    week_list = []
    current_week = []

    for day in day_list:
        if day.weekday == 0:
            try:
                firstDay = current_week[0].date
                week_list.append(Week(firstDay, current_week))
                current_week = []
            except:
                pass
        current_week.append(day)
    firstDay = current_week[0].date
    week_list.append(Week(firstDay, current_week))

    return Calendar(week_list)

def scrape():
    service = get_api_service()
    cal = get_calendar(service, START_TIME, END_TIME)
    return cal


if __name__ == '__main__':
    scrape()