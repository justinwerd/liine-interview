from flask import Flask,jsonify
import pymongo
import datetime
import re
from pprint import pprint
from date_time_parse import break_down_hours,find_date_range
app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["liine-interviews"]
mycol = mydb["restaurants"] 

@app.route('/get-open-restaurants/<date>')
def get_open_restaurants(date):
    formatted_date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M")
    d = formatted_date.weekday() + 1
    h = formatted_date.time().hour
    m = formatted_date.time().minute
    
    mydoc = mydb.hours.find({
        "date_range": d,
        # "opening_hour": {"$lte": h},
        # "closing_hour": {"$gte": h},
        # "closing_minute": {"$gte": m},
                             })
    data = [x['restaurant_name'] for x in mydoc]
    pprint(data)
    pprint(len(data))
    print(d,h,m)
    return jsonify(data), 200

def create_hours_collection():
    mydoc = mycol.find({})
    data = [x for x in mydoc]
    pprint(data)
    for d in data:
        restaurant_id = d['_id']
        restaurant_name = d['Restaurant Name']
        restaurant_hours = d['Hours']
        print(d)
        h = break_down_hours(restaurant_hours)
        for i in h:
            date_data = find_date_range(i)
            print(date_data)
            # mydb.hours.insert_one({"restaurant_id": restaurant_id,
            #                        "restaurant_name":restaurant_name,
            #                        "date_range":date_data[0],
            #                        "opening_hour":date_data[1][0], 
            #                        "opening_minute":date_data[1][1], 
            #                        "closing_hour": date_data[1][2],
            #                        "closing_minute": date_data[1][3]}
            #                        )

if __name__ == "__main__":
    create_hours_collection()
    # test_date = datetime.datetime.strptime("2024-05-06T11:20", "%Y-%m-%dT%H:%M")
    # print(test_date)
    # d = test_date.weekday() + 1
    # h = test_date.time().hour
    # m = test_date.time().minute
    # print(d,h,m)
    # mydoc = mydb.hours.find({
    #     "date_range": {"$all": [d]},
    #     "opening_hour": {"$lte": h},
    #     "closing_hour": {"$gte": h},
    #     # "closing_minute": {"$gte": m},
    #                          })
    # data = [x for x in mydoc]
    # pprint(data)
    # app.run()


