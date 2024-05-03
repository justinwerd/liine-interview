import re
import datetime


day_map = {
    "Mon": 1,
    "Tues": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5,
    "Sat": 6,
    "Sun": 7,
}

def break_down_hours(hours_string):
    hours_arr = hours_string.split('/')
    hours_arr = [hours.strip() for hours in hours_arr]
    return hours_arr

def parse_date_range(date_range):
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

def parse_restaurant_hours(time,date_range=None,day=None):
    time_range = parse_time(time)
    num_range = []
    if date_range:
        num_range.extend(parse_date_range(date_range))
    if day:
        num_range.append(day_map[day])
    return num_range,time_range

def find_restaurant_hours(text):
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
        return parse_restaurant_hours(time=t,date_range=range_and_day[0].strip(),day=range_and_day[1].strip())
    elif pattern2.match(text):
        d = pattern2.match(text).group()
        range_and_day = d.split(',') 
        t = text[len(d):].strip()
        return parse_restaurant_hours(time=t,day=range_and_day[0].strip(),date_range=range_and_day[1].strip())
    elif pattern3.match(text):
        d = pattern3.match(text).group()
        t = text[len(d):].strip()
        return parse_restaurant_hours(time=t,date_range=d)
    elif pattern4.match(text):
        d = pattern4.match(text).group()
        t = text[len(d):].strip()
        return parse_restaurant_hours(time=t,day=d)
    else:
        raise Exception('String not found')

# Used with the functions above to add formatted hour data to mongodb instance
# def create_hours_collection():
#     mydoc = mycol.find({})
#     data = [x for x in mydoc]
#     for d in data:
#         restaurant_id = d['_id']
#         restaurant_name = d['Restaurant Name']
#         restaurant_hours = d['Hours']
#         h = break_down_hours(restaurant_hours)
#         for i in h:
#             date_data = find_restaurant_hours(i)
#             mydb.hours.insert_one({"restaurant_id": restaurant_id,
#                                    "restaurant_name":restaurant_name,
#                                    "date_range":date_data[0],
#                                    "opening_hour":date_data[1][0], 
#                                    "opening_minute":date_data[1][1], 
#                                    "closing_hour": date_data[1][2],
#                                    "closing_minute": date_data[1][3]}
#                                    )
