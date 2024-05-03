from pprint import pprint
import re
import datetime


def break_down_hours(hours_string):
    hours_arr = hours_string.split('/')
    hours_arr = [hours.strip() for hours in hours_arr]
    return hours_arr
day_map = {
    "Mon": 1,
    "Tues": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5,
    "Sat": 6,
    "Sun": 7,
}

def parse_days(date_range):
    i,j = date_range.split('-')
    return list(range(day_map[i],day_map[j]+1))
def unabbreviate_time(time_str):
    if not time_str:
        return
    return time_str + ':00' if ':' not in time_str else time_str
def format_time(time_str):
    if not time_str:
        return
    trimmed = time_str.strip()
    formatted_time = ''
    if 'am' in trimmed:
        formatted_time = trimmed[:trimmed.find(' ')]
        formatted_time = unabbreviate_time(formatted_time)
    else:
        formatted_time = trimmed[:trimmed.find(' ')]
        formatted_time = unabbreviate_time(formatted_time)
        print(formatted_time)
        hour= int(formatted_time.split(':')[0])
        hour = hour + 12 if hour != 12 else hour
        formatted_time = str(hour) + formatted_time[formatted_time.find(':'):]
    return formatted_time
def parse_time(time):
    t_range = time.split('-')
    start = format_time(t_range[0])
    end = format_time(t_range[1])
    start_time = datetime.datetime.strptime(start, "%H:%M").time()
    end_time = datetime.datetime.strptime(end, "%H:%M").time()

    return start_time.hour,start_time.minute,end_time.hour,end_time.minute

def parse_date_range_plus(date_range,time):
    range_and_day = date_range.split(',') 
    num_range = parse_days(range_and_day[0])
    sep_day = day_map[range_and_day[1].strip()]
    num_range.append(sep_day)
    time_range = parse_time(time)
    return num_range,time_range
def parse_date_range(date_range,time):
    print(date_range)
    num_range = parse_days(date_range)
    time_range = parse_time(time)
    return num_range,time_range
def parse_date_pattern(day1,time):
    day = [day_map[day1]]
    time_range = parse_time(time)
    return day,time_range

def parse_date(time,date_range=None,day=None):
    time_range = parse_time(time)
    num_range = []
    if date_range:
        num_range.extend(parse_days(date_range))
    if day:
        num_range.append(day_map[day])
    return num_range,time_range
def find_date_range(text):
    day_range_day_reg = '[A-Za-z]{2,}-[A-Za-z]{2,}, [A-Za-z]{2,}'
    day_day_range_reg = '[A-Za-z]{2,}, [A-Za-z]{2,}-[A-Za-z]{2,}'
    day_range_reg = '[A-Za-z]{2,}-[A-Za-z]{2,}'
    day_reg = '[A-Za-z]{2,}'
    # time_range = r'\d(.*)'
    # time_range = '[0-9]{1,2}:*[0-9]* [a-z]m - [0-9]{1,2}:*[0-9]* [a-z]m'
    pattern1 = re.compile(day_range_day_reg, re.IGNORECASE)
    pattern2 = re.compile(day_day_range_reg, re.IGNORECASE)
    pattern3 = re.compile(day_range_reg, re.IGNORECASE)
    pattern4 = re.compile(day_reg, re.IGNORECASE)

    if pattern1.match(text):
        d = pattern1.match(text).group()
        range_and_day = d.split(',') 
        t = text[len(d):].strip()
        return parse_date(time=t,date_range=range_and_day[0].strip(),day=range_and_day[1].strip())
    if pattern2.match(text):
        d = pattern2.match(text).group()
        range_and_day = d.split(',') 
        t = text[len(d):].strip()
        return parse_date(time=t,day=range_and_day[0].strip(),date_range=range_and_day[1].strip())
    elif pattern3.match(text):
        d = pattern3.match(text).group()
        t = text[len(d):].strip()
        return parse_date(time=t,date_range=d)
    elif pattern4.match(text):
        d = pattern4.match(text).group()
        t = text[len(d):].strip()
        return parse_date(time=t,day=d)
